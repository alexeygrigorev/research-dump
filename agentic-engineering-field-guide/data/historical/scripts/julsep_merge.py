"""Merge Jul-Sep 2026 collected vacancies into raw/vacancies.jsonl.gz with dedupe.

Applies:
  1. Dedupe 1: (source, job_id or url) -> keep earliest posted_date / capture
  2. Dedupe 2: sha1(norm(title)|norm(company)|norm(description)[:2000])
  3. Dedupe 3 (t3593u): reposts/re-listings with same normalized company + title + locations
     -> keep earliest posted_date (or earliest capture if posted_date missing)

Updates raw/vacancies.jsonl.gz, raw/counts_month_role_region.csv, raw/summary.json, raw/COUNTS.md,
and writes work/julsep/merge_stats.json.
"""
import collections
import csv
import gzip
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roles

HERE = Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
COLLECTED = HERE / "work" / "julsep" / "collected"
WINDOW_START = "2025-11"


def load_build_raw():
    argv, sys.argv = sys.argv, ["x", "/nonexistent", "/tmp/_unused"]
    spec = importlib.util.spec_from_file_location("build_raw", Path(__file__).resolve().parent / "build_raw.py")
    bld = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bld)
    sys.argv = argv
    return bld


def norm(s):
    return re.sub(r"\W+", " ", (s or "").lower()).strip()


def month_of(ts):
    return f"{ts[:4]}-{ts[4:6]}" if ts and len(ts) >= 6 else ""


def load_new_records(bld):
    new_recs = []
    per_source_loaded = collections.Counter()

    def add_rec(rec, source, archive, crawl, ts):
        desc = rec.get("description") or ""
        title = (rec.get("title") or "").strip()
        if len(desc) < 200 or not roles.role_of(title):
            return
        locs = rec.get("locations") or []
        if isinstance(locs, str):
            locs = [locs]
        jid = str(rec.get("job_id") or "")
        url = rec.get("url") or ""
        if not jid and url:
            jid = url.rstrip("/").split("/")[-1]
        m = month_of(ts)
        per_source_loaded[f"{source}/{archive}"] += 1
        new_recs.append({
            "vacancy_id": f"{source}:{jid}",
            "source": source,
            "archive": archive,
            "crawl": crawl,
            "job_id": jid,
            "month": m,
            "first_seen": ts,
            "last_seen": ts,
            "n_captures": 1,
            "title": title,
            "role": roles.role_of(title),
            "company": rec.get("company") or "",
            "locations": locs,
            "region": bld.region(locs, bool(rec.get("remote"))),
            "remote": bool(rec.get("remote")),
            "posted_date": (rec.get("posted_date") or "")[:10],
            "valid_through": (rec.get("valid_through") or "")[:10],
            "employment_type": rec.get("employment_type") or rec.get("work_type") or "",
            "url": url,
            "in_window": m >= WINDOW_START,
            "has_description": True,
            "content_hash": "",
            "dup_ids": [],
            "description": desc,
        })

    for fname, source, archive in [
        ("cc_builtin.jsonl", "builtin", "cc"),
        ("wb_builtin.jsonl", "builtin", "wb"),
    ]:
        p = COLLECTED / fname
        if p.exists():
            for l in p.open():
                r = json.loads(l)
                ts = (r.get("archive_ref") or {}).get("timestamp") or ""
                crawl = r.get("crawl") or ("wayback" if archive == "wb" else "")
                for rec in r.get("records", []):
                    add_rec(rec, source, archive, crawl, ts)

    for p in sorted(COLLECTED.glob("cc_gh_jobs_*.jsonl")):
        for l in p.open():
            r = json.loads(l)
            rec = r.get("record")
            if rec:
                ts = (r.get("archive_ref") or {}).get("timestamp") or ""
                add_rec(rec, "greenhouse", "cc", r.get("crawl") or "", ts)

    for p in sorted(COLLECTED.glob("cc_ashby_*.jsonl")):
        for l in p.open():
            r = json.loads(l)
            rec = r.get("record")
            if rec:
                ts = (r.get("archive_ref") or {}).get("timestamp") or ""
                add_rec(rec, "ashby", "cc", r.get("crawl") or "", ts)

    return new_recs, dict(per_source_loaded)


def main():
    bld = load_build_raw()
    existing = []
    with gzip.open(RAW / "vacancies.jsonl.gz", "rt", encoding="utf-8") as fh:
        for l in fh:
            existing.append(json.loads(l))

    before_month = collections.Counter(r["month"] for r in existing)
    before_posted = collections.Counter((r.get("posted_date") or "")[:7] for r in existing)
    before_src = collections.Counter(f"{r['source']}/{r['archive']}" for r in existing)

    new_recs, per_source_loaded = load_new_records(bld)
    combined = existing + new_recs

    # Dedupe 1: (source, job_id or url)
    # Prefer earliest posted_date, then earliest first_seen, then longest description
    def sort_key_d1(r):
        pd = r.get("posted_date") or "9999-99-99"
        fs = r.get("first_seen") or "99999999999999"
        return (pd, fs, -len(r.get("description") or ""))

    by_id = {}
    d1_removed = 0
    for r in sorted(combined, key=sort_key_d1):
        k = (r["source"], r["job_id"] or r["url"])
        if k in by_id:
            v = by_id[k]
            v["n_captures"] = v.get("n_captures", 1) + r.get("n_captures", 1)
            fs = [x for x in (v.get("first_seen"), r.get("first_seen")) if x]
            ls = [x for x in (v.get("last_seen"), r.get("last_seen")) if x]
            v["first_seen"] = min(fs) if fs else ""
            v["last_seen"] = max(ls) if ls else ""
            if v["first_seen"]:
                v["month"] = month_of(v["first_seen"])
                v["in_window"] = v["month"] >= WINDOW_START
            if not v.get("description") and r.get("description"):
                v["description"] = r["description"]
                v["has_description"] = len(v["description"]) >= 200
            d1_removed += 1
            continue
        r["dup_ids"] = list(r.get("dup_ids") or [])
        by_id[k] = r

    # Dedupe 2: sha1(norm(title)|norm(company)|norm(description)[:2000])
    seen_h = {}
    after_d2 = []
    d2_removed = 0
    for r in by_id.values():
        h = hashlib.sha1("|".join([norm(r["title"]), norm(r["company"]), norm(r["description"])[:2000]]).encode()).hexdigest()
        r["content_hash"] = h
        if r["description"] and h in seen_h:
            k = seen_h[h]
            k["dup_ids"].append(r["vacancy_id"])
            k["dup_ids"].extend(r.get("dup_ids") or [])
            k["n_captures"] += r.get("n_captures", 1)
            d2_removed += 1
            continue
        if r["description"]:
            seen_h[h] = r
        after_d2.append(r)

    # Dedupe 3 (t3593u): reposts/re-listings (same normalized company + title + locations)
    # Keep earliest posted_date (fallback to earliest first_seen), preferring builtin display name
    def sort_key_d3(r):
        pd = r.get("posted_date") or "9999-99-99"
        fs = r.get("first_seen") or "99999999999999"
        return (pd, fs, r["source"] != "builtin")

    seen_repost = {}
    out = []
    d3_removed = 0
    for r in sorted(after_d2, key=sort_key_d3):
        co_key = norm(r["company"]).replace(" ", "")
        locs_key = tuple(sorted({norm(l) for l in (r.get("locations") or []) if norm(l)}))
        if co_key:
            rk = (co_key, norm(r["title"]), locs_key)
            if rk in seen_repost:
                k = seen_repost[rk]
                k["dup_ids"].append(r["vacancy_id"])
                k["dup_ids"].extend(r.get("dup_ids") or [])
                k["n_captures"] += r.get("n_captures", 1)
                fs = [x for x in (k.get("first_seen"), r.get("first_seen")) if x]
                ls = [x for x in (k.get("last_seen"), r.get("last_seen")) if x]
                k["first_seen"] = min(fs) if fs else ""
                k["last_seen"] = max(ls) if ls else ""
                d3_removed += 1
                continue
            seen_repost[rk] = r
        out.append(r)

    for r in out:
        r["role"] = roles.role_of(r["title"])
        r["region"] = bld.region(r.get("locations"), r.get("remote"))
        r["in_window"] = r["month"] >= WINDOW_START
        r["has_description"] = len(r.get("description") or "") >= 200
        r["vacancy_id"] = f"{r['source']}:{r['job_id']}"
    out.sort(key=lambda r: (r["month"], r["source"], r["job_id"]))

    cols = ["vacancy_id", "source", "archive", "crawl", "job_id", "month", "first_seen", "last_seen", "n_captures",
            "title", "role", "company", "locations", "region", "remote", "posted_date", "valid_through",
            "employment_type", "url", "in_window", "has_description", "content_hash", "dup_ids", "description"]
    with gzip.open(RAW / "vacancies.jsonl.gz", "wt", encoding="utf-8") as fh:
        for r in out:
            fh.write(json.dumps({c: r.get(c) for c in cols}, ensure_ascii=False) + "\n")

    counts = collections.Counter((r["month"], r["role"], r["region"]) for r in out)
    with open(RAW / "counts_month_role_region.csv", "w", newline="") as fh:
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
    funnel = {
        "existing_raw_before": len(existing),
        "new_julsep_loaded": len(new_recs),
        "combined_before_dedup": len(combined),
        "dedup_by_source_job_id": len(by_id),
        "dedup_by_content_hash": len(after_d2),
        "dedup_reposts_removed_t3593u": d3_removed,
        "final_raw_rows": len(out),
        "with_full_text_200plus_chars": sum(r["has_description"] for r in out),
        "in_window_since_" + WINDOW_START: sum(r["in_window"] for r in out),
    }
    summary = {
        "funnel": funnel,
        "by_source_archive": {f"{a}/{b}": n for (a, b), n in sorted(src.items())},
        "by_month": dict(sorted(collections.Counter(r["month"] for r in out).items())),
        "by_posted_month": dict(sorted(collections.Counter((r.get("posted_date") or "")[:7] for r in out).items())),
        "by_role": dict(collections.Counter(r["role"] for r in out).most_common()),
        "by_region": dict(collections.Counter(r["region"] for r in out).most_common()),
    }
    (RAW / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    md = [
        "# Raw historical vacancies: counts", "",
        "Generated by `scripts/build_raw.py` + `scripts/julsep_merge.py` (no LLM). "
        "Month = month of first archive capture (`month_basis=capture` when `first_seen` is set, else `crawl_batch`). "
        "Reposts deduplicated per t3593u (same normalized company + title + locations kept once at earliest `posted_date`).", "",
        "## Funnel and dedup", "", "```json", json.dumps(summary["funnel"], indent=2), "```", "",
        "## By source / archive", "", "```json", json.dumps(summary["by_source_archive"], indent=2), "```", "",
        "## Month x role", "", table(lambda r: r["role"], out, role_keys), "",
        "## Month x region", "", table(lambda r: r["region"], out, region_keys), "",
        "Full month x role x region grid: `counts_month_role_region.csv`.", "",
    ]
    (RAW / "COUNTS.md").write_text("\n".join(md))

    after_month = collections.Counter(r["month"] for r in out)
    after_posted = collections.Counter((r.get("posted_date") or "")[:7] for r in out)
    after_src = collections.Counter(f"{r['source']}/{r['archive']}" for r in out)
    stats = {
        "per_source_loaded": per_source_loaded,
        "dedup": {"d1_removed": d1_removed, "d2_removed": d2_removed, "d3_reposts_removed": d3_removed},
        "julsep_capture_month": {m: {"before": before_month[m], "after": after_month[m]} for m in ("2026-07", "2026-08", "2026-09")},
        "julsep_posted_month": {m: {"before": before_posted[m], "after": after_posted[m]} for m in ("2026-07", "2026-08", "2026-09")},
        "by_source_before": dict(sorted(before_src.items())),
        "by_source_after": dict(sorted(after_src.items())),
    }
    (HERE / "work" / "julsep" / "merge_stats.json").write_text(json.dumps(stats, indent=2) + "\n")
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
