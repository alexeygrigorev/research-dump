#!/usr/bin/env python3
"""Offline integrity checks, counting invariants and small semantic regression cases."""
import argparse, collections, gzip, json, tempfile, contextlib, io
import report_jobs
from pathlib import Path
from jsonschema import Draft202012Validator
from extract_jobs import MODEL, ROOT, validate
from report_jobs import WINDOWS, dedup, stats

def fixtures():
    def row(i,date,title='Engineer',company='ACME',loc=None,dataset='historical',url=None):
        return dict(vacancy_id='builtin:'+i,source='builtin',job_id=i,posted_date=date,title=title,company=company,locations=loc or ['Berlin, DEU'],url=url or 'https://builtin.com/job/x/'+i,dataset=dataset)
    a=row('1','2025-11-03');b=row('2','2026-03-01',title='ENGINEER!',company='Acme');c=row('2','2026-10-01',title='Backend Engineer',dataset='live')
    canonical,audit=dedup([c,b,a])
    assert len(canonical)==1 and canonical[0]['original_posted_date']=='2025-11-03'
    assert sum(r['is_repost'] for r in audit)==2
    canonical,_=dedup([a,row('3','2026-03-01',loc=['London, GBR']),row('4','')])
    assert len(canonical)==2  # undated observation merges with same employer/title/location
    canonical,_=dedup([a,row('5','',title='QA',url='https://www.builtin.com/job/x/1/?utm_source=x')])
    assert len(canonical)==1 and canonical[0]['original_posted_date']=='2025-11-03'
    canonical,_=dedup([row('9','')]);assert canonical[0]['original_posted_date'] is None
    assert not any(lo <= (canonical[0]['original_posted_date'] or '') <= hi for lo,hi in WINDOWS.values())


def report_smoke():
    """A repost must stay in its original window; unknown fields preserve denominators."""
    original_root=report_jobs.ROOT
    try:
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);report_jobs.ROOT=root
            records=[]
            for i,posted in enumerate(['2025-11-15','2026-04-01','2026-10-15']):
                records.append(dict(dataset='historical',vacancy_id=f'builtin:{i}',job_id=str(i),source='builtin',url=f'https://builtin.com/job/test/{i}',title='Engineer',company=f'Employer {i}',locations=['Berlin'],posted_date=posted,status='ok',tags=dict(qa_sdet=False,intern=False,staff=False,non_english=False),extracted=dict(role='software_engineer',seniority='unknown',skills=[],ai_mentions=[],experience=dict(min_years=None,max_years=None,evidence=None),workplace=dict(mode='unknown',evidence=None),salary=dict(min=None,max=None,currency=None,period='unknown',evidence=None),language='en')))
            repost=dict(records[0],dataset='live',posted_date='2026-10-16')
            for dataset,items in [('historical',records),('live',[repost])]:
                p=root/f'data/{dataset}/extracted/vacancies.jsonl.gz';p.parent.mkdir(parents=True)
                with gzip.open(p,'wt') as f:
                    for r in items:f.write(json.dumps(r)+'\n')
            with contextlib.redirect_stdout(io.StringIO()):report_jobs.main()
            summaries=json.loads((root/'reports/window-summary.json').read_text())
            assert all(s['n']==1 and s['extracted_n']==1 and s['ai_any_n']==0 for s in summaries.values())
            assert summaries['P1']['reposts_removed_original_window']==1
            assert summaries['P3']['repost_observations_in_window']==1
            assert (root/'reports/monthly-by-role.csv').stat().st_size>100
            for name in ['P1','P2','P3','trends']:assert (root/f'reports/charts/{name}.png').stat().st_size>100
    finally:report_jobs.ROOT=original_root


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--pilot-only',action='store_true');args=parser.parse_args()
    fixtures();report_smoke();rows=[]
    schema=Draft202012Validator(json.loads((ROOT/'data/historical/extracted/schema.json').read_text()))
    pilot=json.loads((ROOT/'reports/pilot.json').read_text())
    assert len(pilot)==100 and len({r['text_hash'] for r in pilot})==100
    for r in pilot:
        assert r['status']=='ok' and r['model']==MODEL and r['prompt_version']=='jobs-v2'
        schema.validate(r['extracted']);validate(r['extracted'],r['text'])
    qa=json.loads((ROOT/'reports/pilot-qa.json').read_text());assert len(qa['rows'])==20
    assert all(x['manually_reviewed'] for x in qa['rows'])
    if args.pilot_only:
        print('100 pilot outputs and 20-row manual review record validated; dedup regressions passed');return
    for dataset,expected in [('historical',11292),('live',6215)]:
        with gzip.open(ROOT/f'data/{dataset}/extracted/vacancies.jsonl.gz','rt') as f:r=[json.loads(x) for x in f]
        assert len(r)==expected,(dataset,len(r));assert len({x['vacancy_id'] for x in r})==expected
        for x in r:
            assert x['dataset']==dataset
            assert x['status'] in ['ok','missing_description'], x.get('error')
            assert set(x['tags'])=={'qa_sdet','intern','staff','non_english'}
            if x['status']=='ok':
                schema.validate(x['extracted'])
                assert x['model']==MODEL and x['prompt_version']=='jobs-v2'
                assert x['request_id'] and x['usage_attempts']
                assert set(x['extracted'])=={'role','seniority','skills','ai_mentions','experience','workplace','salary','language'}
        rows+=r
    canonical,audit=dedup(rows)
    with gzip.open(ROOT/'reports/dedup-audit.jsonl.gz','rt') as f:stored=[json.loads(x) for x in f]
    assert stored==audit
    summaries=json.loads((ROOT/'reports/window-summary.json').read_text())
    assigned=set()
    for w,(lo,hi) in WINDOWS.items():
        subset=[r for r in canonical if r['original_posted_date'] and lo<=r['original_posted_date']<=hi]
        s=stats(subset)
        for k,v in s.items():assert v==summaries[w][k],(w,k)
        for r in subset:
            identity=(r['dataset'],r['vacancy_id']);assert identity not in assigned;assigned.add(identity)
        for p in [ROOT/f'reports/{w}.md',ROOT/f'reports/charts/{w}.png']:assert p.stat().st_size>100
    assert (ROOT/'reports/TRENDS.md').stat().st_size>100
    print(json.dumps({'validated_rows':len(rows),'unique_vacancies':len(canonical),'reposts_removed':len(rows)-len(canonical),'counting_regressions':'passed'}))

if __name__=='__main__':main()
