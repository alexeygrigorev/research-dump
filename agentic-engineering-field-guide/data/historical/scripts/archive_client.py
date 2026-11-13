"""Polite clients for free web archives (Wayback CDX, Common Crawl index).

Rate-limited (>= MIN_INTERVAL s between requests per host), retries with
exponential backoff on 429/5xx and on the Internet Archive "Temporarily
Offline" page, which is what CDX returns when a query is too heavy.
"""
import json
import re
import time
import urllib.parse
import urllib.request

UA = "research-dump-historical-snapshots/0.1 (polite archive research; 1 req/s)"
MIN_INTERVAL = {"web.archive.org": 1.5, "index.commoncrawl.org": 1.0, "data.commoncrawl.org": 0.15}
_last = {}
import threading
_lock = threading.Lock()


class ArchiveError(Exception):
    pass


def _wait(host):
    gap = MIN_INTERVAL.get(host, 1.0)
    with _lock:
        now = time.time()
        slot = max(now, _last.get(host, 0) + gap)
        _last[host] = slot
    if slot > now:
        time.sleep(slot - now)


def get(url, headers=None, retries=6, timeout=120, binary=False):
    host = urllib.parse.urlparse(url).netloc
    h = {"User-Agent": UA}
    if headers:
        h.update(headers)
    delay = 10
    last_err = None
    for attempt in range(retries):
        _wait(host)
        try:
            req = urllib.request.Request(url, headers=h)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                body = r.read()
            if body[:2] == b"\x1f\x8b" and not binary:
                # Wayback id_ replays the original Content-Encoding: gzip body as-is
                import gzip
                body = gzip.decompress(body)
            if not binary:
                text = body.decode("utf-8", "replace")
                if "Temporarily Offline" in text[:3000] and "Internet Archive" in text[:3000]:
                    raise ArchiveError("IA temporarily offline")
                return text
            return body
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code == 404:
                raise
            if e.code not in (429, 500, 502, 503, 504):
                raise
        except (ArchiveError, urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
            last_err = e
        time.sleep(delay)
        delay = min(delay * 2, 300)
    raise ArchiveError(f"giving up on {url}: {last_err}")


def cdx(params):
    """Wayback CDX query. Returns list of dict rows (output=json)."""
    p = dict(params)
    p.setdefault("output", "json")
    url = "https://web.archive.org/cdx/search/cdx?" + urllib.parse.urlencode(p, doseq=True)
    text = get(url)
    if p.get("showNumPages"):
        return int(re.findall(r"\d+", text)[-1])
    if not text.strip():
        return []
    rows = json.loads(text)
    if not rows:
        return []
    head = rows[0]
    return [dict(zip(head, r)) for r in rows[1:]]


def cc_index(crawl, params):
    p = dict(params)
    p.setdefault("output", "json")
    url = f"https://index.commoncrawl.org/{crawl}-index?" + urllib.parse.urlencode(p, doseq=True)
    try:
        text = get(url)
    except urllib.error.HTTPError as e:
        if e.code == 404:  # "No Captures found"
            return [] if not p.get("showNumPages") else 0
        raise
    if p.get("showNumPages"):
        return json.loads(text)
    out = []
    for l in text.splitlines():
        try:
            out.append(json.loads(l))
        except ValueError:
            pass
    return out


def wayback_raw(timestamp, original):
    """Original archived bytes (id_ = no Wayback toolbar/rewrite)."""
    return get(f"https://web.archive.org/web/{timestamp}id_/{original}")


def cc_record(filename, offset, length):
    import gzip
    rng = f"bytes={int(offset)}-{int(offset) + int(length) - 1}"
    raw = get("https://data.commoncrawl.org/" + filename, headers={"Range": rng}, binary=True)
    data = gzip.decompress(raw)
    # WARC record: warc headers \r\n\r\n http headers \r\n\r\n body
    parts = data.split(b"\r\n\r\n", 2)
    return parts[2].decode("utf-8", "replace") if len(parts) == 3 else ""
