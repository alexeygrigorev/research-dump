"""Index of archived builtin job-detail captures: job_id -> list of refs.

Sources: ../work/cc_job_cdx/*.jsonl (Common Crawl) and
../work/wayback_job_cdx/*.jsonl (Wayback). Only HTTP 200 HTML captures.
"""
import glob, json
from collections import defaultdict
from pathlib import Path
from roles import role_of, slug_of

W = Path(__file__).resolve().parent.parent / "work"
WINDOW = ("202507", "202611")


def load(window=WINDOW):
    idx = defaultdict(list)
    for f in sorted(glob.glob(str(W / "cc_job_cdx" / "*.jsonl"))):
        crawl = Path(f).stem
        for l in open(f):
            try:
                r = json.loads(l)
            except ValueError:
                continue
            if r.get("status") != "200" or "html" not in r.get("mime", "html"):
                continue
            slug, jid = slug_of(r["url"])
            m = r["timestamp"][:6]
            if not jid or not (window[0] <= m <= window[1]):
                continue
            idx[jid].append({"src": "cc", "crawl": crawl, "month": m, "timestamp": r["timestamp"], "url": r["url"],
                             "filename": r["filename"], "offset": r["offset"], "length": r["length"], "slug": slug})
    for f in sorted(glob.glob(str(W / "wayback_job_cdx" / "*.jsonl"))):
        for l in open(f):
            r = json.loads(l)
            if r.get("statuscode") != "200" or "html" not in r.get("mimetype", ""):
                continue
            slug, jid = slug_of(r["original"])
            m = r["timestamp"][:6]
            if not jid or not (window[0] <= m <= window[1]):
                continue
            idx[jid].append({"src": "wb", "month": m, "timestamp": r["timestamp"], "original": r["original"],
                             "url": r["original"], "slug": slug})
    for jid in idx:
        idx[jid].sort(key=lambda r: (r["timestamp"], r["src"]))
    return idx


def role_jobs(idx):
    return {jid: refs for jid, refs in idx.items() if role_of(refs[0]["slug"])}
