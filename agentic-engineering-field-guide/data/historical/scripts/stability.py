"""Is each region x month sample big and stable enough to draw conclusions? (Alexey t3382u, t3383u)

Unit: distinct in-scope postings (job key) captured in a month, by region (US, EUROPE = UK + DE +
rest of Europe, UK, DE) and source,
with the role bucket from the title in the URL (Workday, reed, SmartRecruiters, Welcome to the
Jungle, Recruitee) or the Built In slug + the city resolved from the archived page.

Crawl-bias controls:
  * per-source share of each month is reported; a month is FLAGGED when any source's share is
    more than 2x or less than 0.5x its average share over the window (a crawl change, not the market);
  * the role mix is computed per source and combined with FIXED source weights (each source's
    average share over the window), so a crawl that over-collects one board cannot move the mix;
  * only shares are compared month to month, never absolute counts.

Stopping criterion, per region-month (all must hold):
  n >= 300 in-scope postings,
  TVD(role mix, previous month) <= 0.10, and
  TVD <= 2 x the TVD expected from sampling noise alone at that n (bootstrap), i.e. no shift
  beyond what random sampling explains.

Writes ../stability.json and prints the markdown table.
"""
import glob, gzip, json, random, re
from collections import Counter, defaultdict
from pathlib import Path

import coverage
import measure_sources as ms
from regions import region_of, in_region
from roles import role_of, slug_of

ROOT = Path(__file__).resolve().parent.parent
W = ROOT / "work"
ROLES = ["software_engineer", "software_developer", "backend", "frontend", "full_stack", "engineering_manager"]
CITY_REGION = {"london": "UK", "berlin": "DE", "newyork": "US"}
TARGETS = ["US", "EUROPE", "UK", "DE"]
N_MIN, TVD_MAX, NOISE_X = 300, 0.10, 2.0


def collect():
    """target region -> month -> source -> {job_key: role}

    Sources: Built In (Common Crawl + Wayback; city from the resolved page), Workday (title and
    location in the URL), reed / Welcome to the Jungle (URL), Greenhouse company boards
    (stage1_gh_listings.py: title + location for every job of a fixed panel of companies)."""
    data = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))

    def add(region_code, month, source, key, role):
        for target in TARGETS:
            if in_region(region_code, target):
                data[target][month][source][key] = role

    builtin_city = {jid: c for jid, (c, _) in coverage.job_cities().items()}
    for board, crawl, f in ms.board_files():
        if board not in ("builtin", "workday", "reed", "wttj"):
            continue
        for l in open(f):
            r = json.loads(l)
            if str(r.get("status")) != "200":
                continue
            p = ms.parse_url(board, r["url"])
            if not p or p[1] is None:
                continue
            key, title, region, city = p
            role = role_of(title)
            if not role:
                continue
            if board == "builtin":
                region = CITY_REGION.get(builtin_city.get(key, ""), "")
            elif board == "workday":
                m = re.search(r"/job/([^/]+)/", r["url"])
                region = region_of(m.group(1).replace("-", " ")) if m else ""
            add(region, r["timestamp"][:6], board, key, role)
    for f in glob.glob(str(W / "wayback_job_cdx" / "*.jsonl")):  # Wayback Built In captures too
        for l in open(f):
            r = json.loads(l)
            if r.get("statuscode") != "200":
                continue
            slug, jid = slug_of(r["original"])
            role = role_of(slug)
            region = CITY_REGION.get(builtin_city.get(jid, ""), "")
            if role and region:
                add(region, r["timestamp"][:6], "builtin", jid, role)
    for f in glob.glob(str(W / "gh_listings" / "*.jsonl.gz")):
        for l in gzip.open(f, "rt"):
            r = json.loads(l)
            if r.get("role"):
                add(r["region"], r["month"], "greenhouse", r["key"], r["role"])
    return data


def mix(counter):
    n = sum(counter.values())
    return {r: counter.get(r, 0) / n for r in ROLES} if n else {r: 0 for r in ROLES}


def tvd(a, b):
    return 0.5 * sum(abs(a[r] - b[r]) for r in ROLES)


def noise_tvd(p, n, reps=200, seed=0):
    """Expected TVD between two independent samples of size n drawn from mix p."""
    if n == 0:
        return 1.0
    rng = random.Random(seed)
    w = [p[r] for r in ROLES]
    out = []
    for _ in range(reps):
        a = Counter(rng.choices(ROLES, w, k=n)); b = Counter(rng.choices(ROLES, w, k=n))
        out.append(tvd(mix(a), mix(b)))
    return sum(out) / reps


def main(window=("202507", "202611")):
    data = collect()
    result = {}
    for region in TARGETS:
        months = sorted(m for m in data[region] if window[0] <= m <= window[1])
        # dedup across months: a posting counts in the first month it was captured
        seen, per_month = set(), {}
        for m in months:
            src = {}
            for s, jobs in data[region][m].items():
                fresh = {k: v for k, v in jobs.items() if (s, k) not in seen}
                seen.update((s, k) for k in fresh)
                if fresh:
                    src[s] = Counter(fresh.values())
            per_month[m] = src
        tot = Counter()
        for src in per_month.values():
            for s, c in src.items():
                tot[s] += sum(c.values())
        weights = {s: v / sum(tot.values()) for s, v in tot.items()} if tot else {}
        rows, prev_fixed = [], None
        for m in months:
            src = per_month[m]
            n = sum(sum(c.values()) for c in src.values())
            share = {s: sum(c.values()) / n for s, c in src.items()} if n else {}
            raw = mix(sum(src.values(), Counter()))
            # fixed-weight mix over the sources present this month (renormalised)
            present = {s: weights[s] for s in src if weights.get(s)}
            z = sum(present.values()) or 1
            fixed = {r: sum(present[s] / z * mix(src[s])[r] for s in present) for r in ROLES}
            flags = [f"{s} share {share.get(s, 0):.2f} vs avg {weights[s]:.2f}" for s in weights
                     if weights[s] >= 0.05 and not (0.5 * weights[s] <= share.get(s, 0) <= 2 * weights[s])]
            d = tvd(fixed, prev_fixed) if prev_fixed else None
            noise = noise_tvd(fixed, n) if n else None
            stable = (n >= N_MIN and d is not None and d <= TVD_MAX and d <= NOISE_X * noise)
            rows.append({"month": m, "n": n, "sources": {s: sum(c.values()) for s, c in src.items()},
                         "source_share": {s: round(v, 3) for s, v in share.items()},
                         "role_mix_raw": {r: round(v, 3) for r, v in raw.items()},
                         "role_mix_fixed": {r: round(v, 3) for r, v in fixed.items()},
                         "tvd_prev": None if d is None else round(d, 3),
                         "tvd_noise": None if noise is None else round(noise, 3),
                         "crawl_shift_flags": flags, "meets_criterion": stable})
            prev_fixed = fixed if n else prev_fixed
        result[region] = {"weights": {s: round(v, 3) for s, v in weights.items()}, "months": rows}
    crit = {"n_min": N_MIN, "tvd_max": TVD_MAX, "noise_multiple": NOISE_X}
    (ROOT / "stability.json").write_text(json.dumps({"criterion": crit, "regions": result}, indent=1) + "\n")
    for region, r in result.items():
        print(f"\n### {region}  (fixed source weights: {r['weights']})\n")
        print("| month | n | sources | SWE share (fixed) | TVD vs prev | noise TVD | crawl-shift flag | meets |")
        print("|---|---|---|---|---|---|---|---|")
        for x in r["months"]:
            print(f"| {x['month'][:4]}-{x['month'][4:]} | {x['n']} | "
                  + ", ".join(f"{s} {v}" for s, v in sorted(x["sources"].items(), key=lambda kv: -kv[1]))
                  + f" | {x['role_mix_fixed']['software_engineer']:.2f} | {x['tvd_prev'] if x['tvd_prev'] is not None else '-'}"
                  + f" | {x['tvd_noise'] if x['tvd_noise'] is not None else '-'} | {'; '.join(x['crawl_shift_flags']) or '-'}"
                  + f" | {'yes' if x['meets_criterion'] else 'no'} |")


if __name__ == "__main__":
    main()
