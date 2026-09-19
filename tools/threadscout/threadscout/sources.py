"""Read-only collectors. Reddit requires explicit approval; there is no scraper fallback."""
from __future__ import annotations
import json
import os
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, build_opener, HTTPRedirectHandler
from .core import Item, plain, canonical

class RemoteError(RuntimeError): pass
class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl): return None

OPENER = build_opener(NoRedirect())

def request_json(url, *, payload=None, headers=None, timeout=20):
    """Bounded reads, no redirects, TLS verification, no token-bearing URL in errors."""
    h = {'User-Agent':'ThreadScout/0.1 personal read-only monitor'}
    h.update(headers or {})
    data = None
    if payload is not None:
        data = json.dumps(payload).encode(); h['Content-Type']='application/json'
    try:
        with OPENER.open(Request(url,data=data,headers=h),timeout=timeout) as r:
            raw = r.read(2_000_001)
            if len(raw)>2_000_000: raise RemoteError('Response too large.')
            return json.loads(raw)
    except HTTPError as exc:
        # Caller handles cooldown; do not retry side-effecting Telegram sends.
        retry = exc.headers.get('Retry-After','')
        raise RemoteError(f'HTTP {exc.code}; retry-after={retry[:20]}') from None
    except (URLError, TimeoutError, OSError, ValueError):
        raise RemoteError('Network failure or invalid JSON; check connection/provider.') from None

class HackerNews:
    def search(self, queries, hours=48):
        seen=set()
        for query in queries:
            for page in range(2):
                params = urlencode({'query':query,'tags':'(story,comment)', 'numericFilters':f'created_at_i>{int(time.time()-hours*3600)}', 'hitsPerPage':30,'page':page})
                data=request_json('https://hn.algolia.com/api/v1/search_by_date?'+params)
                for hit in data.get('hits',[]):
                    ident=str(hit.get('objectID',''))
                    if not ident.isdigit() or ident in seen: continue
                    seen.add(ident)
                    yield Item('hn:'+ident,'hn','https://news.ycombinator.com/item?id='+ident,
                        plain(hit.get('title') or hit.get('story_title') or 'HN discussion'),
                        plain(hit.get('comment_text') or hit.get('story_text') or ''),
                        float(hit.get('created_at_i') or time.time()), 'hn:'+str(hit.get('story_id') or ident))
                if page+1 >= data.get('nbPages',1): break
                time.sleep(1)
            time.sleep(1)
    def get(self, ident):
        if not str(ident).isdigit(): raise ValueError('Invalid HN ID.')
        time.sleep(.15)
        return request_json(f'https://hacker-news.firebaseio.com/v0/item/{ident}.json')
    def refresh(self,item):
        target=self.get(item.key.split(':')[1])
        item.checked=time.time()
        if not target or target.get('deleted') or target.get('dead'):
            item.available=False; item.text=''; item.context=''; return item
        item.text=plain(target.get('text','')); item.created=float(target.get('time',item.created))
        item.title=plain(target.get('title') or item.title)
        context=[]; parent=target; visited=set()
        for _ in range(6):
            pid=parent.get('parent')
            if not pid or pid in visited: break
            visited.add(pid); parent=self.get(pid) or {}
            if parent.get('deleted') or parent.get('dead'): continue
            context.append('PARENT '+str(pid)+': '+plain(parent.get('title','')+' '+parent.get('text',''))[:2400])
            if parent.get('type')=='story':
                item.thread='hn:'+str(pid)
                if not item.title or item.title=='HN discussion': item.title=plain(parent.get('title',''))
                break
        kids=target.get('kids',[])[:4]
        for kid in kids:
            child=self.get(kid) or {}
            if child and not child.get('deleted') and not child.get('dead'):
                context.append('REPLY '+str(kid)+': '+plain(child.get('text',''))[:1600])
        item.context='\n\n'.join(context)+'\n[Ограниченная выборка: не вся ветка; отсутствие ответа не доказано.]'
        return item

class Reddit:
    def headers(self):
        if os.getenv('REDDIT_APPROVED')!='1':
            raise RemoteError('Reddit disabled: explicit API/commercial approval is required.')
        token=os.getenv('REDDIT_ACCESS_TOKEN','')
        if not token: raise RemoteError('Missing approved Reddit OAuth access token.')
        return {'Authorization':'Bearer '+token,'User-Agent':os.getenv('REDDIT_USER_AGENT','ThreadScout/0.1 by /u/REPLACE_ME')}
    def search(self, communities):
        headers=self.headers()
        for sub in communities:
            if not sub.replace('_','').isalnum(): raise ValueError('Invalid community name.')
            # Scan a bounded recent sample, not an exhaustive historical search.
            for path in (f'/r/{sub}/new',f'/r/{sub}/comments'):
                data=request_json('https://oauth.reddit.com'+path+'?limit=50&raw_json=1',headers=headers)
                for row in data.get('data',{}).get('children',[]):
                    d=row.get('data',{})
                    if d.get('over_18') or d.get('removed_by_category') or d.get('body') in ('[deleted]','[removed]'): continue
                    if not d.get('permalink'): continue
                    key,url=canonical('https://www.reddit.com'+d['permalink'])
                    yield Item(key,'reddit',url,plain(d.get('title') or d.get('link_title') or 'Reddit discussion'),
                        plain(d.get('selftext') or d.get('body') or ''),float(d.get('created_utc') or time.time()),
                        'reddit:'+str(d.get('link_id') or d.get('name')),sub)
                time.sleep(2)
    def refresh(self,item):
        fullname=item.key.split(':',1)[1]
        data=request_json('https://oauth.reddit.com/api/info?'+urlencode({'id':fullname,'raw_json':1}),headers=self.headers())
        children=data.get('data',{}).get('children',[])
        item.checked=time.time()
        if not children:
            item.available=False; item.text=''; item.context=''; return item
        d=children[0]['data']
        body=d.get('body') or d.get('selftext') or ''
        item.available=not (body in ('[deleted]','[removed]') or d.get('removed_by_category') or d.get('locked') or d.get('archived'))
        item.title=plain(d.get('title') or d.get('link_title') or item.title)
        item.created=float(d.get('created_utc') or item.created)
        item.thread='reddit:'+str(d.get('link_id') or d.get('name') or fullname)
        item.community=d.get('subreddit',item.community)
        item.text=plain(body) if item.available else ''
        item.context='Правила сабреддита и соседние ответы в этой версии автоматически не проверены.'
        return item
