"""Local state and deterministic matching. Python 3.11+, standard library only."""
from __future__ import annotations
import hashlib
import html
import json
import re
import sqlite3
import time
from dataclasses import dataclass, asdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, parse_qs

class TextParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.hidden = [], 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'): self.hidden += 1
        if tag in ('p', 'br', 'li'): self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script', 'style'): self.hidden = max(0, self.hidden - 1)
    def handle_data(self, data):
        if not self.hidden: self.parts.append(data)

def plain(value: str) -> str:
    parser = TextParser()
    parser.feed(value or '')
    return re.sub(r'[ \t]+', ' ', ''.join(parser.parts)).strip()

def contains(text: str, term: str) -> bool:
    return bool(re.search(r'(?<!\w)' + re.escape(term.casefold()) + r'(?!\w)', text.casefold()))

def canonical(url: str) -> tuple[str, str]:
    """Allow only public discussion permalinks; never fetch arbitrary URLs."""
    u = urlsplit(url.strip())
    if u.scheme != 'https' or u.username or u.password or u.port not in (None, 443):
        raise ValueError('Use an HTTPS discussion permalink.')
    if u.hostname == 'news.ycombinator.com' and u.path == '/item':
        value = parse_qs(u.query).get('id', [''])[0]
        if value.isdigit(): return 'hn:' + value, 'https://news.ycombinator.com/item?id=' + value
    if u.hostname in ('reddit.com', 'www.reddit.com', 'old.reddit.com'):
        m = re.fullmatch(r'/r/([A-Za-z0-9_]+)/comments/([a-z0-9]+)(?:/([^/]*))?(?:/([a-z0-9]+))?/?', u.path)
        if m:
            sub, post, slug, comment = m.groups()
            tail = f'/{comment}' if comment else ''
            key = 'reddit:' + ('t1_' + comment if comment else 't3_' + post)
            return key, f'https://www.reddit.com/r/{sub}/comments/{post}/{slug or "_"}{tail}/'
    raise ValueError('Use a full HN or Reddit discussion URL, not a share/short link.')

@dataclass
class Item:
    key: str
    platform: str
    url: str
    title: str
    text: str
    created: float
    thread: str
    community: str = ''
    context: str = ''
    checked: float = 0
    available: bool = True
    demo: bool = False

class Store:
    def __init__(self, path: str | Path):
        self.path = str(path)
        if self.path != ':memory:': Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(self.path, timeout=20)
        self.db.row_factory = sqlite3.Row
        self.db.executescript('''
        PRAGMA journal_mode=WAL;
        CREATE TABLE IF NOT EXISTS items (
          key TEXT PRIMARY KEY, data TEXT NOT NULL, score REAL NOT NULL,
          state TEXT NOT NULL DEFAULT 'new', notified REAL NOT NULL DEFAULT 0,
          wake REAL NOT NULL DEFAULT 0, first_seen REAL NOT NULL);
        CREATE TABLE IF NOT EXISTS drafts (
          key TEXT PRIMARY KEY, human TEXT NOT NULL DEFAULT '', version INTEGER NOT NULL DEFAULT 0);
        CREATE TABLE IF NOT EXISTS kv (key TEXT PRIMARY KEY, value TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS feedback (key TEXT NOT NULL, action TEXT NOT NULL, at REAL NOT NULL);
        CREATE TABLE IF NOT EXISTS tombstones (key TEXT PRIMARY KEY, at REAL NOT NULL);
        ''')
        self.db.commit()
    def close(self): self.db.close()
    def set(self, key, value):
        self.db.execute('INSERT OR REPLACE INTO kv VALUES (?,?)', (key, json.dumps(value)))
        self.db.commit()
    def get(self, key, default=None):
        r = self.db.execute('SELECT value FROM kv WHERE key=?', (key,)).fetchone()
        return json.loads(r[0]) if r else default
    def add(self, item: Item, score: float) -> bool:
        if self.db.execute('SELECT 1 FROM tombstones WHERE key=?', (item.key,)).fetchone(): return False
        exists = self.db.execute('SELECT 1 FROM items WHERE key=?', (item.key,)).fetchone()
        if not item.available:
            item.text = ''; item.context = ''
            self.db.execute('DELETE FROM kv WHERE key=?', ('brief:'+item.key,))
        self.db.execute('''INSERT INTO items(key,data,score,first_seen) VALUES(?,?,?,?)
          ON CONFLICT(key) DO UPDATE SET data=excluded.data,score=excluded.score''',
          (item.key, json.dumps(asdict(item), ensure_ascii=False), score, time.time()))
        self.db.commit()
        return not bool(exists)
    def item(self, key: str) -> Item:
        r = self.db.execute('SELECT data FROM items WHERE key=?', (key,)).fetchone()
        if not r: raise ValueError('Item expired or not found.')
        return Item(**json.loads(r[0]))
    def candidates(self, limit=3, min_score=35, max_age_hours=72) -> list[Item]:
        rows = self.db.execute("SELECT data FROM items WHERE state='new' AND notified=0 AND wake<=? AND score>=? ORDER BY score DESC", (time.time(), min_score))
        chosen, threads = [], set()
        for row in rows:
            item = Item(**json.loads(row[0]))
            if item.demo or not item.available or item.created < time.time() - max_age_hours * 3600: continue
            if item.thread in threads: continue
            chosen.append(item); threads.add(item.thread)
            if len(chosen) >= limit: break
        return chosen
    def action(self, key: str, action: str):
        self.item(key)
        if action not in ('skip', 'later', 'done'): raise ValueError('Unknown action.')
        state = 'new' if action == 'later' else action
        self.db.execute('UPDATE items SET state=?,wake=?,notified=? WHERE key=?',
                        (state, time.time()+86400 if action=='later' else 0, 0, key))
        self.db.execute('INSERT INTO feedback VALUES(?,?,?)', (key,action,time.time()))
        self.db.commit()
    def delivered(self, key):
        self.db.execute('UPDATE items SET notified=? WHERE key=?', (time.time(),key)); self.db.commit()
    def draft(self, key):
        self.item(key)
        r = self.db.execute('SELECT human,version FROM drafts WHERE key=?', (key,)).fetchone()
        return dict(r) if r else {'human':'', 'version':0}
    def save(self, key: str, text: str, version: int | None = None):
        if not text.strip() or len(text) > 3500: raise ValueError('Write 1–3500 characters.')
        self.item(key)
        self.db.execute('INSERT OR IGNORE INTO drafts(key) VALUES(?)', (key,))
        if version is None: version = self.draft(key)['version']
        cur = self.db.execute('UPDATE drafts SET human=?,version=version+1 WHERE key=? AND version=?', (text,key,version))
        if not cur.rowcount:
            self.db.rollback(); raise ValueError('Draft changed elsewhere; reopen it before saving.')
        self.db.commit()
        return self.draft(key)
    def purge(self, days=7):
        keys = [r[0] for r in self.db.execute('SELECT key FROM items WHERE first_seen<?',(time.time()-days*86400,))]
        for key in keys:
            self.db.execute('INSERT OR REPLACE INTO tombstones VALUES(?,?)',(key,time.time()))
            self.db.execute('DELETE FROM items WHERE key=?',(key,))
            self.db.execute('DELETE FROM drafts WHERE key=?',(key,))
            self.db.execute('DELETE FROM kv WHERE key=?',('brief:'+key,))
        # Reply bindings and brief caches contain no copies after item expiry.
        for r in list(self.db.execute("SELECT key,value FROM kv WHERE key LIKE 'reply:%'")):
            if json.loads(r['value']) in keys: self.db.execute('DELETE FROM kv WHERE key=?',(r['key'],))
        self.db.execute('DELETE FROM tombstones WHERE at<?',(time.time()-90*86400,))
        self.db.execute('DELETE FROM feedback WHERE at<?',(time.time()-90*86400,))
        self.db.commit()
    def cancel_replies(self):
        self.db.execute("DELETE FROM kv WHERE key LIKE 'reply:%'"); self.db.commit()
    def status(self):
        return {r[0]:r[1] for r in self.db.execute('SELECT state,COUNT(*) FROM items GROUP BY state')}

def match(item: Item, profile: dict) -> dict:
    text = item.title + '\n' + item.text
    topics = [t for t in profile['topics'] if any(contains(text,k) for k in t['terms'])]
    mentions = [x for x in profile['mentions'] if contains(text,x)]
    intent = any(contains(text,k) for k in ('how do','how to','recommend','looking for','struggling','anyone tried','experience with','help')) or '?' in text
    topic_ids = {t['id'] for t in topics}
    assets = [a for a in profile['assets'] if topic_ids.intersection(a['topics'])]
    age = max(0,(time.time()-item.created)/3600)
    score = min(100, 22*min(2,len(topics)) + 18*intent + 42*bool(mentions) + (12 if age<24 else 4 if age<72 else 0))
    if not topics and not mentions: score = 0
    return {'score':score,'topics':[t['id'] for t in topics], 'mentions':mentions,'assets':assets[:3],
            'question':'Какой конкретный пример из твоей практики отвечает на вопрос, и где границы применимости?',
            'why':'; '.join(t['reason'] for t in topics) or ('Упоминание твоего проекта' if mentions else 'Совпадений с профилем пока нет')}

def fingerprint(item: Item) -> str:
    return hashlib.sha256(json.dumps(asdict(item),sort_keys=True).encode()).hexdigest()
