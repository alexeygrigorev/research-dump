"""Step 1 raw dataset (Alexey t3413u part 2): every cached archive vacancy for the
6 roles, all geographies, no city filter, no sampling, no LLM.

Inputs (the 937 MB work/ cache, built by the stage1_* scripts from free archives):
  work/html/*.html.gz          builtin.com job pages fetched from Common Crawl + Wayback
  work/cc_job_cdx/*.jsonl      CC capture index for those pages (key -> capture time)
  work/wayback_job_cdx/*.jsonl Wayback capture index for those pages
  work/gh_listings/*.jsonl.gz  Greenhouse board listings read from Common Crawl
  work/boards_read/*/*.jsonl.gz Greenhouse/Ashby job pages read from Common Crawl

Processing is deterministic: JSON-LD JobPosting parse (field-guide parser), regex role
filter (roles.py), regex region (regions.py + world buckets), dedupe by source job id,
then by content hash (title+company+description) across ids and sources.

Usage: python build_raw.py [WORK_DIR] [OUT_DIR]
"""
import collections, csv, gzip, hashlib, json, re, sys
from multiprocessing import Pool
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import builtin_parse, regions, roles  # noqa: E402

HERE = Path(__file__).resolve().parent.parent
WORK = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "work"
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "raw"
WINDOW_START = "2025-11"

WORLD = [
    ("CA", r"\b(Canada|CAN|Toronto|Vancouver|Montreal|Montréal|Ottawa|Calgary|Waterloo|Ontario|Quebec|British Columbia|Alberta)\b"),
    ("IN", r"\b(India|IND|Bengaluru|Bangalore|Hyderabad|Pune|Chennai|Mumbai|Gurgaon|Gurugram|Noida|Delhi)\b"),
    ("LATAM", r"\b(Brazil|BRA|São Paulo|Sao Paulo|Mexico|MEX|Argentina|ARG|Colombia|COL|Chile|CHL|Peru|PER|Uruguay|URY|"
              r"Costa Rica|Bogot[aá]|Buenos Aires|Latin America|LATAM)\b"),
    ("APAC", r"\b(Singapore|SGP|Australia|AUS|Sydney|Melbourne|Japan|JPN|Tokyo|China|CHN|Hong Kong|HKG|Korea|KOR|Seoul|"
             r"Taiwan|TWN|Philippines|PHL|Vietnam|VNM|Indonesia|IDN|Malaysia|MYS|Thailand|THA|New Zealand|NZL|APAC)\b"),
    ("MEA", r"\b(Israel|ISR|Tel Aviv|UAE|ARE|Dubai|Abu Dhabi|Saudi|SAU|Egypt|EGY|Turkey|TUR|Türkiye|Istanbul|Nigeria|NGA|"
            r"Kenya|KEN|South Africa|ZAF|Cape Town|Morocco|MAR|Pakistan|PAK)\b"),
]
WORLD = [(k, re.compile(p, re.I)) for k, p in WORLD]


def region(locations, remote):
    """First location decides: UK | DE | EU | US | CA | IN | LATAM | APAC | MEA | REMOTE | UNKNOWN."""
    for loc in locations or []:
        r = regions.region_of(loc)
        if r:
            return r
        for k, rx in WORLD:
            if rx.search(loc):
                return k
    text = " ".join(locations or [])
    if remote or re.search(r"\bremote\b|anywhere|worldwide", text, re.I):
        return "REMOTE"
    return "UNKNOWN"


def cache_key(s):
    return hashlib.sha1(s.encode()).hexdigest()


def capture_index():
    idx = {}
    for f in sorted((WORK / "cc_job_cdx").glob("*.jsonl")):
        for line in open(f):
            try:
                r = json.loads(line)
            except ValueError:
                continue
            idx[cache_key(f"cc|{r['filename']}|{r['offset']}")] = ("cc", r["timestamp"], r["url"], f.stem)
    for f in sorted((WORK / "wayback_job_cdx").glob("*.jsonl")):
        for line in open(f):
            try:
                r = json.loads(line)
            except ValueError:
                continue
            idx[cache_key(f"wb|{r['timestamp']}|{r['original']}")] = ("wb", r["timestamp"], r["original"], "wayback")
    return idx


LD = re.compile(r'<script[^>]*type="application/ld(?:\+|&#x2B;|&#43;)json"[^>]*>(.*?)</script>', re.S | re.I)


def parse_page(path):
    try:
        html = gzip.open(path, "rt", encoding="utf-8", errors="replace").read()
    except (OSError, EOFError):
        return {"_err": "gzip", "_key": path.name[:40]}
    if not html.strip():
        return {"_err": "empty", "_key": path.name[:40]}
    jl = None
    for m in LD.finditer(html):
        try:
            data = json.loads(builtin_parse.html.unescape(m.group(1).strip()))
        except ValueError:
            continue
        items = data.get("@graph", [data]) if isinstance(data, dict) else data
        for it in items if isinstance(items, list) else []:
            if isinstance(it, dict) and it.get("@type") == "JobPosting":
                jl = it
                break
        if jl:
            break
    if not jl:
        return {"_err": "no_jobposting", "_key": path.name[:40]}
    title = (jl.get("title") or "").strip()
    if not roles.role_of(title):
        return {"_err": "out_of_scope_role", "_key": path.name[:40]}
    org = jl.get("hiringOrganization") or {}
    locs = builtin_parse.parse_job_locations(jl)
    url = jl.get("url") or ""
    return {
        "_key": path.name[:40],
        "job_id": url.rstrip("/").split("/")[-1] if url else "",
        "title": title,
        "company": (org.get("name") if isinstance(org, dict) else "") or "",
        "locations": locs,
        "remote": jl.get("jobLocationType") == "TELECOMMUTE",
        "posted_date": (jl.get("datePosted") or "")[:10],
        "valid_through": (jl.get("validThrough") or "")[:10],
        "employment_type": jl.get("employmentType") or "",
        "url": url,
        "description": builtin_parse.html_to_markdown(jl.get("description") or ""),
    }


def month_of(ts):
    return f"{ts[:4]}-{ts[4:6]}" if ts and len(ts) >= 6 else ""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    funnel = collections.Counter()
    idx = capture_index()
    pages = sorted((WORK / "html").glob("*.html.gz"))
    funnel["builtin_cached_pages"] = len(pages)
    recs = []
    with Pool(8) as pool:
        for r in pool.imap_unordered(parse_page, pages, chunksize=50):
            if "_err" in r:
                funnel["builtin_drop_" + r["_err"]] += 1
                continue
            cap = idx.get(r.pop("_key"))
            if cap:
                src, ts, cap_url, crawl = cap
                if not r["url"]:
                    r["url"] = cap_url
                r["job_id"] = roles.slug_of(cap_url)[1] or r["job_id"]
            else:
                src, ts, crawl = "cc_or_wb", (r["posted_date"] or "").replace("-", "")[:8], ""
                funnel["builtin_capture_unknown_month_from_posted"] += 1
            r.update(source="builtin", archive=src, crawl=crawl, captured_at=ts, month=month_of(ts))
            recs.append(r)
    funnel["builtin_in_scope_captures"] = len(recs)

    # Greenhouse / Ashby pages and listings read from Common Crawl
    for f in sorted((WORK / "gh_listings").glob("*.jsonl.gz")) + sorted((WORK / "boards_read").glob("*/*.jsonl.gz")):
        board = f.parent.name if f.parent.name != "gh_listings" else "greenhouse"
        for line in gzip.open(f, "rt"):
            d = json.loads(line)
            funnel[f"{board}_records"] += 1
            title = (d.get("title") or "").strip()
            if not roles.role_of(title):
                continue
            loc = d.get("locations") or ([d["location"]] if d.get("location") else [])
            ts = d.get("timestamp") or (d.get("archive_ref") or {}).get("timestamp") or ""
            month = month_of(ts) if ts else (f"{d['month'][:4]}-{d['month'][4:]}" if d.get("month") else "")
            recs.append({
                "job_id": str(d.get("job_id") or d.get("key") or ""), "title": title,
                "company": d.get("company") or "", "locations": loc, "remote": bool(d.get("remote")),
                "posted_date": (d.get("posted_date") or d.get("published_at") or "")[:10],
                "valid_through": (d.get("valid_through") or "")[:10], "employment_type": d.get("work_type") or "",
                "url": d.get("url") or "", "description": d.get("description") or "",
                "source": board, "archive": "cc", "crawl": d.get("crawl") or "", "captured_at": ts, "month": month,
            })
    funnel["all_in_scope_captures"] = len(recs)

    # Dedupe 1: same source + job id -> one vacancy; keep first capture, record capture span.
    by_id = {}
    for r in sorted(recs, key=lambda r: (r["captured_at"] or "9", -len(r["description"]))):
        k = (r["source"], r["job_id"] or r["url"])
        if k in by_id:
            v = by_id[k]
            v["n_captures"] += 1
            v["last_seen"] = max(v["last_seen"], r["captured_at"])
            if not v["description"] and r["description"]:
                v["description"] = r["description"]
            continue
        r["n_captures"], r["first_seen"], r["last_seen"] = 1, r["captured_at"], r["captured_at"]
        by_id[k] = r
    funnel["dedup_by_source_job_id"] = len(by_id)

    # Dedupe 2: identical content under different ids/sources (reposts, mirrors).
    seen, out = {}, []
    for r in by_id.values():
        norm = lambda s: re.sub(r"\W+", " ", (s or "").lower()).strip()
        h = hashlib.sha1("|".join([norm(r["title"]), norm(r["company"]), norm(r["description"])[:2000]]).encode()).hexdigest()
        if r["description"] and h in seen:
            seen[h]["dup_ids"].append(f"{r['source']}:{r['job_id']}")
            continue
        r["content_hash"], r["dup_ids"] = h, []
        if r["description"]:
            seen[h] = r
        out.append(r)
    funnel["dedup_by_content_hash"] = len(out)

    for r in out:
        r["role"] = roles.role_of(r["title"])
        r["region"] = region(r["locations"], r["remote"])
        r["in_window"] = r["month"] >= WINDOW_START
        r["has_description"] = len(r["description"]) >= 200
        r["vacancy_id"] = f"{r['source']}:{r['job_id']}"
    out.sort(key=lambda r: (r["month"], r["source"], r["job_id"]))
    funnel["with_full_text_200plus_chars"] = sum(r["has_description"] for r in out)
    funnel["in_window_since_" + WINDOW_START] = sum(r["in_window"] for r in out)

    cols = ["vacancy_id", "source", "archive", "crawl", "job_id", "month", "first_seen", "last_seen", "n_captures",
            "title", "role", "company", "locations", "region", "remote", "posted_date", "valid_through",
            "employment_type", "url", "in_window", "has_description", "content_hash", "dup_ids", "description"]
    with gzip.open(OUT / "vacancies.jsonl.gz", "wt", encoding="utf-8") as fh:
        for r in out:
            fh.write(json.dumps({c: r.get(c) for c in cols}, ensure_ascii=False) + "\n")

    counts = collections.Counter((r["month"], r["role"], r["region"]) for r in out)
    with open(OUT / "counts_month_role_region.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["month", "role", "region", "vacancies", "with_full_text"])
        ft = collections.Counter((r["month"], r["role"], r["region"]) for r in out if r["has_description"])
        for k in sorted(counts):
            w.writerow([*k, counts[k], ft[k]])

    def table(key_fn, rows, cols_vals):
        c = collections.Counter((r["month"], key_fn(r)) for r in rows)
        months = sorted({r["month"] for r in rows})
        lines = ["| month | " + " | ".join(cols_vals) + " | total |", "|---" * (len(cols_vals) + 2) + "|"]
        for m in months:
            vals = [c[(m, v)] for v in cols_vals]
            lines.append(f"| {m or '?'} | " + " | ".join(map(str, vals)) + f" | {sum(vals)} |")
        tot = [sum(c[(m, v)] for m in months) for v in cols_vals]
        lines.append("| **total** | " + " | ".join(map(str, tot)) + f" | {sum(tot)} |")
        return "\n".join(lines)

    role_keys = [k for k, _ in roles.ROLE_PATTERNS]
    region_keys = ["US", "UK", "DE", "EU", "CA", "IN", "LATAM", "APAC", "MEA", "REMOTE", "UNKNOWN"]
    src = collections.Counter((r["source"], r["archive"]) for r in out)
    summary = {"funnel": dict(funnel), "by_source_archive": {f"{a}/{b}": n for (a, b), n in sorted(src.items())},
               "by_month": dict(sorted(collections.Counter(r["month"] for r in out).items())),
               "by_role": dict(collections.Counter(r["role"] for r in out).most_common()),
               "by_region": dict(collections.Counter(r["region"] for r in out).most_common())}
    (OUT / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    md = ["# Raw historical vacancies: counts", "",
          "Generated by `scripts/build_raw.py` (no LLM). Month = month of first archive capture.", "",
          "## Funnel and dedup", "", "```json", json.dumps(summary["funnel"], indent=2), "```", "",
          "## By source / archive", "", "```json", json.dumps(summary["by_source_archive"], indent=2), "```", "",
          "## Month x role", "", table(lambda r: r["role"], out, role_keys), "",
          "## Month x region", "", table(lambda r: r["region"], out, region_keys), "",
          "Full month x role x region grid: `counts_month_role_region.csv`.", ""]
    (OUT / "COUNTS.md").write_text("\n".join(md))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
