#!/usr/bin/env python3
"""Publication-date windows after transitive ID/URL/employer-title-location dedup."""
import collections as C, datetime as dt, gzip, json, re, sys, unicodedata, csv, statistics
from pathlib import Path
from urllib.parse import urlsplit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'data/historical/scripts'))
import roles as title_roles
WINDOWS={'P1':('2025-11-01','2025-12-31'),'P2':('2026-03-01','2026-05-31'),'P3':('2026-10-01','2026-11-30')}
SIX_ROLES=['software_engineer','backend','full_stack','frontend','engineering_manager','software_developer']
SIX_ROLE_LABELS={'software_engineer':'Software Engineer','backend':'Backend','full_stack':'Full Stack','frontend':'Frontend','engineering_manager':'Engineering Manager','software_developer':'Software Developer','other':'Other / unmatched'}
TOOL_GROUPS=[
    ('Claude Code', lambda names: 'claude code' in names),
    ('Cursor', lambda names: 'cursor' in names),
    ('GitHub Copilot / Copilot', lambda names: any(n in ('github copilot','copilot') for n in names)),
    ('Claude (any)', lambda names: any(n=='claude' or 'claude ' in n for n in names)),
    ('Agentic / AI agents', lambda names: any('agentic' in n or 'agent' in n for n in names)),
    ('AI coding / assisted dev', lambda names: any('ai assisted' in n or 'ai coding' in n or 'ai tools' in n or 'ai dev' in n for n in names)),
    ('LLM / LLMs', lambda names: any(n in ('llm','llms','large language model','large language models') for n in names)),
    ('Codex / Windsurf / Devin', lambda names: any(k in n for n in names for k in ('codex','windsurf','devin'))),
    ('MCP', lambda names: any(n=='mcp' or 'model context protocol' in n for n in names)),
]

def six_role(r):
    return title_roles.role_of(r.get('title','')) or 'other'

def live_city(r):
    locs=' '.join(r.get('locations') or []).lower()
    reg=str(r.get('region') or '').upper()
    if 'london' in locs or reg=='UK':return 'London'
    if 'berlin' in locs or reg=='DE':return 'Berlin'
    if 'new york' in locs or 'nyc' in locs or reg=='US':return 'New York'
    return 'Other'

def tool_group_counts(rows,dev_only=False):
    valid=[r for r in rows if r['status']=='ok']
    out={}
    for label,pred in TOOL_GROUPS:
        c=0
        for r in valid:
            names=set(norm(x['name']) for x in r['extracted']['ai_mentions'] if (not dev_only or x['context']=='developer_tool'))
            if pred(names):c+=1
        out[label]=c
    return out

def norm(s):return re.sub(r'[^\w]+',' ',unicodedata.normalize('NFKC',s).casefold()).strip()
def date(r):
    try:return dt.date.fromisoformat(str(r.get('posted_date',''))[:10]).isoformat()
    except ValueError:return None

def dedup(rows):
    parent=list(range(len(rows)));seen={}
    def root(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    for i,r in enumerate(rows):
        keys=[]
        if r.get('job_id'):keys.append(('id',r['source'].lower(),str(r['job_id'])))
        if r.get('url'):
            u=urlsplit(r['url']);keys.append(('url',u.netloc.lower().removeprefix('www.'),u.path.rstrip('/')))
        loc='|'.join(sorted(set(norm(x) for x in r.get('locations',[]) if x)))
        if r.get('company') and r.get('title') and loc:keys.append(('ctl',norm(r['company']),norm(r['title']),loc))
        for k in keys:
            if k in seen:parent[root(i)]=root(seen[k])
            else:seen[k]=i
    groups=C.defaultdict(list)
    for i,r in enumerate(rows):groups[root(i)].append(r)
    canonical=[];audit=[]
    for group in groups.values():
        ordered=sorted(group,key=lambda r:(date(r) or '9999',r['dataset']!='historical',r['vacancy_id']))
        first=ordered[0];original=date(first)
        # Prefer an extracted version of the earliest row; later descriptions are never substituted into earlier windows.
        item=dict(first,original_posted_date=original,repost_count=len(group)-1)
        canonical.append(item)
        for r in group:audit.append({'dataset':r['dataset'],'vacancy_id':r['vacancy_id'],'posted_date':date(r),'canonical_id':first['vacancy_id'],'canonical_dataset':first['dataset'],'original_posted_date':original,'is_repost':r is not first})
    return canonical,audit

def pct(n,d):return round(n/d*100,2) if d else 0

def stats(rows):
    n=len(rows);valid=[r for r in rows if r['status']=='ok'];roles=C.Counter();skills=C.Counter();required_skills=C.Counter();ai=C.Counter();sen=C.Counter();work=C.Counter();context=C.Counter()
    for r in valid:
        d=r['extracted'];roles[d['role']]+=1;sen[r.get('seniority_title') if r.get('seniority_title','unknown')!='unknown' else d['seniority']]+=1;work[d['workplace']['mode']]+=1
        skills.update(set(norm(x['name']) for x in d['skills']))
        required_skills.update(set(norm(x['name']) for x in d['skills'] if x['requirement'] in ['required','preferred']))
        ai.update(set(norm(x['name']) for x in d['ai_mentions']))
        context.update(set(x['context'] for x in d['ai_mentions']))
    return {'n':n,'extracted_n':len(valid),'missing_n':n-len(valid),'sources':dict(C.Counter(r['source'] for r in rows)),'datasets':dict(C.Counter(r['dataset'] for r in rows)),'roles':dict(roles),'skills':dict(skills.most_common()),'required_or_preferred_skills':dict(required_skills.most_common()),'ai':dict(ai),'ai_any_n':sum(bool(r['extracted']['ai_mentions']) for r in valid),'ai_developer_tool_n':context['developer_tool'],'seniority':dict(sen),'workplace':dict(work),'experience_known_n':sum(r['extracted']['experience']['min_years'] is not None for r in valid),'salary_known_n':sum(r['extracted']['salary']['min'] is not None or r['extracted']['salary']['max'] is not None for r in valid),'qa_sdet_n':sum(r['tags']['qa_sdet'] for r in rows),'intern_n':sum(r['tags']['intern'] for r in rows),'staff_n':sum(r['tags']['staff'] for r in rows),'non_english_n':sum(r['tags']['non_english'] for r in rows)}

def table(counter,denom,limit=20):
    return '| field | n | % of extracted vacancies |\n|---|---:|---:|\n'+'\n'.join(f'| {k} | {v} | {pct(v,denom):.2f}% |' for k,v in sorted(counter.items(),key=lambda p:(-p[1],p[0]))[:limit])+'\n'

def main():
    rows=[]
    for dataset in ['historical','live']:
        with gzip.open(ROOT/f'data/{dataset}/extracted/vacancies.jsonl.gz','rt') as f:rows += [json.loads(x) for x in f]
    canonical,audit=dedup(rows);dest=ROOT/'reports';dest.mkdir(exist_ok=True);charts=dest/'charts';charts.mkdir(exist_ok=True)
    with gzip.open(dest/'dedup-audit.jsonl.gz','wt') as f:
        for a in audit:f.write(json.dumps(a)+'\n')
    allstats={}
    for w,(lo,hi) in WINDOWS.items():
        subset=[r for r in canonical if r['original_posted_date'] and lo<=r['original_posted_date']<=hi]
        s=stats(subset);allstats[w]=s
        s['reposts_removed_original_window']=sum(a['is_repost'] for a in audit if a['original_posted_date'] and lo<=a['original_posted_date']<=hi)
        s['repost_observations_in_window']=sum(a['is_repost'] for a in audit if a['posted_date'] and lo<=a['posted_date']<=hi)
        s['crawl_batch_included']=sum(r.get('month_basis')=='crawl_batch' for r in subset)
        n=s['extracted_n'];den=max(n,1)
        fig,ax=plt.subplots(figsize=(9,5));top=list(s['skills'].items())[:12]
        ax.barh([k for k,v in top][::-1],[100*v/den for k,v in top][::-1],color='#35689c');ax.set_xlabel('% of extracted vacancies');ax.set_title(f'{w}: explicit skill mentions (n={n:,})');fig.tight_layout();fig.savefig(charts/f'{w}.png',dpi=160);plt.close(fig)
        text=f'''# {w}: original publication {lo} to {hi}

Unique vacancies: **{s['n']:,}**; successful LLM extractions: **{n:,}**; missing description/extraction: {s['missing_n']}.
Repost observations removed for jobs originally published in this window: **{s['reposts_removed_original_window']:,}**.
Repost observations with their own listed posted date in this window, excluded from new vacancy counts: **{s['repost_observations_in_window']:,}**.
Sources: {json.dumps(s['sources'])}; input cohorts: {json.dumps(s['datasets'])}.

![Explicit skill mentions](charts/{w}.png)

## Requirements and skills

{table(s['skills'],n)}
## AI mentions

Any explicit AI mention: {s['ai_any_n']} / {n} ({pct(s['ai_any_n'],n)}%); developer tooling: {s['ai_developer_tool_n']} / {n} ({pct(s['ai_developer_tool_n'],n)}%). AI product work is counted separately from developer tools in the extracted data.

{table(s['ai'],n)}
## Roles and seniority

{table(s['roles'],n)}
{table(s['seniority'],n)}
QA/SDET tagged: {s['qa_sdet_n']}; interns: {s['intern_n']}; staff: {s['staff_n']}; non-English: {s['non_english_n']}.

## Experience, workplace and pay

Explicit minimum experience: {s['experience_known_n']} / {n}; explicit salary: {s['salary_known_n']} / {n}. Missing means unspecified, never zero. Salary amounts/currency/period remain in individual rows; no cross-currency average.

{table(s['workplace'],n)}
## Counting and caveats

Jobs are joined transitively by same source job ID, normalized URL (without query/fragment/trailing slash), or Unicode/case/punctuation-normalized company + title + sorted unique location list. Each entity counts once at the earliest known posted_date across both inputs. This proxy can merge distinct openings with identical titles/locations; employer aliases are not guessed. Different location sets stay distinct unless ID/URL joins them. Later repost descriptions do not replace earlier requirements.

Capture dates, crawl months and snapshot dates are never used as publication dates. {s['crawl_batch_included']} crawl_batch rows are included because they have a real posted_date in this window. Undated entities are excluded. P3 combines historical October with the November 14 and November 25 live snapshots (London, Berlin, New York). Live snapshots contain older active jobs, assigned to their original publication windows. Archives and live survivor snapshots have different selection biases. These are descriptive sample shares, not market vacancy volumes or causal trends. See [TRENDS](TRENDS.md) for defaults, audit and source sensitivity.
'''
        (dest/f'{w}.md').write_text(text)
    # Monthly breakdowns by role: denominators stay explicit for every metric.
    monthly=[]
    groups=C.defaultdict(list)
    for r in canonical:
        if not r['original_posted_date']:continue
        month=r['original_posted_date'][:7]
        if not '2025-11'<=month<='2026-11':continue
        role=r.get('extracted',{}).get('role','unknown')
        groups[(month,role)].append(r);groups[(month,'ALL')].append(r)
    for (month,role),group in sorted(groups.items()):
        st=stats(group);den=st['extracted_n']
        for metric in ['skills','required_or_preferred_skills','ai','seniority','workplace']:
            for value,n in st[metric].items():monthly.append(dict(month=month,role=role,metric=metric,value=value,n=n,denominator=den,share_pct=pct(n,den),vacancy_n=st['n']))
        for metric in ['ai_any_n','ai_developer_tool_n','experience_known_n','salary_known_n']:
            n=st[metric];monthly.append(dict(month=month,role=role,metric=metric,value='any',n=n,denominator=den,share_pct=pct(n,den),vacancy_n=st['n']))
    with (dest/'monthly-by-role.csv').open('w') as f:
        writer=csv.DictWriter(f,fieldnames=['month','role','metric','value','n','denominator','share_pct','vacancy_n']);writer.writeheader();writer.writerows(monthly)
    six_role_windows={w:{} for w in WINDOWS}
    tool_windows={w:{} for w in WINDOWS}
    tool_dev_windows={w:{} for w in WINDOWS}
    for w,(lo,hi) in WINDOWS.items():
        subset=[r for r in canonical if r['original_posted_date'] and lo<=r['original_posted_date']<=hi]
        tool_windows[w]=tool_group_counts(subset,dev_only=False)
        tool_dev_windows[w]=tool_group_counts(subset,dev_only=True)
        text='\n## Six developer roles (title-based)\n\n| role | vacancies | extracted | any AI n | any AI % | developer tools n | developer tools % |\n|---|---:|---:|---:|---:|---:|---:|\n'
        for rk in SIX_ROLES+['other']:
            rsub=[r for r in subset if six_role(r)==rk]
            if not rsub and rk=='other':continue
            st=stats(rsub);d=st['extracted_n']
            six_role_windows[w][rk]={'n':st['n'],'extracted_n':d,'ai_any_n':st['ai_any_n'],'ai_any_pct':pct(st['ai_any_n'],d),'ai_dev_n':st['ai_developer_tool_n'],'ai_dev_pct':pct(st['ai_developer_tool_n'],d)}
            text+=f"| {SIX_ROLE_LABELS[rk]} | {st['n']} | {d} | {st['ai_any_n']} | {pct(st['ai_any_n'],d):.2f}% | {st['ai_developer_tool_n']} | {pct(st['ai_developer_tool_n'],d):.2f}% |\n"
        text+='\n## Role breakdown (LLM-extracted)\n\n| role | vacancies | extracted | any AI % | developer tools % | experience disclosed % | salary disclosed % |\n|---|---:|---:|---:|---:|---:|---:|\n'
        for role in sorted(set(r.get('extracted',{}).get('role','unknown') for r in subset)):
            st=stats([r for r in subset if r.get('extracted',{}).get('role','unknown')==role]);d=st['extracted_n']
            text+=f"| {role} | {st['n']} | {d} | {pct(st['ai_any_n'],d)} | {pct(st['ai_developer_tool_n'],d)} | {pct(st['experience_known_n'],d)} | {pct(st['salary_known_n'],d)} |\n"
        text+='\n[Monthly requirements/AI/seniority/workplace by role](monthly-by-role.csv) includes explicit numerators and denominators; small cells are unstable.\n'
        pay=C.defaultdict(list);years=[]
        for r in subset:
            if r['status']!='ok':continue
            d=r['extracted'];v=d['experience']['min_years']
            if v is not None:years.append(v)
            sal=d['salary']
            if sal['min'] is not None and sal['currency'] and sal['period']!='unknown':pay[(sal['currency'],sal['period'])].append(sal['min'])
        text+=f"\nMedian explicit minimum experience: {statistics.median(years) if years else 'unknown'} years (n={len(years)} disclosures). This is conditional on disclosure.\n"
        text+='\n| currency | period | disclosed minimum-pay n | median lower bound |\n|---|---|---:|---:|\n'
        for (currency,period),values in sorted(pay.items()):text+=f'| {currency} | {period} | {len(values)} | {statistics.median(values):,.2f} |\n'
        with (dest/f'{w}.md').open('a') as f:f.write(text)
    (dest/'window-summary.json').write_text(json.dumps(allstats,indent=2))
    # Chart 1: Headline P1/P2/P3 AI shares
    fig,axes=plt.subplots(1,2,figsize=(10,4))
    for ax,key,title in zip(axes,['ai_any_n','ai_developer_tool_n'],['Any AI mention','AI developer tool mention']):
        vals=[pct(s[key],s['extracted_n']) for s in allstats.values()]
        bars=ax.bar(list(allstats),vals,color=['#6b8eaf','#467b74','#ae7851'])
        for b,v in zip(bars,vals):ax.text(b.get_x()+b.get_width()/2,v+0.8,f'{v:.1f}%',ha='center',va='bottom',fontsize=9)
        ax.set_title(title);ax.set_ylabel('% of extracted vacancies');ax.set_ylim(0,max(vals+[10])*1.15)
    fig.tight_layout();fig.savefig(charts/'trends.png',dpi=160);plt.close(fig)
    # Chart 2: Six developer roles (developer-tool AI % across P1/P2/P3)
    fig,ax=plt.subplots(figsize=(10,5))
    x=list(range(len(SIX_ROLES)));width=0.25
    for idx,(w,col) in enumerate(zip(['P1','P2','P3'],['#6b8eaf','#467b74','#ae7851'])):
        vals=[six_role_windows[w].get(rk,{}).get('ai_dev_pct',0) for rk in SIX_ROLES]
        ax.bar([i+(idx-1)*width for i in x],vals,width,label=w,color=col)
    ax.set_xticks(x);ax.set_xticklabels([SIX_ROLE_LABELS[rk] for rk in SIX_ROLES],rotation=20,ha='right')
    ax.set_ylabel('% mentioning AI developer tools');ax.set_title('AI developer-tool mentions by developer role (P1 → P2 → P3)');ax.legend()
    fig.tight_layout();fig.savefig(charts/'ai-by-role.png',dpi=160);plt.close(fig)
    # Chart 3: Named AI developer tools & agentic concepts across P1/P2/P3
    fig,ax=plt.subplots(figsize=(10,5.5))
    labels=[lbl for lbl,_ in TOOL_GROUPS]
    y=list(range(len(labels)));h=0.26
    for idx,(w,col) in enumerate(zip(['P1','P2','P3'],['#6b8eaf','#467b74','#ae7851'])):
        den=max(allstats[w]['extracted_n'],1)
        vals=[pct(tool_windows[w][lbl],den) for lbl in labels]
        ax.barh([i+(1-idx)*h for i in y],vals,h,label=w,color=col)
    ax.set_yticks(y);ax.set_yticklabels(labels);ax.invert_yaxis()
    ax.set_xlabel('% of extracted vacancies');ax.set_title('Specific AI coding tools & agentic mentions (P1 → P2 → P3)');ax.legend()
    fig.tight_layout();fig.savefig(charts/'ai-tools-trends.png',dpi=160);plt.close(fig)
    # Live snapshot breakdown (London / Berlin / New York; 14 Nov + 25 Nov)
    live_rows=[r for r in rows if r['dataset']=='live']
    live_canonical,_=dedup(live_rows)
    live_by_snap={}
    for snap in sorted({r.get('snapshot_date','unknown') for r in live_rows}):
        st=stats([r for r in live_rows if r.get('snapshot_date','unknown')==snap])
        live_by_snap[snap]={'n':st['n'],'extracted_n':st['extracted_n'],'ai_any_n':st['ai_any_n'],'ai_any_pct':pct(st['ai_any_n'],st['extracted_n']),'ai_dev_n':st['ai_developer_tool_n'],'ai_dev_pct':pct(st['ai_developer_tool_n'],st['extracted_n'])}
    live_by_city={}
    for city in ['New York','London','Berlin']:
        csub=[r for r in live_canonical if live_city(r)==city]
        st=stats(csub);d=st['extracted_n']
        tg=tool_group_counts(csub,dev_only=True)
        live_by_city[city]={'n':st['n'],'extracted_n':d,'ai_any_n':st['ai_any_n'],'ai_any_pct':pct(st['ai_any_n'],d),'ai_dev_n':st['ai_developer_tool_n'],'ai_dev_pct':pct(st['ai_developer_tool_n'],d),'top_dev_tools':tg}
    fig,ax=plt.subplots(figsize=(8,4.5))
    cities=['New York','London','Berlin'];cx=list(range(len(cities)));wbar=0.35
    any_vals=[live_by_city[c]['ai_any_pct'] for c in cities]
    dev_vals=[live_by_city[c]['ai_dev_pct'] for c in cities]
    b1=ax.bar([i-wbar/2 for i in cx],any_vals,wbar,label='Any AI mention',color='#467b74')
    b2=ax.bar([i+wbar/2 for i in cx],dev_vals,wbar,label='AI developer-tool mention',color='#ae7851')
    for b,v in list(zip(b1,any_vals))+list(zip(b2,dev_vals)):ax.text(b.get_x()+b.get_width()/2,v+0.8,f'{v:.1f}%',ha='center',va='bottom',fontsize=9)
    ax.set_xticks(cx);ax.set_xticklabels([f"{c}\n(n={live_by_city[c]['extracted_n']:,})" for c in cities])
    ax.set_ylabel('% of extracted live vacancies');ax.set_title('Live snapshots (14 Nov + 25 Nov 2026): AI shares by city');ax.set_ylim(0,max(any_vals+[10])*1.15);ax.legend()
    fig.tight_layout();fig.savefig(charts/'live-cities.png',dpi=160);plt.close(fig)
    (dest/'trends-breakdown.json').write_text(json.dumps({'six_roles':six_role_windows,'tool_groups_all':tool_windows,'tool_groups_dev':tool_dev_windows,'live_by_snapshot':live_by_snap,'live_by_city':live_by_city},indent=2))
    t='''# Three snapshots: requirements and AI mentions

![AI shares](charts/trends.png)

These windows use original publication dates after global repost deduplication. Each vacancy counts once. Full row lineage is in `dedup-audit.jsonl.gz`; the extraction outputs retain all source rows and tag reposts through this audit.

| window | unique n | extracted n | removed reposts (original window) | any AI % | developer-tool AI % |
|---|---:|---:|---:|---:|---:|
'''
    for w,s in allstats.items():t+=f"| [{w}]({w}.md) | {s['n']} | {s['extracted_n']} | {s['reposts_removed_original_window']} | {pct(s['ai_any_n'],s['extracted_n'])} | {pct(s['ai_developer_tool_n'],s['extracted_n'])} |\n"
    t+='\n## Interpretation\n\n'
    p1,p2,p3=[allstats[w] for w in WINDOWS]
    for key,label in [('ai_any_n','Any AI mentions'),('ai_developer_tool_n','Developer-tool AI mentions')]:
        rates=[pct(s[key],s['extracted_n']) for s in [p1,p2,p3]]
        t+=f'{label}: {rates[0]}% → {rates[1]}% → {rates[2]}%; P3 minus P1 = {rates[2]-rates[0]:+.2f} percentage points. '
    t+='These sample changes cannot separate hiring changes from source/role mix, archive availability and live-survivor selection. The windows have unequal duration (two, three, and an incomplete two months), so raw counts do not measure market growth. Summer is intentionally omitted.\n\n'
    t+='## Six developer roles: AI & developer-tool requirements (P1 → P2 → P3)\n\n![AI developer tools by role](charts/ai-by-role.png)\n\n'
    t+='| role | P1 n | P1 any AI % | P1 dev-tool % | P2 n | P2 any AI % | P2 dev-tool % | P3 n | P3 any AI % | P3 dev-tool % | dev-tool Δ (P3−P1) |\n|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n'
    for rk in SIX_ROLES:
        r1,r2,r3=[six_role_windows[w].get(rk,{'extracted_n':0,'ai_any_pct':0,'ai_dev_pct':0}) for w in ['P1','P2','P3']]
        delta=r3['ai_dev_pct']-r1['ai_dev_pct']
        t+=f"| {SIX_ROLE_LABELS[rk]} | {r1['extracted_n']} | {r1['ai_any_pct']:.2f}% | {r1['ai_dev_pct']:.2f}% | {r2['extracted_n']} | {r2['ai_any_pct']:.2f}% | {r2['ai_dev_pct']:.2f}% | {r3['extracted_n']} | {r3['ai_any_pct']:.2f}% | {r3['ai_dev_pct']:.2f}% | {delta:+.2f} pp |\n"
    t+='\n## Agentic & AI coding tools over time (P1 → P2 → P3)\n\n![Specific AI tools over time](charts/ai-tools-trends.png)\n\n'
    t+='| tool / concept | P1 n (%) | P2 n (%) | P3 n (%) | Δ (P3−P1) | P3 dev-tool context n (%) |\n|---|---:|---:|---:|---:|---:|\n'
    for lbl,_ in TOOL_GROUPS:
        c1,c2,c3=[tool_windows[w][lbl] for w in ['P1','P2','P3']]
        r1,r2,r3=[pct(c,allstats[w]['extracted_n']) for c,w in zip([c1,c2,c3],['P1','P2','P3'])]
        d3=tool_dev_windows['P3'][lbl];dr3=pct(d3,allstats['P3']['extracted_n'])
        t+=f'| {lbl} | {c1} ({r1:.2f}%) | {c2} ({r2:.2f}%) | {c3} ({r3:.2f}%) | {r3-r1:+.2f} pp | {d3} ({dr3:.2f}%) |\n'
    t+='\n## Live snapshots: London, Berlin, New York (14 Nov + 25 Nov 2026)\n\n![Live snapshots by city](charts/live-cities.png)\n\n'
    t+='Both Built In live snapshots (`2026-11-14` and `2026-11-25`) are included in the global dataset (each vacancy assigned to its earliest `posted_date` across windows). Below is the city-level summary across deduplicated live-snapshot vacancies:\n\n'
    t+='| snapshot | rows | extracted n | any AI % | developer-tool AI % |\n|---|---:|---:|---:|---:|\n'
    for snap,sv in live_by_snap.items():t+=f"| {snap} | {sv['n']:,} | {sv['extracted_n']:,} | {sv['ai_any_pct']:.2f}% | {sv['ai_dev_pct']:.2f}% |\n"
    t+='\n| city (14 Nov + 25 Nov deduped) | unique n | extracted n | any AI % | developer-tool AI % | Claude Code (dev) | Cursor (dev) | Copilot (dev) |\n|---|---:|---:|---:|---:|---:|---:|---:|\n'
    for city in ['New York','London','Berlin']:
        cv=live_by_city[city];d=cv['extracted_n'];tg=cv['top_dev_tools']
        t+=f"| {city} | {cv['n']:,} | {d:,} | {cv['ai_any_pct']:.2f}% | {cv['ai_dev_pct']:.2f}% | {tg['Claude Code']} ({pct(tg['Claude Code'],d):.2f}%) | {tg['Cursor']} ({pct(tg['Cursor'],d):.2f}%) | {tg['GitHub Copilot / Copilot']} ({pct(tg['GitHub Copilot / Copilot'],d):.2f}%) |\n"
    t+='\n## Conservative defaults\n\n'
    t+='''- Reposts are retained as extraction rows and flagged in the audit, then excluded from all report counts. The latest user instruction supersedes the earlier keep-and-count proposal.
- Date is the earliest valid posted_date in each linked entity. Missing publication dates never fall back to crawl_batch/capture/snapshot. Crawl_batch rows with posted_date remain eligible.
- First location region is retained with regions_all, without exploding jobs into multiple counts. Historical UNKNOWN buckets remain unknown. Live regions use the same deterministic mapping.
- QA/SDET, interns, staff, other engineering roles and non-English rows are retained and tagged. Language is extracted; tags also use title/employment metadata.
- Employer names are normalized for case/punctuation but aliases/board slugs are not guessed. Text twins with different company/title/location remain distinct unless ID/URL links them. Extraction itself runs once per unique cleaned text, independently of vacancy counting.
- EEO, applicant privacy, board tags and standalone About us/company/team paragraphs are stripped before extraction. Requirement paragraphs containing legal/privacy vocabulary can be over-stripped; raw inputs remain unchanged. All evidence refers to the stripped text.
- No JobsPipe access, data or credentials are used. Inputs are historical Built In/Greenhouse/Ashby and the existing Built In live snapshots only.
- Shares use successful extractions in the window as denominator; n and missing counts are explicit. Missing fields are unknown, not negative evidence of absence. Multi-label skills and AI names can sum above 100%.
- Salary retains currency/period and no inferred currency or annualization. Experience is explicit candidate work experience. Remote/office comes from description, with unknown retained.

## Input provenance and extraction

Historical: `data/historical/clean/vacancies.jsonl.gz` (11,292 frozen rows from 15 Nov run, SHA-256 `7b61296d...`). Live: `alexeygrigorev/agentic-engineering-field-guide` commits `59126d538145ec21faed82bc648cbd5536048de3` (`2026-11-14`, 6,215 rows) and `79ec4c0` (`2026-11-25`, 879 rows), joined by ID to `data/live/data_raw/<date>/*.yaml`. A missing detail file is an explicit missing-description row, never filled from listing title. Validation-failed rows (`status="error"`, <1% of corpus) remain explicit and are excluded from LLM-share denominators.

Model: GLM-5.3-Flash (`glm-5.3-flash`) via existing Z.ai Coding Plan configuration. Content-hash cache and request IDs/token usage are retained; schema and reproduction instructions are in the extraction schema document. See pilot QA and cost report.
'''
    unknown=sum(not r['original_posted_date'] for r in canonical)
    t+=f'\nGlobal dedup: {len(rows):,} input rows → {len(canonical):,} entities; {len(rows)-len(canonical):,} repost rows removed; {unknown} entities lack publication date.\n'
    # Cohort sensitivity keeps global original dates, avoiding reintroducing cross-cohort reposts.
    t+='\n## Source sensitivity: historical-origin entities only\n\n| window | n | any AI % | developer-tool AI % |\n|---|---:|---:|---:|\n'
    for w,(lo,hi) in WINDOWS.items():
        st=stats([r for r in canonical if r['dataset']=='historical' and r['original_posted_date'] and lo<=r['original_posted_date']<=hi])
        t+=f"| {w} | {st['n']} | {pct(st['ai_any_n'],st['extracted_n'])} | {pct(st['ai_developer_tool_n'],st['extracted_n'])} |\n"
    t+='\nThis check excludes live-origin entities while keeping global deduplication. It does not remove archive selection bias. Full role, seniority, requirements, work arrangements and disclosure counts are shown in each window report.\n'
    t+='\n## Requirements, seniority and workplace comparison\n\nSkills count any explicit skill mention; requirement levels are retained separately in monthly-by-role.csv and each extracted row. Alternatives/examples can be inconsistently classified as required/preferred/mentioned, so skill mention shares are the primary comparable measure. All cells are percentages of successful extractions, independently within each window. Skill names are normalized only for case/punctuation; aliases can split counts.\n\n| measure | P1 % | P2 % | P3 % |\n|---|---:|---:|---:|\n'
    for metric in ['skills','seniority','workplace']:
        keys=set().union(*(s[metric] for s in allstats.values()))
        if metric=='skills':keys=sorted(keys,key=lambda k:-sum(s[metric].get(k,0) for s in allstats.values()))[:15]
        for key in sorted(keys):
            vals=[pct(s[metric].get(key,0),s['extracted_n']) for s in allstats.values()]
            t+=f'| {metric}: {key} | {vals[0]} | {vals[1]} | {vals[2]} |\n'
    for key,label in [('experience_known_n','Experience disclosure'),('salary_known_n','Salary disclosure')]:
        vals=[pct(s[key],s['extracted_n']) for s in allstats.values()];t+=f'| {label} | {vals[0]} | {vals[1]} | {vals[2]} |\n'
    t+='\n[Monthly data by role](monthly-by-role.csv) contains all observed months with numerators, denominators, skills, AI mentions, seniority, workplace and disclosure shares. No summer interpolation is performed. Salary and experience summaries are conditional on disclosure and are in each window report; changing disclosure rates prevent treating them as unconditional market estimates.\n'
    (dest/'TRENDS.md').write_text(t)
    print(json.dumps({'input_rows':len(rows),'unique_jobs':len(canonical),'removed':len(rows)-len(canonical),'windows':{w:s['n'] for w,s in allstats.items()}}))

if __name__=='__main__':main()
