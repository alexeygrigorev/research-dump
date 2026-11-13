"""Stage 1a: dump the full Wayback CDX index for builtin.com/job/* (all pages).

Output: ../work/wayback_job_cdx/page_NNN.jsonl (one capture per line).
Resumable: pages already on disk are skipped. Sequential = polite.
"""
import json, sys
from pathlib import Path
import archive_client as a

OUT = Path(__file__).resolve().parent.parent / "work" / "wayback_job_cdx"
OUT.mkdir(parents=True, exist_ok=True)
prefix = sys.argv[1] if len(sys.argv) > 1 else "builtin.com/job/"
tag = sys.argv[2] if len(sys.argv) > 2 else "builtin"
n = a.cdx({"url": prefix, "matchType": "prefix", "showNumPages": "true"})
print("pages", n, flush=True)
for p in range(n):
    f = OUT / f"{tag}_page_{p:03d}.jsonl"
    if f.exists():
        continue
    rows = a.cdx({"url": prefix, "matchType": "prefix", "page": str(p),
                  "fl": "timestamp,original,statuscode,mimetype,digest"})
    tmp = f.with_suffix(".tmp")
    with open(tmp, "w") as fh:
        for r in rows:
            fh.write(json.dumps(r) + "\n")
    tmp.rename(f)
    print(p, len(rows), flush=True)
