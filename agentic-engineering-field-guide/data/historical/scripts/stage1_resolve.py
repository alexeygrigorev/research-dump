"""Stage 1e: resolve the city of every in-scope job-detail link.

Job URLs carry no location, so each in-scope link (slug matches a scoped role)
is read once from the archive and its JSON-LD location recorded. Pages land in
the shared cache, so stage 2 reuses them for free.

  python stage1_resolve.py cc        # Common Crawl links (range reads, fast)
  python stage1_resolve.py wb        # Wayback links (slow, 1 request / 1.5 s)
  python stage1_resolve.py wb 202612 # only one month

Output: ../work/resolved_<src>.jsonl, one row per (job_id, month).
"""
import json, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import builtin_parse, capture_index, fetch_cache
from roles import role_of

W = Path(__file__).resolve().parent.parent / "work"
CITIES = {"london": "London", "berlin": "Berlin", "newyork": "New York"}


def city_of(locs):
    for k, name in CITIES.items():
        if any(l.startswith(name + ",") or l == name for l in locs):
            return k
    return "other"


def resolve(task):
    jid, month, ref = task
    try:
        job = builtin_parse.parse_job_html(fetch_cache.fetch(ref))
    except Exception as e:
        return {"job_id": jid, "month": month, "src": ref["src"], "error": str(e)[:120]}
    locs = job.get("locations") or ([job["location"]] if job.get("location") else [])
    return {"job_id": jid, "month": month, "src": ref["src"], "timestamp": ref["timestamp"],
            "title": job.get("title"), "role": role_of(job.get("title")), "locations": locs,
            "city": city_of(locs), "posted_date": job.get("posted_date"),
            "has_description": bool(job.get("description")), "remote": job.get("remote")}


def main():
    src = sys.argv[1]
    only = set(sys.argv[2:])  # optional YYYYMM months; default all
    workers = 2 if src == "cc" else 1  # CC 403s this host above ~5 parallel readers
    out_f = W / f"resolved_{src}.jsonl"
    done = set()
    if out_f.exists():
        for l in open(out_f):
            r = json.loads(l)
            if "error" not in r:
                done.add((r["job_id"], r["month"]))
    idx = capture_index.load()
    tasks = []
    for jid, refs in idx.items():
        if not role_of(refs[0]["slug"]):
            continue
        for month in sorted({r["month"] for r in refs if r["src"] == src}):
            if (jid, month) in done or (only and month not in only):
                continue
            ref = [r for r in refs if r["src"] == src and r["month"] == month][0]
            tasks.append((jid, month, ref))
    print(src, "to resolve", len(tasks), "already", len(done), flush=True)
    with open(out_f, "a") as out, ThreadPoolExecutor(workers) as ex:
        for i, r in enumerate(ex.map(resolve, tasks)):
            out.write(json.dumps(r) + "\n"); out.flush()
            if i % 200 == 0:
                print(i, len(tasks), flush=True)


if __name__ == "__main__":
    main()
