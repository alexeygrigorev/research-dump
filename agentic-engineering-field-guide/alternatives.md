# Agentic Engineering Field Guide: Alternatives to TheirStack ($400)

Research date: 2026-11-13 (in response to Alexey's request t3288u on [plan.md](plan.md)).
Target requirement from `plan.md`: ~12 months of historical job postings (Nov 2025 – Nov 2026), Software Engineer + agentic titles, full job descriptions (or counts for trend lines), across 8 geographies (SF Bay, NYC, rest of US, London/UK, Germany, Netherlands, India, Remote).
**Nothing was purchased or scraped in bulk.**

---

## Executive Summary & Recommendations

No single **$0** source provides a clean, stratified 12-month (Nov 2025 – Nov 2026) *full-text* Software Engineer corpus across all 8 target geographies (especially India and the Netherlands). However, several **free** and **cheaper paid (< $400)** options can replace or drastically reduce the $400 TheirStack spend depending on the trade-off between engineering effort and coverage:

1. **Cheapest Paid Full-Text Replacement (< $400): Bright Data Datasets ($250 one-off for 100k records)**
   - Pre-collected LinkedIn and Indeed datasets with `job_posted_date` and `job_description_formatted` (full text), delivered via S3/GCS/Parquet. Twice as many records (100k vs 50k) for $250 instead of $400. *Next step before buying: inspect the free sample/preview to verify Nov 2025–Nov 2026 coverage for India, Netherlands, and Germany.*
2. **Cheapest Paid API Replacement (< $400): Coresignal Jobs API ($0 trial for 2,000 credits; $49/mo for 2,500; $199/mo for 12,000)**
   - Tracks 6+ years of historical and closed postings with full text (1 credit = 1 job). Useful for a free 2,000-credit coverage test or a $199 targeted 12k sample.
3. **Hybrid "Counts + Free Texts" Option ($169 or $0):**
   - Use **TheirStack $169 (10,000 credits)** *only* for population-level count queries (1 credit = 1 count query across all 8 geos × 13 months × signals), and source full-text examples from **free** datasets below.
4. **Best Pure-$0 Stack (Higher Engineering Effort):**
   - **US + Global Startups (12-mo full text):** Hacker News "Who is hiring" (Firebase API / BigQuery, 10+ years, full text) + **Common Crawl Columnar Index via AWS Athena** (~$0.10–$0.20 Athena scan fee for `CC-MAIN-2025-47` through `CC-MAIN-2026-43`, targeting `jobs.ashbyhq.com` and `job-boards.greenhouse.io`; note `jobs.lever.co` blocks `CCBot`).
   - **Europe (Germany, Netherlands, UK, Remote-EU, Apr–Nov 2026 full text):** Hugging Face `Aramente/eu-tech-jobs` (197 daily snapshots, full `description_md`, CC BY 4.0).
   - **US Indeed Snapshot (Sep 2026 full text):** Kaggle `scrapifier/indeed-usa-job-postings` (10k rows, CC0).
   - **Macro & Trend Benchmarks ($0):** Indeed Hiring Lab (`job_postings_tracker` & `ai-tracker`), Revelio Public Labor Statistics (monthly US SOC 15 counts via S3 CSV), UK ONS Textkernel (replaced discontinued Adzuna series), Eurostat, CBS StatLine (NL), and Destatis/BA-X (DE).

---

## 1. Cheaper Paid & Freemium Providers (< $400)

| Source | Что даёт (история 12 мес., текст/счётчики, гео) | Цена | Ссылка | Проверено вживую |
|---|---|---|---|---|
| **Bright Data Datasets (LinkedIn / Indeed)** | **История:** да (по `job_posted_date`). **Текст:** полные описания (`job_description_formatted`). **Гео:** Global (US, UK, DE, NL, IN, Remote). | **$250** (мин. пакет 100,000 записей; $2.50/1k) | https://brightdata.com/products/datasets | **Да** (прайсинг и схема полей проверены на сайте; покрытие по гео/датам нужно проверить в free preview) |
| **Coresignal Jobs API** | **История:** 6+ лет (с 2020, включая закрытые). **Текст:** полные описания. **Гео:** Global (500M+ записей). | **$0** (триал 2,000 кредитов / 7 дней); **$49/мес** (2.5k); **$199/мес** (12k) | https://coresignal.com | **Да** (прайсинг и документация кредитов 1 credit = 1 job проверены на сайте) |
| **TheirStack (младшие тарифы)** | **История:** с 2021 (`posted_at_gte/lte`, `is_closed`). **Текст:** полные описания + count queries. **Гео:** 195+ стран. | **$0** (200 кр.); **$49** (1.5k); **$100** (5k); **$169** (10k); **$240** (20k) | https://theirstack.com/en/pricing | **Да** (OpenAPI-спецификация и страница тарифов проверены) |
| **Fantastic.jobs** | **История:** только **6 месяцев** (не достаёт до нояб. 2025). **Текст:** полные описания. **Гео:** Global (275k+ ATS). | **$45 – $95/мес** (5k–20k); ~$4/1k на Apify | https://fantastic.jobs | **Да** (тарифы и 6-мес. лимит бэкфилла проверены) |
| **USAJobs Historic API** | **История:** да (многолетняя). **Текст:** полные описания. **Гео:** только федеральные вакансии США (US Federal). | **$0** (без ключа) | https://developer.usajobs.gov/api-reference/get-api-historicjoa | **Да** (живой HTTP-ответ от `/api/historicjoa` получен; нерелевантно для частного SWE-рынка) |
| **Adzuna API** | **История:** **НЕТ** (поиск только за ~30 дней; `/history` отдаёт только средние зарплаты/агрегаты). **Гео:** 16 стран (US, UK, DE, NL, IN). | **$0** (250 req/day) | https://developer.adzuna.com/ | **Да** (эндпоинты `/search` и `/history` проверены в документации) |
| **Reed UK / Jooble / Careerjet / The Muse** | **История:** **НЕТ** (только текущие открытые вакансии). **Текст:** Reed/The Muse — да; Jooble/Careerjet — сниппеты. | **$0** (free tier / лимиты) | https://www.reed.co.uk/developers | **Да** (документация API проверена: архивов за 12 мес. нет) |
| **DataForSEO / SerpApi / RapidAPI JSearch / Apify** | **История:** **НЕТ** (живая выдача Google Jobs / LinkedIn, макс. фильтр 30 дней). **Текст:** да. **Гео:** Global. | **$0–$50/мес** (депозит/подписка) | https://dataforseo.com/apis/jobs-data-api | **Да** (документация проверена: исторического архива за 12 мес. нет) |
| **LinkUp / JobsPikr** | **История:** да. **Текст:** да. **Гео:** Global. | **>$400** (LinkUp $10k+ enterprise; JobsPikr ~$4,000/год) | https://www.jobspikr.com/ | **Да** (не укладываются в бюджет < $400) |

---

## 2. Kaggle & Hugging Face Datasets (Free, $0)

| Источник | Что даёт (история 12 мес., текст/счётчики, гео) | Цена | Ссылка | Проверено вживую |
|---|---|---|---|---|
| **HF: `Aramente/eu-tech-jobs`** | **История:** **29 апр – 12 нояб 2026** (197 ежедневных снапшотов + diffs, ~6.5 мес.). **Текст:** полные описания (`description_md`). **Гео:** DE, NL, UK, FR, Remote-EU (~18.8k активных/день, 1,866 компаний). | **$0** (CC BY 4.0) | https://huggingface.co/datasets/Aramente/eu-tech-jobs | **Да** (HF API HTTP 200; проверен `latest/metadata.json` от `2026-11-12T14:43:53Z`) |
| **HF: `ryang2/linkedin-job-scrape`** | **История:** мар 2023 – 12 нояб 2026 (170k строк, ~17k за 2026). **Текст:** полные описания. **Гео:** US, Remote. *Важно: первые 10 строк 2026 сплита — Data/ML Scientist, доля обычных SWE требует проверки.* | **$0** (OpenRAIL-M) | https://huggingface.co/datasets/ryang2/linkedin-job-scrape | **Да** (HF API HTTP 200 + выборка 10 строк через `datasets-server.huggingface.co`) |
| **Kaggle: `scrapifier/indeed-usa-job-postings`** | **История:** снапшот от **6 сен 2026** (не 12 мес.). **Текст:** 10,000 полных описаний + зарплаты + теги. **Гео:** US (50 городов + Remote). | **$0** (CC0) | https://www.kaggle.com/datasets/scrapifier/indeed-usa-job-postings | **Да** (Kaggle API dataset view) |
| **Kaggle: `m0sm71/ai-jobs-dataset-2026`** | **История:** снапшот **июнь 2026**. **Текст:** 50k+ полных описаний. **Гео:** US, UK, DE, IN, Remote. *Предупреждение: в описании указано использование semantic scaling generator для объёма.* | **$0** (CC0) | https://www.kaggle.com/datasets/m0sm71/ai-jobs-dataset-2026 | **Да** (Kaggle API; обнаружена пометка о синтетическом масштабировании) |
| **Kaggle/HF: `factden/indeed-jobs-2026-salaries-company-data`** | **История:** снапшот **июнь 2026** (1,000 вакансий). **Текст:** полные описания. **Гео:** US (SF, NYC, Austin, Chicago). | **$0** | https://www.kaggle.com/datasets/factden/indeed-jobs-2026-salaries-company-data | **Да** (проверено через Kaggle & HF API) |
| **HF: `zalizedata/tech-job-postings-salary-dataset`** | **История:** снапшоты до **авг 2026** (394k записей из ATS). **Текст:** **НЕТ** (только метаданные, тайтлы, зарплаты, без полного текста). **Гео:** US, UK, EU, Remote. | **$0** (CC-BY-NC 4.0) | https://huggingface.co/datasets/zalizedata/tech-job-postings-salary-dataset | **Да** (HF API HTTP 200) |
| **Kaggle: `chandranshbinjola/job-listings`** | **История:** ежедневное обновление до **12 нояб 2026** (11.35M строк, закрытые за 90 дней). **Текст:** **НЕТ** (описания удалены, оставлены извлечённые скиллы и счётчики). **Гео:** US, UK, DE, NL, IN, Remote. | **$0** (CC BY 4.0) | https://www.kaggle.com/datasets/chandranshbinjola/job-listings | **Да** (Kaggle API) |
| **Kaggle: `carmelon23/career-site-jobs-100k-open-roles-nov-2026`** | **История:** снапшот **9 нояб 2026** (100k открытых вакансий). **Текст:** **НЕТ** (только метаданные + URL). **Гео:** US (51k), UK (5.6k), IN (5k), DE (2.5k), Remote (19k). | **$0** (CC BY 4.0) | https://www.kaggle.com/datasets/carmelon23/career-site-jobs-100k-open-roles-nov-2026 | **Да** (Kaggle API) |
| **Kaggle: `shree0910/india-tech-job-market-2026-23k-records`** | **История:** снапшот **июнь 2025** (Naukri, 23.2k записей). **Текст:** полные описания. **Гео:** Индия (10 городов + Remote). | **$0** (CC BY-SA 4.0) | https://www.kaggle.com/datasets/shree0910/india-tech-job-market-2026-23k-records | **Да** (Kaggle API) |
| **Kaggle: `nikhilvarmakandula/deutschland-tech-job-market-skill-demand-nlpcorpus`** | **История:** янв 2024 – **мар 2025** (3.2k записей). **Текст:** полные описания. **Гео:** Германия (StepStone, Indeed DE, LinkedIn). | **$0** (CC BY-NC-SA 4.0) | https://www.kaggle.com/datasets/nikhilvarmakandula/deutschland-tech-job-market-skill-demand-nlpcorpus | **Да** (Kaggle API) |
| **Kaggle: `asaniczka/1-3m-linkedin-jobs-and-skills-2024`** | **История:** начало **2024** (1.3M записей — хороший исторический baseline). **Текст:** полные описания (`job_summary.csv`). **Гео:** US, Global. | **$0** (ODC-By) | https://www.kaggle.com/datasets/asaniczka/1-3m-linkedin-jobs-and-skills-2024 | **Да** (Kaggle API) |

---

## 3. Common Crawl, Web Data Commons & Wayback Machine ($0 / ~$0.20)

| Источник | Что даёт (история 12 мес., текст/счётчики, гео) | Цена | Ссылка | Проверено вживую |
|---|---|---|---|---|
| **Common Crawl Columnar Index (AWS Athena / S3 Parquet)** | **История:** **12 ежемесячных краулов** в окне нояб 2025 – нояб 2026 (`CC-MAIN-2025-47` … `CC-MAIN-2026-43`). **Текст:** полный HTML/JSON из WARC. **Ограничения:** `jobs.lever.co` блокирует `CCBot` (HTTP 403); публичный CDX API `index.commoncrawl.org` даёт **504 Gateway Time-out** на wildcard-запросах по `job-boards.greenhouse.io/*`, `jobs.ashbyhq.com/*` и `builtin.com/job/*` — нужен запрос через Parquet/Athena. | **$0** за данные (~$0.05–$0.20 за SQL-запрос в AWS Athena) | https://index.commoncrawl.org/collinfo.json | **Да** (проверены `collinfo.json` и живые CDX-запросы: 504 на wildcard, 403 на Lever, 301 на `boards.greenhouse.io`) |
| **Web Data Commons (`schema.org/JobPosting`)** | **История:** последний релиз — **2024-12** (краул окт 2024, 4.07M сущностей JobPosting, 4.86 GB). **Релизов 2025/2026 ещё нет.** В 2024-12 есть **Ashby** (`part_8.gz`, 1,693 сущности), но **нет Greenhouse, Lever и Built In**. | **$0** | https://data.dws.informatik.uni-mannheim.de/structureddata/2024-12/quads/classspecific/JobPosting/ | **Да** (проверены directory, `JobPosting_lookup.csv` и `JobPosting_domain_stats.csv`) |
| **Wayback Machine CDX API** | **История:** захваты за 2025–2026 есть, но wildcard-запросы дают **503 / таймауты >20s**, строгий лимит ~60 req/min. `job-boards.greenhouse.io` часто сохранён как пустая SPA-оболочка; `boards.greenhouse.io` — 301 редиректы. Подходит только как точечный fallback. | **$0** | https://web.archive.org/cdx/search/cdx | **Да** (точный URL отвечает за 2.1s HTTP 200; wildcard даёт 503/таймаут) |

---

## 4. Hacker News & GitHub-Hosted Job Archives ($0)

| Источник | Что даёт (история 12 мес., текст/счётчики, гео) | Цена | Ссылка | Проверено вживую |
|---|---|---|---|---|
| **Hacker News "Who is hiring" (Firebase API + BigQuery + GitHub парсеры)** | **История:** 10+ лет (553 ежемесячных треда; нояб 2026 — тред `50338728`, 288 комментариев). **Текст:** полный текст. **Гео:** Global / US-skewed, стартапы, много Remote. Парсеры: `flaviaouyang/hackerjobs`, `gabfl/hn-whoishiring`, `nemanjam/hn-new-jobs`. | **$0** (BigQuery 1 TB/мес free) | https://hacker-news.firebaseio.com/v0/user/whoishiring.json | **Да** (HTTP 200 live check `whoishiring.json`) |
| **GitHub: `Riley-Dorrington/job-board-data`** | **История:** **НЕТ** (ежедневный force-push orphan-коммита затирает историю). **Текст:** **НЕТ** (метаданные + URL + зарплата, 1.43M активных вакансий из 7 ATS). | **$0** | https://github.com/Riley-Dorrington/job-board-data | **Да** (проверены схема `jobs_chunk_*.json.gz` и политика orphan-коммитов) |
| **GitHub: `SimplifyJobs/New-Grad-Positions` & `Summer2027-Internships`** | **История:** есть папка `archived/` с 2021 года (`README-2025.md` и др.). **Текст:** **НЕТ** (только таблицы Company / Role / Location / ATS URL). **Гео:** в основном US/CA, junior/intern. | **$0** | https://github.com/SimplifyJobs/New-Grad-Positions | **Да** (проверены ветка `dev` и `archived/`) |
| **Arbeitnow / Remotive / Hiring.cafe API** | **История:** **НЕТ** (только активные вакансии за 2–4 недели). **Текст:** полный (HTML) у Arbeitnow (DE/EU) и Remotive (14–20 шт.). | **$0** | https://www.arbeitnow.com/api/job-board-api | **Да** (проверено вживую) |

---

## 5. Academic Datasets, Revelio / Lightcast Free Tiers & Government Stats ($0)

| Источник | Что даёт (история 12 мес., текст/счётчики, гео) | Цена | Ссылка | Проверено вживую |
|---|---|---|---|---|
| **Indeed Hiring Lab (`job_postings_tracker` & `ai-tracker`)** | **История:** ежедневный индекс с фев 2020 по **6 нояб 2026** (AI tracker до **30 сен 2026**). **Текст:** только агрегированные индексы (без текстов). **Гео:** US, UK, DE, NL, FR, CA, AU, IT, IE (нет Индии). | **$0** (MIT / CC BY 4.0) | https://github.com/hiring-lab/job_postings_tracker | **Да** (HTTP 200 live CSV check) |
| **Revelio Labs Public Labor Statistics (RPLS)** | **История:** помесячно с янв 2022 по **окт 2026** (прямые CSV на S3). **Текст:** только агрегированные счётчики по 2-digit SOC (`SOC 15: Computer & Mathematical` — ~1.37M–1.62M активных/мес). **Гео:** US. Сырые постинги — только академический доступ через Dewey Data / WRDS. | **$0** (публичные CSV) | https://www.reveliolabs.com/public-labor-statistics/ | **Да** (HTTP 200 live check S3 CSV `rpls/202610/postings/postings_by_occupation.csv`) |
| **Lightcast (Open Skills + Dewey Data)** | **История/Сырые тексты:** **НЕТ** в бесплатном доступе (только коммерция или вузовские подписки Dewey Data). Бесплатно: **Open Skills Taxonomy** (34k+ навыков, API для нормализации). | **$0** (Open Skills API) | https://lightcast.io/open-skills | **Да** (проверено на `lightcast.io/open-skills`) |
| **UK ONS: Textkernel New Online Job Adverts** | **История:** еженедельно/помесячно до **окт 2026**. *Важно: старая серия ONS на базе Adzuna закрыта 24 окт 2024.* **Текст:** только счётчики по SOC. **Гео:** UK. | **$0** (Open Gov Licence) | https://www.ons.gov.uk/economy/economicoutputandproductivity/output/datasets/textkernelnewonlinejobadverts | **Да** (HTTP 200 verified) |
| **US BLS (JOLTS & OEWS)** | **История:** JOLTS до **сен 2026** (NAICS 51 Information), OEWS ежегодный (SOC 15-1252). **Текст:** только макро-счётчики/зарплаты. **Гео:** US. | **$0** (Public API) | https://api.bls.gov/publicAPI/v2/timeseries/data/JTS510000000000000JOL | **Да** (HTTP 200 verified) |
| **Eurostat (`jvs_q_nace2`) & CBS StatLine (`80472NED`) & Destatis/BA-X** | **История:** квартальные/месячные данные до **2026** по сектору Information & Communication / IT. **Текст:** только агрегаты. **Гео:** DE, NL, EU-27. | **$0** (REST / OData API) | https://opendata.cbs.nl/ODataApi/OData/80472NED/TypedDataSet?$top=1 | **Да** (HTTP 200 verified) |
| **India: Naukri JobSpeak** | **История:** ежемесячные пресс-релизы до **окт 2026** (IT-Software vs AI/ML YoY). **Текст:** только индексы/проценты. **Гео:** Индия (Bangalore, Hyderabad, Pune, Delhi NCR). | **$0** | https://www.naukri.com/hiring-trends/ | **Да** (проверено по отчётам за 2026) |
| **Zenodo / arXiv академические наборы** | ICSE 2026 SWE job postings (`10.5281/zenodo.17606700`, нояб 2025), NLP SWE skills (`10.5281/zenodo.20837583`, июнь 2026), Saturation AI skill ads (Record `14931899`, мар 2026), arXiv:2605.00843. Малые выборки (сотни–тысячи), не 12-мес. панель по всем гео. | **$0** | https://zenodo.org/records/17606700 | **Частично** (DOI найдены в поиске; прямой API-запрос к `zenodo.org/api` получил HTTP 403) |
