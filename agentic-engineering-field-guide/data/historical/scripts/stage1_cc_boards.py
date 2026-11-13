"""Stage 1 (multi-source): Common Crawl index rows for job boards / ATS hosts,
read from the ZipNum index (see stage1_cc_zipnum.py). Index only, no pages.

  python stage1_cc_boards.py [crawl ...]     # default: every crawl already dumped for builtin

Output: ../work/cc_boards/<board>/<crawl>.jsonl  (timestamp, url, status, mime, filename, offset, length)
"""
import json, sys, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from stage1_cc_zipnum import rows

W = Path(__file__).resolve().parent.parent / "work"
BOARDS = {
    "greenhouse": "io,greenhouse,job-boards)/",
    "ashby": "com,ashbyhq,jobs)/",
    "workable": "com,workable,apply)/",
    "personio_de": "de,personio,jobs,",
    "personio_com": "com,personio,jobs,",
    "recruitee": "com,recruitee,",
    "smartrecruiters": "com,smartrecruiters,jobs)/",
    "workday": "com,myworkdayjobs,",
    "reed": "uk,co,reed)/jobs/",
    "wttj": "com,welcometothejungle)/",
    "lever": "co,lever,jobs)/",
}


def end_of(p):
    return p[:-1] + chr(ord(p[-1]) + 1)


def dump(task):
    board, crawl = task
    d = W / "cc_boards" / board; d.mkdir(parents=True, exist_ok=True)
    f = d / f"{crawl}.jsonl"
    if f.exists():
        return board, crawl, "cached"
    p = BOARDS[board]
    for attempt in range(4):
        try:
            rs = [r for r in rows(crawl, p, end_of(p)) if r["status"] == "200"]
            break
        except Exception as e:  # data.commoncrawl.org 503s under load: back off, retry, else skip
            err = e
            time.sleep(30 * (attempt + 1))
    else:
        return board, crawl, f"FAILED {str(err)[:80]} (re-run to retry)"
    tmp = f.with_suffix(".tmp")
    tmp.write_text("".join(json.dumps(r) + "\n" for r in rs))
    tmp.rename(f)
    return board, crawl, len(rs)


if __name__ == "__main__":
    crawls = sys.argv[1:] or sorted(p.stem for p in (W / "cc_job_cdx").glob("*.jsonl"))
    tasks = [(b, c) for c in crawls for b in BOARDS]
    with ThreadPoolExecutor(2) as ex:  # CC returns 403 to this host above ~6 parallel readers
        for b, c, n in ex.map(dump, tasks):
            print(c, b, n, flush=True)
