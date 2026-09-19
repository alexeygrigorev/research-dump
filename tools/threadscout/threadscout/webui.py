"""Optional Telegram Mini App. Bind locally; supply your own HTTPS tunnel.
Not a public production HTTP server. No endpoint can publish a social comment.
"""
from __future__ import annotations
import hashlib
import hmac
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import time
from urllib.parse import parse_qsl, urlsplit
from .core import Store

def verify_init_data(raw: str, token: str, owner: int, now=None) -> dict:
    if not raw or len(raw)>10000 or owner<=0: raise ValueError('Unauthorized.')
    pairs=parse_qsl(raw,keep_blank_values=True,strict_parsing=True)
    if len({k for k,_ in pairs})!=len(pairs): raise ValueError('Duplicate authentication fields.')
    values=dict(pairs); signature=values.pop('hash','')
    secret=hmac.new(b'WebAppData',token.encode(),hashlib.sha256).digest()
    check='\n'.join(k+'='+values[k] for k in sorted(values))
    expected=hmac.new(secret,check.encode(),hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected,signature): raise ValueError('Unauthorized.')
    age=(time.time() if now is None else now)-int(values.get('auth_date','0'))
    if age < -30 or age>3600: raise ValueError('Session expired; reopen the editor from Telegram.')
    user=json.loads(values.get('user','{}'))
    if user.get('id')!=owner: raise ValueError('Unauthorized.')
    return user

def serve(cfg,profile,tg):
    public=os.getenv('TELEGRAM_WEBAPP_URL','').rstrip('/')
    origin=urlsplit(public)
    if origin.scheme!='https' or not origin.netloc or origin.path not in ('','/'):
        raise ValueError('Set TELEGRAM_WEBAPP_URL to the HTTPS origin of your local tunnel.')
    allowed_origin=origin.scheme+'://'+origin.netloc
    page=(Path(__file__).parent/'editor.html').read_bytes()
    class Handler(BaseHTTPRequestHandler):
        def log_message(self,*args): pass
        def reply(self,code,data,kind='application/json; charset=utf-8'):
            blob=data if isinstance(data,bytes) else json.dumps(data,ensure_ascii=False).encode()
            self.send_response(code); self.send_header('Content-Type',kind)
            self.send_header('Content-Length',str(len(blob))); self.send_header('Cache-Control','no-store')
            self.send_header('X-Content-Type-Options','nosniff'); self.send_header('Referrer-Policy','no-referrer')
            self.end_headers(); self.wfile.write(blob)
        def do_GET(self):
            if urlsplit(self.path).path not in ('/','/index.html'): self.reply(404,{'error':'Not found'}); return
            self.reply(200,page,'text/html; charset=utf-8')
        def do_POST(self):
            try:
                if self.headers.get('Origin')!=allowed_origin: raise ValueError('Origin mismatch.')
                n=int(self.headers.get('Content-Length','0'))
                if not 0<n<=20000: raise ValueError('Invalid request size.')
                data=json.loads(self.rfile.read(n)); verify_init_data(data.get('init_data',''),tg.token,tg.owner)
                key=data.get('key','')
                if not isinstance(key,str) or len(key)>80: raise ValueError('Invalid item.')
                db=Store(cfg['db'])
                try:
                    item=db.item(key)
                    if self.path=='/api/save':
                        text=data.get('text'); version=data.get('version')
                        if not isinstance(text,str) or type(version) is not int: raise ValueError('Invalid draft.')
                        saved=db.save(key,text,version); self.reply(200,saved)
                    elif self.path=='/api/item':
                        self.reply(200,{'key':key,'title':item.title,'original':item.text,
                            'context':item.context,'platform':item.platform,'url':item.url,
                            'brief':db.get('brief:'+key,{}),'draft':db.draft(key)})
                    else: self.reply(404,{'error':'Not found'})
                finally: db.close()
            except (ValueError,KeyError,TypeError): self.reply(400,{'error':'Invalid or expired request; reopen the editor.'})
    server=ThreadingHTTPServer(('127.0.0.1',8765),Handler)
    print('Mini App listening on 127.0.0.1:8765. HTTPS tunnel and Telegram client test are required.')
    try: server.serve_forever()
    finally: server.server_close()
