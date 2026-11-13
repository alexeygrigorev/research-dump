"""Stage 1b (fast path): Common Crawl index rows for builtin.com/job/* read
straight from the ZipNum index files on data.commoncrawl.org.

index.commoncrawl.org is often overloaded (504s, ~40 s per query). The same
data sits in static files: cluster.idx (one line per 3000-row block, sorted by
SURT key) and cdx-NNNNN.gz (gzip members = blocks). We binary-search
cluster.idx with HTTP range reads, then range-read only the blocks that cover
`com,builtin)/job/`. ~30 small requests per crawl instead of 36 heavy ones.

  python stage1_cc_zipnum.py CC-MAIN-2026-04 CC-MAIN-2026-08 ...

Output: ../work/cc_job_cdx/<crawl>.jsonl (same fields as stage1_cc_dump.sh).
"""
import gzip, json, sys, urllib.request
from pathlib import Path
import archive_client as a

OUT = Path(__file__).resolve().parent.parent / "work" / "cc_job_cdx"
BASE = "https://data.commoncrawl.org/cc-index/collections/{c}/indexes/"
PREFIX = "com,builtin)/job/"
END = "com,builtin)/job0"  # first key after the prefix ('/' < '0')


def rng(url, start, end):
    return a.get(url, headers={"Range": f"bytes={start}-{end}"}, binary=True)


def size(url):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": a.UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return int(r.headers["Content-Length"])


def line_at(url, pos, total):
    """First complete line starting at or after byte pos."""
    chunk = rng(url, pos, min(pos + 4095, total - 1)).decode("utf-8", "replace")
    if pos > 0:
        nl = chunk.find("\n")
        if nl < 0:
            return None, None
        start = pos + nl + 1
        chunk = chunk[nl + 1:]
    else:
        start = pos
    line = chunk.split("\n", 1)[0]
    return start, line


def blocks(crawl):
    url = BASE.format(c=crawl) + "cluster.idx"
    total = size(url)
    lo, hi = 0, total
    # find last line whose key < PREFIX (the block containing the first match)
    while hi - lo > 8192:
        mid = (lo + hi) // 2
        _, line = line_at(url, mid, total)
        if line is None or line.split(" ", 1)[0] >= PREFIX:
            hi = mid
        else:
            lo = mid
    # read forward from lo until keys pass END
    out, prev, pos = [], None, lo
    while True:
        data = rng(url, pos, min(pos + 65535, total - 1)).decode("utf-8", "replace")
        lines = data.split("\n")
        if pos > 0 and pos == lo:
            lines = lines[1:]  # partial first line
        last_complete = lines[:-1] if pos + 65536 < total else lines
        for l in last_complete:
            if not l:
                continue
            key = l.split(" ", 1)[0]
            f = l.split("\t")
            if key < PREFIX:
                prev = f
                continue
            if prev is not None and not out:
                out.append(prev)
            if key >= END:
                return out
            out.append(f)
        if pos + 65536 >= total:
            return out
        pos = pos + len(data.encode("utf-8")) - len(lines[-1].encode("utf-8"))


def rows(crawl):
    for f in blocks(crawl):
        _, fname, off, length = f[0], f[1], int(f[2]), int(f[3])
        raw = rng(BASE.format(c=crawl) + fname, off, off + length - 1)
        for l in gzip.decompress(raw).decode("utf-8", "replace").splitlines():
            key, ts, js = l.split(" ", 2)
            if not key.startswith(PREFIX):
                continue
            j = json.loads(js)
            yield {"timestamp": ts, "url": j.get("url"), "status": j.get("status"), "mime": j.get("mime"),
                   "length": j.get("length"), "offset": j.get("offset"), "filename": j.get("filename")}


if __name__ == "__main__":
    for crawl in sys.argv[1:]:
        f = OUT / f"{crawl}.jsonl"
        if f.exists() and f.stat().st_size:
            continue
        rs = list(rows(crawl))
        tmp = f.with_suffix(".tmp")
        tmp.write_text("".join(json.dumps(r) + "\n" for r in rs))
        tmp.rename(f)
        print(crawl, len(rs), flush=True)
