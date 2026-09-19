"""Hermetic tests: no credentials, network, model, or publication needed."""
import hashlib
import hmac
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time
from types import SimpleNamespace
import unittest
from unittest.mock import patch
from urllib.parse import urlencode

from threadscout.core import Item, Store, canonical, contains, match, plain
from threadscout.app import authorized, demo_items, digest, handle, keyboard, render, scan, show_copy, Telegram
from threadscout.codex import brief, SCHEMA
from threadscout.sources import HackerNews, Reddit, RemoteError
from threadscout.webui import verify_init_data

ROOT=Path(__file__).resolve().parents[1]
PROFILE=json.loads((ROOT/'profile.json').read_text())

def item(key='hn:1',thread=None,**kwargs):
    d=dict(key=key,platform='hn',url='https://news.ycombinator.com/item?id=1',
           title='How do I build RAG search?',text='Looking for text search in Python.',
           created=time.time(),thread=thread or key)
    d.update(kwargs); return Item(**d)

class FakeTelegram:
    owner=123
    def __init__(self): self.sent=[]; self.calls=[]
    def send(self,text,keyboard=None,force=False):
        self.sent.append((text,keyboard,force)); return {'message_id':len(self.sent)}
    def call(self,method,**data): self.calls.append((method,data)); return {}

class Immediate:
    def submit(self,fn,*args): return fn(*args)

class MatchingTests(unittest.TestCase):
    def test_html_is_text(self): self.assertEqual(plain('<p>a &amp; b</p><script>steal()</script>'), 'a & b')
    def test_term_not_substring(self): self.assertFalse(contains('storage fragmentation','rag'))
    def test_term_casefold(self): self.assertTrue(contains('Try RAG?','rag'))
    def test_relevant_question(self): self.assertGreaterEqual(match(item(),PROFILE)['score'],35)
    def test_irrelevant_zero(self): self.assertEqual(match(item(title='Football',text='Who won?'),PROFILE)['score'],0)
    def test_mention_priority(self): self.assertGreaterEqual(match(item(title='DataTalks.Club',text=''),PROFILE)['score'],42)
    def test_assets_from_catalogue(self): self.assertTrue(all(a['id'] in {x['id'] for x in PROFILE['assets']} for a in match(item(),PROFILE)['assets']))
    def test_card_escapes_html(self):
        s=render(item(title='<script>x</script>',text='<b>unsafe</b>'),PROFILE)
        self.assertIn('&lt;script&gt;',s); self.assertNotIn('<script>',s)

class URLTests(unittest.TestCase):
    def test_hn_tracking_removed(self): self.assertEqual(canonical('https://news.ycombinator.com/item?id=123&utm_x=1'),('hn:123','https://news.ycombinator.com/item?id=123'))
    def test_reddit_post(self): self.assertEqual(canonical('https://old.reddit.com/r/test/comments/abc/title/')[0],'reddit:t3_abc')
    def test_reddit_comment(self): self.assertEqual(canonical('https://www.reddit.com/r/test/comments/abc/title/def/?context=3')[0],'reddit:t1_def')
    def test_reject_other_host(self):
        for url in ('https://localhost/','http://news.ycombinator.com/item?id=1','https://news.ycombinator.com@evil.example/item?id=1','https://news.ycombinator.com:8443/item?id=1','https://www.reddit.com/r/test/s/abc'):
            with self.subTest(url=url),self.assertRaises(ValueError): canonical(url)

class StateTests(unittest.TestCase):
    def setUp(self): self.store=Store(':memory:'); self.i=item(); self.store.add(self.i,80)
    def tearDown(self): self.store.close()
    def test_upsert_no_duplicate(self): self.assertFalse(self.store.add(self.i,99)); self.assertEqual(len(self.store.candidates()),1)
    def test_delivered_not_requeued(self): self.store.delivered('hn:1'); self.store.add(self.i,100); self.assertEqual(self.store.candidates(),[])
    def test_skip_preserved(self): self.store.action('hn:1','skip'); self.store.add(self.i,100); self.assertEqual(self.store.candidates(),[])
    def test_later_wakes(self):
        self.store.action('hn:1','later'); self.assertEqual(self.store.candidates(),[])
        self.store.db.execute('UPDATE items SET wake=0'); self.store.db.commit(); self.assertEqual(len(self.store.candidates()),1)
    def test_thread_diversity(self): self.store.add(item('hn:2',thread='hn:1'),90); self.assertEqual(len(self.store.candidates()),1)
    def test_stale_excluded(self): self.i.created=time.time()-100*3600; self.store.add(self.i,99); self.assertEqual(self.store.candidates(),[])
    def test_demo_excluded(self):
        for i in demo_items(): self.store.add(i,100)
        self.assertEqual([i.key for i in self.store.candidates()],['hn:1'])
    def test_only_human_draft(self): self.store.set('brief:hn:1',{'why':'AI notes'}); self.assertEqual(self.store.draft('hn:1')['human'],'')
    def test_draft_conflict(self):
        self.store.save('hn:1','my text',0)
        with self.assertRaises(ValueError): self.store.save('hn:1','stale overwrite',0)
        self.assertEqual(self.store.draft('hn:1')['human'],'my text')
    def test_draft_validation(self):
        for text in ('',' '*3,'x'*3501):
            with self.assertRaises(ValueError): self.store.save('hn:1',text)
    def test_deletion_clears_cached_brief(self):
        self.store.set('brief:hn:1',{'why':'old source'}); self.i.available=False; self.store.add(self.i,0)
        self.assertEqual(self.store.item('hn:1').text,''); self.assertIsNone(self.store.get('brief:hn:1'))
    def test_retention_and_tombstone(self):
        self.store.save('hn:1','mine'); self.store.set('reply:10','hn:1')
        self.store.db.execute('UPDATE items SET first_seen=?',(time.time()-8*86400,)); self.store.db.commit(); self.store.purge()
        self.assertIsNone(self.store.get('reply:10')); self.assertFalse(self.store.add(self.i,100))
        with self.assertRaises(ValueError): self.store.item('hn:1')
    def test_cancel_all_bindings(self): self.store.set('reply:10','hn:1'); self.store.cancel_replies(); self.assertIsNone(self.store.get('reply:10'))

class CollectorTests(unittest.TestCase):
    def test_reddit_off_by_default(self):
        with patch.dict(os.environ,{},clear=True),patch('threadscout.sources.request_json') as req:
            with self.assertRaises(RemoteError): list(Reddit().search(['test']))
            req.assert_not_called()
    def test_reddit_token_required(self):
        with patch.dict(os.environ,{'REDDIT_APPROVED':'1','REDDIT_ACCESS_TOKEN':''},clear=True):
            with self.assertRaises(RemoteError): Reddit().headers()
    def test_hn_deletion(self):
        with patch.object(HackerNews,'get',return_value={'deleted':True}):
            got=HackerNews().refresh(item()); self.assertFalse(got.available); self.assertEqual(got.text,'')
    def test_hn_parent_and_bounded_replies(self):
        rows={1:{'text':'Question?','parent':2,'kids':[3,4,5,6,7]},2:{'title':'Root','type':'story'},3:{'text':'reply'},4:{'deleted':True},5:{'text':'reply'},6:{'text':'reply'}}
        with patch.object(HackerNews,'get',side_effect=lambda x:rows.get(int(x))) as get:
            got=HackerNews().refresh(item(title='HN discussion'))
            self.assertEqual(got.title,'Root'); self.assertEqual(got.thread,'hn:2'); self.assertNotIn(unittest.mock.call(7),get.call_args_list)
    def test_hn_search_dedup(self):
        data={'hits':[{'objectID':'1','title':'Search','created_at_i':time.time()},{'objectID':'1'}],'nbPages':1}
        with patch('threadscout.sources.request_json',return_value=data),patch('threadscout.sources.time.sleep'):
            self.assertEqual(len(list(HackerNews().search(['q','q2']))),1)
    def test_reddit_archived_not_candidate(self):
        data={'data':{'children':[{'data':{'archived':True,'body':'old','name':'t1_a'}}]}}
        with patch.object(Reddit,'headers',return_value={}),patch('threadscout.sources.request_json',return_value=data):
            self.assertFalse(Reddit().refresh(item(key='reddit:t1_a',platform='reddit')).available)

class AuthTests(unittest.TestCase):
    def update(self,user=123,chat=123,kind='private'):
        return {'message':{'from':{'id':user},'chat':{'id':chat,'type':kind}}}
    def test_owner_private_only(self): self.assertTrue(authorized(self.update(),123))
    def test_others_denied(self):
        for u in (self.update(user=999),self.update(chat=999),self.update(kind='group')): self.assertFalse(authorized(u,123))
    def test_callback_sender_checked(self):
        u={'callback_query':{'from':{'id':999},'message':self.update()['message']}}; self.assertFalse(authorized(u,123))
    def test_telegram_method_allowlist(self):
        with patch.dict(os.environ,{'TELEGRAM_BOT_TOKEN':'fake','TELEGRAM_OWNER_ID':'123'}):
            with self.assertRaises(ValueError): Telegram().call('forwardMessage')
    def signed(self,owner=123,stamp=1000):
        values={'auth_date':str(stamp),'query_id':'q','user':json.dumps({'id':owner})}
        secret=hmac.new(b'WebAppData',b'fake',hashlib.sha256).digest()
        check='\n'.join(k+'='+values[k] for k in sorted(values))
        values['hash']=hmac.new(secret,check.encode(),hashlib.sha256).hexdigest(); return urlencode(values)
    def test_miniapp_valid(self): self.assertEqual(verify_init_data(self.signed(),'fake',123,now=1010)['id'],123)
    def test_miniapp_tamper(self):
        with self.assertRaises(ValueError): verify_init_data(self.signed()+'x','fake',123,now=1010)
    def test_miniapp_expired_or_future(self):
        for now in (5000,900):
            with self.assertRaises(ValueError): verify_init_data(self.signed(),'fake',123,now=now)
    def test_miniapp_other_user(self):
        with self.assertRaises(ValueError): verify_init_data(self.signed(999),'fake',123,now=1010)
    def test_miniapp_duplicate_fields(self):
        with self.assertRaises(ValueError): verify_init_data(self.signed()+'&auth_date=1000','fake',123,now=1010)

class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.cfg=json.loads((ROOT/'config.json').read_text()); self.cfg['db']=self.tmp.name+'/db.sqlite3'; self.tg=FakeTelegram()
        db=Store(self.cfg['db']); db.add(item(),80); db.close()
    def tearDown(self): self.tmp.cleanup()
    def test_digest_marks_after_send(self):
        with patch('threadscout.app.refresh',side_effect=lambda x:x): self.assertEqual(digest(self.cfg,PROFILE,self.tg),1)
        db=Store(self.cfg['db']); self.assertEqual(db.candidates(),[]); db.close()
    def test_digest_does_not_send_deleted(self):
        with patch('threadscout.app.refresh',return_value=item(available=False)): self.assertEqual(digest(self.cfg,PROFILE,self.tg),0)
        self.assertEqual(self.tg.sent,[])
    def test_digest_send_failure_retains_candidate(self):
        self.tg.send=unittest.mock.Mock(side_effect=[RemoteError('failed'),{}])
        with patch('threadscout.app.refresh',side_effect=lambda x:x): self.assertEqual(digest(self.cfg,PROFILE,self.tg),0)
        db=Store(self.cfg['db']); self.assertEqual(len(db.candidates()),1); db.close()
    def test_scan_failure_is_visible(self):
        def fail(*args): raise RemoteError('offline'); yield
        with patch.dict(os.environ,{'REDDIT_APPROVED':'0'}),patch.object(HackerNews,'search',fail):
            result=scan(self.cfg,PROFILE); self.assertFalse(result['sources']['hn']['ok']); self.assertIn('disabled',result['sources']['reddit'])
    def test_human_reply_binding(self):
        db=Store(self.cfg['db']); db.set('reply:10','hn:1'); db.close()
        u={'message':{'from':{'id':123},'chat':{'id':123,'type':'private'},'text':'I wrote this myself.','reply_to_message':{'message_id':10}}}
        handle(u,self.cfg,PROFILE,self.tg,Immediate())
        db=Store(self.cfg['db']); self.assertEqual(db.draft('hn:1')['human'],'I wrote this myself.'); db.close()
    def test_unbound_message_not_saved(self):
        u={'message':{'from':{'id':123},'chat':{'id':123,'type':'private'},'text':'hello'}}
        handle(u,self.cfg,PROFILE,self.tg,Immediate()); db=Store(self.cfg['db']); self.assertEqual(db.draft('hn:1')['human'],''); db.close()
    def test_long_copy_not_native_button(self):
        db=Store(self.cfg['db']); db.save('hn:1','x'*500); show_copy(db,self.tg,'hn:1'); db.close()
        self.assertFalse(any('copy_text' in json.dumps(k) for _,k,_ in self.tg.sent))
    def test_short_copy_user_text(self):
        db=Store(self.cfg['db']); db.save('hn:1','my words'); show_copy(db,self.tg,'hn:1'); db.close()
        self.assertIn('my words',json.dumps(self.tg.sent[-1][1]))
    def test_demo_has_no_external_link(self):
        with patch.dict(os.environ,{'TELEGRAM_WEBAPP_URL':''}): self.assertNotIn('"url"',json.dumps(keyboard(demo_items()[0])))

class CodexTests(unittest.TestCase):
    def test_no_public_draft_schema(self): self.assertNotIn('draft',SCHEMA['properties']); self.assertNotIn('comment',SCHEMA['properties'])
    def test_reddit_external_processing_gate(self):
        with patch.dict(os.environ,{'REDDIT_LLM_APPROVED':'0'}):
            with self.assertRaises(RuntimeError): brief(item(platform='reddit'),PROFILE)
    def fake_run(self,cmd,**kwargs):
        self.cmd=cmd; self.env=kwargs['env']
        Path(cmd[cmd.index('-o')+1]).write_text(json.dumps({'why':'topic fit','question':'What did you measure?','caveat':'Incomplete context','asset_ids':['sqlitesearch']}))
        return SimpleNamespace(returncode=0)
    def test_codex_subscription_flags_and_secret_stripping(self):
        with patch('threadscout.codex.shutil.which',return_value='/fake/codex'),patch('threadscout.codex.subprocess.run',side_effect=self.fake_run),patch.dict(os.environ,{'OPENAI_API_KEY':'never-pass','TELEGRAM_BOT_TOKEN':'never-pass'}):
            got=brief(item(),PROFILE)
        self.assertEqual(got['asset_ids'],['sqlitesearch']); self.assertIn('forced_login_method="chatgpt"',self.cmd)
        self.assertIn('--ignore-user-config',self.cmd); self.assertIn('features.shell_tool=false',self.cmd)
        self.assertNotIn('OPENAI_API_KEY',self.env); self.assertNotIn('TELEGRAM_BOT_TOKEN',self.env)
    def test_codex_timeout_no_fallback(self):
        with patch('threadscout.codex.shutil.which',return_value='/fake/codex'),patch('threadscout.codex.subprocess.run',side_effect=subprocess.TimeoutExpired('codex',100)):
            with self.assertRaises(RuntimeError): brief(item(),PROFILE)
    def test_codex_unknown_asset_rejected(self):
        def fake(cmd,**kwargs):
            Path(cmd[cmd.index('-o')+1]).write_text(json.dumps({'why':'x','question':'x','caveat':'x','asset_ids':['invented']})); return SimpleNamespace(returncode=0)
        with patch('threadscout.codex.shutil.which',return_value='/fake/codex'),patch('threadscout.codex.subprocess.run',side_effect=fake):
            with self.assertRaises(RuntimeError): brief(item(),PROFILE)

if __name__=='__main__': unittest.main()
