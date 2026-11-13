"""Scope filter (Alexey t3349u-t3353u): Software Engineer, Software Developer,
Backend, Frontend, Full Stack, Engineering Manager. Matches a title or a URL slug.
German titles (Personio, StepStone-style): Softwareentwickler(in), Software-Ingenieur,
Teamleiter Softwareentwicklung; Backend-/Frontend-/Fullstack-Entwickler match via back/front/full stack."""
import re

ROLE_PATTERNS = [
    ("engineering_manager", r"\b(engineering[\s-]+manager|manager[\s,-]+(of[\s-]+)?(software[\s-]+)?engineering|software[\s-]+engineering[\s-]+manager|(team|abteilungs)?leit(er|erin|ung)[\s-]+(der[\s-]+)?software[\s-]*entwicklung)\b"),
    ("full_stack", r"\bfull[\s-]?stack\b"),
    ("backend", r"\bback[\s-]?end\b"),
    ("frontend", r"\bfront[\s-]?end\b"),
    ("software_developer", r"\bsoftware[\s-]+developer\b|\bsoftware[\s-]*entwickler(in)?\b"),
    ("software_engineer", r"\bsoftware[\s-]+(development[\s-]+)?engineer|\bsoftware[\s-]*ingenieur"),
]
_COMPILED = [(k, re.compile(p, re.I)) for k, p in ROLE_PATTERNS]


def role_of(text):
    """First matching role bucket for a title or slug, else None."""
    if not text:
        return None
    t = text.replace("_", " ")
    for k, rx in _COMPILED:
        if rx.search(t):
            return k
    return None


def slug_of(url):
    """https://builtin.com/job/<slug>/<id>  (older: /job/<category>/<slug>/<id>)."""
    parts = url.split("?")[0].rstrip("/").split("/")
    try:
        i = parts.index("job")
    except ValueError:
        return "", ""
    rest = parts[i + 1:]
    if len(rest) >= 2 and rest[-1].isdigit():
        return rest[-2], rest[-1]
    return "", ""


if __name__ == "__main__":
    for t in ["senior-software-engineer-fleet-security", "manager-software-engineering-platform-reports",
              "full-stack-developer", "backend-engineer-go", "front-end-developer", "data-engineer",
              "engineering-manager-payments", "software-developer-ii", "Staff Software Engineer, Backend"]:
        print(t, role_of(t))
