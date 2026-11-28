"""Collect Jul-Sep 2026 vacancies from Common Crawl (CC-MAIN-2026-30, 34, 39).

No LLM. Respects archive_client rate limit (0.15s / req, max 3 readers).
Resumable per board and crawl under work/julsep/collected/.
"""
import collections
import gzip
import html as htmlmod
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import archive_client as a
import builtin_parse
import jobposting_parse as jp
import measure_sources as ms
import stage1_gh_listings as gh
import stage1_read_boards as rb
from roles import role_of, slug_of

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / "work" / "julsep"
OUT_DIR = WORK / "collected"
CRAWLS = ["CC-MAIN-2026-30", "CC-MAIN-2026-34", "CC-MAIN-2026-39"]
LD = re.compile(r'<script[^>]*type="application/ld(?:\+|&#x2B;|&#43;)json"[^>]*>(.*?)</script>', re.S | re.I)


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


def collect_builtin():
    dest = OUT_DIR / "cc_builtin.jsonl"
    done = {json.loads(l)["key"] for l in dest.open()} if dest.exists() else set()
    with dest.open("a") as out:
        for crawl in CRAWLS:
            p = WORK / "cc_job_cdx" / f"{crawl}.jsonl"
            by_jid = {}
            for l in p.open():
                r = json.loads(l)
                if str(r.get("status")) != "200":
                    continue
                slug, jid = slug_of(r["url"])
                if jid and role_of(slug):
                    if jid not in by_jid or r["timestamp"] < by_jid[jid]["timestamp"]:
                        by_jid[jid] = r
            todo = [(jid, r) for jid, r in sorted(by_jid.items()) if f"{crawl}:{jid}" not in done]
            ok = 0
            for jid, r in todo:
                key = f"{crawl}:{jid}"
                try:
                    body = a.cc_record(r["filename"], r["offset"], r["length"])
                    rec = parse_builtin_html(body, r["url"].split("?")[0])
                    row = {"key": key, "board": "builtin", "crawl": crawl, "archive_ref": r,
                           "records": [rec] if rec else []}
                    if rec:
                        ok += 1
                except Exception as e:
                    row = {"key": key, "board": "builtin", "crawl": crawl, "archive_ref": r, "error": str(e)}
                out.write(json.dumps(row, ensure_ascii=False) + "\n")
                out.flush()
            print(f"[builtin] {crawl}: todo={len(todo)} ok={ok}", flush=True)


def collect_greenhouse():
    for crawl in CRAWLS:
        p = WORK / "cc_boards" / "greenhouse" / f"{crawl}.jsonl"
        listings = {}
        job_pages = {}
        for l in p.open():
            r = json.loads(l)
            if str(r.get("status")) != "200" or "html" not in (r.get("mime") or "html"):
                continue
            u = r["url"].split("?")[0]
            m = re.fullmatch(r"https?://job-boards\.greenhouse\.io/([^/?#]+)/?", u)
            if m:
                co = m.group(1).lower()
                if gh.in_panel(co) and int(r.get("length", 0)) >= 8000:
                    if co not in listings or r["timestamp"] < listings[co]["timestamp"]:
                        listings[co] = r
            else:
                parsed = ms.parse_url("greenhouse", r["url"])
                if parsed:
                    k = parsed[0]
                    if k not in job_pages or r["timestamp"] < job_pages[k]["timestamp"]:
                        job_pages[k] = r

        dest_list = OUT_DIR / f"cc_gh_listings_{crawl}.jsonl"
        done = {json.loads(l)["key"] for l in dest_list.open()} if dest_list.exists() else set()
        todo = [(co, r) for co, r in sorted(listings.items()) if co not in done]
        print(f"[gh-listings] {crawl}: panel_ge8k={len(listings)} todo={len(todo)}", flush=True)

        def fetch_one(item):
            k, ref = item
            try:
                return k, ref, a.cc_record(ref["filename"], ref["offset"], ref["length"]), None
            except Exception as e:
                return k, ref, None, str(e)

        with dest_list.open("a") as out, ThreadPoolExecutor(3) as ex:
            for n, (co, ref, body, err) in enumerate(ex.map(fetch_one, todo), 1):
                if err is not None:
                    out.write(json.dumps({"key": co, "crawl": crawl, "archive_ref": ref, "error": err}) + "\n")
                else:
                    jobs, pages = gh.jobs_in(body)
                    recs = []
                    for d in jobs:
                        if not role_of(d.get("title")):
                            continue
                        loc = d.get("location") or ""
                        if isinstance(loc, dict):
                            loc = loc.get("name", "")
                        recs.append({
                            "job_id": str(d.get("id")),
                            "title": d["title"],
                            "company": co,
                            "locations": [loc] if loc else [],
                            "remote": "remote" in loc.lower(),
                            "posted_date": (d.get("published_at") or "")[:10],
                            "url": d.get("absolute_url") or "",
                            "description": jp.clean_html(d.get("content") or ""),
                            "employment_type": "",
                            "valid_through": "",
                        })
                    out.write(json.dumps({"key": co, "crawl": crawl, "archive_ref": ref,
                                          "total_pages": pages, "records": recs}, ensure_ascii=False) + "\n")
                out.flush()
                if n % 300 == 0:
                    print(f"[gh-listings] {crawl}: {n}/{len(todo)}", flush=True)

        # Now fetch individual job pages for in-scope jobs that lack description
        dest_jobs = OUT_DIR / f"cc_gh_jobs_{crawl}.jsonl"
        done_jobs = {json.loads(l)["key"] for l in dest_jobs.open()} if dest_jobs.exists() else set()
        need_desc = {}
        for l in dest_list.open():
            row = json.loads(l)
            for rec in row.get("records", []):
                jk = f"{rec['company']}/{rec['job_id']}"
                if not rec.get("description") and jk in job_pages and jk not in done_jobs:
                    need_desc[jk] = (rec, job_pages[jk])
        print(f"[gh-jobs] {crawl}: need_desc={len(need_desc)}", flush=True)
        todo_jobs = [(jk, ref) for jk, (_, ref) in sorted(need_desc.items())]
        with dest_jobs.open("a") as out, ThreadPoolExecutor(3) as ex:
            for n, (jk, ref, body, err) in enumerate(ex.map(fetch_one, todo_jobs), 1):
                if err is not None:
                    out.write(json.dumps({"key": jk, "crawl": crawl, "error": err}) + "\n")
                else:
                    parsed = jp.parse_greenhouse(body, ref["url"].split("?")[0])
                    base_rec = need_desc[jk][0]
                    if parsed and parsed.get("description"):
                        base_rec["description"] = parsed["description"]
                        if parsed.get("company"):
                            base_rec["company"] = parsed["company"]
                    out.write(json.dumps({"key": jk, "crawl": crawl, "archive_ref": ref, "record": base_rec},
                                         ensure_ascii=False) + "\n")
                out.flush()
                if n % 200 == 0:
                    print(f"[gh-jobs] {crawl}: {n}/{len(todo_jobs)}", flush=True)


def collect_ashby(fraction=0.08):
    for crawl in CRAWLS:
        p = WORK / "cc_boards" / "ashby" / f"{crawl}.jsonl"
        byk = {}
        for l in p.open():
            r = json.loads(l)
            if str(r.get("status")) != "200" or "html" not in (r.get("mime") or "html"):
                continue
            parsed = ms.parse_url("ashby", r["url"])
            if parsed and int(r.get("length", 0)) >= 7000:
                k = parsed[0]
                if k not in byk or r["timestamp"] < byk[k]["timestamp"]:
                    byk[k] = r
        todo_map = {k: r for k, r in byk.items() if rb.picked(k, fraction)}
        dest = OUT_DIR / f"cc_ashby_{crawl}.jsonl"
        done = {json.loads(l)["key"] for l in dest.open()} if dest.exists() else set()
        todo = [(k, r) for k, r in sorted(todo_map.items()) if k not in done]
        print(f"[ashby] {crawl}: pool={len(byk)} picked={len(todo_map)} todo={len(todo)}", flush=True)

        def fetch_one(item):
            k, ref = item
            try:
                return k, ref, a.cc_record(ref["filename"], ref["offset"], ref["length"]), None
            except Exception as e:
                return k, ref, None, str(e)

        in_scope = 0
        with dest.open("a") as out, ThreadPoolExecutor(3) as ex:
            for n, (k, ref, body, err) in enumerate(ex.map(fetch_one, todo), 1):
                if err is not None:
                    out.write(json.dumps({"key": k, "crawl": crawl, "error": err}) + "\n")
                else:
                    rec = jp.parse_any(body, ref["url"].split("?")[0], "ashby")
                    if rec and role_of(rec.get("title")):
                        in_scope += 1
                        out.write(json.dumps({"key": k, "crawl": crawl, "archive_ref": ref, "record": rec},
                                             ensure_ascii=False) + "\n")
                    else:
                        out.write(json.dumps({"key": k, "crawl": crawl, "archive_ref": ref, "record": None}) + "\n")
                out.flush()
                if n % 200 == 0:
                    print(f"[ashby] {crawl}: {n}/{len(todo)} in_scope={in_scope}", flush=True)
        print(f"[ashby] {crawl}: DONE in_scope={in_scope}", flush=True)


if __name__ == "__main__":
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    collect_builtin()
    collect_greenhouse()
    collect_ashby(0.08)
