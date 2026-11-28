#!/usr/bin/env python3
"""Isolated HN snapshot collection and deterministic, non-LLM mention counts."""
import argparse
import csv
import gzip
import hashlib
import html
import io
import json
import re
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode, urlparse
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parent
API = 'https://hn.algolia.com/api/v1/'
AS_OF = '2026-11-15'
MONTHS = ['2025-12'] + [f'2026-{m:02d}' for m in range(1, 12)]
# Earlier threads fetched ONLY to detect reposts of jobs first published before the window.
LOOKBACK = [f'2024-{m:02d}' for m in range(12, 13)] + [f'2025-{m:02d}' for m in range(1, 12)]


def fetch(url):
    for attempt in range(5):
        try:
            with urlopen(url, timeout=90) as response:
                return response.read()
        except Exception:
            if attempt == 4:
                raise
            time.sleep(2 ** attempt)


def save_raw(name, payload):
    path = ROOT / 'raw' / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(gzip.compress(payload, mtime=0))
    return hashlib.sha256(payload).hexdigest()


def read_raw(name):
    return json.loads(gzip.decompress((ROOT / 'raw' / name).read_bytes()))


def collect():
    # Paginate discovery; do not use ranked search, or approximate title matching.
    params = dict(query='Ask HN: Who is hiring?', tags='story,author_whoishiring',
                  hitsPerPage=100, numericFilters='created_at_i<' + str(int(
                      datetime(2026, 11, 16, tzinfo=timezone.utc).timestamp())))
    page, hits, discovery = 0, [], []
    while True:
        url = API + 'search_by_date?' + urlencode(dict(params, page=page))
        payload = fetch(url)
        result = json.loads(payload)
        filename = f'discovery-{page}.json.gz'
        discovery.append(dict(url=url, file=filename, sha256=save_raw(filename, payload)))
        hits.extend(result['hits'])
        if page + 1 >= result['nbPages'] or any(h['created_at'][:7] < LOOKBACK[0] for h in result['hits']):
            break
        page += 1
    selected = {}
    for hit in hits:
        month = hit['created_at'][:7]
        if month in LOOKBACK + MONTHS and re.fullmatch(r'Ask HN: Who is hiring\? \([A-Za-z]+ \d{4}\)', hit['title'] or ''):
            assert month not in selected, f'Duplicate thread for {month}'
            selected[month] = hit
    assert sorted(selected) == LOOKBACK + MONTHS, 'Missing requested monthly thread'
    manifest = dict(as_of=AS_OF, fetched_at=datetime.now(timezone.utc).isoformat(),
                    source='HN Algolia only', discovery=discovery, threads=[])
    for month in LOOKBACK + MONTHS:
        hit = selected[month]
        url = API + 'items/' + hit['objectID']
        payload = fetch(url)
        tree = json.loads(payload)
        assert tree['id'] == int(hit['objectID']) and tree['author'] == 'whoishiring'
        filename = month + '.json.gz'
        manifest['threads'].append(dict(month=month, id=tree['id'], title=tree['title'],
            url=url, hn_url=f"https://news.ycombinator.com/item?id={tree['id']}",
            file=filename, sha256=save_raw(filename, payload), partial=month == MONTHS[-1], lookback=month in LOOKBACK))
        print(month, len(tree['children']), 'top-level posts', flush=True)
    write_json('manifest.json', manifest)


def write_json(name, value):
    (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def plain(value):
    # Keep paragraph boundaries for header-only location matching; ignore link targets.
    value = re.sub(r'<(?:p|br)\s*/?>', '\n', value or '', flags=re.I)
    return html.unescape(re.sub(r'<[^>]+>', ' ', value)).strip()


NOISE = re.compile(r'\b(?:remote|onsite|on site|hybrid|full ?time|part ?time|contract|intern(?:ship)?|visa|relocation|sponsorship|hiring)\b')
SUFFIX = re.compile(r'\b(?:inc|llc|ltd|gmbh|corp|co|plc|ag|sa)\b')


def norm(value):
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9+#]+', ' ', value.lower())).strip()


def repost_keys(raw_html, text):
    """Dedup keys: (company, header fields) and (company, deep job URL). Original publication wins."""
    header = next((line.strip() for line in text.splitlines() if line.strip()), '')
    parts = [p for p in re.split(r'\s*\|\s*', header) if p.strip()]
    keys = []
    if len(parts) >= 2:
        company = norm(SUFFIX.sub(' ', norm(parts[0])))
        rest = sorted({f for f in (norm(NOISE.sub(' ', norm(p))) for p in parts[1:]) if f})
        if company and rest:
            keys.append(('hdr', company, tuple(rest)))
        if company:
            for href in re.findall(r'href="([^"]+)"', raw_html or ''):
                u = urlparse(html.unescape(href))
                path = u.path.rstrip('/')
                if u.netloc and 'ycombinator.com' not in u.netloc and path.count('/') >= 1 and len(path) > 1:
                    keys.append(('url', company, u.netloc.lower().removeprefix('www.') + path.lower()))
    return keys


def matches(text, patterns):
    return sorted(k for k, pattern in patterns.items() if re.search(pattern, text))


def walk(nodes):
    for node in nodes:
        yield node
        yield from walk(node.get('children', []))


def write_csv(name, rows, fields):
    with (ROOT / name).open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def analyze():
    manifest = json.loads((ROOT / 'manifest.json').read_text())
    patterns = json.loads((ROOT / 'patterns.json').read_text())
    months, all_posts, mentions = [], [], []
    seen = set()
    first_seen = {}
    for entry in manifest['threads']:
        lookback = entry.get('lookback', False)
        payload = gzip.decompress((ROOT / 'raw' / entry['file']).read_bytes())
        assert hashlib.sha256(payload).hexdigest() == entry['sha256']
        tree = json.loads(payload)
        nodes = list(walk(tree['children']))
        assert all(n['id'] not in seen for n in nodes)
        seen.update(n['id'] for n in nodes)
        assert len({n['id'] for n in nodes}) == len(nodes)
        for parent in [tree] + nodes:
            assert all(child['parent_id'] == parent['id'] for child in parent.get('children', []))
        if lookback:
            for node in sorted(tree['children'], key=lambda n: (n['created_at_i'], n['id'])):
                for k in repost_keys(node['text'], plain(node['text'])):
                    first_seen.setdefault(k, (node['id'], entry['month']))
            continue
        counts = dict(month=entry['month'], thread_id=tree['id'], partial=entry['partial'],
                      total_posts=len(tree['children']), all_comments=len(nodes),
                      replies=len(nodes) - len(tree['children']), text_posts=0, empty_posts=0, reposts_removed=0, unique_posts=0,
                      remote=0, onsite=0, hybrid=0, remote_only=0, onsite_only=0, both=0, unspecified=0)
        groups = {group: Counter() for group in patterns}
        for node in sorted(tree['children'], key=lambda n: (n['created_at_i'], n['id'])):
            assert node['parent_id'] == tree['id']
            text = plain(node['text'])
            available = bool(text and text not in ('[deleted]', '[dead]'))
            counts['text_posts' if available else 'empty_posts'] += 1
            # Repost rule: a vacancy counts once, in the month of its original publication.
            keys = repost_keys(node['text'], text) if available else []
            original = next((first_seen[k] for k in keys if k in first_seen), None)
            for k in keys:
                first_seen.setdefault(k, (node['id'], entry['month']))
            duplicate = original is not None
            if duplicate:
                counts['reposts_removed'] += 1
                all_posts.append(dict(month=entry['month'], thread_id=tree['id'], id=node['id'],
                    url=f"https://news.ycombinator.com/item?id={node['id']}", text_available=True,
                    duplicate=True, original_id=original[0], original_month=original[1]))
                continue
            counts['unique_posts'] += 1
            # These are keyword mentions, not a semantic work-arrangement classifier.
            arrangement = re.sub(r'(?i)\b(?:no|not|non)[ -]+remote\b|\bremote\s*:\s*no\b', '', text)
            arrangement = re.sub(r'(?i)\b(?:no|not|non)[ -]+on[ -]?site\b|\bon[ -]?site\s*:\s*no\b', '', arrangement)
            remote = available and bool(re.search(r'(?i)\bremote\b', arrangement))
            onsite = available and bool(re.search(r'(?i)\bon[ -]?site\b|\bin[ -]person\b|\bin[ -]office\b', arrangement))
            hybrid = available and bool(re.search(r'(?i)\bhybrid\b', text))
            for key, value in [('remote', remote), ('onsite', onsite), ('hybrid', hybrid)]:
                counts[key] += int(value)
            counts['both' if remote and onsite else 'remote_only' if remote else 'onsite_only' if onsite else 'unspecified'] += 1
            # First nonempty paragraph/line, capped at 500 characters: hiring header proxy.
            header = next((line.strip() for line in text.splitlines() if line.strip()), '')[:500]
            found = {group: matches(header if group == 'locations' else text, pats) if available else []
                     for group, pats in patterns.items()}
            for group, labels in found.items():
                groups[group].update(labels)
            all_posts.append(dict(month=entry['month'], thread_id=tree['id'], id=node['id'],
                url=f"https://news.ycombinator.com/item?id={node['id']}", text_available=available,
                duplicate=False, remote=remote, onsite=onsite, hybrid=hybrid, **found))
        assert counts['total_posts'] == counts['text_posts'] + counts['empty_posts']
        counts['unique_text_posts'] = counts['text_posts'] - counts['reposts_removed']
        assert counts['total_posts'] == counts['unique_posts'] + counts['reposts_removed']
        assert counts['unique_posts'] == sum(counts[k] for k in ('remote_only', 'onsite_only', 'both', 'unspecified'))
        for group, pats in patterns.items():
            for label in sorted(pats):
                mentions.append(dict(month=entry['month'], group=group, label=label,
                    posts=groups[group][label], text_posts=counts['unique_text_posts'],
                    percent=round(100 * groups[group][label] / max(1, counts['unique_text_posts']), 3)))
        counts['any_ai_tool'] = sum(bool(p.get('ai_tools')) for p in all_posts if p['month'] == entry['month'])
        months.append(counts)
    write_csv('counts_monthly.csv', months, list(months[0]))
    write_csv('counts_mentions.csv', mentions, ['month', 'group', 'label', 'posts', 'text_posts', 'percent'])
    write_json('counts.json', dict(months=months, mentions=mentions))
    with (ROOT / 'posts.jsonl').open('w') as stream:
        for post in all_posts:
            stream.write(json.dumps(post, ensure_ascii=False, sort_keys=True) + '\n')
    return months, mentions


def render(months, mentions):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'figure.dpi': 150, 'font.size': 9})
    labels = [m['month'] + ('*' if m['partial'] else '') for m in months]
    fig, axes = plt.subplots(2, 1, figsize=(11, 7), constrained_layout=True)
    axes[0].bar(labels, [m['unique_posts'] for m in months], color=['#377eb8'] * 11 + ['#a6cee3'])
    axes[0].set(title='HN Who is hiring? — unique vacancies (reposts removed)', ylabel='Posts')
    for key in ['remote', 'onsite', 'hybrid']:
        axes[1].plot(labels, [100 * m[key] / max(1, m['unique_text_posts']) for m in months], marker='o', label=key)
    axes[1].set(title='Explicit work-arrangement mentions (overlap allowed)', ylabel='% of unique text posts')
    axes[1].legend()
    for axis in axes:
        axis.tick_params(axis='x', rotation=45)
        axis.grid(axis='y', alpha=.2)
    fig.suptitle('December 2025–November 2026 | *November partial, snapshot 2026-11-15')
    fig.savefig(ROOT / 'monthly-trends.png')
    plt.close(fig)
    fig, axes = plt.subplots(2, 2, figsize=(13, 8), constrained_layout=True)
    for axis, group in zip(axes.flat, ['ai_tools', 'technologies', 'locations', 'roles']):
        totals = Counter()
        for row in mentions:
            if row['group'] == group:
                totals[row['label']] += row['posts']
        for label, _ in totals.most_common(6):
            axis.plot(labels, [next(r['percent'] for r in mentions if r['month'] == m['month'] and r['group'] == group and r['label'] == label) for m in months], marker='.', label=label)
        axis.set(title=group.replace('_', ' ').title() + (' (header only)' if group == 'locations' else ''), ylabel='% of unique text posts')
        axis.tick_params(axis='x', rotation=60)
        axis.legend(fontsize=7)
        axis.grid(alpha=.2)
    fig.suptitle('HN keyword mentions | fixed dictionaries, multi-label | *November partial')
    fig.savefig(ROOT / 'mention-trends.png')
    plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--collect', action='store_true', help='Refresh Algolia snapshot (network)')
    parser.add_argument('--charts', action='store_true', help='Render PNGs (requires requirements.txt)')
    args = parser.parse_args()
    if args.collect:
        collect()
    months, mentions = analyze()
    if args.charts:
        render(months, mentions)
    print(f"Validated {len(months)} months, {sum(m['unique_posts'] for m in months)} unique posts, {sum(m['reposts_removed'] for m in months)} reposts removed")
