"""Stage 1d: fetch each archived builtin listing page (city-filtered search
results) and extract the job links on it -> ../work/listing_links.jsonl

One row per (listing capture, job card): city, month, job_id, url, title,
company, card location, role bucket. Mirrors scrape_builtin_requests.py.
"""
import glob, json, re, sys
from pathlib import Path
from bs4 import BeautifulSoup
import fetch_cache
from roles import role_of

W = Path(__file__).resolve().parent.parent / "work"
OUT = W / "listing_links.jsonl"
DONE = W / "listing_done.txt"


def city_of(url):
    if re.search(r"city=London", url): return "london"
    if re.search(r"city=Berlin", url): return "berlin"
    if re.search(r"city=New(%20|\+|%2B)York", url): return "newyork"
    return None


def cards(html):
    s = BeautifulSoup(html, "html.parser")
    for a in s.select('h2 a[href*="/job/"]'):
        href = a.get("href", "")
        jid = href.rstrip("/").rsplit("/", 1)[-1]
        if not jid.isdigit():
            continue
        card = a.find_parent("div", id=lambda x: x and x.startswith("job-card-"))
        company = loc = ""
        if card:
            cl = card.find("a", href=lambda x: x and "/company/" in x)
            if cl:
                img = cl.find("img")
                company = (img.get("alt", "") if img else cl.get_text(strip=True)).replace(" Logo", "").strip()
            li = card.find("i", class_=lambda c: c and "fa-location-dot" in c)
            if li and li.parent:
                loc = li.parent.get_text(strip=True)
        url = href if href.startswith("http") else "https://builtin.com" + href
        yield {"job_id": jid, "url": url, "title": a.get_text(strip=True), "company": company, "card_location": loc}


def main():
    caps = []
    for f in sorted(glob.glob(str(W / "listing_cdx_pages" / "*.jsonl"))):
        caps += [json.loads(l) for l in open(f)]
    # one capture per (url, day) is plenty
    seen, todo = set(), []
    for c in sorted(caps, key=lambda c: c["timestamp"]):
        k = (c["original"], c["timestamp"][:8])
        if k not in seen and city_of(c["original"]):
            seen.add(k); todo.append(c)
    done = set(DONE.read_text().split()) if DONE.exists() else set()
    print("listing captures", len(todo), "done", len(done), flush=True)
    with open(OUT, "a") as out, open(DONE, "a") as dn:
        for i, c in enumerate(todo):
            k = c["timestamp"] + "|" + c["original"]
            if k in done:
                continue
            try:
                html = fetch_cache.fetch({"src": "wb", **c})
            except Exception as e:
                print("fail", k, str(e)[:100], flush=True); continue
            n = 0
            for card in cards(html):
                card.update(city=city_of(c["original"]), month=c["timestamp"][:6], listing_ts=c["timestamp"],
                            listing_url=c["original"], role=role_of(card["title"]), source="wayback_listing")
                out.write(json.dumps(card) + "\n"); n += 1
            out.flush(); dn.write(k + "\n"); dn.flush()
            if i % 25 == 0:
                print(i, len(todo), c["timestamp"][:6], city_of(c["original"]), n, flush=True)


if __name__ == "__main__":
    main()
