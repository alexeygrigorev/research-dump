"""Crawl-bias and pool-size measurement across all archived sources (index only, no page reads).

For every board x crawl: captures, distinct job pages, in-scope (by URL title) and, where
the URL or host gives it, region. Writes ../source_measurement.json and prints tables.

Region = country market: UK, DE, US (city kept separately: london/berlin/newyork).
"""
import glob, json, re
from collections import defaultdict
from pathlib import Path
from roles import role_of, slug_of

ROOT = Path(__file__).resolve().parent.parent
W = ROOT / "work"

US_STATE = (r"AL|AK|AZ|AR|CA|CO|CT|DE|FL|GA|HI|ID|IL|IN|IA|KS|KY|LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|OH|"
            r"OK|OR|PA|RI|SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY|DC")
US_RE = re.compile(rf"(United-States|\bUSA\b|\bUS\b|-(?:{US_STATE})$|-(?:{US_STATE})-|New-York|California|Texas|Remote---US)", re.I)
UK_RE = re.compile(r"(London|United-Kingdom|\bUK\b|\bGBR\b|England|Manchester|Edinburgh|Glasgow|Bristol|Leeds|Cambridge-GB|Belfast)", re.I)
DE_RE = re.compile(r"(Berlin|Germany|Deutschland|\bDEU\b|M(ue|ü)nchen|Munich|Hamburg|Frankfurt|K(oe|ö)ln|Cologne|Stuttgart|D(ue|ü)sseldorf)", re.I)


def region_of_loc(loc):
    if UK_RE.search(loc):
        return "UK"
    if DE_RE.search(loc):
        return "DE"
    if US_RE.search(loc):
        return "US"
    return ""


def city_of_loc(loc):
    l = loc.lower()
    return "london" if "london" in l else "berlin" if "berlin" in l else "newyork" if "new-york" in l or "new york" in l else ""


def parse_url(board, url):
    """-> (job_key, title_text or None, region or '', city or '') or None when not a job page."""
    u = url.split("?")[0].split("#")[0].rstrip("/")
    if board == "builtin":
        slug, jid = slug_of(u)
        return (jid, slug, "", "") if jid else None
    if board == "workday":
        m = re.search(r"//([^/]+)/(?:[a-z]{2}-[A-Z]{2}/)?([^/]+)/job/([^/]+)/([^/]+?)_([A-Za-z0-9-]+?)(?:/apply.*)?$", u)
        if not m:
            return None
        host, site, loc, title, rid = m.groups()
        return (f"{host.split('.')[0]}/{rid}", title.replace("-", " "), region_of_loc(loc), city_of_loc(loc))
    if board == "reed":
        m = re.search(r"/jobs/([a-z0-9-]+)/(\d{6,})$", u)
        return (m.group(2), m.group(1), "UK", "") if m else None
    if board == "smartrecruiters":
        m = re.search(r"smartrecruiters\.com/([^/]+)/(\d{9,})-([^/]+)$", u)
        return (m.group(2), m.group(3), "", "") if m else None
    if board == "recruitee":
        m = re.search(r"//([^.]+)\.recruitee\.com/o/([^/]+)$", u)
        return (f"{m.group(1)}/{m.group(2)}", m.group(2), "", "") if m else None
    if board == "wttj":
        m = re.search(r"/companies/([^/]+)/jobs/([^/]+?)_([a-z0-9-]+)$", u)
        if not m:
            return None
        return (f"{m.group(1)}/{m.group(2)}", m.group(2), region_of_loc(m.group(3).replace("-", " ").title()),
                city_of_loc(m.group(3)))
    if board in ("ashby", "lever"):
        m = re.search(r"//jobs\.[^/]+/([^/]+)/([0-9a-f-]{36})$", u)
        return (f"{m.group(1)}/{m.group(2)}", None, "", "") if m else None
    if board.startswith("personio"):
        m = re.search(r"//([^.]+)\.jobs\.personio\.(?:de|com)/job/(\d+)$", u)
        return (f"{m.group(1)}/{m.group(2)}", None, "DE" if board == "personio_de" else "", "") if m else None
    if board == "greenhouse":
        m = re.search(r"/([^/]+)/jobs/(\d+)$", u)
        return (f"{m.group(1)}/{m.group(2)}", None, "", "") if m else None
    if board == "workable":
        m = re.search(r"workable\.com/([^/]+)/j/([0-9A-F]+)$", u)
        return (f"{m.group(1)}/{m.group(2)}", None, "", "") if m else None
    return None


def board_files():
    for f in glob.glob(str(W / "cc_job_cdx" / "*.jsonl")):
        yield "builtin", Path(f).stem, f
    for f in glob.glob(str(W / "cc_boards" / "*" / "*.jsonl")):
        yield Path(f).parent.name, Path(f).stem, f


def main():
    per_crawl = defaultdict(dict)        # crawl -> board -> stats
    per_month = defaultdict(lambda: defaultdict(lambda: defaultdict(set)))  # month -> board -> key -> set
    for board, crawl, f in board_files():
        caps, jobs, scope, by_region = 0, set(), set(), defaultdict(set)
        for l in open(f):
            r = json.loads(l)
            if str(r.get("status")) != "200":
                continue
            caps += 1
            p = parse_url(board, r["url"])
            if not p:
                continue
            key, title, region, city = p
            jobs.add(key)
            m = r["timestamp"][:6]
            per_month[m][board]["jobs"].add(key)
            if title is not None and role_of(title):
                scope.add(key)
                per_month[m][board]["scope"].add(key)
                if region:
                    by_region[region].add(key)
                    per_month[m][board]["scope_" + region].add(key)
        per_crawl[crawl][board] = {"captures": caps, "job_pages": len(jobs),
                                   "in_scope_by_url": len(scope) if board in TITLE_IN_URL else None,
                                   **{f"in_scope_{k}": len(v) for k, v in by_region.items()}}
    months = {m: {b: {k: len(v) for k, v in d.items()} for b, d in bd.items()} for m, bd in sorted(per_month.items())}
    out = {"per_crawl": dict(sorted(per_crawl.items())), "per_month": months}
    (ROOT / "source_measurement.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
    boards = sorted({b for c in per_crawl.values() for b in c})
    print("| crawl | " + " | ".join(boards) + " |")
    print("|---" * (len(boards) + 1) + "|")
    for c, d in sorted(per_crawl.items()):
        print(f"| {c} | " + " | ".join(str(d.get(b, {}).get("job_pages", "")) for b in boards) + " |")


TITLE_IN_URL = {"builtin", "workday", "reed", "smartrecruiters", "recruitee", "wttj"}

if __name__ == "__main__":
    main()
