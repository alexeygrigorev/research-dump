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

Command: `python stage2_snapshot.py london 202511 202512 202601 --n 100 --max-fetch 120`. Output is in `data/historical/london/`, with stats in `data/historical/manifest.json`.

| Month | Postings kept | Source | Roles | Description length (min / median, chars) |
|---|---|---|---|---|
| 2025-11 | 19 | Common Crawl 17, Wayback 2 | software_engineer 9, backend 4, full_stack 3, engineering_manager 2, frontend 1 | 2163 / 4672 |
| 2025-12 | 17 | Common Crawl 15, Wayback 2 | software_engineer 6, backend 4, engineering_manager 2, frontend 2, full_stack 2, software_developer 1 | 2291 / 4863 |
| 2026-01 | 19 | Common Crawl 18, Wayback 1 | software_engineer 10, backend 5, full_stack 2, engineering_manager 1, frontend 1 | 1911 / 4857 |

In total there are 55 postings, each with full description text. Dedup check across the three files: 0 duplicate `job_id`s and 0 duplicate URLs.

What the pilot found:

- **London is far below the 100-per-month target.** The measured pool is only 19–22 in-scope London jobs a month, and the sample takes almost all of them. The 98–102 `other_city` rejections a month are unresolved Wayback links that turned out to be other cities.
- **A Wayback bug was found and fixed.** Wayback `id_` replays the original `Content-Encoding: gzip` bytes, and the first run stored them undecoded, so every Wayback page looked empty. `archive_client.get` now decompresses them, and the 223 corrupted cache files were purged.
- **Multi-location postings are included.** A posting that lists London among several locations counts as London. `locations` keeps the full list, so the analysis can filter these out.

## Rebuilding all past months

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

## Every month: one command

Alexey t3381u: «можно будет повторять каждый месяц. это стоит чего-то?»

Yes, it can be repeated every month, and it costs nothing. One command does the whole month:

```bash
cd agentic-engineering-field-guide/data/historical/scripts
python monthly.py            # the previous calendar month
python monthly.py 2026-11    # or a given month; re-running a month rebuilds it
```

`monthly.py` is incremental. It only adds what is new:

1. **Common Crawl.** It reads `collinfo.json` and dumps the Built In job rows of every crawl that is not on disk yet.
2. **Wayback job pages.** It runs a CDX query for `builtin.com/job/*` captures, limited to that month (`from=YYYYMM&to=YYYYMM`). The query is resumable per page.
3. **Wayback listing pages.** It runs the same month-limited query for the London, Berlin and New York listing pages, then reads their job cards.
4. **City resolution.** It reads the in-scope links captured that month: Common Crawl in parallel, Wayback at one request per 1.5 s. Use `--skip-wb-resolve` to make the run faster.
5. **Coverage.** It runs `coverage.py`.
6. **Samples.** It runs `stage2_snapshot.py <city> <month>` for each city, which writes `<city>/<YYYY-MM>.jsonl.gz` and updates `manifest.json`.

Before you commit the new files, check that n in the manifest has not dropped below 30. If it has, treat that month as "not enough data".

**Cost: $0.**

- No paid API, no JobsPipe credits, and no AWS account. Common Crawl is plain HTTPS to `data.commoncrawl.org`, and the Wayback Machine is free.
- The only cost is runtime, roughly 15 to 60 minutes a month. Most of it is the polite Wayback rate limit.
- Disk grows by about 20 to 40 MB of cached HTML a month in the git-ignored `work/` folder.

**When to run it.**

- Run it a few days after the month ends, in the same week as the field guide's monthly Built In scrape.
- Common Crawl publishes a crawl 2 to 4 weeks after it runs. So also re-run the month before: `python monthly.py <previous month>`. That picks up the late crawl and rebuilds the earlier month.
- A rebuild ignores the month's own old sample, but it still respects postings that other months have claimed. So dedup holds.

**Live scrape.** Starting now, also save a live field-guide-style scrape for these roles each month (the field guide's `scrape_builtin_requests.py` with these search terms and cities). A live scrape covers the whole population instead of an archive sample. Archives are only needed for months we did not scrape ourselves.

## Expanding the sample until it is stable

Alexey asked for two things here:

- t3382u: «расширяй выборку пока не будет достаточно данных - чтобы данные были стабильные из месяца в месяц»
- t3383u: «надо аккуратно только потому что там могут быть смещения в крауле»

### Stopping criterion

A region-month is good enough to draw conclusions from when all three of these hold. They are checked in `scripts/stability.py`, and the output is in `data/historical/stability.json`.

1. **n ≥ 300** distinct in-scope postings, after dedup across months.
2. **Role-mix shift.** The total variation distance (TVD) between this month's role mix and last month's is **≤ 0.10**. TVD is half the sum of absolute share differences over the six role buckets: 0.10 means at most 10% of postings would need to change bucket.
3. **Shift no bigger than noise.** That TVD is **≤ 2× the TVD expected from sampling noise alone** at this n. The noise level comes from a bootstrap of two random samples of size n drawn from the same mix. A shift within noise is not a finding.

Regions are country markets (UK, DE, US). The city (london, berlin, newyork) is kept on every record, so London, Berlin and NYC can still be cut out of a region.

### Sources added

All sources are Common Crawl index rows, read free from ZipNum (`scripts/stage1_cc_boards.py`). The roles and region come from the URL where the URL carries them; otherwise a page has to be read.

| Source | Job pages per crawl | Title in URL | Region in URL | JSON-LD full text (sample read) | Role in the sample |
|---|---|---|---|---|---|
| Built In | 4,900–6,600 | yes (slug) | no (resolved from page) | yes | baseline, matches the field guide |
| Workday (`*.myworkdayjobs.com`) | 30,000–37,600 | yes | yes (location slug) | 2/12 | the main US source: 450–600 in-scope US postings per crawl |
| Greenhouse (`job-boards.greenhouse.io`) | 16,000–18,400 | no | no | 0/12 (getro redirect wrappers) | large but needs page reads; not used yet |
| Welcome to the Jungle | 6,400–9,500 | yes | yes (city slug) | 5/12 | mostly France; few UK/DE in-scope |
| Lever | 5,800–6,500, then **0 from CC-MAIN-2025-47** | no | no | 7/12 | lost when Lever started blocking CCBot |
| Ashby | **3,000–8,600** | no | no | 9/12 | read sample: 7% in scope, mostly US |
| Personio (.de/.com) | **290–4,200** | no | DE by host | 3/12 | German titles («Softwareentwickler») need German role terms |
| reed.co.uk | 500–1,600 job pages | yes | UK | 2/12 | 5–24 in-scope a crawl |
| SmartRecruiters, Recruitee, Workable | 1,300–3,100 each | partly | no | low | small |

### Crawl bias, measured

`data/historical/source_measurement.json` has, for every crawl and source, the captures, distinct job pages and in-scope counts (from URL). The crawler changes far more than the market does:

- **Personio.de:** 294 job pages in CC-MAIN-2025-30, then 4,058 in the next crawl (14×).
- **Ashby:** 3,000 → 8,600 → 3,100 across crawls.
- **Recruitee:** 2,364 → 85 → 1,614.
- **Lever:** about 6,000 → 0 from Nov 2025.
- **Built In:** about 5,500, then 128–172 in Jul–Sep 2026, then 4,563.

Raw counts per month are therefore crawler behaviour and must never be read as the market growing or shrinking.

Workday's share of all job pages is the steadiest of the sources, at 0.36–0.43 across crawls.

### How bias is controlled

1. **Only shares are compared** (role mix, and later seniority and skills), never counts.
2. **Fixed source weights.** The role mix is computed per source, then combined with fixed weights equal to each source's average share over the window. A crawl that over-collects one board therefore cannot shift the mix. `stability.json` has both `role_mix_raw` and `role_mix_fixed`, so the effect of the reweighting is visible.
3. **Crawl-shift flag.** A month is flagged when any source's share falls outside 0.5× to 2× its average. A flagged month is reported but not used as a trend point.
4. **Sample design (next step, not implemented yet).** Today, `stage2_snapshot.py` samples Built In only. When it is extended to the new boards, it should draw a fixed quota per source each month (the same weights as above) instead of a draw from whatever the crawl happened to capture.
5. **Provenance.** `archive_source`, `archive_ref` and the crawl id are kept on every record, so any result can be re-cut per source.

### Result so far (`stability.json`)

| Region | Months that meet the criterion | Typical n per month | Status |
|---|---|---|---|
| **US** | 2025-09, 2025-10, 2025-11. Role-mix TVD 0.040–0.046 at a noise level of 0.042–0.046, so the shifts are pure noise | 450–650 (Workday about 85%, Built In about 15%) | **stable.** Jan–Oct 2026 are not measured yet (the Workday dump for those crawls was stopped by the Common Crawl block, see below). Jul 2025 is flagged because Built In's share was low; Dec 2025 is flagged the same way |
| **UK** | none | 20–67 | **not enough data.** Built In plus reed plus Workday give at most 67 a month |
| **DE** | none | 2–24 | **not enough data** |

What to conclude, as of 2026-11-13:

- **US:** the archives can already give a stable monthly role mix. The software-engineer share sits at 0.62–0.65 for Sep–Nov 2025.
- **UK and DE:** under the stopping criterion, these months are "not enough data". Archived pages of these boards cannot support conclusions about them yet.

### Why the expansion stopped, and the next step

While reading Ashby, Personio and Greenhouse pages in parallel with the index dump, `data.commoncrawl.org` started answering **HTTP 403** to this machine, even for single requests. That is Common Crawl's rate limiting. The run was stopped to let it recover.

- The data access rate is set back to 1 request per 0.15 s.
- The index dump is resumable: run `python stage1_cc_boards.py` again and it skips finished files.

To bring UK and DE to n ≥ 300, the remaining free steps are:

1. Finish the board index dump for CC-MAIN-2026-04 to CC-MAIN-2026-43, at one worker.
2. Add German role terms to `roles.py`: Softwareentwickler, Software-Entwickler, Backend-/Frontend-/Fullstack-Entwickler, Teamleiter Softwareentwicklung.
3. Read Personio (DE), Ashby and Greenhouse pages for UK/DE location and title. Greenhouse has no JSON-LD, so take the title and location from `<title>` and the page's embedded JSON.
4. Re-run `stability.py`. Keep adding sources until UK and DE pass, or report them as not reconstructable.

The other route is the live crawl that Alexey started in parallel (`alexeygrigorev/software-dev-jobs`, t3385u). For months from now on, it gives full populations for UK and DE without archive bias.

## Recommendation

1. **US:** use Workday plus Built In from the archives. It meets the stability criterion (n ≈ 450–650 a month, role-mix shifts within sampling noise). Build the snapshots with fixed source quotas.
2. **London (UK) and Berlin (DE):** the Built In archives give 20–40 and under 15 postings a month, and the measured add-on sources reach at most 67 (UK) and 24 (DE). That is below the criterion. Keep these as samples with their n reported, and expand with Personio, Ashby and Greenhouse reads once Common Crawl unblocks (steps above). Do not draw trend conclusions from them before they pass `stability.py`.
3. **Always compare shares, never counts,** and drop months that carry a crawl-shift flag. The crawler, not the market, drives the counts.
4. **Jul–Sep 2026:** the archives are thin (Built In 128–172 pages a crawl). The live crawl covers this period better.
