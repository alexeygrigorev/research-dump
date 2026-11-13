#!/usr/bin/env python3
"""One-command monthly live snapshot runner for software-dev-jobs."""
from __future__ import annotations

import argparse
import subprocess
import sys
from collections import Counter
from datetime import date
from pathlib import Path

import pandas as pd

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from pipeline_paths import RAW_YAML_DIR, combined_csv_path, dedup_csv_path


def run_step(label: str, cmd: list[str]) -> None:
    print(f"\n{'=' * 60}\nSTEP: {label}\nCMD: {' '.join(cmd)}\n{'=' * 60}")
    subprocess.run(cmd, cwd=REPO_ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run monthly Built In software dev job snapshot")
    parser.add_argument("--date", default=date.today().isoformat(), help="Snapshot date (YYYY-MM-DD)")
    parser.add_argument("--sample-per-city", type=int, default=100, help="Random sample size per city-month")
    parser.add_argument("--pages-per-role", type=int, default=3, help="Pages sampled per (city, role)")
    args = parser.parse_args()

    scraped_date = args.date
    py = sys.executable

    run_step(
        "1. Scrape Built In listings",
        [
            py,
            str(SCRIPT_DIR / "scrape_builtin_requests.py"),
            "--date",
            scraped_date,
            "--sample-per-city",
            str(args.sample_per_city),
            "--pages-per-role",
            str(args.pages_per_role),
        ],
    )

    raw_csv = combined_csv_path(scraped_date)
    if not raw_csv.exists():
        print(f"No jobs scraped for {scraped_date}; exiting.")
        return

    run_step(
        "2. Clean & deduplicate",
        [py, str(SCRIPT_DIR / "clean_dedup.py"), str(raw_csv)],
    )

    dedup_csv = dedup_csv_path(scraped_date)
    if not dedup_csv.exists():
        print(f"No dedup CSV found at {dedup_csv}; exiting.")
        return

    run_step(
        "3. Download job HTML pages",
        [py, str(SCRIPT_DIR / "download_all_html.py"), "--csv", str(dedup_csv)],
    )

    run_step(
        "4. Extract structured YAML",
        [py, str(SCRIPT_DIR / "extract_from_html.py"), "--all", "--csv", str(dedup_csv)],
    )

    # Print per-city summary
    df = pd.read_csv(dedup_csv)
    yaml_dir = RAW_YAML_DIR / scraped_date
    yaml_ids = {p.name.split("_", 1)[0] for p in yaml_dir.glob("*.yaml")} if yaml_dir.exists() else set()

    print(f"\n{'=' * 60}")
    print(f"SNAPSHOT SUMMARY ({scraped_date})")
    print(f"{'=' * 60}")
    print(f"{'City':15s} {'Listings':>10s} {'Extracted YAML':>15s}")
    print("-" * 42)
    city_counts = Counter(df["city"].fillna("unknown"))
    extracted_counts: Counter[str] = Counter()
    for _, row in df.iterrows():
        if str(row.get("id", "")) in yaml_ids:
            extracted_counts[str(row.get("city", "unknown"))] += 1
    for city in sorted(city_counts):
        print(f"{city:15s} {city_counts[city]:10d} {extracted_counts[city]:15d}")
    print("-" * 42)
    print(f"{'TOTAL':15s} {len(df):10d} {len(yaml_ids):15d}")


if __name__ == "__main__":
    main()
