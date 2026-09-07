#!/usr/bin/env python3
"""Recalculate the archived 100-opportunity model using Python's standard library.

All inputs are analyst hypotheses, not actual sales or probabilities.
EUR; 12-month horizon; ex VAT, before tax and ownership splits.

Examples (run inside this directory):
    python model.py
    python model.py --hourly-rate 300 --output recalculated.csv
    python model.py --scenario down --top 100
    python model.py --weights 25,15,20,10,15,15

CSV input fields correspond to the original Model100 worksheet. Derived fields:
    revenue = price * paid_units
    cash_cost = launch_cash + annual_fixed_cash + variable_cash * paid_units
    founder_hours = setup_hours + annual_fixed_hours + hours_per_unit * paid_units
    cash_surplus = revenue - cash_cost
    economic_surplus = cash_surplus - founder_hours * hourly_rate
    economic_roi = economic_surplus / (cash_cost + founder_hours * hourly_rate)
    cash_per_hour = cash_surplus / founder_hours

Ranking weights: fit 25%, adjacent-demand evidence 20%, cash-return grade 20%,
speed 10%, scalability 15%, potential moat 10%. Return-grade cash/hour thresholds:
400 -> 5, 250 -> 4, 150 -> 3, 75 -> 2, below 75 -> 1. Scores are judgments,
not probabilities. Ties retain report order. All 100 cases are alternatives.

All setup capital is expensed for cash screening; no residual/terminal value.
That is not an investment valuation, GAAP/IFRS profit or an IRR. Standalone cases
retain full fixed annual costs and sales time even under downside volume.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from typing import Any

TEXT_FIELDS = {"id", "opportunity", "paid_unit", "source_ids"}
NUMERIC_FIELDS = (
    "report_rank", "price_eur", "base_units", "down_units", "up_units",
    "launch_cash_eur", "annual_fixed_cash_eur", "variable_cash_per_unit",
    "setup_founder_hours", "annual_fixed_founder_hours", "founder_hours_per_unit",
    "fit", "demand", "speed", "scale", "moat_now", "moat_potential",
)
SCORE_FIELDS = ("fit", "demand", "speed", "scale", "moat_now", "moat_potential")


def load_inputs(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        required = TEXT_FIELDS | set(NUMERIC_FIELDS)
        if not required.issubset(reader.fieldnames or []):
            raise ValueError(f"Missing CSV fields: {required - set(reader.fieldnames or [])}")
        rows = list(reader)
    if len(rows) != 100:
        raise ValueError(f"Expected 100 opportunities, found {len(rows)}")
    for row in rows:
        for key in NUMERIC_FIELDS:
            value = float(row[key])
            if not math.isfinite(value) or value < 0:
                raise ValueError(f"{row.get('id')}: invalid nonnegative input {key}")
            row[key] = value
        if not row["report_rank"].is_integer():
            raise ValueError("Report ranks must be integers")
        row["report_rank"] = int(row["report_rank"])
        if any(not 1 <= row[key] <= 5 for key in SCORE_FIELDS):
            raise ValueError(f"{row['id']}: scores must lie between 1 and 5")
    if {r["report_rank"] for r in rows} != set(range(1, 101)):
        raise ValueError("Report ranks must contain each integer from 1 to 100")
    if len({r["id"] for r in rows}) != 100:
        raise ValueError("Opportunity IDs must be unique")
    return rows


def calculate(row: dict[str, Any], units: float, hourly_rate: float,
              weights: tuple[float, ...], thresholds: tuple[float, ...],
              capacity: float, revenue_override: float | None = None) -> dict[str, Any]:
    revenue = row["price_eur"] * units if revenue_override is None else revenue_override
    cash_cost = row["launch_cash_eur"] + row["annual_fixed_cash_eur"] + row["variable_cash_per_unit"] * units
    hours = row["setup_founder_hours"] + row["annual_fixed_founder_hours"] + row["founder_hours_per_unit"] * units
    cash = revenue - cash_cost
    time_cost = hours * hourly_rate
    economic = cash - time_cost
    cash_per_hour = cash / hours if hours else 0.0
    grade = next((5 - i for i, threshold in enumerate(thresholds) if cash_per_hour >= threshold), 1)
    components = (row["fit"], row["demand"], grade, row["speed"], row["scale"], row["moat_potential"])
    score = sum(value * weight for value, weight in zip(components, weights)) / 5
    unit_economic_margin = row["price_eur"] - row["variable_cash_per_unit"] - row["founder_hours_per_unit"] * hourly_rate
    fixed_economic = row["launch_cash_eur"] + row["annual_fixed_cash_eur"] + (row["setup_founder_hours"] + row["annual_fixed_founder_hours"]) * hourly_rate
    break_even = math.ceil(fixed_economic / unit_economic_margin) if unit_economic_margin > 0 else "No break-even"
    return {
        "paid_units": units, "revenue_eur": revenue, "all_cash_cost_eur": cash_cost,
        "founder_hours": hours, "cash_surplus_eur": cash, "time_cost_eur": time_cost,
        "economic_surplus_eur": economic,
        "economic_roi": economic / (cash_cost + time_cost) if cash_cost + time_cost else 0.0,
        "cash_eur_per_founder_hour": cash_per_hour, "return_grade": grade,
        "weighted_score": score, "break_even_units_at_csv_price": break_even,
        "capacity_check": "Within cap" if hours <= capacity else "Exceeds cap",
    }


def portfolio(rows: list[dict[str, Any]], hourly_rate: float, weights: tuple[float, ...],
              thresholds: tuple[float, ...], capacity: float, displaced: float) -> list[dict[str, Any]]:
    by_id = {r["id"]: r for r in rows}
    cases = [("Downside", 2, 1, None), ("Base normalized", 6, 6, None),
             ("Upside", 10, 12, None),
             ("Base with 2 x EUR12000 + 4 x EUR20000 shipping pilots", 6, 6, 104000.0)]
    outputs = []
    for label, shipping_units, hiring_units, shipping_revenue in cases:
        shipping = calculate(by_id["SPRINT"], shipping_units, hourly_rate, weights, thresholds, capacity, shipping_revenue)
        hiring = calculate(by_id["HIRING"], hiring_units, hourly_rate, weights, thresholds, capacity)
        total = {key: shipping[key] + hiring[key] for key in (
            "revenue_eur", "all_cash_cost_eur", "founder_hours", "cash_surplus_eur", "time_cost_eur", "economic_surplus_eur")}
        total["economic_surplus_eur"] -= displaced
        # Additional displaced baseline is an economic cost, not a cash payment.
        denominator = total["all_cash_cost_eur"] + total["time_cost_eur"] + displaced
        total["economic_roi"] = total["economic_surplus_eur"] / denominator if denominator else 0.0
        total["additional_displaced_contribution_eur"] = displaced
        total["capacity_check"] = "Within cap" if total["founder_hours"] <= capacity else "Exceeds cap"
        outputs.append({"case": label, "shipping_units": shipping_units, "hiring_units": hiring_units, **total})
    return outputs


def parse_sequence(text: str, count: int) -> tuple[float, ...]:
    values = tuple(float(part) for part in text.split(","))
    if len(values) != count or any(not math.isfinite(v) or v < 0 for v in values):
        raise ValueError(f"Expected {count} nonnegative finite numbers separated by commas")
    return values


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", type=Path, default=Path(__file__).with_name("model100.csv"))
    parser.add_argument("--hourly-rate", type=float, default=150)
    parser.add_argument("--capacity-hours", type=float, default=600)
    parser.add_argument("--scenario", choices=("base", "down", "up"), default="base")
    parser.add_argument("--weights", default="25,20,20,10,15,10")
    parser.add_argument("--return-thresholds", default="400,250,150,75")
    parser.add_argument("--displaced-contribution", type=float, default=0,
                        help="Additional annual portfolio opportunity cost; do not double-count hourly opportunity cost")
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--output", type=Path, help="Optional CSV containing all 100 recalculated standalone results")
    args = parser.parse_args()
    try:
        for value in (args.hourly_rate, args.capacity_hours, args.displaced_contribution):
            if not math.isfinite(value) or value < 0:
                raise ValueError("Hourly rate, capacity and displaced contribution must be nonnegative and finite")
        if not 1 <= args.top <= 100:
            raise ValueError("--top must be between 1 and 100")
        weights = parse_sequence(args.weights, 6)
        thresholds = parse_sequence(args.return_thresholds, 4)
        if not math.isclose(sum(weights), 100):
            raise ValueError("Ranking weights must sum to 100")
        if any(a <= b for a, b in zip(thresholds, thresholds[1:])):
            raise ValueError("Return-grade thresholds must be strictly descending")
        rows = load_inputs(args.input)
        results = [{**row, **calculate(row, row[f"{args.scenario}_units"], args.hourly_rate,
                    weights, thresholds, args.capacity_hours)} for row in rows]
        results.sort(key=lambda row: (-row["weighted_score"], row["report_rank"]))
        for rank, row in enumerate(results, 1):
            row["live_rank"] = rank
        print("Analyst scenarios only; EUR ex VAT, before tax and ownership splits. Do not sum all 100 ideas.\n")
        print("Rank | Opportunity | Score | Revenue | Founder h | Economic surplus | ROI")
        for row in results[:args.top]:
            print(f"{row['live_rank']} | {row['opportunity']} | {row['weighted_score']:.0f} | "
                  f"{row['revenue_eur']:,.0f} | {row['founder_hours']:g} | "
                  f"{row['economic_surplus_eur']:,.0f} | {row['economic_roi']:.1%}")
        print("\nTwo-offer portfolio (fixed scenario volumes; full fixed costs retained):")
        print(json.dumps(portfolio(rows, args.hourly_rate, weights, thresholds,
                                  args.capacity_hours, args.displaced_contribution), indent=2))
        if args.output:
            if args.output.resolve() == args.input.resolve():
                raise ValueError("Output must not overwrite the input CSV")
            args.output.parent.mkdir(parents=True, exist_ok=True)
            with args.output.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=list(results[0]))
                writer.writeheader()
                writer.writerows(results)
    except (OSError, ValueError, KeyError, csv.Error) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
