"""Count coding-agent / AI-assisted-development signals in the existing
AI Engineering Field Guide job corpus. No scraping, no LLM calls.

Usage:
    python3 coding_agent_signals.py /path/to/ai-engineering-field-guide [out.json]

Reads job-market/data_raw/<scrape>/*.yaml (text parsed from the posting HTML)
and job-market/data_structured/<scrape>/*.yaml (for the ai_type label only).
Every match is a case-insensitive regular expression on title + description +
the posting's own skills list, unless noted.
"""
import collections
import glob
import json
import os
import random
import re
import sys

import yaml

ROOT = sys.argv[1]
OUT = sys.argv[2] if len(sys.argv) > 2 else None
I = re.IGNORECASE

TOOLS = {
    "Claude Code": re.compile(r"claude[\s-]?code", I),
    "Cursor": re.compile(r"\bCursor\b(?![\s-]based)"),  # capitalised only
    "GitHub Copilot": re.compile(r"github[\s-]+copilot", I),
    "Codex": re.compile(r"\bCodex\b"),
    "Windsurf": re.compile(r"\bWindsurf\b"),
    "Devin": re.compile(r"\bDevin\b"),
    "Cline": re.compile(r"\bCline\b"),
    "Aider": re.compile(r"\bAider\b"),
    "Gemini CLI": re.compile(r"gemini[\s-]cli", I),
    "OpenCode": re.compile(r"\bOpenCode\b"),
    "Kiro": re.compile(r"\bKiro\b"),
    "Amazon Q": re.compile(r"amazon q\b|\bq developer\b", I),
    "Replit": re.compile(r"\bReplit\b"),
    "Lovable": re.compile(r"\bLovable\b"),
}
CONCEPTS = {
    "coding agent / coding assistant": re.compile(
        r"\bcoding[\s-]+(agents?|assistants?)\b|\bcode[\s-]+assistants?\b|\bcoding[\s-]+copilots?\b", I),
    "AI-assisted / AI-native development": re.compile(
        r"\bai[\s-]+(assisted|augmented|native|first|powered|driven|enabled)[\s-]+"
        r"(software[\s-]+)?(development|coding|engineering|programming|developer|sdlc)\b", I),
    "agentic coding / development / engineering": re.compile(
        r"\bagentic[\s-]+(coding|software[\s-]+(development|engineering)|development|engineering|sdlc)\b", I),
    "vibe coding": re.compile(r"\bvibe[\s-]?cod", I),
    "spec-driven": re.compile(r"\bspec(ification)?[\s-]driven\b", I),
    "context engineering": re.compile(r"\bcontext[\s-]engineering\b", I),
    "harness": re.compile(r"\b(agent(ic)?|harness)[\s-]+(harness|engineering)\b", I),
    "AI code review": re.compile(r"\bai[\s-]+(code[\s-]+)?review", I),
    "MCP": re.compile(r"\bMCP\b|model context protocol", I),
    "AGENTS.md / CLAUDE.md / agent skills": re.compile(r"agents\.md|claude\.md|skill\.md|\bagent skills\b", I),
}
ANY_COPILOT = re.compile(r"\bcopilot\b", I)

TITLE_FAMILIES = [
    ("AI/ML/LLM in title", re.compile(r"\b(ai|a\.i\.|ml|llm|genai|gen ai|machine learning|agent|agentic|applied)\b", I)),
    ("software/full-stack/backend/frontend", re.compile(
        r"software|full[\s-]?stack|back[\s-]?end|front[\s-]?end|developer|platform|devops|sre|infrastructure", I)),
]


def title_family(title):
    for name, rx in TITLE_FAMILIES:
        if rx.search(title or ""):
            return name
    return "other"


def region(loc):
    loc = loc or ""
    if "DEU" in loc:
        return "Germany"
    for code, name in (("USA", "USA"), ("IND", "India"), ("GBR", "UK"), ("NLD", "Netherlands")):
        if code in loc:
            return name
    return "other"


def load(path):
    with open(path) as fh:
        return yaml.load(fh, Loader=yaml.CSafeLoader)


def main():
    ai_type = {}
    for f in glob.glob(os.path.join(ROOT, "job-market/data_structured/*/*.yaml")):
        try:
            d = load(f)
            ai_type[os.path.basename(f).split("_")[0]] = (
                ((d.get("position") or {}).get("ai_type") or {}).get("type") or "unknown")
        except Exception:
            pass

    rows = []
    for f in sorted(glob.glob(os.path.join(ROOT, "job-market/data_raw/*/*.yaml"))):
        scrape = f.split(os.sep)[-2]
        try:
            d = load(f)
        except Exception:
            continue
        jid = str(d.get("job_id"))
        text = "\n".join([str(d.get("title") or ""), str(d.get("description") or ""),
                          ", ".join(map(str, d.get("skills") or []))])
        tools = [k for k, rx in TOOLS.items() if rx.search(text)]
        concepts = [k for k, rx in CONCEPTS.items() if rx.search(text)]
        rows.append({
            "scrape": scrape, "job_id": jid, "title": d.get("title"), "company": d.get("company"),
            "url": d.get("url"), "region": region(d.get("location")), "location": d.get("location"),
            "ai_type": ai_type.get(jid, "unknown"), "family": title_family(d.get("title")),
            "tools": tools, "concepts": concepts, "any_copilot": bool(ANY_COPILOT.search(text)),
            "text": text,
        })

    def share(sub, pred):
        n = len(sub)
        k = sum(1 for r in sub if pred(r))
        return {"n": n, "k": k, "pct": round(100 * k / n, 1) if n else None}

    named = lambda r: bool(r["tools"])
    practice = lambda r: any(c in r["concepts"] for c in list(CONCEPTS)[:4])
    either = lambda r: named(r) or practice(r)

    res = {"total": len(rows), "by_scrape": {}, "by_region": {}, "by_ai_type": {}, "by_family": {},
           "tools": {}, "concepts": {}, "tools_by_scrape": {}}
    scrapes = sorted({r["scrape"] for r in rows})
    for s in scrapes:
        sub = [r for r in rows if r["scrape"] == s]
        res["by_scrape"][s] = {"named_tool": share(sub, named), "practice_phrase": share(sub, practice),
                               "either": share(sub, either),
                               "mcp": share(sub, lambda r: "MCP" in r["concepts"])}
        res["tools_by_scrape"][s] = {t: share(sub, lambda r, t=t: t in r["tools"])["pct"]
                                     for t in ("Claude Code", "Cursor", "GitHub Copilot", "Codex")}
    for key, out in (("region", "by_region"), ("ai_type", "by_ai_type"), ("family", "by_family")):
        for v in sorted({r[key] for r in rows}):
            sub = [r for r in rows if r[key] == v]
            res[out][v] = {"all": share(sub, either),
                           "first3": share([r for r in sub if r["scrape"] in scrapes[:3]], either),
                           "last3": share([r for r in sub if r["scrape"] in scrapes[-3:]], either)}
    for t in TOOLS:
        res["tools"][t] = share(rows, lambda r, t=t: t in r["tools"])
    res["tools"]["any 'Copilot' (incl. Microsoft/product copilots)"] = share(rows, lambda r: r["any_copilot"])
    for c in CONCEPTS:
        res["concepts"][c] = share(rows, lambda r, c=c: c in r["concepts"])

    # number of distinct tools named per posting that names any
    res["tools_per_posting"] = dict(sorted(collections.Counter(
        len(r["tools"]) for r in rows if r["tools"]).items()))
    # co-mentions of tool pairs
    pairs = collections.Counter()
    for r in rows:
        ts = sorted(r["tools"])
        for i in range(len(ts)):
            for j in range(i + 1, len(ts)):
                pairs[f"{ts[i]} + {ts[j]}"] += 1
    res["tool_pairs"] = pairs.most_common(8)

    # words that co-occur with a coding-agent signal, for the hand-read sample
    ctx = re.compile(r"[^.\n•;]*(" + "|".join(rx.pattern for rx in list(TOOLS.values())[:4]) +
                     r"|coding[\s-]+agents?|ai[\s-]+assisted[\s-]+(development|coding))[^.\n•;]*", I)
    random.seed(7)
    hits = [r for r in rows if either(r)]
    sample = []
    for r in random.sample(hits, min(150, len(hits))):
        m = ctx.search(r["text"])
        if m:
            sample.append({"scrape": r["scrape"], "job_id": r["job_id"], "company": r["company"],
                           "title": r["title"], "region": r["region"], "ai_type": r["ai_type"],
                           "url": r["url"], "sentence": " ".join(m.group(0).split())[:400]})
    res["sample_sentences"] = sample

    # practice-themed vocabulary inside signal postings vs. the rest (same corpus)
    THEMES = {
        "review / verify AI output": r"(review|verif|validat)\w*[^.\n]{0,60}(ai[\s-]generated|generated code|agent[\s-]generated|ai output)|"
                                     r"(ai[\s-]generated|generated code)[^.\n]{0,60}(review|verif|validat)",
        "testing (unit/integration/e2e/TDD)": r"\b(unit|integration|end[\s-]to[\s-]end|e2e|automated)\s+test|\btdd\b|test[\s-]driven",
        "CI/CD": r"\bci/?cd\b|continuous (integration|delivery|deployment)",
        "code review": r"\bcode reviews?\b",
        "system design / architecture": r"system design|architecture",
        "observability / monitoring": r"observability|monitoring|opentelemetry",
        "security": r"\bsecurity\b|secure coding",
        "Docker / Kubernetes": r"docker|kubernetes",
        "evals / evaluation": r"\bevals?\b|evaluation",
        "productivity framing": r"productivity|velocity|ship faster|accelerat",
    }
    res["themes"] = {}
    rest = [r for r in rows if not either(r)]
    for name, pat in THEMES.items():
        rx = re.compile(pat, I)
        res["themes"][name] = {"signal": share(hits, lambda r: bool(rx.search(r["text"])))["pct"],
                               "rest": share(rest, lambda r: bool(rx.search(r["text"])))["pct"]}

    # what is asked near the mention: themes within 300 characters of each match
    WINDOW = {
        "workflows / automation / pipelines": r"workflow|automat|pipeline",
        "review / verify / validate / quality": r"review|verif|validat|quality",
        "productivity / velocity / speed": r"productiv|velocity|faster|accelerat|speed|efficien",
        "testing": r"\btest",
        "security / guardrails / governance": r"secur|guardrail|governance|responsibl|complian",
        "specs / requirements / planning": r"\bspec|requirement|planning|\bplan\b",
        "teach / champion / enable others": r"champion|mentor|evangel|enablement|coach|best practices|adoption",
        "prompting": r"prompt",
        "multi-agent / orchestration / parallel": r"orchestrat|multi[\s-]agent|parallel|sub[\s-]?agent",
        "daily use": r"daily|day[\s-]to[\s-]day|every ?day|core part",
        "context / instruction files / rules": r"context|rules\b|agents\.md|claude\.md|instructions",
        "measure impact / metrics": r"metric|measur|telemetry|\broi\b",
        "MCP / skills / hooks / plugins": r"\bMCP\b|skill\.md|agent skills|\bhooks?\b|plugins?",
        "wording: required / proficient / hands-on": r"required|must\b|proficien|hands[\s-]on|demonstrated|proven",
        "wording: preferred / bonus / familiarity": r"nice[\s-]to[\s-]have|preferred|bonus|\bplus\b|familiarity",
    }
    sig_rx = list(TOOLS.values()) + list(CONCEPTS.values())[:4]
    wcount = collections.Counter()
    for r in hits:
        flat = " ".join(r["text"].split())
        win = " ".join(flat[max(0, m.start() - 300):m.end() + 300] for rx in sig_rx for m in rx.finditer(flat))
        for name, pat in WINDOW.items():
            if re.search(pat, win, I):
                wcount[name] += 1
    res["window_themes"] = {k: {"k": v, "pct": round(100 * v / len(hits), 1)} for k, v in wcount.most_common()}

    # seniority words in the title, signal postings vs the rest
    SEN = [("junior / entry / intern / associate", r"\b(junior|jr|entry|intern|graduate|associate|new grad)\b"),
           ("senior", r"\b(senior|sr)\b"),
           ("staff / principal / lead / architect / manager+", r"\b(staff|principal|lead|architect|manager|director|head|vp)\b")]

    def seniority(title):
        lab = "no level word"
        for name, pat in SEN:
            if re.search(pat, title or "", I):
                lab = name
        return lab
    res["seniority"] = {}
    for label, sub in (("signal", hits), ("rest", rest)):
        c = collections.Counter(seniority(r["title"]) for r in sub)
        res["seniority"][label] = {k: round(100 * v / len(sub), 1) for k, v in c.most_common()}

    # the "AI-native engineer" title cluster
    cl_rx = re.compile(r"ai[\s-]?(native|enabled|first|assisted|augmented)|ai enablement|"
                       r"developer (productivity|experience)|agentic (software|coding|engineer)", I)
    cluster = [r for r in rows if cl_rx.search(r["title"] or "")]
    res["title_cluster"] = {
        "n": len(cluster),
        "by_scrape": {s: share([r for r in rows if r["scrape"] == s], lambda r: bool(cl_rx.search(r["title"] or "")))
                      for s in scrapes},
        "labels": collections.Counter(
            re.sub(r"\s+", " ", cl_rx.search(r["title"]).group(0).lower().replace("-", " ")) for r in cluster
        ).most_common(),
        "germany": [{k: r[k] for k in ("scrape", "job_id", "company", "title", "location", "url")}
                    for r in cluster if r["region"] == "Germany"],
        "signal_share_inside_cluster": share(cluster, either),
    }

    # titles that themselves carry the vocabulary
    title_rx = re.compile(r"agentic (engineer|software|coding|developer)|ai[\s-]native|ai[\s-]assisted|"
                          r"coding agent|claude code|developer productivity|ai developer tool|"
                          r"forward deployed", I)
    res["title_hits"] = collections.Counter(
        (title_rx.search(r["title"] or "").group(0).lower()) for r in rows if title_rx.search(r["title"] or "")
    ).most_common()
    res["agentic_titles"] = sorted({f'{r["title"]} — {r["company"]} ({r["scrape"]})' for r in rows
                                    if re.search(r"agentic", r["title"] or "", I)})[:400]
    res["agentic_title_count"] = sum(1 for r in rows if re.search(r"agentic", r["title"] or "", I))

    germany = [r for r in rows if r["region"] == "Germany"]
    res["germany"] = {"n": len(germany), "either": share(germany, either), "named": share(germany, named),
                      "examples": [{k: r[k] for k in ("scrape", "job_id", "company", "title", "url", "tools", "concepts")}
                                   for r in germany if either(r)]}
    text = json.dumps(res, indent=1, ensure_ascii=False)
    if OUT:
        with open(OUT, "w") as fh:
            fh.write(text)
    slim = {k: v for k, v in res.items() if k not in ("sample_sentences", "agentic_titles", "germany", "by_scrape",
                                                      "tools_by_scrape", "by_region", "by_ai_type", "by_family", "tools", "concepts")}
    print(json.dumps(slim, indent=1, ensure_ascii=False))
    print("germany", res["germany"]["n"], res["germany"]["either"], res["germany"]["named"])


if __name__ == "__main__":
    main()
