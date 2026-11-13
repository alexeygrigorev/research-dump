"""Fetch an archived page once and cache it gzipped under ../work/html/.

A capture ref is a dict with "src" = "cc" (filename, offset, length) or
"wb" (timestamp, original).
"""
import gzip, hashlib
from pathlib import Path
import archive_client as a

CACHE = Path(__file__).resolve().parent.parent / "work" / "html"
CACHE.mkdir(parents=True, exist_ok=True)


def key(ref):
    if ref["src"] == "cc":
        s = f"cc|{ref['filename']}|{ref['offset']}"
    else:
        s = f"wb|{ref['timestamp']}|{ref['original']}"
    return hashlib.sha1(s.encode()).hexdigest()


def fetch(ref):
    f = CACHE / (key(ref) + ".html.gz")
    if f.exists():
        return gzip.open(f, "rt", encoding="utf-8", errors="replace").read()
    if ref["src"] == "cc":
        html = a.cc_record(ref["filename"], ref["offset"], ref["length"])
    else:
        html = a.wayback_raw(ref["timestamp"], ref["original"])
    with gzip.open(f, "wt", encoding="utf-8") as fh:
        fh.write(html)
    return html
