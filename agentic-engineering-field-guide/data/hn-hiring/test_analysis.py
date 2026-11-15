"""Meaningful offline integrity and classification checks for the fixed snapshot."""
import gzip
import hashlib
import json
import unittest
from pathlib import Path

import analyze


class SnapshotTests(unittest.TestCase):
    def test_exact_months_provenance_and_discovery(self):
        manifest = json.loads((analyze.ROOT / 'manifest.json').read_text())
        self.assertEqual([e['month'] for e in manifest['threads']], analyze.LOOKBACK + analyze.MONTHS)
        discovered = set()
        for entry in manifest['discovery']:
            payload = gzip.decompress((analyze.ROOT / 'raw' / entry['file']).read_bytes())
            self.assertEqual(hashlib.sha256(payload).hexdigest(), entry['sha256'])
            discovered.update(int(h['objectID']) for h in json.loads(payload)['hits'])
        for entry in manifest['threads']:
            tree = analyze.read_raw(entry['file'])
            self.assertEqual(tree['id'], entry['id'])
            self.assertEqual(tree['author'], 'whoishiring')
            self.assertEqual(tree['title'], entry['title'])
            self.assertTrue(tree['title'].startswith('Ask HN: Who is hiring? ('))
            self.assertEqual(tree['created_at'][:7], entry['month'])
            self.assertIn(tree['id'], discovered)
            self.assertEqual(entry['partial'], entry['month'] == '2026-11')

    def test_keyword_boundaries_and_html(self):
        patterns = json.loads((analyze.ROOT / 'patterns.json').read_text())
        text = analyze.plain('Company | NYC &amp; London<p>Claude, LLMs, agentic, Copilot, Cursor<br>C++ and C#')
        self.assertEqual(analyze.matches(text, patterns['ai_tools']), ['Claude', 'Copilot', 'Cursor', 'LLM', 'agentic'])
        self.assertIn('C++', analyze.matches(text, patterns['technologies']))
        self.assertIn('C#', analyze.matches(text, patterns['technologies']))
        self.assertEqual(analyze.matches('Tell us about your cursor movement', patterns['ai_tools']), [])
        self.assertEqual(analyze.matches('Tell us about yourself', patterns['locations']), [])
        self.assertEqual(analyze.matches('London | US remote', patterns['locations']), ['London', 'USA (country)'])

    def test_repost_keys(self):
        a = analyze.repost_keys('', 'Acme Inc | Senior Engineer | London | REMOTE | Full-time')
        b = analyze.repost_keys('', 'ACME | London | Senior Engineer | Onsite')
        self.assertEqual(a, b)
        c = analyze.repost_keys('', 'Acme | Senior Engineer | Berlin')
        self.assertNotEqual(a, c)
        u1 = analyze.repost_keys('<a href="https://www.acme.com/jobs/42?utm=1">x</a>', 'Acme | Foo')
        u2 = analyze.repost_keys('<a href="https://acme.com/jobs/42/">x</a>', 'Acme | Bar')
        self.assertTrue(set(u1) & set(u2))

    def test_counts_match_archive_and_post_audit(self):
        data = json.loads((analyze.ROOT / 'counts.json').read_text())
        posts = [json.loads(line) for line in (analyze.ROOT / 'posts.jsonl').read_text().splitlines()]
        self.assertEqual(len({p['id'] for p in posts}), len(posts))
        for entry, month in zip([e for e in json.loads((analyze.ROOT / 'manifest.json').read_text())['threads'] if not e.get('lookback')], data['months']):
            tree = analyze.read_raw(entry['file'])
            subset = [p for p in posts if p['month'] == month['month']]
            self.assertEqual({p['id'] for p in subset}, {p['id'] for p in tree['children']})
            self.assertEqual(len(subset), month['total_posts'])
            self.assertEqual(sum(p['duplicate'] for p in subset), month['reposts_removed'])
            self.assertEqual(len(subset) - month['reposts_removed'], month['unique_posts'])
            self.assertEqual(len(list(analyze.walk(tree['children']))), month['all_comments'])
            self.assertEqual(sum(bool(p.get('ai_tools')) for p in subset), month['any_ai_tool'])
            for row in data['mentions']:
                if row['month'] == month['month']:
                    self.assertEqual(sum(row['label'] in p.get(row['group'], []) for p in subset), row['posts'])


if __name__ == '__main__':
    unittest.main()
