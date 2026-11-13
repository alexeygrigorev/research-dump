# Historical monthly snapshots of software-developer jobs

Goal (Alexey): «я хочу чтобы было как в ai engineering field guide только чтобы мы могли вернуться в прошлое и сделать слепок с того времени».

The AI Engineering Field Guide (`~/git/ai-engineering-field-guide/job-market`) scrapes Built In (builtin.com) once a month. Its scraper, `_internal/scrapers/scrape_builtin_requests.py`, works in two steps:

1. Read the city search pages (`builtin.com/jobs?search=...&city=London&country=GBR&allLocations=true`) and collect only job links.
2. Download each `builtin.com/job/<slug>/<id>` page and parse its JSON-LD `JobPosting` with `extract_from_html.py` into the `data_raw` YAML schema.

To go back in time, we rebuild both steps from web archives instead of the live site. Everything below is free: no JobsPipe credits, no Coresignal, no AWS Athena.

Scope (Alexey t3349u–t3353u):

- Roles: Software Engineer, Software Developer, Backend, Frontend, Full Stack, Engineering Manager. The title and URL-slug filter is in `data/historical/scripts/roles.py`.
- Cities: London, Berlin, New York.
- Months: Jul 2025 to Nov 2026, so earlier than the required Nov 2025.
- Sample size: about 100 postings per city and month.

Code and data are in [`data/historical/`](data/historical/). The `work/` cache (288 MB of archived HTML and index dumps) is git-ignored and can be rebuilt with the scripts.

## Pipeline

### Stage 1: links that existed in a given month

| Step | Script | Source | What it gives |
|---|---|---|---|
| 1a | `stage1_wayback_dump.py` | Wayback CDX API, prefix `builtin.com/job/` (56 pages, sequential, 1.5 s between requests, retries with backoff) | Every archived capture of a Built In job page, with its timestamp |
| 1b | `stage1_cc_zipnum.py` | Common Crawl ZipNum index files on `data.commoncrawl.org`: binary search in `cluster.idx`, then range reads of the `com,builtin)/job/` blocks | Every Built In job page in 16 crawls (CC-MAIN-2025-30 to CC-MAIN-2026-43), in about 2 minutes. The `index.commoncrawl.org` server times out (504) on these wildcard queries and returned truncated dumps |
| 1c, 1d | `stage1_listing_cdx.py`, `stage1_fetch_listings.py` | Wayback captures of the Built In city listing pages (the same URLs the field guide scrapes) | Job cards that appeared on the London, Berlin or New York search page in that month |
| 1e | `stage1_resolve.py` | One read of each in-scope job page (Common Crawl WARC range read, or Wayback `id_` raw) | The job's city, taken from its JSON-LD `jobLocation`. Job URLs carry no location |

A job page counts for month M if any capture of it has a timestamp in M. That is the archive's version of "the posting was live in M".

### Stage 2: snapshot

`stage2_snapshot.py <city> <months...> --n 100`:

1. Build the candidate pool for each month:
   - links from archived listing pages, which are already known to be in the city;
   - detail captures already resolved to the city;
   - in-scope detail captures whose city is still unknown.
2. Shuffle each group with a fixed seed: `random.Random("20261113-<city>-<month>")`.
3. Fetch each candidate from the archive (Common Crawl first, then Wayback). Every page is cached once in `work/html/`.
4. Parse it with `builtin_parse.py`, which is the field guide's `extract_from_html.py` vendored unchanged (commit 2c6221c6). The output therefore has the same fields as the field guide's `data_raw`.
5. Keep the posting if the title is in scope, a location is in the city, and there is a description.
6. Write `data/historical/<city>/<YYYY-MM>.jsonl.gz` and record per-month stats in `data/historical/manifest.json`.

Each record has the field-guide fields plus six more:

- `role`
- `snapshot_month`
- `city`
- `archive_source`: `common_crawl` or `wayback`
- `archive_timestamp`
- `archive_ref`: the WARC file, offset and length, or the Wayback URL

### Dedup

Months are processed in order. The first month that samples a `job_id` (and its canonical URL without the query string) claims it for good. Before a new run, every published `*/*.jsonl.gz` file is loaded into the claimed set. So:

- a posting never appears in two monthly samples, across all cities and months;
- re-runs and new months keep that guarantee.

A long-running posting therefore counts in the first month it was sampled. That matches the field guide, whose monthly scrapes also deduplicate by job id.

## Measured coverage

All counts come from the real index dumps in this repo, as of 2026-11-13.

### Raw Built In job-page captures per month, all cities

| Month | Common Crawl: all jobs | Common Crawl: in-scope slug | Wayback: all jobs | Wayback: in-scope slug |
|---|---|---|---|---|
| 2025-07 | 6176 | 772 | 15697 | 1414 |
| 2025-08 | 5937 | 715 | 9656 | 1301 |
| 2025-09 | 5589 | 761 | 9216 | 1295 |
| 2025-10 | 6484 | 901 | 8129 | 1130 |
| 2025-11 | 6336 | 908 | 10052 | 1382 |
| 2025-12 | 5835 | 773 | 7924 | 1124 |
| 2026-01 | 5001 | 662 | 7439 | 1048 |
| 2026-02 | 4944 | 642 | 10145 | 1447 |
| 2026-03 | 5254 | 627 | 8179 | 1042 |
| 2026-04 | 5300 | 632 | 6217 | 736 |
| 2026-05 | 6590 | 837 | 7614 | 967 |
| 2026-06 | 5919 | 725 | 7054 | 833 |
| 2026-07 | 128 | 21 | 1548 | 141 |
| 2026-08 | 137 | 26 | 1131 | 121 |
| 2026-09 | 172 | 33 | 1712 | 147 |
| 2026-10 | 4563 | 622 | 1582 | 204 |
| 2026-11 | 0 | 0 | 916 | 85 |

### In-scope postings per city and month

Each cell is in-scope job ids found in the city, written as Common Crawl / Wayback detail pages / listing pages / **distinct ids in any of the three**. Output of `scripts/coverage.py`, saved as `data/historical/coverage.json`.

| Month | London | Berlin | New York |
|---|---|---|---|
| 2025-07 | 20/21/0/**21** | 5/5/0/**5** | 45/50/0/**50** |
| 2025-08 | 21/24/0/**24** | 1/2/0/**2** | 40/73/0/**73** |
| 2025-09 | 17/21/0/**21** | 11/12/1/**13** | 60/84/1/**85** |
| 2025-10 | 13/14/3/**17** | 10/10/2/**12** | 78/89/6/**95** |
| 2025-11 | 17/18/4/**22** | 9/9/0/**9** | 84/99/11/**110** |
| 2025-12 | 15/17/2/**19** | 4/4/0/**4** | 57/69/7/**74** |
| 2026-01 | 18/19/0/**19** | 2/2/0/**2** | 56/60/6/**64** |
| 2026-02 | 20/31/9/**40** | 4/4/0/**4** | 61/71/12/**83** |
| 2026-03 | 29/38/1/**39** | 6/6/0/**6** | 39/47/2/**49** |
| 2026-04 | 24/27/0/**27** | 5/5/0/**5** | 48/54/5/**59** |
| 2026-05 | 26/27/5/**31** | 3/3/0/**3** | 48/54/8/**61** |
| 2026-06 | 19/20/0/**20** | 1/1/0/**1** | 48/49/2/**51** |
| 2026-07 | 0/2/0/**2** | 0/0/0/**0** | 3/3/1/**5** |
| 2026-08 | 0/0/0/**0** | 0/0/0/**0** | 3/3/0/**3** |
| 2026-09 | 1/0/0/**1** | 0/0/0/**0** | 5/1/0/**6** |
| 2026-10 | 13/1/0/**14** | 4/0/0/**4** | 67/1/0/**67** |
| 2026-11 | 0/0/0/**0** | 0/0/0/**0** | 0/0/0/**0** |

Some Wayback-only in-scope links have not been resolved to a city yet: between 69 and 613 per month across all cities (`unresolved_in_scope_links` in `coverage.json`). `stage1_resolve.py wb` resolves them at 1.5 s per request. Based on the resolved share, about 10% of them should land in the three cities, which would add roughly 5 to 60 postings per month.

### Bias of each source

- **Built In itself is US-centric.** Of the 9,657 in-scope Common Crawl job pages resolved to a city:
  - 750 (7.8%) are New York;
  - 255 (2.6%) are London;
  - 67 (0.7%) are Berlin;
  - the rest are other cities, mostly in the US.

  The live field guide has the same skew, so the archive keeps the source's mix. It does not invent one.
- **Common Crawl.**
  - It is a crawler sample, about 5,000 to 6,500 Built In job pages per crawl. Selection follows CCBot's link ranking, so it favours pages that are linked a lot (big companies, featured jobs) over a random draw.
  - There is about one crawl per month. CC-MAIN-2026-30, -34 and -39 (Jul–Sep 2026) hold almost no Built In pages, and the crawl that will cover Nov 2026 is not out yet.
  - The full page HTML, including JSON-LD, is in the WARC, so a capture always gives the full text.
- **Wayback Machine.**
  - It holds more captures (7,000 to 16,000 per month up to Jun 2026). They come from Save Page Now, from Archive Team and from Wayback's own crawls, so they cluster around popular companies and around pages someone chose to save.
  - Capture volume falls sharply from Jul 2026. The archive also had outages during this work.
  - Some captures are redirects or "job no longer available" pages. Stage 2 drops these because they have no JSON-LD description.
- **Archived listing pages.** These are the closest match to the field guide's own step 1 (the city search page), but only a few were archived. They are useful for checking the city, not for volume.
- **Web Data Commons JobPosting.** This was not used. WDC publishes a schema.org extract about once a year from a single Common Crawl crawl, so it cannot give monthly snapshots. Reading Common Crawl directly, as above, gives the same JSON-LD for every crawl. This is from WDC's release notes and was not measured here.
- **Within-month timing.** A capture shows that the posting was live on the capture date, not when it was posted. `posted_date` from the JSON-LD is kept, so the analysis can filter on it.

How to control the bias:

- Report Built In history per source and per month with the n from the manifest.
- Compare shares (role mix, seniority, skills), not absolute counts.
- Treat months with n < 30 (most of Berlin, and Jul–Sep 2026 everywhere) as "not enough data" instead of trends.
- Keep `archive_source` on every record so the analysis can check that the Common Crawl and Wayback halves agree.

## Pilot: London, three past months

Command: `python stage2_snapshot.py london 202511 202512 202601 --n 100 --max-fetch 70`. Output is in `data/historical/london/`, with stats in `data/historical/manifest.json`.

| Month | Postings kept | Source | Roles | Description length (min / median, chars) |
|---|---|---|---|---|
| 2025-11 | 17 | Common Crawl 17 | software_engineer 8, full_stack 3, backend 3, engineering_manager 2, frontend 1 | 2271 / 5036 |
| 2025-12 | 15 | Common Crawl 15 | software_engineer 6, backend 4, frontend 2, full_stack 2, software_developer 1 | 2291 / 4750 |
| 2026-01 | 18 | Common Crawl 18 | software_engineer 10, backend 4, full_stack 2, engineering_manager 1, frontend 1 | 1911 / 4969 |

In total there are 50 postings, each with full description text. Dedup check across the three files: 0 duplicate `job_id`s and 0 duplicate URLs.

What the pilot found:

- **London is far below the 100-per-month target.** The measured pool is only 19–22 in-scope London jobs a month, and the sample takes almost all of them.
- **Wayback reads were broken during this run.** Wayback `id_` replays the original `Content-Encoding: gzip` bytes, and `archive_client.get` stored them undecoded. As a result, every Wayback fetch in this run looked like a page without JSON-LD (the `no_jsonld` count in the manifest).
- **That bug is now fixed,** together with a purge of 223 corrupted cache files. A Wayback fetch now returns the full page with JSON-LD.
- **Multi-location postings are included.** A posting that lists London among several locations (for example a remote job open in many countries) counts as London. The `locations` field keeps the full list, so the analysis can filter these out.

## Rebuilding every month

```bash
cd agentic-engineering-field-guide/data/historical/scripts
python stage1_wayback_dump.py                       # Wayback job CDX (resumable)
python stage1_cc_zipnum.py CC-MAIN-2025-30 ... CC-MAIN-2026-43
python stage1_listing_cdx.py && python stage1_fetch_listings.py
python stage1_resolve.py cc && python stage1_resolve.py wb
python coverage.py                                   # -> ../coverage.json + table
python stage2_snapshot.py london   202507 202508 ... 202610 --n 100
python stage2_snapshot.py newyork  202507 202508 ... 202610 --n 100
python stage2_snapshot.py berlin   202507 202508 ... 202610 --n 100
```

Cost is $0:

- Common Crawl data is read over HTTPS range requests from `data.commoncrawl.org`. No AWS account is needed.
- The Wayback Machine is free. `archive_client.py` waits at least 1.5 s between Wayback requests and retries with exponential backoff.

Rough time for the full rebuild:

- Common Crawl reads: a few minutes.
- Wayback reads: about 1 to 3 hours for the unresolved links.
- Everything already fetched is cached in `work/html/`, so re-runs are free.

## Adding new months

- When Common Crawl publishes a new crawl (see `https://data.commoncrawl.org/crawl-data/index.html`), run `stage1_cc_zipnum.py <new crawl>`.
- Re-run `stage1_wayback_dump.py`. It is resumable, but delete the last page so that new captures are picked up.
- Run `stage1_resolve.py`, `coverage.py`, then `stage2_snapshot.py <city> <new month>`. The dedup set comes from the published samples, so the new month never repeats an earlier posting.
- From now on, also save the live monthly field-guide-style scrape for these roles. A live scrape gives the full population instead of an archive sample. Archives are only needed for months we did not scrape ourselves.

## Recommendation

1. **New York:** Built In archives alone give about 50 to 110 in-scope postings a month for Jul 2025 to Jun 2026. That is close to the 100 target, so build it now.
2. **London:** about 20 to 40 a month. Build it, and treat it as a sample that has n in the manifest.
3. **Berlin:** under 15 a month, because Built In has little Berlin content. Built In archives cannot give a Berlin series.
4. **To reach about 100 a month in London and Berlin for free,** run the same ZipNum method on the Common Crawl index for the ATS boards that host these jobs directly: `job-boards.greenhouse.io`, `jobs.ashbyhq.com`, `jobs.smartrecruiters.com` and `*.workable.com`. All of them publish JSON-LD `JobPosting`. Only `stage1_cc_zipnum.py`'s `PREFIX` and the parser need changing. This was not done in this task. Note that `jobs.lever.co` blocks CCBot.
5. **Jul–Sep 2026:** both archives are thin. The live field-guide scrapes and JobsPipe (for live postings since Aug 2026) cover this period better.
