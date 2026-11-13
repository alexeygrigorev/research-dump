"""Stage 1c: find every Wayback capture of a builtin.com listing page
(builtin.com/jobs...) for London / Berlin / New York, Sep 2025 - Nov 2026.

Output: ../work/listing_cdx.jsonl  (timestamp, original, statuscode, city)
Resumable per CDX page (../work/listing_cdx_pages/).
"""
import json, re
from pathlib import Path
import archive_client as a

W = Path(__file__).resolve().parent.parent / "work"
PD = W / "listing_cdx_pages"; PD.mkdir(parents=True, exist_ok=True)
CITY_RE = r".*city=(London|Berlin|New(%20|\+|%2B)York).*"
n = a.cdx({"url": "builtin.com/jobs", "matchType": "prefix", "showNumPages": "true"})
print("pages", n, flush=True)
for p in range(n):
    f = PD / f"{p:03d}.jsonl"
    if f.exists():
        continue
    rows = a.cdx({"url": "builtin.com/jobs", "matchType": "prefix", "page": str(p),
                  "from": "20250901", "to": "20261130", "filter": ["original:" + CITY_RE, "statuscode:200"],
                  "fl": "timestamp,original,statuscode,digest"})
    with open(f.with_suffix(".tmp"), "w") as fh:
        for r in rows:
            fh.write(json.dumps(r) + "\n")
    f.with_suffix(".tmp").rename(f)
    print(p, len(rows), flush=True)
