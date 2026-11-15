"""Collect Jul-Sep 2026 builtin.com/job/* vacancies from Wayback Machine CDX.

No LLM. Respects archive_client rate limit (1.5s / req to web.archive.org).
Resumable under work/julsep/collected/.
"""
import gzip
import html as htmlmod
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import archive_client as a
import builtin_parse
from roles import role_of, slug_of

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / "work" / "julsep"
OUT_DIR = WORK / "collected"
LD = re.compile(r'<script[^>]*type="application/ld(?:\+|&#x2B;|&#43;)json"[^>]*>(.*?)</script>', re.S | re.I)


def existing_builtin_ids():
    ids = set()
    with gzip.open(ROOT / "raw" / "vacancies.jsonl.gz", "rt") as fh:
        for l in fh:
            r = json.loads(l)
            if r["source"] == "builtin":
                ids.add(r["job_id"])
    return ids


def parse_builtin_html(body, url):
    jl = None
    for m in LD.finditer(body):
        try:
            data = json.loads(htmlmod.unescape(m.group(1).strip()))
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
        return None
    title = (jl.get("title") or "").strip()
    if not role_of(title):
        return None
    org = jl.get("hiringOrganization") or {}
    locs = builtin_parse.parse_job_locations(jl)
    jurl = jl.get("url") or url
    jid = slug_of(url)[1] or (jurl.rstrip("/").split("/")[-1] if jurl else "")
    return {
        "job_id": jid,
        "title": title,
        "company": (org.get("name") if isinstance(org, dict) else "") or "",
        "locations": locs,
        "remote": jl.get("jobLocationType") == "TELECOMMUTE",
        "posted_date": (jl.get("datePosted") or "")[:10],
        "valid_through": (jl.get("validThrough") or "")[:10],
        "employment_type": jl.get("employmentType") or "",
        "url": jurl,
        "description": builtin_parse.html_to_markdown(jl.get("description") or ""),
    }


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    cdx_file = OUT_DIR / "wb_builtin_cdx.jsonl"
    if not cdx_file.exists():
        pages = a.cdx({"url": "builtin.com/job/*", "from": "20260701", "to": "20260930", "showNumPages": "true"})
        print(f"[wb-cdx] total pages: {pages}", flush=True)
        seen_jid = {}
        with cdx_file.with_suffix(".tmp").open("w") as out:
            for p in range(pages):
                rows = a.cdx({
                    "url": "builtin.com/job/*",
                    "from": "20260701",
                    "to": "20260930",
                    "filter": ["statuscode:200", "mimetype:text/html"],
                    "collapse": "urlkey",
                    "page": str(p),
                })
                for r in rows:
                    out.write(json.dumps(r) + "\n")
                    slug, jid = slug_of(r["original"])
                    if jid and role_of(slug):
                        if jid not in seen_jid or r["timestamp"] < seen_jid[jid]["timestamp"]:
                            seen_jid[jid] = r
                if (p + 1) % 10 == 0 or p + 1 == pages:
                    print(f"[wb-cdx] page {p + 1}/{pages}, in_scope_jids={len(seen_jid)}", flush=True)
        cdx_file.with_suffix(".tmp").replace(cdx_file)

    existing = existing_builtin_ids()
    by_jid = {}
    for l in cdx_file.open():
        r = json.loads(l)
        slug, jid = slug_of(r["original"])
        if jid and role_of(slug) and jid not in existing:
            if jid not in by_jid or r["timestamp"] < by_jid[jid]["timestamp"]:
                by_jid[jid] = r

    dest = OUT_DIR / "wb_builtin.jsonl"
    done = {json.loads(l)["key"] for l in dest.open()} if dest.exists() else set()
    todo = [(jid, r) for jid, r in sorted(by_jid.items()) if jid not in done]
    print(f"[wb-fetch] new_in_scope={len(by_jid)} todo={len(todo)}", flush=True)
    ok = 0
    with dest.open("a") as out:
        for n, (jid, r) in enumerate(todo, 1):
            try:
                body = a.wayback_raw(r["timestamp"], r["original"])
                rec = parse_builtin_html(body, r["original"])
                row = {"key": jid, "board": "builtin", "archive": "wb", "archive_ref": r,
                       "records": [rec] if rec else []}
                if rec:
                    ok += 1
            except Exception as e:
                row = {"key": jid, "board": "builtin", "archive": "wb", "archive_ref": r, "error": str(e)}
            out.write(json.dumps(row, ensure_ascii=False) + "\n")
            out.flush()
            if n % 25 == 0:
                print(f"[wb-fetch] {n}/{len(todo)} ok={ok}", flush=True)
    print(f"[wb-fetch] DONE ok={ok}", flush=True)


if __name__ == "__main__":
    main()
