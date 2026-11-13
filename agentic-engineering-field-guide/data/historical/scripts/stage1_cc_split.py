"""Fallback for stage1_cc_dump.sh: when a crawl's full builtin.com/job/* index
query times out, fetch it in 36 prefix slices (builtin.com/job/a ... /job/9)."""
import json, string, sys, time
from pathlib import Path
import archive_client as a

OUT = Path(__file__).resolve().parent.parent / "work" / "cc_job_cdx"
FL = "timestamp,url,status,mime,length,offset,filename"
for crawl in sys.argv[1:]:
    f = OUT / f"{crawl}.jsonl"
    if f.exists() and f.stat().st_size:
        continue
    part = OUT / f"{crawl}.parts"; part.mkdir(exist_ok=True)
    for ch in string.ascii_lowercase + string.digits:
        pf = part / f"{ch}.jsonl"
        if pf.exists():
            continue
        rows = a.cc_index(crawl, {"url": f"builtin.com/job/{ch}", "matchType": "prefix", "fl": FL})
        pf.write_text("".join(json.dumps(r) + "\n" for r in rows))
        print(crawl, ch, len(rows), flush=True)
    with open(f, "w") as out:
        for pf in sorted(part.glob("*.jsonl")):
            out.write(pf.read_text())
    print(crawl, "total", sum(1 for _ in open(f)), flush=True)
