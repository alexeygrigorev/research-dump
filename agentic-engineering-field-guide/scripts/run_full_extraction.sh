#!/usr/bin/env bash
# Run from repository root. Repeat only failed hashes; successful model calls are cached.
set -euo pipefail
input=${1:?frozen live input directory required}
python_bin=${JOBS_EXTRACTOR_PYTHON:-python3}
for attempt in 1 2 3 4 5; do
  if "$python_bin" agentic-engineering-field-guide/scripts/extract_jobs.py --live-input "$input" --workers 8; then
    "$python_bin" agentic-engineering-field-guide/scripts/report_jobs.py
    "$python_bin" agentic-engineering-field-guide/scripts/check_extraction.py
    exit 0
  fi
done
exit 1
