# Raw historical vacancies (step 1, t3413u part 2)

All archived vacancies for the 6 roles (Software Engineer, Backend, Frontend, Full Stack,
Software Developer, Engineering Manager), **every geography, no city filter, no sampling,
no LLM**. Step 2 (filtering / LLM structuring) is not started.

- `vacancies.jsonl.gz` - one deduplicated vacancy per line: title, role, company, locations,
  region, posted_date, first/last archive capture, source + archive, url, full-text description
  (markdown), content hash, ids of content-duplicates that were merged.
- `counts_month_role_region.csv` - month x role x region grid.
- `COUNTS.md` - funnel, dedup proof, month x role and month x region tables.
- `summary.json` - same numbers, machine-readable.

Rebuild: `python scripts/build_raw.py <work_dir> raw` (about 15 s, 8 processes).

Sources (all free, no spend): the 937 MB `work/` cache produced by the stage1 scripts -
builtin.com job pages fetched from Common Crawl and the Wayback Machine (10,275 cached pages),
Greenhouse board listings and Greenhouse/Ashby job pages read from Common Crawl CC-MAIN-2025-47.

Processing: JSON-LD JobPosting parse (field-guide parser, `builtin_parse.py`), regex role
filter on title (`roles.py`), regex region from first location (`regions.py` + world buckets),
dedupe 1 by source+job id (keeps first capture, records capture span), dedupe 2 by
sha1(title|company|description[:2000]) across ids and sources.

Month = month of the first archive capture. Known gaps: Common Crawl captured few builtin
pages in 2026-07..09 (see `work/logs/measure.txt`), and the Greenhouse/Ashby boards were read
for one crawl only (2025-11), which inflates that month. The `work/` cache itself is not in git.
