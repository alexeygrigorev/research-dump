"""Measured Stage-1 coverage: distinct in-scope job links per city x month x source.

Sources
  cc       Common Crawl job-detail captures (city read from the archived JSON-LD)
  wayback  Wayback job-detail captures (city from the JSON-LD; a job's city is
           taken from any resolved capture of the same job id)
  listing  job cards on archived builtin.com city listing pages (Wayback)
  union    distinct job ids from any of the three

Writes ../coverage.json and prints a markdown table.
"""
import json
from collections import defaultdict
from pathlib import Path
import capture_index
from roles import role_of

ROOT = Path(__file__).resolve().parent.parent
W = ROOT / "work"
CITIES = ["london", "berlin", "newyork"]


def job_cities():
    """job_id -> (city, title-role) from every resolved capture."""
    out = {}
    for f in W.glob("resolved_*.jsonl"):
        for l in open(f):
            r = json.loads(l)
            if "error" in r or not r.get("locations"):
                continue
            out.setdefault(r["job_id"], (r["city"], r.get("role")))
    return out


def main():
    idx = capture_index.load()
    jc = job_cities()
    cov = defaultdict(lambda: defaultdict(set))  # (city, month) -> src -> job ids
    unresolved = defaultdict(lambda: defaultdict(set))
    for jid, refs in idx.items():
        if not role_of(refs[0]["slug"]):
            continue
        for r in refs:
            src = "cc" if r["src"] == "cc" else "wayback"
            if jid not in jc:
                unresolved[r["month"]][src].add(jid)
                continue
            city, role = jc[jid]
            if city in CITIES and role:
                cov[(city, r["month"])][src].add(jid)
    lf = W / "listing_links.jsonl"
    if lf.exists():
        for l in open(lf):
            r = json.loads(l)
            if r["role"] and r["city"] in CITIES:
                cov[(r["city"], r["month"])]["listing"].add(r["job_id"])
    months = sorted({m for _, m in cov} | set(unresolved))
    table = {}
    for c in CITIES:
        for m in months:
            d = cov[(c, m)]
            u = set().union(*d.values()) if d else set()
            table[f"{c}/{m}"] = {s: len(d[s]) for s in ("cc", "wayback", "listing")} | {"union": len(u)}
    unres = {m: {s: len(v) for s, v in d.items()} for m, d in unresolved.items()}
    (ROOT / "coverage.json").write_text(json.dumps({"by_city_month": table, "unresolved_in_scope_links": unres},
                                                   indent=1, sort_keys=True) + "\n")
    print("| month | " + " | ".join(f"{c} cc/wb/list/∪" for c in CITIES) + " |")
    print("|---|" + "---|" * len(CITIES))
    for m in months:
        cells = []
        for c in CITIES:
            t = table[f"{c}/{m}"]
            cells.append(f"{t['cc']}/{t['wayback']}/{t['listing']}/**{t['union']}**")
        print(f"| {m[:4]}-{m[4:]} | " + " | ".join(cells) + " |")
    print("unresolved:", unres)


if __name__ == "__main__":
    main()
