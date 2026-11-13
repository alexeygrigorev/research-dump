"""One command per month: add a monthly snapshot from free web archives.

  python monthly.py                 # the previous calendar month
  python monthly.py 2026-11         # a given month (re-running it rebuilds that month)
  python monthly.py 2026-11 --cities london --n 100 --skip-wb-resolve

Steps (all incremental, everything fetched is cached in ../work/html/):
  1. Common Crawl: dump the builtin.com/job/ index rows of every crawl since
     CC-MAIN-2025-30 that is not on disk yet (ZipNum range reads, ~1 min/crawl).
  2. Wayback: CDX of builtin.com/job/* captures taken in that month.
  3. Wayback: CDX of the London/Berlin/New York listing pages in that month,
     then read each listing page and keep its job cards.
  4. Resolve the city of in-scope job links captured that month
     (Common Crawl in parallel, Wayback at 1 request / 1.5 s).
  5. coverage.py -> ../coverage.json
  6. stage2_snapshot.py <city> <month> for each city -> ../<city>/<YYYY-MM>.jsonl.gz + manifest

Cost: $0. Common Crawl is read over plain HTTPS from data.commoncrawl.org (no AWS
account); the Wayback Machine is free and is queried politely (archive_client
rate limits + backoff). No paid APIs, no JobsPipe.

Run it a few days after the month ends. Common Crawl publishes a crawl 2-4 weeks
after it ran, so re-running the previous month later picks up its crawl too.
"""
import argparse, datetime, json, subprocess, sys
from pathlib import Path

import archive_client as a

HERE = Path(__file__).resolve().parent
W = HERE.parent / "work"
FIRST_CRAWL = "CC-MAIN-2025-30"
CITY_RE = r".*city=(London|Berlin|New(%20|\+|%2B)York).*"


def run(*args):
    print("+", " ".join(args), flush=True)
    subprocess.run([sys.executable, *args], cwd=HERE, check=True)


def prev_month():
    first = datetime.date.today().replace(day=1)
    return (first - datetime.timedelta(days=1)).strftime("%Y-%m")


def new_crawls():
    """Crawl ids >= FIRST_CRAWL that are published but not dumped yet."""
    try:
        text = a.get("https://index.commoncrawl.org/collinfo.json", retries=3, timeout=60)
        ids = [c["id"] for c in json.loads(text)]
    except Exception as e:  # the index server is sometimes down; data files are not
        print("collinfo unavailable, skipping new crawls:", e, flush=True)
        return []
    have = {p.stem for p in (W / "cc_job_cdx").glob("*.jsonl") if p.stat().st_size}
    return sorted(c for c in ids if c.startswith("CC-MAIN-") and c >= FIRST_CRAWL and c not in have)


def cdx_month(out_dir, tag, ym, params):
    """Paged Wayback CDX query restricted to one month; resumable per page."""
    out_dir.mkdir(parents=True, exist_ok=True)
    base = dict(params, **{"from": ym, "to": ym})
    try:
        n = a.cdx(dict(base, showNumPages="true"))
    except (IndexError, ValueError):
        # showNumPages sometimes comes back empty under load: one un-paged query for the month instead
        f = out_dir / f"{tag}_{ym}_all.jsonl"
        if not f.exists():
            rows = a.cdx(base)
            tmp = f.with_suffix(".tmp")
            with open(tmp, "w") as fh:
                for r in rows:
                    fh.write(json.dumps(r) + "\n")
            tmp.rename(f)
        print(f"{tag} {ym}: un-paged CDX, {sum(1 for _ in open(f))} captures", flush=True)
        return
    rows_total = 0
    for p in range(n):
        f = out_dir / f"{tag}_{ym}_{p:03d}.jsonl"
        if not f.exists():
            rows = a.cdx(dict(base, page=str(p)))
            tmp = f.with_suffix(".tmp")
            with open(tmp, "w") as fh:
                for r in rows:
                    fh.write(json.dumps(r) + "\n")
            tmp.rename(f)
        rows_total += sum(1 for _ in open(f))
    print(f"{tag} {ym}: {n} CDX pages, {rows_total} captures", flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("month", nargs="?", default=prev_month(), help="YYYY-MM (default: previous month)")
    ap.add_argument("--cities", nargs="+", default=["london", "berlin", "newyork"])
    ap.add_argument("--n", type=int, default=100, help="target postings per city")
    ap.add_argument("--max-fetch", type=int, default=600, help="archive reads per city in stage 2")
    ap.add_argument("--skip-wb-resolve", action="store_true",
                    help="skip step 4 for Wayback (stage 2 still reads those pages, just later)")
    args = ap.parse_args()
    ym = args.month.replace("-", "")
    assert len(ym) == 6 and ym.isdigit(), "month must be YYYY-MM"

    crawls = new_crawls()
    if crawls:
        run("stage1_cc_zipnum.py", *crawls)
    cdx_month(W / "wayback_job_cdx", "month", ym,
              {"url": "builtin.com/job/", "matchType": "prefix",
               "fl": "timestamp,original,statuscode,mimetype,digest"})
    cdx_month(W / "listing_cdx_pages", "month", ym,
              {"url": "builtin.com/jobs", "matchType": "prefix", "filter": ["original:" + CITY_RE, "statuscode:200"],
               "fl": "timestamp,original,statuscode,digest"})
    run("stage1_fetch_listings.py")
    run("stage1_resolve.py", "cc", ym)
    if not args.skip_wb_resolve:
        run("stage1_resolve.py", "wb", ym)
    run("coverage.py")
    for city in args.cities:
        run("stage2_snapshot.py", city, ym, "--n", str(args.n), "--max-fetch", str(args.max_fetch))
    print("done:", args.month, "->", ", ".join(f"{c}/{args.month}.jsonl.gz" for c in args.cities), flush=True)


if __name__ == "__main__":
    main()
