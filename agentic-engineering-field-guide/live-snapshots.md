# Live monthly snapshots of software-developer jobs

Goal (Alexey): start collecting monthly live snapshots of software engineering job postings using the same proven Built In scraper and HTML-to-YAML extractor as the [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide), so historical data accumulates going forward.

## Scope

- **Roles (6):** Software Engineer, Software Developer, Backend, Frontend, Full Stack, Engineering Manager.
- **Cities (15):**
  - Core: `london` (London, UK), `berlin` (Berlin, Germany), `newyork` (New York, USA)
  - Expanded: `sf_bay_area` (SF Bay Area, USA), `seattle` (Seattle, USA), `austin` (Austin, USA), `boston` (Boston, USA), `chicago` (Chicago, USA), `toronto` (Toronto, Canada), `amsterdam` (Amsterdam, Netherlands), `paris` (Paris, France), `munich` (Munich, Germany), `dublin` (Dublin, Ireland), `warsaw` (Warsaw, Poland), `remote` (Remote).
- **Sampling & no-overlap:** Random sample of up to 100 listings per city-month (`--sample-per-city 100`, `--pages-per-role 3`). Any job ID already in `data/live/data/all_jobs_dedup.csv` is excluded so consecutive monthly snapshots do not overlap. Spam companies (`Alignerr`) are filtered out, and within-scrape `(title, company)` and `id` duplicates are removed.
- **Cost:** $0 paid job-data APIs; uses Built In public pages via existing residential proxy config (`DATAIMPULSE_*` / `OXYLABS_*` in `.env` or `~/.config/youtube/.env`).

## One-command monthly run

From `agentic-engineering-field-guide/data/live/`:

```bash
./run_monthly.sh
```

Or with explicit options:

```bash
uv run python scripts/run_monthly.py --date 2026-11-25 --sample-per-city 100 --pages-per-role 3
```

Pipeline steps executed by `scripts/run_monthly.py`:
1. `scripts/scrape_builtin_requests.py` — scrapes 15 cities x 6 roles, excludes prior-month IDs, samples up to 100 per city, writes `data/builtin/{city}_{YYYYMMDD}.json` and `data/scrapes/{YYYY-MM-DD}/all_jobs.csv`.
2. `scripts/clean_dedup.py` — deduplicates by `id` and `(title, company)`, writes `data/scrapes/{YYYY-MM-DD}/all_jobs_dedup.csv` and updates global `data/all_jobs_dedup.csv`.
3. `scripts/download_all_html.py` — 8-threaded download of job detail HTML pages into `jobs/raw/{YYYY-MM-DD}/` (gitignored).
4. `scripts/extract_from_html.py --all` — parses JSON-LD `JobPosting` + HTML fields into `data_raw/{YYYY-MM-DD}/{id}_{company}_{title}.yaml`.

### 25th-of-month schedule wiring

The AI Engineering Field Guide monthly scrape runs on the 25th of each month via Hub schedule (not local crontab). Worker credentials cannot read or modify Hub schedules (`hub schedule list` returns HTTP 403), so wiring `./run_monthly.sh` into the 25th Hub schedule requires adding `cd agentic-engineering-field-guide/data/live && ./run_monthly.sh` to the 25th field-guide schedule by an operator/owner.

## First snapshot: `2026-11` (`2026-11-13`)

1,500 listings sampled (100 per city across all 15 cities); 159 cross-city / same-`(title, company)` duplicates removed by `clean_dedup.py`, yielding **1,341 unique jobs**, **1,341 downloaded HTML pages** (0 failed), and **1,341 extracted YAML files** in `data/live/data_raw/2026-11-13/`.

| City | Sampled (raw) | Unique (dedup) | Extracted YAML |
|---|---:|---:|---:|
| `amsterdam` | 100 | 100 | 100 |
| `austin` | 100 | 100 | 100 |
| `berlin` | 100 | 97 | 97 |
| `boston` | 100 | 100 | 100 |
| `chicago` | 100 | 99 | 99 |
| `dublin` | 100 | 72 | 72 |
| `london` | 100 | 96 | 96 |
| `munich` | 100 | 92 | 92 |
| `newyork` | 100 | 100 | 100 |
| `paris` | 100 | 86 | 86 |
| `remote` | 100 | 69 | 69 |
| `seattle` | 100 | 97 | 97 |
| `sf_bay_area` | 100 | 97 | 97 |
| `toronto` | 100 | 92 | 92 |
| `warsaw` | 100 | 44 | 44 |
| **TOTAL** | **1,500** | **1,341** | **1,341** |
