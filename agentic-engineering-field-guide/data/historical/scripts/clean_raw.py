"""Step 1b: deterministic cleaning of raw/vacancies.jsonl.gz (t3450u). No LLM, no network.

Usage: python clean_raw.py [RAW_FILE] [OUT_DIR]     (default raw/vacancies.jsonl.gz -> clean/)

Steps (each counted in clean/summary.json):
 1. reject rows whose description is empty / a template placeholder ("${desc}", ".", "Description here")
 2. text normalisation: NBSP -> space, zero-width chars out, stray HTML tags out, trailing blanks out,
    3+ blank lines -> 1 blank line
 3. un-wrap builtin descriptions (hard-wrapped at 62 columns by the source) by reversing the wrap
 4. region: resolve bare ISO-3 country codes ("POL", "ESP, ESP") which the regex ignored; region of the
    first resolvable location; add regions_all / n_locations; old value kept in region_original
 5. second dedupe on the cleaned text: same normalised title + full description, and same company
    or different source (cross-source twin, e.g. builtin "DRW" vs greenhouse "drweng")
 6. flags only (nothing dropped): lang, month_basis, posted_month
Everything questionable is left untouched and listed in QUALITY_REPORT.md as an open question.
"""
import collections, gzip, hashlib, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import quality  # noqa: E402

HERE = Path(__file__).resolve().parent.parent
RAW = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "raw" / "vacancies.jsonl.gz"
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "clean"
WRAP = 62

ISO3 = {}
for reg, codes in {
    "US": "USA", "CA": "CAN", "IN": "IND", "UK": "GBR", "DE": "DEU",
    "EU": "POL PRT ESP FRA ROU IRL BGR CZE ITA HUN NLD UKR SWE AUT LTU DNK SRB CHE CYP EST NOR BEL SVN LUX FIN "
          "BLR MDA HRV SVK MNE GRC EUR VAT",
    "MEA": "ISR ARE UAE TUR PAK EGY ZAF NGA MAR GHA NAM MWI MOZ KEN BEN GMB IRQ QAT CMR TLV",
    "LATAM": "MEX BRA ARG CHL COL CRI VEN PER URY PRY ECU NIC BLZ JAM",
    "APAC": "SGP NZL PHL MYS AUS JPN VNM HKG TWN IDN THA CHN KOR BGD LKA NPL",
}.items():
    for c in codes.split():
        ISO3[c] = reg
# not mapped on purpose (ambiguous, open question): ARM GEO TJK UZB KGZ KAZ PRI VIR DOM HTI

TAG = re.compile(r"</?(?:span|strong|b|i|em|p|br|div|ul|li|ol)\b[^>]*>", re.I)
LIST = re.compile(r"^\s*(?:[-*•]|\d+[.)])\s")
ZW = re.compile("[​‌﻿⁠]")


def clean_text(t):
    t = t.replace(" ", " ")
    t = ZW.sub("", t)
    t = TAG.sub("", t)
    t = re.sub(r"[ \t]+\n", "\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def unwrap(t):
    """Reverse a textwrap(width=62): join a line to the previous one only if the previous
    line plus the next word would not have fit in 62 columns."""
    out = []
    for line in t.split("\n"):
        s = line.strip()
        if out and s and out[-1].strip() and not LIST.match(line) and \
                len(out[-1]) + 1 + len(s.split(" ", 1)[0]) > WRAP and len(out[-1]) >= WRAP - 14:
            out[-1] = out[-1] + " " + s
        else:
            out.append(line.rstrip())
    return "\n".join(out)


def loc_region(loc, bld):
    m = re.fullmatch(r"(?:[^,]+, )?([A-Z]{3})", loc.strip())
    if m and m.group(1) in ISO3:
        return ISO3[m.group(1)]
    r = bld.region([loc], False)
    return None if r in ("UNKNOWN", "REMOTE") else r


def main():
    import importlib.util
    argv, sys.argv = sys.argv, ["x", "/nonexistent", "/tmp/_unused"]
    spec = importlib.util.spec_from_file_location("build_raw", Path(__file__).resolve().parent / "build_raw.py")
    bld = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bld)
    sys.argv = argv

    rows = quality.read(RAW)
    before = quality.metrics(rows)
    st = collections.Counter()
    st["rows_in"] = len(rows)

    keep, rejects = [], []
    for r in rows:
        if quality.PLACEHOLDER.match(r["description"] or ""):
            r["reject_reason"] = "empty_or_placeholder_description"
            rejects.append(r)
        else:
            keep.append(r)
    st["rejected_placeholder_description"] = len(rejects)

    for r in keep:
        d0 = r["description"]
        d = clean_text(d0)
        if r["source"] == "builtin":
            d2 = unwrap(d)
            st["unwrapped_docs"] += d2 != d
            d = d2
        st["text_changed_docs"] += d != d0
        r["description"] = d
        r["has_description"] = len(d) >= 200
        r["content_hash"] = hashlib.sha1(f"{r['title']}|{r['company']}|{d[:2000]}".encode()).hexdigest()
        # region
        regs = [loc_region(l, bld) for l in r["locations"]]
        first = next((x for x in regs if x), None)
        new = first or ("REMOTE" if r.get("remote") or re.search(r"\bremote\b|anywhere|worldwide", " ".join(r["locations"]), re.I) else "UNKNOWN")
        if new != r["region"]:
            r["region_original"] = r["region"]
            st["region_changed"] += 1
            st[f"region_{r['region']}->{new}"] += 1
        r["region"] = new
        r["regions_all"] = sorted({x for x in regs if x})
        r["n_locations"] = len(r["locations"])
        # flags
        r["lang"] = quality.lang(d)
        r["month_basis"] = "capture" if r.get("first_seen") else "crawl_batch"
        r["posted_month"] = (r.get("posted_date") or "")[:7]

    # dedupe 2: cleaned title + full text; same company or different source
    groups = collections.defaultdict(list)
    for r in keep:
        groups[(quality.norm(r["title"]), quality.norm(r["description"]))].append(r)
    out, merged = [], []
    for g in groups.values():
        if len(g) == 1:
            out.append(g[0])
            continue
        # prefer builtin (display company name) then earliest capture
        g.sort(key=lambda r: (r["source"] != "builtin", r.get("first_seen") or "9"))
        k, rest = g[0], []
        for o in g[1:]:
            same_co = quality.norm(o["company"]).replace(" ", "") == quality.norm(k["company"]).replace(" ", "")
            if same_co or o["source"] != k["source"]:
                rest.append(o)
            else:
                out.append(o)
                st["same_text_diff_company_same_source_kept"] += 1
        for o in rest:
            k["dup_ids"] = k["dup_ids"] + [o["vacancy_id"]] + o["dup_ids"]
            k["locations"] = k["locations"] + [l for l in o["locations"] if l not in k["locations"]]
            k["n_captures"] += o["n_captures"]
            fs = [x for x in (k.get("first_seen"), o.get("first_seen")) if x]
            ls = [x for x in (k.get("last_seen"), o.get("last_seen")) if x]
            k["first_seen"], k["last_seen"] = (min(fs) if fs else ""), (max(ls) if ls else "")
            if quality.norm(o["company"]) != quality.norm(k["company"]):
                st["merged_cross_source_company_name_differs"] += 1
            st["merged_by_dedupe2_" + o["source"] + "_into_" + k["source"]] += 1
            merged.append({"dropped": o["vacancy_id"], "kept": k["vacancy_id"], "title": k["title"],
                           "company_kept": k["company"], "company_dropped": o["company"]})
        k["n_locations"] = len(k["locations"])
        out.append(k)
    st["dedupe2_rows_removed"] = len(keep) - len(out)
    out.sort(key=lambda r: r["vacancy_id"])
    st["rows_out"] = len(out)

    OUT.mkdir(parents=True, exist_ok=True)
    for name, data in (("vacancies.jsonl.gz", out), ("rejects.jsonl.gz", rejects)):
        with gzip.open(OUT / name, "wt", compresslevel=9) as f:
            for r in data:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(OUT / "dedupe2_merges.jsonl", "w") as f:
        for m in merged:
            f.write(json.dumps(m, ensure_ascii=False) + "\n")
    after = quality.metrics(out)
    (OUT / "summary.json").write_text(json.dumps({"steps": dict(st), "before": before, "after": after}, indent=1, ensure_ascii=False))
    print(json.dumps(dict(st), indent=1))


main()
