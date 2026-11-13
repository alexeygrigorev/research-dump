"""Generic schema.org JobPosting (JSON-LD) -> field-guide record, for ATS / job-board
pages other than Built In. Same core fields as builtin_parse / the field guide's
data_raw: job_id, title, company, location, locations, remote, work_type, description,
posted_date, url, source (+ country codes for region filtering)."""
import html as htmlmod, json, re

LD_RE = re.compile(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', re.S | re.I)
TAG_RE = re.compile(r"<[^>]+>")

COUNTRY = {
    "united kingdom": "GB", "uk": "GB", "gb": "GB", "gbr": "GB", "england": "GB", "great britain": "GB", "scotland": "GB",
    "germany": "DE", "deutschland": "DE", "de": "DE", "deu": "DE",
    "united states": "US", "usa": "US", "us": "US", "united states of america": "US",
}
US_STATES_NY = {"ny", "new york"}


def _iter(obj):
    if isinstance(obj, list):
        for o in obj:
            yield from _iter(o)
    elif isinstance(obj, dict):
        if "@graph" in obj:
            yield from _iter(obj["@graph"])
        yield obj


def _text(v):
    if isinstance(v, dict):
        v = v.get("name") or v.get("@value") or ""
    if isinstance(v, list):
        v = ", ".join(_text(x) for x in v)
    return str(v or "").strip()


def clean_html(s):
    s = htmlmod.unescape(s or "")
    s = re.sub(r"<(br|/p|/li|/h\d|/div)[^>]*>", "\n", s, flags=re.I)
    s = htmlmod.unescape(TAG_RE.sub("", s))
    return re.sub(r"\n\s*\n+", "\n\n", s).strip()


def _place(loc):
    a = loc.get("address", loc) if isinstance(loc, dict) else {}
    if isinstance(a, list):
        a = a[0] if a else {}
    if isinstance(a, str):
        return {"locality": a, "region": "", "country": ""}
    return {"locality": _text(a.get("addressLocality")), "region": _text(a.get("addressRegion")),
            "country": _text(a.get("addressCountry"))}


def country_code(p):
    c = p["country"].lower().strip()
    if c in COUNTRY:
        return COUNTRY[c]
    blob = f"{p['locality']} {p['region']} {p['country']}".lower()
    if re.search(r"\blondon\b|united kingdom|england", blob):
        return "GB"
    if re.search(r"\bberlin\b|germany|deutschland|münchen|munich|hamburg", blob):
        return "DE"
    if re.search(r"\bnew york\b|united states|\bny\b", blob):
        return "US"
    return c.upper()[:2] if len(c) == 2 else ""


def city_of(p):
    blob = f"{p['locality']} {p['region']}".lower()
    if "london" in blob:
        return "london"
    if "berlin" in blob:
        return "berlin"
    if re.search(r"new york|brooklyn|manhattan", blob) or (p["locality"].lower() in ("nyc",)):
        return "newyork"
    return ""


def parse(html_text, url="", source=""):
    """Return a record or {} when there is no JobPosting with a title and description."""
    for m in LD_RE.finditer(html_text or ""):
        raw = m.group(1).strip()
        try:
            data = json.loads(raw)
        except ValueError:
            try:
                data = json.loads(re.sub(r"[\x00-\x1f]", " ", raw))
            except ValueError:
                continue
        for o in _iter(data):
            t = o.get("@type")
            if not (t == "JobPosting" or (isinstance(t, list) and "JobPosting" in t)):
                continue
            title = _text(o.get("title"))
            desc = clean_html(o.get("description") or "")
            if not title or not desc:
                continue
            locs = o.get("jobLocation") or []
            locs = locs if isinstance(locs, list) else [locs]
            places = [_place(l) for l in locs if l]
            remote = str(o.get("jobLocationType", "")).upper() == "TELECOMMUTE"
            ident = o.get("identifier")
            jid = _text(ident.get("value")) if isinstance(ident, dict) else _text(ident)
            sal = o.get("baseSalary")
            return {
                "job_id": jid or url, "title": title, "company": _text(o.get("hiringOrganization")),
                "location": ", ".join(x for x in (places[0].values() if places else []) if x),
                "locations": [", ".join(x for x in p.values() if x) for p in places],
                "countries": sorted({country_code(p) for p in places} - {""}),
                "cities": sorted({city_of(p) for p in places} - {""}),
                "remote": remote, "work_type": _text(o.get("employmentType")),
                "compensation": json.dumps(sal, ensure_ascii=False) if sal else "",
                "description": desc, "posted_date": _text(o.get("datePosted"))[:10],
                "valid_through": _text(o.get("validThrough"))[:10],
                "url": url, "source": source,
            }
    return {}


GH_TITLE = re.compile(r"<title>\s*Job Application for (.*?) at (.*?)\s*</title>", re.S)
GH_LOC = re.compile(r'<meta property="og:description" content="([^"]*)"')
GH_CONTENT = re.compile(r'"title":"((?:[^"\\]|\\.)*)","hiring_plan_id":\d+,"content":"((?:[^"\\]|\\.)*)"')


def parse_greenhouse(html_text, url=""):
    """job-boards.greenhouse.io has no JSON-LD: title/company from <title>, location from
    og:description, description from the embedded job JSON."""
    t = GH_TITLE.search(html_text or "")
    if not t:
        return {}
    loc = GH_LOC.search(html_text)
    loc = htmlmod.unescape(loc.group(1)) if loc else ""
    c = GH_CONTENT.search(html_text)
    desc = clean_html(json.loads('"' + c.group(2) + '"')) if c else ""
    parts = [x.strip() for x in loc.split(",")]
    place = {"locality": parts[0] if parts else "", "region": ", ".join(parts[1:-1]),
             "country": parts[-1] if len(parts) > 1 else ""}
    m = re.search(r"/jobs/(\d+)", url)
    return {"job_id": m.group(1) if m else url, "title": htmlmod.unescape(t.group(1)).strip(),
            "company": htmlmod.unescape(t.group(2)).strip(), "location": loc, "locations": [loc] if loc else [],
            "countries": [country_code(place)] if country_code(place) else [], "cities": [city_of(place)] if city_of(place) else [],
            "remote": "remote" in loc.lower(), "work_type": "", "compensation": "", "description": desc,
            "posted_date": "", "valid_through": "", "url": url, "source": "greenhouse"}


def parse_any(html_text, url="", source=""):
    rec = parse(html_text, url, source)
    if not rec and source == "greenhouse":
        rec = parse_greenhouse(html_text, url)
    return rec
