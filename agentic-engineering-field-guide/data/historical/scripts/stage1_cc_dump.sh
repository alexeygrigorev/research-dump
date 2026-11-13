#!/bin/bash
# Stage 1b: dump Common Crawl index rows for builtin.com/job/* for each monthly crawl.
# Output: ../work/cc_job_cdx/<crawl>.jsonl  (resumable; sequential; polite)
OUT="$(dirname "$0")/../work/cc_job_cdx"; mkdir -p "$OUT"
UA="research-dump-historical-snapshots/0.1 (polite archive research)"
CRAWLS="${CRAWLS:-CC-MAIN-2025-38 CC-MAIN-2025-43 CC-MAIN-2025-47 CC-MAIN-2025-51 CC-MAIN-2026-04 CC-MAIN-2026-08 CC-MAIN-2026-12 CC-MAIN-2026-17 CC-MAIN-2026-21 CC-MAIN-2026-25 CC-MAIN-2026-30 CC-MAIN-2026-34 CC-MAIN-2026-39 CC-MAIN-2026-43}"
for c in $CRAWLS; do
  f="$OUT/$c.jsonl"; [ -s "$f" ] && continue
  for try in 1 2 3 4 5 6; do
    if curl -sf -m 1500 -A "$UA" "https://index.commoncrawl.org/$c-index?url=builtin.com/job/*&output=json&fl=timestamp,url,status,mime,length,offset,filename" -o "$f.tmp"; then
      mv "$f.tmp" "$f"; echo "$c $(wc -l < "$f")"; break
    fi
    echo "$c try $try failed"; sleep $((30*try))
  done
  sleep 5
done
