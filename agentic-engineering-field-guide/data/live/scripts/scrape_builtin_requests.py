#!/usr/bin/env python3
"""
Built In job listing scraper using requests + DataImpulse proxy.
Vendored and extended from ai-engineering-field-guide/job-market/_internal/scrapers/scrape_builtin_requests.py.

Scrapes 15 cities x 6 software engineering roles, excludes jobs already in
data/all_jobs_dedup.csv (no overlap with earlier months), and takes a random
sample per city-month.
"""
from __future__ import annotations

import argparse
import csv
import json
import random
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path
from urllib.parse import quote_plus, urlparse

import pandas as pd
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

SCRIPT_DIR = Path(__file__).parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from pipeline_paths import BUILTIN_JSON_DIR, GLOBAL_DEDUP_CSV, combined_csv_path
from proxy_config import get_requests_proxies, proxy_provider

if sys.stdout.encoding != "utf-8":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

load_dotenv()

ROLES = [
    "Software Engineer",
    "Software Developer",
    "Backend",
    "Frontend",
    "Full Stack",
    "Engineering Manager",
]

BUILTIN_CITIES = {
    "london": {
        "name": "London, UK",
        "base_url": "https://builtin.com/jobs?city=London&state=England&country=GBR&allLocations=true",
    },
    "berlin": {
        "name": "Berlin, Germany",
        "base_url": "https://builtin.com/jobs?city=Berlin&state=Berlin&country=DEU&allLocations=true",
    },
    "newyork": {
        "name": "New York, USA",
        "base_url": "https://builtin.com/jobs?city=New+York&state=New+York&country=USA&allLocations=true",
    },
    "sf_bay_area": {
        "name": "SF Bay Area, USA",
        "base_url": "https://builtin.com/jobs?city=San+Francisco&state=California&country=USA&allLocations=true",
    },
    "seattle": {
        "name": "Seattle, USA",
        "base_url": "https://builtin.com/jobs?city=Seattle&state=Washington&country=USA&allLocations=true",
    },
    "austin": {
        "name": "Austin, USA",
        "base_url": "https://builtin.com/jobs?city=Austin&state=Texas&country=USA&allLocations=true",
    },
    "boston": {
        "name": "Boston, USA",
        "base_url": "https://builtin.com/jobs?city=Boston&state=Massachusetts&country=USA&allLocations=true",
    },
    "chicago": {
        "name": "Chicago, USA",
        "base_url": "https://builtin.com/jobs?city=Chicago&state=Illinois&country=USA&allLocations=true",
    },
    "toronto": {
        "name": "Toronto, Canada",
        "base_url": "https://builtin.com/jobs?city=Toronto&state=Ontario&country=CAN&allLocations=true",
    },
    "amsterdam": {
        "name": "Amsterdam, Netherlands",
        "base_url": "https://builtin.com/jobs?city=Amsterdam&state=Noord-Holland&country=NLD&allLocations=true",
    },
    "paris": {
        "name": "Paris, France",
        "base_url": "https://builtin.com/jobs?city=Paris&state=Ile-de-France&country=FRA&allLocations=true",
    },
    "munich": {
        "name": "Munich, Germany",
        "base_url": "https://builtin.com/jobs?city=Munich&state=Bavaria&country=DEU&allLocations=true",
    },
    "dublin": {
        "name": "Dublin, Ireland",
        "base_url": "https://builtin.com/jobs?city=Dublin&state=Leinster&country=IRL&allLocations=true",
    },
    "warsaw": {
        "name": "Warsaw, Poland",
        "base_url": "https://builtin.com/jobs?city=Warsaw&state=Masovia&country=POL&allLocations=true",
    },
    "remote": {
        "name": "Remote",
        "base_url": "https://builtin.com/jobs/remote",
    },
}

SPAM_COMPANIES = {"Alignerr"}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

CSV_FIELDS = [
    "title",
    "company",
    "location",
    "work_type",
    "level",
    "compensation",
    "link",
    "id",
    "city",
    "search_role",
    "scraped_date",
]


def load_existing_ids() -> set[str]:
    """Load job IDs already in data/all_jobs_dedup.csv to avoid overlap across months."""
    if not GLOBAL_DEDUP_CSV.exists():
        return set()
    df = pd.read_csv(GLOBAL_DEDUP_CSV)
    if "id" not in df.columns:
        return set()
    return set(df["id"].dropna().astype(str))


def fetch_page(url: str, retries: int = 3) -> str | None:
    """Fetch a page with retries via configured proxy."""
    proxies = get_requests_proxies()
    for attempt in range(retries):
        try:
            resp = requests.get(url, proxies=proxies, headers=HEADERS, timeout=60)
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            if attempt < retries - 1:
                wait = 3 * (attempt + 1) + random.uniform(0, 2)
                time.sleep(wait)
            else:
                print(f"    Failed after {retries} attempts ({url}): {e}")
                return None
    return None


def build_search_url(base_url: str, role: str, page_num: int = 1) -> str:
    """Construct Built In search URL for a city base_url, role, and page."""
    sep = "&" if "?" in base_url else "?"
    url = f"{base_url}{sep}search={quote_plus(role)}"
    if page_num > 1:
        url = f"{url}&page={page_num}"
    return url


def extract_max_page(html_content: str) -> int:
    """Return the highest page number linked in pagination."""
    soup = BeautifulSoup(html_content, "html.parser")
    pages = [a.get_text(strip=True) for a in soup.select('a[href*="page="]')]
    return max((int(p) for p in pages if p.isdigit()), default=1)


def extract_jobs_from_html(html_content: str, base_domain: str) -> list[dict]:
    """Extract job cards from listing page HTML."""
    soup = BeautifulSoup(html_content, "html.parser")
    jobs = []
    title_links = soup.select('h2 a[href*="/job/"]')

    for link_el in title_links:
        job = {}
        job["title"] = link_el.get_text(strip=True)
        href = link_el.get("href", "")
        job["link"] = f"https://{base_domain}{href}" if href.startswith("/") else href
        job["id"] = href.rstrip("/").rsplit("/", 1)[-1]

        card = link_el.find_parent("div", id=lambda x: x and x.startswith("job-card-"))
        if not card:
            card = link_el.find_parent("div", class_=lambda x: x and "job" in x.lower()) if link_el.parent else None
        if not card:
            card = link_el.parent
            for _ in range(5):
                if card and card.parent:
                    card = card.parent
                else:
                    break

        job["company"] = ""
        if card:
            company_link = card.find("a", href=lambda x: x and "/company/" in x)
            if company_link:
                img = company_link.find("img")
                if img and img.get("alt"):
                    job["company"] = img["alt"].replace(" Logo", "").replace(" logo", "").strip()
                else:
                    span = company_link.find("span")
                    job["company"] = span.get_text(strip=True) if span else company_link.get_text(strip=True)

        job["location"] = ""
        job["work_type"] = ""
        job["compensation"] = ""
        job["level"] = ""

        if card:
            loc_icon = card.find("i", class_=lambda c: c and "fa-location-dot" in c)
            if loc_icon and loc_icon.parent:
                job["location"] = loc_icon.parent.get_text(strip=True)

            wt_icon = card.find("i", class_=lambda c: c and "fa-house-building" in c)
            if wt_icon and wt_icon.parent:
                job["work_type"] = wt_icon.parent.get_text(strip=True)

            comp_icon = card.find("i", class_=lambda c: c and "fa-sack-dollar" in c)
            if comp_icon and comp_icon.parent:
                job["compensation"] = comp_icon.parent.get_text(strip=True)

            level_icon = card.find("i", class_=lambda c: c and "fa-trophy" in c)
            if level_icon and level_icon.parent:
                job["level"] = level_icon.parent.get_text(strip=True)

        if job["title"] and job["link"]:
            jobs.append(job)

    return jobs


def scrape_city_role(
    city_id: str,
    base_url: str,
    role: str,
    scraped_date: str,
    pages_per_role: int,
    rng: random.Random,
) -> list[dict]:
    """Fetch page 1 + random sample of remaining pages for one (city, role)."""
    base_domain = urlparse(base_url).netloc
    url_p1 = build_search_url(base_url, role, page_num=1)
    html_p1 = fetch_page(url_p1)
    if not html_p1:
        return []

    jobs = extract_jobs_from_html(html_p1, base_domain)
    max_page = extract_max_page(html_p1)

    extra_pages: list[int] = []
    if max_page > 1 and pages_per_role > 1:
        candidates = list(range(2, max_page + 1))
        k = min(pages_per_role - 1, len(candidates))
        extra_pages = sorted(rng.sample(candidates, k))

    for p in extra_pages:
        url_p = build_search_url(base_url, role, page_num=p)
        html_p = fetch_page(url_p)
        if html_p:
            jobs.extend(extract_jobs_from_html(html_p, base_domain))

    for job in jobs:
        job["city"] = city_id
        job["search_role"] = role
        job["scraped_date"] = scraped_date

    return jobs


def scrape_city(
    city_id: str,
    city_config: dict,
    roles: list[str],
    scraped_date: str,
    pages_per_role: int,
    sample_per_city: int,
    existing_ids: set[str],
    seed: int,
    workers: int,
) -> list[dict]:
    """Scrape all roles for a city, deduplicate, exclude prior months, and sample."""
    print(f"\n[{city_id}] {city_config['name']}")
    rng = random.Random(f"{seed}:{city_id}")

    raw_jobs: list[dict] = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(
                scrape_city_role,
                city_id,
                city_config["base_url"],
                role,
                scraped_date,
                pages_per_role,
                random.Random(f"{seed}:{city_id}:{role}"),
            ): role
            for role in roles
        }
        for future in as_completed(futures):
            role = futures[future]
            try:
                role_jobs = future.result()
                raw_jobs.extend(role_jobs)
                print(f"  {role:20s}: {len(role_jobs):3d} raw cards")
            except Exception as e:
                print(f"  {role:20s}: ERROR {e}")

    # Deduplicate within city by id and (title, company), filter spam & prior months
    seen_ids: set[str] = set()
    seen_pairs: set[tuple[str, str]] = set()
    candidates: list[dict] = []

    for job in raw_jobs:
        jid = str(job.get("id", ""))
        company = job.get("company", "")
        pair = (job.get("title", ""), company)
        if not jid or jid in seen_ids or jid in existing_ids:
            continue
        if company in SPAM_COMPANIES or pair in seen_pairs:
            continue
        seen_ids.add(jid)
        seen_pairs.add(pair)
        candidates.append(job)

    if sample_per_city > 0 and len(candidates) > sample_per_city:
        sampled = rng.sample(candidates, sample_per_city)
    else:
        sampled = candidates

    print(f"  -> {len(candidates)} unique new candidates, sampled {len(sampled)}")
    return sampled


def main():
    parser = argparse.ArgumentParser(description="Scrape Built In software dev job listings")
    parser.add_argument("cities", nargs="*", help="Cities to scrape (default: all 15)")
    parser.add_argument("--date", default=date.today().isoformat(), help="Date label (YYYY-MM-DD)")
    parser.add_argument("--roles", nargs="*", default=ROLES, help="Role search queries")
    parser.add_argument("--pages-per-role", type=int, default=3, help="Max pages sampled per (city, role)")
    parser.add_argument("--sample-per-city", type=int, default=100, help="Random sample size per city-month (0 = no cap)")
    parser.add_argument("--workers", type=int, default=6, help="Concurrent role threads per city")
    parser.add_argument("--seed", type=str, default=None, help="Random seed (default: scraped_date)")
    args = parser.parse_args()

    scraped_date = args.date
    date_stamp = scraped_date.replace("-", "")
    cities = args.cities if args.cities else list(BUILTIN_CITIES.keys())
    seed = hash(args.seed or scraped_date)
    existing_ids = load_existing_ids()

    print("=" * 60)
    print("Built In Software Dev Jobs Scraper")
    print(f"Date: {scraped_date}")
    print(f"Proxy: {proxy_provider() or 'none (direct)'}")
    print(f"Cities ({len(cities)}): {', '.join(cities)}")
    print(f"Roles ({len(args.roles)}): {', '.join(args.roles)}")
    print(f"Sample per city: {args.sample_per_city} (pages/role={args.pages_per_role})")
    print(f"Existing global IDs to exclude: {len(existing_ids)}")
    print("=" * 60)

    all_jobs: list[dict] = []
    global_seen_ids: set[str] = set()

    for city_id in cities:
        if city_id not in BUILTIN_CITIES:
            print(f"Unknown city: {city_id}. Available: {', '.join(BUILTIN_CITIES.keys())}")
            continue

        city_jobs = scrape_city(
            city_id=city_id,
            city_config=BUILTIN_CITIES[city_id],
            roles=args.roles,
            scraped_date=scraped_date,
            pages_per_role=args.pages_per_role,
            sample_per_city=args.sample_per_city,
            existing_ids=existing_ids | global_seen_ids,
            seed=seed,
            workers=args.workers,
        )

        if city_jobs:
            for job in city_jobs:
                global_seen_ids.add(str(job["id"]))
            json_file = BUILTIN_JSON_DIR / f"{city_id}_{date_stamp}.json"
            with open(json_file, "w", encoding="utf-8") as f:
                json.dump(city_jobs, f, indent=2, ensure_ascii=False)
            all_jobs.extend(city_jobs)

    if all_jobs:
        csv_file = combined_csv_path(scraped_date)
        with open(csv_file, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_FIELDS, lineterminator="\n")
            writer.writeheader()
            for job in all_jobs:
                writer.writerow({field: job.get(field, "") for field in CSV_FIELDS})
        print(f"\nCombined CSV: {csv_file} ({len(all_jobs)} jobs)")

    print(f"\n{'=' * 60}")
    print(f"COMPLETE - {len(all_jobs)} total sampled jobs across {len(cities)} cities")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
