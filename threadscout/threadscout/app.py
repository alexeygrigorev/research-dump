"""Telegram-first personal radar. No social-network publishing functions exist."""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict
from datetime import datetime
import html
import json
import os
from pathlib import Path
import shutil
import socket
import sys
import threading
import time
from zoneinfo import ZoneInfo
from .core import Item, Store, canonical, match
from .sources import HackerNews, Reddit, request_json, RemoteError

ROOT=Path(__file__).resolve().parent.parent

def load_env(path):
    if not Path(path).exists(): return
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        line=line.strip()
        if not line or line.startswith('#'): continue
        key,sep,value=line.partition('=')
        if sep and key.replace('_','').isalnum(): os.environ.setdefault(key,value.strip().strip('\"\''))

def settings():
    load_env(ROOT/'.env')
    cfg=json.loads((ROOT/'config.json').read_text(encoding='utf-8'))
    cfg['db']=str(Path(os.getenv('THREADSCOUT_DB',str(ROOT/'data'/'threadscout.sqlite3'))).expanduser())
    if not 1<=cfg['digest_limit']<=3: raise ValueError('digest_limit must be 1–3.')
    if cfg['scan_interval_minutes']<30: raise ValueError('Use a scan interval of at least 30 minutes.')
    datetime.strptime(cfg['digest_time'], '%H:%M'); ZoneInfo(cfg['timezone'])
    return cfg,json.loads((ROOT/'profile.json').read_text(encoding='utf-8'))

class Telegram:
    def __init__(self):
        self.token=os.getenv('TELEGRAM_BOT_TOKEN','')
        self.owner=int(os.getenv('TELEGRAM_OWNER_ID','0'))
        if not self.token: raise ValueError('Set TELEGRAM_BOT_TOKEN locally in .env.')
    def call(self,method,**data):
        allowed={'getMe','getWebhookInfo','getUpdates','sendMessage','answerCallbackQuery'}
        if method not in allowed: raise ValueError('Telegram method not allowed.')
        result=request_json('https://api.telegram.org/bot'+self.token+'/'+method,payload=data,timeout=40)
        if not result.get('ok'): raise RemoteError('Telegram rejected the request.')
        return result['result']
    def send(self,text,keyboard=None,force=False):
        if self.owner<=0: raise ValueError('Set TELEGRAM_OWNER_ID using the whoami command.')
        args={'chat_id':self.owner,'text':text,'parse_mode':'HTML','link_preview_options':{'is_disabled':True}}
        if keyboard: args['reply_markup']={'inline_keyboard':keyboard}
        if force: args['reply_markup']={'force_reply':True,'selective':True}
        return self.call('sendMessage',**args)

def authorized(update,owner):
    cb=update.get('callback_query')
    msg=cb.get('message',{}) if cb else update.get('message',{})
    sender=cb.get('from',{}) if cb else msg.get('from',{})
    return owner>0 and sender.get('id')==owner and msg.get('chat',{}).get('id')==owner and msg.get('chat',{}).get('type')=='private'

def chunks(text,size=1800):
    for start in range(0,len(text),size): yield text[start:start+size]

def keyboard(item):
    key=item.key
    rows=[[{'text':'Контекст','callback_data':'context|'+key},{'text':'Почему я','callback_data':'brief|'+key}],
          [{'text':'Написать самому','callback_data':'write|'+key},{'text':'Мой текст','callback_data':'copy|'+key}],
          [{'text':'Пропустить','callback_data':'skip|'+key},{'text':'Завтра','callback_data':'later|'+key},{'text':'Готово','callback_data':'done|'+key}]]
    if not item.demo: rows.append([{'text':'Открыть обсуждение / опубликовать вручную','url':item.url}])
    mini=os.getenv('TELEGRAM_WEBAPP_URL','').rstrip('/')
    if mini and mini.startswith('https://'):
        from urllib.parse import quote
        rows.append([{'text':'Редактор: оригинал + мой ответ','web_app':{'url':mini+'/?item='+quote(key)}}])
    return rows

def render(item,profile):
    m=match(item,profile)
    esc=lambda x:html.escape(str(x))
    return (f'<b>{"ДЕМО · " if item.demo else ""}{esc(item.platform.upper())} · {esc(item.title[:170])}</b>\n\n'
            f'{esc(item.text[:650])}\n\n<b>Почему тебе:</b> {esc(m["why"][:300])}\n'
            f'<b>Вопрос тебе:</b> {esc(m["question"])}\n'
            '<b>Ссылка:</b> по умолчанию не добавлять. Правила и уместность не подтверждены.\n'
            f'<b>Контекст:</b> {"проверен частично" if item.checked else "ещё не проверен"}. '
            'Это приватная справка, не текст ответа.')

def refresh(item):
    if item.demo: return item
    return (HackerNews() if item.platform=='hn' else Reddit()).refresh(item)

def scan(cfg,profile):
    store=Store(cfg['db']); report={}; added=0
    try:
        collectors=[('hn',HackerNews().search(cfg['hn_queries'],cfg['lookback_hours']))]
        if os.getenv('REDDIT_APPROVED')=='1': collectors.append(('reddit',Reddit().search(cfg['reddit_communities'])))
        else: report['reddit']='disabled: approval required'
        for name,items in collectors:
            count=0
            try:
                for item in items:
                    m=match(item,profile)
                    if m['score']>=cfg['min_score']:
                        count+=1; added+=store.add(item,m['score'])
                report[name]={'ok':True,'matched':count,'at':time.time()}
            except (RemoteError,ValueError,KeyError,TypeError) as exc:
                report[name]={'ok':False,'error':str(exc)[:180],'at':time.time()}
        store.purge(cfg['retention_days']); store.set('scan',report)
        return {'added':added,'sources':report}
    finally: store.close()

def digest(cfg,profile,tg,manual=False):
    store=Store(cfg['db']); sent=0; failures=[]
    try:
        for item in store.candidates(cfg['digest_limit']*3,cfg['min_score'],cfg['max_age_hours']):
            try:
                item=refresh(item); store.add(item,match(item,profile)['score'])
                if not item.available:
                    store.action(item.key,'skip'); continue
                tg.send(render(item,profile),keyboard(item)); store.delivered(item.key); sent+=1
                if sent>=cfg['digest_limit']: break
            except (RemoteError,ValueError) as exc: failures.append(str(exc))
        if failures: tg.send('Часть источников недоступна. Это не означает, что обсуждений нет. Проверь /status.')
        elif manual and not sent: tg.send('Новых подходящих карточек нет. Состояние сборщиков: /status.')
        store.set('digest',{'at':time.time(),'sent':sent,'errors':failures})
        return sent
    finally: store.close()

HELP='''<b>ThreadScout</b> — персональный радар Reddit и HN.
/digest — до трёх новых карточек
/scan — обновить источники
/status — состояние и ограничения
/demo — демонстрационные карточки
/add URL — добавить обсуждение; Reddit без доступа сохраняется как закладка
/cancel — отменить все предыдущие запросы ввода
После «Написать самому» ответь на сообщение бота своим текстом.
Публикации, голосования и личные сообщения на площадках отключены и не реализованы.
Для HN не копируй и не перефразируй AI-текст: пиши ответ самостоятельно.'''

def show_copy(store,tg,key):
    draft=store.draft(key); text=draft['human']
    if not text: tg.send('Твоего текста пока нет. Нажми «Написать самому».'); return
    buttons=[]
    if len(text)<=256: buttons=[[{'text':'Скопировать мой текст','copy_text':{'text':text}}]]
    for part in chunks(text,1500): tg.send('<pre>'+html.escape(part)+'</pre>')
    if buttons: tg.send('Копируется только твой текст, без справки.',buttons)
    else: tg.send('Для длинного ответа используй копирование блока в Telegram или кнопку редактора. Нативная кнопка ограничена 256 символами.')

def explain(cfg,profile,tg,key):
    store=Store(cfg['db'])
    try:
        item=refresh(store.item(key)); store.add(item,match(item,profile)['score'])
        if not item.available: tg.send('Обсуждение удалено или недоступно.'); return
        m=match(item,profile)
        data={'why':m['why'],'question':m['question'],'caveat':'Не вся ветка проверена; уместность ссылки не подтверждена.','asset_ids':[a['id'] for a in m['assets']]}
        if os.getenv('USE_CODEX')=='1':
            from .codex import brief
            try: data=brief(item,profile)
            except (RuntimeError,ValueError,OSError) as exc: data['caveat']+=' '+str(exc)
        store.set('brief:'+key,data)
        text='\n\n'.join((data['why'],data['question'],data['caveat']))
        for part in chunks(text): tg.send(html.escape(part))
        assets={a['id']:a for a in profile['assets']}
        for ident in data['asset_ids'][:3]:
            a=assets[ident]
            tg.send(html.escape(a['title']+' · '+a['access']+'\n'+a['use_when']),[[{'text':'Мой материал (не рекомендация вставить ссылку)','url':a['url']}]])
    finally: store.close()

def demo_items():
    # Invented examples only, never presented as live opportunities.
    return [Item('hn:demo','hn','','DEMO: A small persistent search system?',
                 'How do I add text search and RAG to a small Python project without running another server?',time.time(),'demo:1',demo=True),
            Item('reddit:demo','reddit','','DEMO: How do I finish my first ML project?',
                 'Looking for a project-based machine learning course and deployment advice.',time.time(),'demo:2','learnmachinelearning',demo=True)]

def handle(update,cfg,profile,tg,pool):
    if not authorized(update,tg.owner): return
    store=Store(cfg['db'])
    try:
        cb=update.get('callback_query')
        if cb:
            tg.call('answerCallbackQuery',callback_query_id=cb['id'])
            action,sep,key=cb.get('data','').partition('|')
            if not sep: return
            item=store.item(key)
            if action in ('skip','later','done'):
                store.action(key,action); tg.send('Сохранено. «Готово» — твоя отметка, а не подтверждение публикации.'); return
            if action=='context':
                item=refresh(item); store.add(item,match(item,profile)['score'])
                text=(item.title+'\n\n'+item.text+'\n\n'+item.context) if item.available else 'Удалено/недоступно.'
                for part in chunks(text[:9000]): tg.send(html.escape(part))
            elif action=='brief':
                tg.send('Готовлю приватную справку, не комментарий.'); pool.submit(explain,cfg,profile,tg,key)
            elif action=='write':
                prompt=tg.send('Напиши ответ самостоятельно. Для HN — без AI-перевода, переписывания и готовых формулировок. Ответь именно на это сообщение.',force=True)
                store.set('reply:'+str(prompt['message_id']),key)
            elif action=='copy': show_copy(store,tg,key)
            return
        msg=update['message']; text=msg.get('text','')
        if not text:
            tg.send('В этой версии принимается текст. Для HN лучше набрать его самостоятельно; голосовые ещё не поддерживаются.'); return
        if text.startswith('/cancel'):
            store.cancel_replies(); tg.send('Предыдущие запросы ввода отменены.'); return
        ref=msg.get('reply_to_message',{}).get('message_id')
        key=store.get('reply:'+str(ref)) if ref else None
        if key and not text.startswith('/'):
            store.save(key,text); tg.send('Сохранён твой текст. Ничего не опубликовано.'); show_copy(store,tg,key); return
        if text.startswith('/demo'):
            for item in demo_items():
                store.add(item,match(item,profile)['score']); tg.send(render(item,profile),keyboard(item))
        elif text.startswith('/digest'): pool.submit(digest,cfg,profile,tg,True)
        elif text.startswith('/scan'):
            tg.send('Запрос обновления принят. Результат будет виден в /status; карточки — /digest.'); pool.submit(scan,cfg,profile)
        elif text.startswith('/status'):
            status={'queue':store.status(),'last_scan':store.get('scan'),'last_digest':store.get('digest'),'worker_error':store.get('worker_error'),
                    'codex':os.getenv('USE_CODEX')=='1','reddit_enabled':os.getenv('REDDIT_APPROVED')=='1','publishing':False}
            for part in chunks(json.dumps(status,ensure_ascii=False,indent=2)): tg.send('<pre>'+html.escape(part)+'</pre>')
        elif text.startswith('/add '):
            key,url=canonical(text[5:].strip()); platform=key.split(':')[0]
            item=Item(key,platform,url,'HN discussion' if platform=='hn' else 'Reddit bookmark','',time.time(),key)
            if platform=='hn' or os.getenv('REDDIT_APPROVED')=='1': item=refresh(item)
            else:
                item.context='Только закладка. Reddit Pro не экспортируется, чужой текст не загружается.'
            store.add(item,max(cfg['min_score'],match(item,profile)['score'])); tg.send(render(item,profile),keyboard(item))
        else: tg.send(HELP)
    finally: store.close()

class Jobs:
    """Bounded background work, deduplicated per function/item; errors stay visible."""
    def __init__(self,cfg,tg):
        self.cfg=cfg; self.tg=tg; self.pool=ThreadPoolExecutor(max_workers=1)
        self.pending=set(); self.lock=threading.Lock()
    def __enter__(self): return self
    def __exit__(self,*args): self.pool.shutdown(wait=True,cancel_futures=True)
    def submit(self,fn,*args):
        label=fn.__name__+(':'+str(args[-1]) if fn is explain else '')
        with self.lock:
            if label in self.pending or len(self.pending)>=8: return None
            self.pending.add(label)
        def work():
            try: return fn(*args)
            except Exception as exc:
                db=Store(self.cfg['db'])
                try: db.set('worker_error',{'job':label,'type':type(exc).__name__,'at':time.time()})
                finally: db.close()
                try: self.tg.send('Задача не завершилась. Проверь /status; автоматической публикации нет.')
                except RemoteError: pass
            finally:
                with self.lock: self.pending.discard(label)
        return self.pool.submit(work)

def scheduled_digest(cfg,profile,tg,day):
    digest(cfg,profile,tg)
    db=Store(cfg['db'])
    try: db.set('scheduled_day',day)
    finally: db.close()

def run(cfg,profile,tg):
    if tg.owner<=0: raise ValueError('Run whoami, then set TELEGRAM_OWNER_ID.')
    if tg.call('getWebhookInfo').get('url'): raise ValueError('This token has a webhook. Use a separate bot token; do not disrupt another bot.')
    guard=socket.socket()
    try: guard.bind(('127.0.0.1',8766))
    except OSError: raise ValueError('Another instance is running, or local port 8766 is occupied.') from None
    zone=ZoneInfo(cfg['timezone']); store=Store(cfg['db']); next_scan=0
    tg.send('ThreadScout запущен. /demo для проверки интерфейса, /digest для новых карточек. Публикация отключена.')
    with guard, Jobs(cfg,tg) as pool:
        while True:
            now=time.time(); local=datetime.now(zone); day=local.date().isoformat()
            if now>=next_scan:
                pool.submit(scan,cfg,profile); next_scan=now+cfg['scan_interval_minutes']*60
            if local.strftime('%H:%M')>=cfg['digest_time'] and store.get('scheduled_day')!=day:
                pool.submit(scheduled_digest,cfg,profile,tg,day)
            try:
                updates=tg.call('getUpdates',offset=store.get('offset',0),timeout=25,allowed_updates=['message','callback_query'])
                for update in updates:
                    try: handle(update,cfg,profile,tg,pool)
                    except (ValueError,RemoteError,KeyError,TypeError) as exc:
                        if authorized(update,tg.owner): tg.send(html.escape(str(exc)[:350]))
                    finally: store.set('offset',update['update_id']+1)
            except RemoteError:
                print('Telegram unavailable; retrying after cooldown.',flush=True); time.sleep(60)

def main():
    parser=argparse.ArgumentParser(description='ThreadScout: personal Reddit/HN monitoring, no automatic publishing.')
    parser.add_argument('command',choices=['doctor','whoami','demo','scan','digest','run','serve'])
    args=parser.parse_args(); cfg,profile=settings()
    if args.command=='doctor':
        print(json.dumps({'python':sys.version.split()[0],'codex_installed':bool(shutil.which('codex')),
            'token_configured':bool(os.getenv('TELEGRAM_BOT_TOKEN')),'owner_configured':int(os.getenv('TELEGRAM_OWNER_ID','0'))>0,
            'reddit_approved':os.getenv('REDDIT_APPROVED')=='1','timezone':cfg['timezone'],
            'network_tested':False,'publishing_implemented':False},indent=2)); return
    if args.command=='demo':
        for item in demo_items(): print(render(item,profile)+'\n')
        return
    if args.command=='scan': print(json.dumps(scan(cfg,profile),ensure_ascii=False,indent=2)); return
    tg=Telegram()
    if args.command=='whoami':
        if tg.call('getWebhookInfo').get('url'): raise ValueError('Use a separate bot token; webhook is active.')
        print('Send /start to your NEW bot. Showing only private chat/user numeric IDs.')
        for update in tg.call('getUpdates',timeout=25,allowed_updates=['message']):
            m=update.get('message',{})
            if m.get('chat',{}).get('type')=='private': print({'user_id':m.get('from',{}).get('id'),'chat_id':m['chat']['id']})
    elif args.command=='digest': digest(cfg,profile,tg,True)
    elif args.command=='serve':
        from .webui import serve
        serve(cfg,profile,tg)
    else: run(cfg,profile,tg)
