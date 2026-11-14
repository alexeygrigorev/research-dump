"""Quality metrics for a vacancies.jsonl.gz (no LLM, stdlib only). Used by clean_raw.py for
before/after numbers and runnable on its own: python quality.py <file.jsonl.gz> [out.json]"""
import collections, datetime as dt, gzip, json, re, sys

C = collections.Counter
PLACEHOLDER = re.compile(r"^\s*(\$\{desc\}|description here|\.|)\s*$", re.I)
STOP = {
    "en": set("the and to of a in for with you our we is are will be as on or your that this".split()),
    "de": set("und der die das mit für sie wir ein eine zu von im den auf ist".split()),
    "fr": set("et le la les des pour vous nous avec une un du de dans est".split()),
    "es": set("y el la los las para con una un del de en que nuestro".split()),
    "pt": set("e o os as para com uma um do da em que nosso você".split()),
}
EEO = re.compile(r"equal opportunity|qualified applicants will receive consideration|protected (?:basis|veteran|attribute)", re.I)
TAGS = re.compile(r"#(?:LI|BI)-[A-Za-z]+")
PRIVACY = re.compile(r"privacy (?:notice|policy)|GDPR|CCPA", re.I)
NONSW = re.compile(r"\b(mechanical|electrical|civil|hardware|construction|manufacturing|sales engineering)\b", re.I)
QA = re.compile(r"\b(test|qa|sdet|quality)\b", re.I)


def read(path):
    with gzip.open(path, "rt") as f:
        return [json.loads(l) for l in f]


def lang(text):
    w = re.findall(r"[A-Za-zÀ-ÿ]+", text.lower())
    if len(w) < 30:
        return "short"
    s = {k: sum(x in v for x in w) for k, v in STOP.items()}
    return max(s, key=s.get)


def norm(s):
    return re.sub(r"\W+", " ", (s or "").lower()).strip()


def metrics(rows):
    d = lambda r: r.get("description") or ""
    m = {"rows": len(rows)}
    m["by_source"] = dict(C(r["source"] for r in rows))
    m["by_region"] = dict(C(r["region"] for r in rows).most_common())
    m["by_role"] = dict(C(r["role"] for r in rows).most_common())
    # duplicates
    m["dup_same_source_jobid"] = len(rows) - len({(r["source"], r["job_id"]) for r in rows})
    m["dup_title_desc_exact"] = len(rows) - len({(norm(r["title"]), norm(d(r))) for r in rows})
    m["dup_company_title_loc_diff_text"] = len(rows) - len({(norm(r["title"]), norm(r["company"]), tuple(r["locations"])) for r in rows})
    m["dup_company_title"] = len(rows) - len({(norm(r["title"]), norm(r["company"])) for r in rows})
    m["dup_desc_only"] = len(rows) - len({norm(d(r)) for r in rows})
    # descriptions
    L = [len(d(r)) for r in rows]
    for t in (1, 200, 500, 1000):
        m[f"desc_lt_{t}"] = sum(x < t for x in L)
    m["desc_placeholder"] = sum(bool(PLACEHOLDER.match(d(r))) for r in rows)
    m["desc_median_len"] = sorted(L)[len(L) // 2] if L else 0
    m["desc_ends_no_punct"] = sum(1 for r in rows if d(r).rstrip()[-1:].isalnum())
    m["desc_ends_with_empty_heading"] = sum(1 for r in rows if re.search(r"\n\n[A-Z][A-Z &/]{3,}\s*$", d(r)))
    # language
    m["lang"] = dict(C(lang(d(r)) for r in rows))
    m["nonlatin_over50chars"] = sum(len(re.findall(r"[Ѐ-ӿ֐-ۿ぀-ヿ一-鿿가-힯]", d(r))) > 50 for r in rows)
    # text hygiene
    for k, p in {"nbsp": " ", "zero_width": "[​‌‍﻿]", "trailing_ws": r"[ \t]+\n",
                 "blank_run_3plus": r"\n{4,}", "html_tag": r"</?(?:span|strong|b|i|em|p|br|div|ul|li|ol|a)\b[^>]*>",
                 "template_var": r"\$\{[^}]+\}", "entity": r"&(?:amp|lt|gt|nbsp|quot|#\d+);"}.items():
        m["text_" + k] = sum(bool(re.search(p, d(r))) for r in rows)
    b = [r for r in rows if r["source"] == "builtin"]
    m["builtin_hardwrapped_docs"] = sum(1 for r in b if max((len(l) for l in d(r).split("\n")), default=0) <= 62 and len(d(r)) > 400)
    m["builtin_wrapped_looking_lines"] = sum(1 for r in b for l, nx in zip(d(r).split("\n"), d(r).split("\n")[1:]) if 48 <= len(l) <= 62 and nx.strip() and not re.match(r"\s*(?:[-*•]|\d+[.)])\s", nx))
    # boilerplate
    m["boiler_eeo"] = sum(bool(EEO.search(d(r))) for r in rows)
    m["boiler_privacy"] = sum(bool(PRIVACY.search(d(r))) for r in rows)
    m["boiler_board_tag"] = sum(bool(TAGS.search(d(r))) for r in rows)
    # roles
    m["title_nonsw_domain"] = sum(bool(NONSW.search(r["title"])) for r in rows)
    m["title_qa_test"] = sum(bool(QA.search(r["title"])) for r in rows)
    m["employment_intern"] = sum(r.get("employment_type") == "INTERN" for r in rows)
    # region
    m["region_unknown"] = sum(r["region"] == "UNKNOWN" for r in rows)
    m["region_remote"] = sum(r["region"] == "REMOTE" for r in rows)
    m["loc_gt_20"] = sum(len(r["locations"]) > 20 for r in rows)
    m["loc_multi"] = sum(len(r["locations"]) > 1 for r in rows)
    m["company_slug_like_greenhouse"] = sum(1 for r in rows if r["source"] != "builtin" and r["company"] == r["company"].lower() and " " not in r["company"])
    # dates
    gaps = []
    for r in rows:
        if r.get("first_seen") and r.get("posted_date"):
            try:
                f = dt.datetime.strptime(r["first_seen"][:8], "%Y%m%d").date()
                p = dt.datetime.strptime(r["posted_date"][:10], "%Y-%m-%d").date()
                gaps.append((f - p).days)
            except ValueError:
                pass
    gaps.sort()
    n = len(gaps)
    m["no_capture_ts"] = sum(not r.get("first_seen") for r in rows)
    m["no_posted_date"] = sum(not r.get("posted_date") for r in rows)
    m["capture_minus_posted_days_p10_50_90_99"] = [gaps[int(n * q)] for q in (.1, .5, .9, .99)] if n else []
    m["posted_gt_90d_before_capture"] = sum(g > 90 for g in gaps)
    m["posted_gt_365d_before_capture"] = sum(g > 365 for g in gaps)
    m["posted_month_eq_capture_month"] = sum(1 for r in rows if r.get("posted_date") and r["posted_date"][:7] == r["month"])
    m["by_month"] = dict(sorted(C(r["month"] for r in rows).items()))
    return m


if __name__ == "__main__":
    res = metrics(read(sys.argv[1]))
    out = json.dumps(res, indent=1, ensure_ascii=False)
    if len(sys.argv) > 2:
        open(sys.argv[2], "w").write(out)
    print(out)
