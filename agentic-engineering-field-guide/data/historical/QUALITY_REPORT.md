# Quality report: raw historical vacancies (t3450u)

Input: `raw/vacancies.jsonl.gz` (**12,584 rows** after Jul–Sep 2026 fill; 11,359 in PR #10). Output: `clean/vacancies.jsonl.gz` (**12,522 rows**; 11,292 in PR #10).
Everything below is deterministic (no LLM, no network). Numbers: `clean/summary.json` (before/after for every metric);
reproduce with `python scripts/clean_raw.py` (about 45 s) and `python scripts/quality.py <file>`.
Language is a stop-word heuristic (en/de/fr/es/pt), not a classifier.

## Row counts

| step | rows |
|---|---|
| raw | 11,359 |
| rejected: empty / template-placeholder description | -9 |
| dedupe 2 on cleaned text (cross-source twins) | -58 |
| **clean** | **11,292** (in_window since 2025-11: 8,453 -> 8,387) |

By source after cleaning: builtin 9,228, greenhouse 2,037, ashby 27 (raw 9,237 / 2,095 / 27).

## Findings (before -> after)

**Duplicates.** No two rows share a source job id (0) and no row pairs share title + first 2000 chars of text (the PR #10 dedupe holds).
It missed twins that only differ in whitespace/wrapping, because builtin text is hard-wrapped and greenhouse is not:
same title + same full text went from 90 pairs to 32 after unwrapping; 58 were merged, all greenhouse into builtin
(e.g. builtin "DRW" = greenhouse `drweng`, "IMC Trading" = `imc`; list in `clean/dedupe2_merges.jsonl`).
The 32 remaining have the same text under different company names in the same source (Block/Square, Alta Genetics/URUS Group,
Arcadia.com/Arcadia (DC)); kept, see open questions. Still present by design: 423 rows share title + company + location
list with a different text (reposts over months, e.g. builtin 3318468 in 2025-07 and 7938229 in 2026-02, both "Senior Software Engineer");
about 190 rows share the exact text with another row under a different title (G2i "Software Engineer for Training AI Data (JavaScript)" vs
"... (Python)" style siblings, Datadog per-city postings).

**Empty / truncated descriptions.** 9 rows are placeholders, all builtin: `''`, `'.'`, `'Description here'`, and `'${desc}'` x6
(e.g. "Lead Software Engineer", "Senior Software Engineer (Java Full Stack, Gen AI)"). Rejected (`clean/rejects.jsonl.gz`).
After that the shortest text is 292 chars; 4 rows < 500 and 16 < 1000 chars (they look like genuinely short postings, e.g. ELEKS
JR786). Median 5,200 chars. No fixed-length cut-off found. 2,969 texts (26%) end without punctuation, mostly job-board tags
(`#LI-Remote`) or a last bullet; 28 end on an empty section heading ("REQUIREMENTS\n\nRESPONSIBILITIES", bodies lost in the source).
Not dropped.

**Non-English.** 52 of 11,359 (0.5%): pt 34, fr 17, es 1 (+ 17 rows with >50 CJK/Cyrillic/Arabic characters, mostly English text with a
Japanese header, e.g. route06 `Software Engineer (業務委託)`). Examples: "Engenheiro de Software Fullstack PL (Python/Angular)",
"Lead Développeur Backend Java" (ibanfirst), "Unity Software Engineer" (Fanatee, pt text). 41 greenhouse, 11 builtin. Flagged in `lang`, not removed.

**Roles.** Role = regex on title and is exactly reproduced (0 mismatches), so no regex errors. Semantic doubt remains: 41 titles with a
non-software domain ("Electrical Engineering Manager", "Hardware Engineering Manager", "Sales Engineering Manager", "Construction Support
Engineering Manager", "Mechanical Software Engineer"), 196 QA/test/SDET/quality titles, 187 INTERN employment type, 100+ titles with
DevOps/SRE/network/customer/marketing wording. Nothing removed (open question).

**Region.** The regex ignored bare ISO-3 country codes (builtin writes "POL", "ESP, ESP", "CZE, CZE", "Praha, CZE"), and used the first
location that *happened to match*, which for multi-country lists was arbitrary. Before: 317 UNKNOWN, 483 REMOTE (many of those just a
European country with the remote flag set), "GRC" rows landed in MEA/CA/LATAM. After the ISO-3 fix: 143 UNKNOWN, 196 REMOTE, EU 824 -> 1,482;
728 rows changed, old value in `region_original`. Remaining UNKNOWN is mostly free text ("Remoto", "Brasil", "リモート勤務", "Hybrid",
"Guadalajara Office") and unmapped codes (ARM, GEO, TJK, UZB, PRI...). 2,092 rows (18%) list more than one location, 256 list more
than 20 (G2i: about 300 cities in 90 countries) and 792 span more than one region; the single `region` field is only "first resolvable
location". New `regions_all`, `n_locations`.

**Date reliability.** `month` is the month of the first archive capture, not posting. 2,064 rows (greenhouse+ashby, one crawl CC-MAIN-2025-47)
have no capture timestamp at all, so their month "2025-11" is the crawl batch (`month_basis=crawl_batch`); that is why 2025-11 has ~3,000 rows vs
~700 elsewhere. Posted date exists for all but 47 rows. Capture minus posting: median 15 days, p90 39, p99 353; 219 rows were posted
>90 days and 83 >365 days before capture (e.g. builtin 1111476 posted 2024-07-21, captured 2025-07; posted years go back to 2019).
Posted month equals capture month for only 4,173 of 11,292 rows (37%). Posted-date by month (raw): 2026-07 3 rows, 2026-08..10 ~200-260 each,
2026-06 299, vs ~600-700 in earlier months, so coverage is thin/uneven in the last months (builtin captures in 2026-07..09 are 24 rows).
`posted_month` added; nothing recomputed.

**Source mix.** builtin 81% (CC 8,747 + Wayback 481), greenhouse 18%, ashby 0.2%. Greenhouse/Ashby come from a single crawl,
have no capture date, `employment_type` empty and company = board slug (1,990 rows, e.g. `canonical`, `ziprecruiter`, `payhawkio`,
`flowtraders`) while builtin has display names, so the same employer appears under two names. US 56%, EU 13%, IN 9%.

**Boilerplate / HTML.** No HTML entities, mojibake or markdown escapes. Leftovers cleaned: NBSP in 1,877 texts, zero-width chars 166 -> 117 texts (joiners inside emoji kept), trailing
blanks in 267, runs of 3+ blank lines in 1,437, stray `</span>`/`<strong>` in 1 text, template var `${desc}` (placeholder rows).
Builtin text is hard-wrapped at 62 columns in 8,918 of 9,237 texts (about 675k broken lines); unwrapped (27.5k wrap-looking lines
remain, mostly list items/headings). Not touched: EEO/legal paragraphs in 5,905 texts (52%), GDPR/CCPA privacy notices in 2,316 (21%),
board tags `#LI-*`/`#BI-*` in 2,508 (22%), employer "About us" paragraphs repeated verbatim across a company's postings
(Coinbase 239 rows). These are not noise for every use; see open questions.

## What cleaning did (all in `scripts/clean_raw.py`)

1. rejected 9 placeholder descriptions; 2. text normalisation (NBSP, zero-width, stray tags, blanks); 3. un-wrapped 9,227 builtin texts
(reverse of 62-col wrap; list items untouched); 4. ISO-3 region fix + `regions_all`/`n_locations`; 5. second dedupe (-58);
6. added flags `lang`, `month_basis`, `posted_month`; `content_hash` recomputed on the cleaned text. `description` is now cleaned text; the
original is in `raw/`.

## Open questions (not decided)

1. **Reposts**: 423 rows have same company + title + locations but different text and date. Collapse to one posting, or keep (they count as new demand in a time series)?
2. **Same text, different title/location** (G2i siblings, Datadog per-city, ~190 rows) and **same text, different company alias** (32, Block/Square): one posting or several?
3. **Multi-location postings** (2,092; 256 with >20 locations): keep first-location region, explode into one row per region, or tag as multi-geo? G2i alone dominates the long lists.
4. **Greenhouse/Ashby company names** are slugs; map to display names (needs a lookup, e.g. via builtin names), or leave?
5. **Dates**: which one is the analysis date, posted_date or capture month? 2025-11 is inflated by the one-crawl board read; posted dates go back to 2019 for 83 rows. Drop rows posted >N days before capture, or drop crawl_batch rows from time series?
6. **Role relevance**: drop non-software engineering managers (41), QA/SDET (196), interns (187), or keep and tag?
7. **Non-English** (52) and **non-Latin** text: drop or keep?
8. **Boilerplate**: strip EEO/privacy/board-tag/"about us" paragraphs before any extraction, or keep verbatim? (Affects length and token cost, not content of requirements.)
9. **Region leftovers**: ARM/GEO/TJK/UZB/KGZ/KAZ (Caucasus/Central Asia), Puerto Rico/US Virgin Islands, Dominican Rep./Haiti stay UNKNOWN; and "Remote" rows with a country keep REMOTE only if no country resolves (remote flag is in `remote`). Bucket them?
10. **Coverage gaps (resolved for Jul–Sep 2026)**: see below.

## Jul–Sep 2026 gap fill (t3586u, t3593u)

Added deterministic, non-LLM collection from Common Crawl (`CC-MAIN-2026-30`, `34`, `39` for `builtin`, `greenhouse` 50% board panel + individual job pages, `ashby` 8% job-page panel) and Wayback Machine CDX (`builtin.com/job/*` for `20260701–20260930`). All new rows carry `first_seen` from their archive capture timestamp (`month_basis=capture`: 10,600 rows; `crawl_batch`: 1,922 rows from `CC-MAIN-2025-47`).

**Repost deduplication (t3593u):** `scripts/julsep_merge.py` deduplicates in 3 stages:
1. `(source, job_id or url)` keeping earliest `posted_date` / `first_seen`: **-368** rows.
2. `content_hash` (`title|company|description[:2000]`): **-128** rows.
3. Reposts/re-listings (`norm(company).replace(" ", ""), norm(title), sorted(norm(locations))`), keeping the **earliest `posted_date`** (fallback earliest `first_seen`): **-484** reposts removed.
`clean_raw.py` additionally rejected **9** placeholder descriptions and merged **53** cross-source twins (`12,584 -> 12,522`).

### Before vs. After for 2026-07, 2026-08, 2026-09

| month | capture before (raw) | capture after (raw) | capture after (clean) | posted before (raw) | posted after (raw/clean) |
|---|---|---|---|---|---|
| 2026-07 | 13 | 597 | 596 | 3 | 446 |
| 2026-08 | 7 | 597 | 597 | 264 | 592 |
| 2026-09 | 4 | 581 | 581 | 268 | 328 |
