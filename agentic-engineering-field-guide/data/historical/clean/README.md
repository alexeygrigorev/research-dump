# Cleaned vacancies (t3450u)

`vacancies.jsonl.gz` 11,292 rows (raw: 11,359). Same schema as `raw/` plus `lang`, `month_basis`, `posted_month`, `regions_all`,
`n_locations`, `region_original` (only where region changed). `rejects.jsonl.gz`: 9 rows with placeholder descriptions.
`dedupe2_merges.jsonl`: 58 merged rows. `summary.json`: step counts and before/after quality metrics.
Rebuild: `python scripts/clean_raw.py` (needs `raw/vacancies.jsonl.gz`). Report: `../QUALITY_REPORT.md`. No structuring or extraction done.
