"""Stage 1g: Greenhouse company boards (job-boards.greenhouse.io/<company>) as listing pages.

Like the field guide's stage 1 (listing pages -> job links), one archived company
board page embeds every open job of that company: id, title, location, URL,
published_at (and usually the full description). One read per company per crawl
replaces reading every job page (~2,650 reads per crawl instead of ~17,000).

  python stage1_gh_listings.py [crawl ...]      # default: every crawl with a greenhouse index dump

Panel design: only companies whose name hash falls in a fixed half (PANEL_FRACTION) are read,
in every crawl. The same companies are followed month to month, so a crawl that captures more
or fewer boards changes n, not the company mix (crawl-bias control, Alexey t3383u).

3 readers (Common Crawl 403s this host above ~5 parallel readers). Resumable per crawl.
Output: ../work/gh_listings/<crawl>.jsonl.gz, one row per (company, job):
  key, company, job_id, title, location, region, city, role, published_at, month, url, description (in-scope only)
Only the first page of a board is archived as one capture; boards with >1 page are counted in
`boards_with_more_pages` in the log (their extra jobs are not seen).
"""
import gzip, hashlib, json, re, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import archive_client as a
import jobposting_parse as jp
from regions import region_of, city_of
from roles import role_of

W = Path(__file__).resolve().parent.parent / "work"
DEC = json.JSONDecoder()
PANEL_FRACTION = 0.5
READERS = 3  # Common Crawl answers 403 to this host above ~5 parallel readers


def in_panel(company):
    return int(hashlib.sha1(company.lower().encode()).hexdigest()[:8], 16) < PANEL_FRACTION * 0xFFFFFFFF


def jobs_in(html):
    i = html.find('"jobPosts":')
    if i < 0:
        return [], 0
    j = html.find('"data":[', i)
    if j < 0:
        return [], 0
    try:
        data, _ = DEC.raw_decode(html, j + len('"data":'))
    except ValueError:
        return [], 0
    tp = re.search(r'"total_pages":(\d+)', html[i:j])
    return data, int(tp.group(1)) if tp else 1


def main():
    crawls = sys.argv[1:] or sorted(p.stem for p in (W / "cc_boards" / "greenhouse").glob("*.jsonl"))
    outd = W / "gh_listings"; outd.mkdir(parents=True, exist_ok=True)
    for crawl in crawls:
        out = outd / f"{crawl}.jsonl.gz"
        if out.exists():
            print(crawl, "done", flush=True); continue
        boards = {}
        for l in open(W / "cc_boards" / "greenhouse" / f"{crawl}.jsonl"):
            r = json.loads(l)
            m = re.fullmatch(r"https?://job-boards\.greenhouse\.io/([^/?#]+)/?", r["url"].split("?")[0])
            if m and "html" in (r.get("mime") or "html"):
                boards.setdefault(m.group(1).lower(), r)
        boards = {co: r for co, r in boards.items() if in_panel(co)}
        rows, errors, multi = [], 0, 0

        def read(item):
            co, r = item
            try:
                return co, r, a.cc_record(r["filename"], r["offset"], r["length"]), None
            except Exception as e:
                return co, r, None, e

        with ThreadPoolExecutor(READERS) as ex:
            results = ex.map(read, sorted(boards.items()))
            for n, (co, r, html, err) in enumerate(results):
                if err is not None:
                    errors += 1
                    if errors >= 20 and errors > n // 2:
                        print(crawl, "too many errors, stopping:", err, flush=True); sys.exit(2)
                    continue
                rows_for(co, r, html, rows, crawl)
                multi_pages = jobs_in(html)[1] > 1
                multi += multi_pages
                if n % 500 == 0:
                    print(crawl, n, len(boards), len(rows), flush=True)
        with gzip.open(out.with_suffix(".tmp"), "wt", encoding="utf-8") as fh:
            for row in rows:
                fh.write(json.dumps(row, ensure_ascii=False) + "\n")
        out.with_suffix(".tmp").rename(out)
        print(crawl, "boards", len(boards), "jobs", len(rows), "in_scope", sum(bool(x["role"]) for x in rows),
              "boards_with_more_pages", multi, "errors", errors, flush=True)


def rows_for(co, r, html, rows, crawl):
    data, pages = jobs_in(html)
    for d in data:
        loc = d.get("location") or ""
        if isinstance(loc, dict):
            loc = loc.get("name", "")
        role = role_of(d.get("title"))
        row = {"key": f"gh/{co}/{d.get('id')}", "company": co, "job_id": str(d.get("id")),
               "title": d.get("title"), "location": loc, "region": region_of(loc), "city": city_of(loc),
               "role": role, "published_at": (d.get("published_at") or "")[:10],
               "month": r["timestamp"][:6], "url": d.get("absolute_url"), "source": "greenhouse",
               "crawl": crawl}
        if role and d.get("content"):
            row["description"] = jp.clean_html(d["content"])
        rows.append(row)


if __name__ == "__main__":
    main()
