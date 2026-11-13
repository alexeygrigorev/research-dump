"""Stage 2: build monthly snapshot samples for one city from archived pages.

  python stage2_snapshot.py london 202511 202512 202601 --n 100

Candidate pool for month M (stage 1 links):
  a) job-detail captures (Common Crawl, Wayback) taken in M whose URL slug
     matches a scoped role, and
  b) job links seen on archived city listing pages in M with a scoped title.
Candidates are shuffled with a fixed seed and fetched (CC range read first,
Wayback id_ second). A posting is kept when its JSON-LD (the field-guide
parser) has a title in scope, a location in the city, and a description.

Dedup: months are processed in order; a job_id (and its canonical URL) is
claimed by the first month it lands in and is never sampled again, so no
posting appears in two monthly samples. Previously published samples under
../<city>/ are loaded first, so re-runs and new months keep that guarantee.
"""
import argparse, datetime, gzip, json, random
from collections import Counter
from pathlib import Path

import builtin_parse, capture_index, coverage, fetch_cache
from roles import role_of

ROOT = Path(__file__).resolve().parent.parent  # data/historical
W = ROOT / "work"
CITY = {
    "london": ("London", "GBR"),
    "berlin": ("Berlin", "DEU"),
    "newyork": ("New York", "USA"),
}


def in_city(job, city):
    name, cc = CITY[city]
    locs = job.get("locations") or [job.get("location", "")]
    return any(l.startswith(name + ",") or l == name for l in locs)


def listing_pool(city):
    pool = {}
    f = W / "listing_links.jsonl"
    if not f.exists():
        return pool
    for l in open(f):
        r = json.loads(l)
        if r["city"] == city and r["role"]:
            pool.setdefault(r["month"], {}).setdefault(r["job_id"], r)
    return pool


def refs_for_month(refs, month):
    """Captures in that month first (CC before Wayback), then the nearest others."""
    inm = [r for r in refs if r["month"] == month]
    inm.sort(key=lambda r: (r["src"] != "cc", r["timestamp"]))
    return inm


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("city", choices=CITY)
    ap.add_argument("months", nargs="+", help="YYYYMM")
    ap.add_argument("--n", type=int, default=100)
    ap.add_argument("--max-fetch", type=int, default=2500, help="per month fetch budget")
    ap.add_argument("--seed", type=int, default=20261113)
    args = ap.parse_args()

    idx = capture_index.load()
    known_city = {jid: c for jid, (c, _) in coverage.job_cities().items()}
    listing = listing_pool(args.city)
    outdir = ROOT / args.city
    outdir.mkdir(parents=True, exist_ok=True)
    manifest_f = ROOT / "manifest.json"
    manifest = json.loads(manifest_f.read_text()) if manifest_f.exists() else {"samples": {}}

    claimed = set()  # job ids and urls already in any published sample
    rebuilding = {outdir / f"{m[:4]}-{m[4:]}.jsonl.gz" for m in args.months}
    for f in ROOT.glob("*/*.jsonl.gz"):
        if f in rebuilding:  # re-running a month replaces its own sample
            continue
        for l in gzip.open(f, "rt"):
            r = json.loads(l)
            claimed.add(r["job_id"]); claimed.add(r["url"].split("?")[0])

    for month in sorted(args.months):
        rng = random.Random(f"{args.seed}-{args.city}-{month}")
        detail = [jid for jid, refs in idx.items()
                  if any(r["month"] == month for r in refs) and role_of(refs[0]["slug"])]
        from_listing = list(listing.get(month, {}))
        rng.shuffle(detail); rng.shuffle(from_listing)
        # listing links are already known to be in the city: try them first
        order, seen = [], set()
        # then detail captures already known (from a resolved capture) to be in this city,
        # then the ones whose city is still unknown (these cost a fetch each)
        known_here = [j for j in detail if known_city.get(j) == args.city]
        unknown = [j for j in detail if j not in known_city]
        for jid in from_listing + known_here + unknown:
            if jid not in seen:
                seen.add(jid); order.append(jid)
        stats = Counter(pool_detail=len(detail), pool_listing=len(from_listing))
        kept = []
        for jid in order:
            if len(kept) >= args.n or stats["fetched"] >= args.max_fetch:
                break
            if jid in claimed:
                stats["skip_claimed"] += 1; continue
            if known_city.get(jid, args.city) != args.city:
                stats["known_other_city"] += 1; continue
            refs = refs_for_month(idx.get(jid, []), month)
            if not refs:
                stats["no_capture_in_month"] += 1; continue
            job = None
            for ref in refs[:2]:
                try:
                    html = fetch_cache.fetch(ref)
                except Exception:
                    stats["fetch_error"] += 1; continue
                stats["fetched"] += 1
                job = builtin_parse.parse_job_html(html)
                if job.get("description"):
                    break
            if not job or not job.get("description"):
                stats["no_jsonld"] += 1; continue
            if not role_of(job["title"]):
                stats["title_out_of_scope"] += 1; continue
            if not in_city(job, args.city):
                stats["other_city"] += 1; continue
            canon = (job["url"] or ref["url"]).split("?")[0]
            if job["job_id"] in claimed or canon in claimed:
                stats["skip_claimed"] += 1; continue
            claimed.add(job["job_id"]); claimed.add(canon)
            job.update(
                role=role_of(job["title"]),
                snapshot_month=f"{month[:4]}-{month[4:]}",
                city=args.city,
                archive_source="common_crawl" if ref["src"] == "cc" else "wayback",
                archive_timestamp=ref["timestamp"],
                archive_ref=({"filename": ref["filename"], "offset": ref["offset"], "length": ref["length"]}
                             if ref["src"] == "cc" else
                             f"https://web.archive.org/web/{ref['timestamp']}/{ref['original']}"),
                found_via="listing" if jid in listing.get(month, {}) else "detail_capture",
            )
            kept.append(job)
            stats["kept"] += 1
        out = outdir / f"{month[:4]}-{month[4:]}.jsonl.gz"
        with gzip.open(out, "wt", encoding="utf-8") as fh:
            for j in kept:
                fh.write(json.dumps(j, ensure_ascii=False) + "\n")
        manifest["samples"][f"{args.city}/{out.name}"] = {
            "city": args.city, "month": f"{month[:4]}-{month[4:]}", "count": len(kept), "target": args.n,
            "seed": args.seed, "stats": dict(stats),
            "sources": dict(Counter(j["archive_source"] for j in kept)),
            "found_via": dict(Counter(j["found_via"] for j in kept)),
            "roles": dict(Counter(j["role"] for j in kept)),
            "built_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        }
        print(args.city, month, dict(stats), flush=True)
    manifest["schema"] = ("field-guide data_raw fields (job_id, title, company, location, locations, remote, "
                          "work_type, level, skills, company_size, compensation, description, benefits, industries, "
                          "posted_date, url, source) + role, snapshot_month, city, archive_source, "
                          "archive_timestamp, archive_ref, found_via")
    manifest["dedup"] = "a job_id/canonical URL appears in at most one sample across all cities and months"
    manifest_f.write_text(json.dumps(manifest, indent=1, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
