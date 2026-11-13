"""Stage 1f: read archived job pages of boards whose URL has no title/location
(Greenhouse, Ashby, Personio) and keep the parsed posting.

  python stage1_read_boards.py --boards greenhouse ashby --fraction 0.1 [--crawls CC-MAIN-2025-47 ...]

A FIXED random fraction of each board's distinct job pages is read in every crawl
(hash of the job key, so the same jobs are picked on re-runs). A fixed fraction
per board keeps the source mix the same from crawl to crawl by design, instead of
following whatever the crawler happened to capture (Alexey t3383u).

One reader, Common Crawl rate limit 1 request / 0.15 s: data.commoncrawl.org
answers 403 to this host above ~5 parallel readers.

Output: ../work/boards_read/<board>/<crawl>.jsonl.gz, one parsed record per line
(field-guide fields + role, countries, cities, month, archive_ref); rows with
"error" are retried on the next run.
"""
import argparse, gzip, hashlib, json, sys
from pathlib import Path

import archive_client as a
import jobposting_parse as jp
import measure_sources as ms
from roles import role_of

W = Path(__file__).resolve().parent.parent / "work"


def picked(key, fraction):
    h = int(hashlib.sha1(key.encode()).hexdigest()[:8], 16)
    return h < fraction * 0xFFFFFFFF


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--boards", nargs="+", default=["greenhouse", "ashby", "personio_de", "personio_com"])
    ap.add_argument("--fraction", type=float, default=0.1)
    ap.add_argument("--crawls", nargs="*")
    args = ap.parse_args()
    crawls = args.crawls or sorted(p.stem for p in (W / "cc_job_cdx").glob("*.jsonl"))
    for crawl in crawls:
        for board in args.boards:
            src = W / "cc_boards" / board / f"{crawl}.jsonl"
            if not src.exists():
                print(crawl, board, "no index dump", flush=True); continue
            byk = {}
            for l in open(src):
                r = json.loads(l)
                p = ms.parse_url(board, r["url"])
                if p and "html" in (r.get("mime") or "html"):
                    byk.setdefault(p[0], r)
            todo = {k: r for k, r in byk.items() if picked(k, args.fraction)}
            out = W / "boards_read" / board / f"{crawl}.jsonl.gz"
            out.parent.mkdir(parents=True, exist_ok=True)
            done = set()
            if out.exists():
                for l in gzip.open(out, "rt"):
                    x = json.loads(l)
                    if "error" not in x:
                        done.add(x["key"])
            n_new = n_scope = n_err = 0
            with gzip.open(out, "at", encoding="utf-8") as fh:
                for k, r in todo.items():
                    if k in done:
                        continue
                    try:
                        rec = jp.parse_any(a.cc_record(r["filename"], r["offset"], r["length"]), r["url"].split("?")[0], board)
                    except Exception as e:
                        n_err += 1
                        fh.write(json.dumps({"key": k, "error": str(e)[:100]}) + "\n")
                        if n_err >= 20 and n_err > n_new:  # blocked: stop instead of hammering
                            print("too many errors, stopping:", e, flush=True); sys.exit(2)
                        continue
                    rec = rec or {}
                    rec.update(key=k, board=board, crawl=crawl, month=r["timestamp"][:6],
                               archive_ref={"filename": r["filename"], "offset": r["offset"], "length": r["length"]},
                               role=role_of(rec.get("title")))
                    if not rec["role"]:
                        rec.pop("description", None)  # keep out-of-scope rows small
                    fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    n_new += 1; n_scope += bool(rec["role"])
            print(crawl, board, "pool", len(byk), "picked", len(todo), "read", n_new, "in_scope", n_scope, "errors", n_err, flush=True)


if __name__ == "__main__":
    main()
