# Agentic engineering: preliminary analysis for track A

**13 November 2026. Draft. Nothing here has been sent, published or submitted.** Intake t3267u-E.

This is a first analysis of agentic engineering (software engineers working with coding agents) from data that already exists: the job corpus of the [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide), the research already in this folder, and the public sources that research catalogued on 12 November 2026. No new job data was scraped or bought, and no new web pages were fetched for it. A separate plan for a dedicated agentic engineering field guide (t3267u-D) is being written in parallel; this analysis does not depend on it.

It is meant as a basis for [variant A, Agentic engineering](../bildungsgutschein/variante-a-agentic-engineering.md).

What is new here compared with [bildungsgutschein/research.md](../bildungsgutschein/research.md): that file covers what practitioners write and what other courses teach. This one adds what employers write in job postings, counted over the existing corpus, and puts the three views side by side.

Marks used: *(computed)* is my own count from the corpus with the script in [scripts/](scripts/coding_agent_signals.py). **Unknown** means no available source settles it.

## 1. Short version

1. **Employers describe agentic engineering as a way of working inside existing engineering jobs, not as a new job.** In 9,760 postings found by searching "AI Engineer" on Built In, 21.0% mention coding agents or AI-assisted development *(computed)*. Only 14 titles contain "agentic engineer", "agentic engineering", "agentic software" or "agentic coding", and those are mostly about building agents, not about developing with them.
2. **The share doubled in nine months.** 12.8% of postings in the 4 February 2026 scrape, 25.1% in the 6 November 2026 scrape *(computed)*. Most of the rise happened by June; since then it has stayed at 22–26%.
3. **Postings increasingly describe the practice and not the product.** Postings that name a tool went from 8.8% to 13.8% and peaked in June. Postings that use a phrase such as "AI-assisted development" or "coding agents" went from 8.3% to 20.5% and are still rising *(computed)*.
4. **No single tool owns the requirement.** Of the postings that name a coding tool, 58% name two or more *(computed)*. Claude Code and Cursor are level over the whole period; Claude Code has been ahead since July.
5. **What employers ask for next to the tool is verification and delivery skill.** Near the mention, postings talk about workflows and automation (67%), review and validation (48%), productivity (45%), testing (36%), security and governance (35%), and specs and requirements (31%) *(computed)*. Practitioners and course syllabi name the same things.
6. **Three role shapes appear.** The engineer who is expected to work with agents every day; the titled "AI-native" or "AI-augmented" software engineer; and the AI enablement or developer-productivity engineer who builds the setup for a whole team. The third is the least covered by the current syllabus.
7. **Almost none of this is junior.** 1.5% of the postings with a signal have a junior word in the title *(computed)*. This matters for a Bildungsgutschein audience that includes career changers.
8. **The syllabus is supported in its main lines.** The data backs the order (one supervised agent, then verification and safety, then automation), the tool-neutral outcomes and the weight on review and testing. It suggests five adjustments, listed in section 7.
9. **The largest gap is the corpus itself.** It contains AI-titled jobs only. It cannot say what share of ordinary software engineering jobs in Germany ask for these skills, and nothing available can say whether graduates of such a course get hired.

## 2. Data used and what it can support

| Source | What it is | Supports | Does not support |
|---|---|---|---|
| Field Guide job corpus, `job-market/data_raw/` and `data_structured/` in [alexeygrigorev/ai-engineering-field-guide](https://github.com/alexeygrigorev/ai-engineering-field-guide) at commit `d48b83e5` | 9,760 postings from Built In, ten scrapes from 4 February to 6 November 2026, found with the search "AI Engineer" for Los Angeles (all locations), New York, London, Amsterdam, Berlin and India (`job-market/_internal/scrapers/scrape_builtin_requests.py`) | How AI-titled engineering jobs word their expectations about coding agents; direction of change over nine months; which tools are named together | Anything about jobs that are not AI-titled; German market size; hiring outcomes; salaries. Each scrape is an independent cross-section with no shared job IDs (`role/07-trends.md`) |
| Field Guide analysis, `role/02-skills.md`, `role/07-trends.md`, `role/08-trends-appendix.md`, `interview/03-get-hired.md`, `interview/05-trends.md` | Published analysis of the first eight scrapes (6,964 postings) and interview research | Cross-check of my counts; interview formats that test AI-tool use | Same limits as the corpus |
| [research-notes/practitioner-sources.md](../bildungsgutschein/research-notes/practitioner-sources.md), track A | 52 sources fetched 12 November 2026: practitioners, vendor engineering blogs, Thoughtworks Radar, developer surveys, Hacker News | Practices, disagreements, what changed in 2025–2026, self-reported tool use | Reddit and X are not covered; some pages are known from search snippets only and are marked so there |
| [research-notes/international-syllabi.md](../bildungsgutschein/research-notes/international-syllabi.md), track A | 17 syllabi, 2025 and 2026 versions | What others teach and in what order | Whether those courses work |
| [research-notes/germany-azav-programmes.md](../bildungsgutschein/research-notes/germany-azav-programmes.md), [../research.md](../research.md) | German funded programmes, Bitkom and BA labour-market releases, four employer examples | Competitor landscape, general IT labour market | Demand for agentic-engineering skills in German software jobs |
| Alexey's own material as listed in [research.md section 2](../bildungsgutschein/research.md#2-alexeys-own-material) | AI Dev Tools Zoomcamp and 26 Substack posts | The role definition and the practices the course teaches | Independent evidence |

How the counts were made:

- Regular expressions over title, description and the posting's own skills list. No LLM was used. The patterns are in the script.
- Two measures. **Named tool:** Claude Code, Cursor, GitHub Copilot, Codex and ten smaller ones. **Practice phrase:** "coding agent/assistant", "AI-assisted/-native/-augmented/-enabled/-first/-powered/-driven development/coding/engineering/SDLC", "agentic coding/development/engineering", "vibe coding". **Either** is the union.
- Precision, from reading samples by hand. Of 70 sentences around a match, about 7 were not about the engineer's own way of working (a customer called Cursor, a product for developers, security of coding agents). Of 50 practice-phrase matches with the modifiers other than "assisted", 38 were on target; "AI-native engineering" and "AI-driven development" sometimes describe the product. "AI-assisted" is 700 of the phrase matches and read cleanly in the sample. So the named-tool measure is the firmer one, and the "either" figure is somewhat too high in level. I have no reason to think the error changed over time, but I did not test that.
- "Cursor" and "Codex" are matched with a capital letter only. "Copilot" alone is not counted, because it also means Microsoft 365 Copilot and product copilots (10.1% of postings say "Copilot" in some sense; 4.8% say "GitHub Copilot").
- My figures differ from the Field Guide's published ones (7.6% in February, 12.8% in August, `role/08-trends-appendix.md`). The guide counts tools in the LLM-extracted skills list over eight scrapes; I count the raw text over ten. Both show the same direction.

## 3. Role definitions

### 3.1 The definitions in use

- **Alexey's:** "Agentic engineering - agents help you build the product", against "AI engineering - AI is part of the product" ([Trends in Agentic Engineering](https://aishippingblog.com/p/trends-in-agentic-engineering), quoted in [research.md section 2.4](../bildungsgutschein/research.md#24-track-b-maven-course)).
- **Practitioners:** the term was attached to professional, verified work with coding agents in February 2026 (Karpathy, known from a snippet only) and is used that way by Simon Willison (https://simonwillison.net/guides/agentic-engineering-patterns/) and on Martin Fowler's site (catalogue entries A1–A6, A44 in [practitioner-sources.md](../bildungsgutschein/research-notes/practitioner-sources.md)). The vocabulary moved quickly: vibe coding, context engineering, agentic engineering, harness engineering, loop engineering, all within about 18 months.
- **Job postings:** employers mostly do not use the term in this sense. "Agentic" appears in 538 titles, and the titles I read are about building agentic products ("Senior Agentic AI Engineer", "Frontend Engineer - Agentic AI"). The employer vocabulary for the working practice is "AI-assisted development" (700 postings), "AI-native" and "coding agents" *(computed)*.

Consequence for the course: "Agentic Engineering" as a title matches practitioner usage and Alexey's own definition, but a participant searching job boards for it will mostly find track B jobs. The German working title, *Agentische Softwareentwicklung: Software mit Coding-Agenten entwickeln, testen und ausliefern*, already says what the job postings say. For the labour-market argument the target occupation is software developer, not a new occupation.

### 3.2 Three role shapes in the postings

**1. The engineer who works with agents.** The requirement sits inside an ordinary role. This is the bulk of the 2,045 postings with a signal. Typical wording:

- "Daily, fluent use of AI coding agents (Claude Code, Cursor, or equivalent) as your primary execution layer, with clear opinions on when agents accelerate or hinder development." (taleroo / SCHWAPe, Berlin, https://builtin.com/job/senior-fullstack-engineer-ai-native-dri-native-german-m-w-d/9763092)
- "Use AI-assisted development tools for discovery, implementation, debugging, testing, code review, documentation, and refactoring while maintaining strong engineering quality standards" (qlub, Berlin, https://builtin.com/job/senior-software-engineer-ai-native-development/11894527)

**2. The titled "AI-native" software engineer.** 364 postings carry a label such as AI-native (139), AI enablement (90), AI-first (34), AI-enabled (31), AI-assisted (18) or AI-augmented (10) in the title; 1.7% of the February scrape, about 4% since April *(computed)*. The descriptions define the job as owning the result of AI-generated work:

- "Generate 80–90% of initial solution drafts using AI tools, then review, validate, and refine the output." and "Convert product and business requirements into clear technical prompts, implementation plans, and acceptance criteria." (Greenway Health, https://www.builtinla.com/job/ai-native-software-engineer/11426154)
- "Own the quality of AI-generated outputs in your delivery scope ... know when AI output is production-ready and when it is not" and "Define and track KPIs to evaluate the effectiveness and ROI of AI-assisted workflows" (Accenture, Hamburg, https://builtin.com/job/junior-ai-native-software-engineer-all-genders/11369908)

**3. The AI enablement or developer-productivity engineer.** Builds and maintains the agent setup for a team and gets other engineers to use it:

- "the shared harness layer (skills, context, MCP servers, per-repo configuration) that makes every engineer's agent dramatically better than stock", "tuned AI code reviewers, codified review rules mined from our own PR history", "Own the measurement. Cycle time, review latency, escaped defects, cost per feature" (HubSync, https://www.builtinla.com/job/staff-or-senior-software-engineer-ai-native-sdlc/10911459)
- "Set and maintain the team's engineering standards for working with coding agents (authoring CLAUDE, AGENTS, cursorrules) and configure MCP servers" (taleroo, link above)
- "Drive adoption while helping reduce shadow AI and improving governance processes" (GetYourGuide, Berlin, https://builtin.com/job/senior-ai-enablement-engineer/8990334). This one is closer to internal IT governance than to engineering.

A fourth group, people who build coding agents as a product, is in the corpus too. It belongs to track B and is not analysed here.

These shapes are my reading of the postings I opened, eight in full and 70 sentence samples. They are not a counted classification. The URLs were live when scraped; whether the roles are still open was not checked.

## 4. Skills

### 4.1 What postings say next to the mention *(computed)*

Share of the 2,045 signal postings in which the theme appears within 300 characters of a coding-agent mention. Keyword matching, so read these as rough ranks, not exact shares.

| Theme | Share |
|---|---:|
| Workflows, automation, pipelines | 67.3% |
| Review, verification, validation, quality | 48.4% |
| Productivity, velocity, speed | 45.3% |
| Testing | 35.9% |
| Security, guardrails, governance | 35.4% |
| Specs, requirements, planning | 30.6% |
| Teaching, championing, enabling others | 28.6% |
| Prompting | 21.5% |
| Multi-agent, orchestration, parallel work | 21.0% |
| Daily use | 19.7% |
| Context, instruction files, rules | 14.7% |
| Measuring impact, metrics | 14.3% |
| MCP, skills, hooks, plugins | 11.8% |

Wording of the requirement near the mention: 53.7% use "required", "proficient", "hands-on", "demonstrated" or "proven"; 38.8% use "preferred", "bonus", "plus" or "familiarity". The two overlap.

Across the whole posting, signal postings mention these more often than the rest of the corpus: reviewing or validating AI-generated code (7.4% against 0.6%), code review (25.2% against 12.0%), testing (19.6% against 11.0%), CI/CD (45.9% against 34.3%), security (48.3% against 39.6%). Docker and Kubernetes are equal (30.0% against 30.1%). This is co-occurrence in job text, not proof of what the work needs.

MCP is named in 15.2% of all postings (9.9% in February, 20.1% in November). In this corpus that is mostly MCP as a product skill for track B. Next to coding-agent mentions, MCP, skills, hooks and plugins are in 11.8%. The newer practitioner terms are rare in postings: "context engineering" 2.9%, "harness" 1.9%, "vibe coding" 0.7%, "spec-driven" 0.5%, "AGENTS.md / CLAUDE.md / agent skills" 0.7%.

### 4.2 The three views side by side

| Skill | Postings (4.1) | Practitioners ([research.md 5.1](../bildungsgutschein/research.md#51-agentic-engineering)) | 2026 syllabi ([research.md 4.1](../bildungsgutschein/research.md#41-track-a)) | Variant A week |
|---|---|---|---|---|
| Verify and review agent output | Strong | Named as the core skill; review is the bottleneck (Faros: time to first review up 156.6%) | In most | 6, 7 |
| Tests and CI as the feedback loop | Strong | Broad agreement | In most | 6, 8 |
| Specs, acceptance criteria, small tasks | Present | Broad agreement on the habit, dispute over spec frameworks | In most | 3 |
| Security, permissions, sandboxing | Present, worded as governance and compliance | Broad agreement on sandboxing | In most | 9 |
| Context and instruction files | Weak in wording | Broad agreement | In most | 2, 11 |
| MCP, skills, subagents, hooks | Weak next to coding-agent mentions | Disputed which mechanism to use | In most | 11, 12 |
| Parallel agents, orchestration | Present | Disputed how many and whether it pays | 2026 only | 13 |
| Unattended runs, software factory | Rare | Disputed | 2026 only | 14 |
| Teaching and enabling a team, shared standards | Present (28.6%) | Named as an organisational gap | 2026 only | X3 only |
| Measuring impact | Present (14.3%) | Agreement that lines and tokens are bad measures; no agreed good one | 2026 only | X3 only |
| Cost, usage limits, model choice | Not measured | Named as missing | 2026 only | 14 |
| Keeping debugging and code-reading skill without AI | Not visible | Named as a risk (Anthropic trial, 50% against 67% on a quiz) | Some universities keep closed exams | Checkpoints in 2, 6, 9 |
| Ordinary delivery: Git, deployment, observability | Same as other postings | "Matters more, not less" | Shrinking as separate weeks | 8, 10 |

Where all three agree, the evidence is as good as it currently gets: verification and review, tests and CI, specs and task decomposition, and security. Where only practitioners and new syllabi speak (context management, skills, MCP, factories), the course is teaching ahead of what job postings ask for in words. That is defensible, because postings lag practice, but it should not be presented as employer demand.

## 5. Tools

Share of all postings naming the tool *(computed)*:

| Scrape | Claude Code | Cursor | GitHub Copilot | Codex | Any named tool |
|---|---:|---:|---:|---:|---:|
| 4 Feb | 3.0% | 5.4% | 2.6% | 1.0% | 8.8% |
| 27 Feb | 2.3% | 5.1% | 4.4% | 1.5% | 9.0% |
| 27 Mar | 5.6% | 6.6% | 3.2% | 3.2% | 11.2% |
| 22 Apr | 6.4% | 7.4% | 5.1% | 1.9% | 13.5% |
| 29 May | 7.9% | 8.7% | 5.0% | 2.5% | 14.6% |
| 25 Jun | 10.0% | 10.0% | 6.3% | 2.9% | 17.0% |
| 22 Jul | 8.7% | 8.5% | 5.8% | 3.4% | 14.8% |
| 25 Aug | 8.1% | 7.9% | 5.3% | 3.8% | 14.0% |
| 23 Sep | 8.0% | 7.0% | 4.9% | 3.4% | 13.7% |
| 6 Nov | 9.5% | 7.3% | 5.1% | 3.9% | 13.8% |
| All ten | 7.3% | 7.4% | 4.8% | 2.9% | 13.2% |

- Other tools are below 1% each over the period: Windsurf 0.7%, Devin 0.5%, Lovable 0.4%, Replit 0.2%, Amazon Q 0.2%, Kiro 0.2%, Cline, Aider, Gemini CLI and OpenCode 0.1% or less.
- 1,285 postings name a tool. 545 name one, 740 name two or more. The most common pairs are Claude Code with Cursor (392), Cursor with GitHub Copilot (257), Claude Code with GitHub Copilot (202) and Claude Code with Codex (187). Postings often add "or equivalent" or "whatever tool is actually best this quarter".
- Developer surveys in the catalogue report much higher use than postings report demand. Pragmatic Engineer, 906 responses, early 2026: 95% use AI tools weekly, 55% regularly use agents, 70% use two to four tools, Claude Code most used; in companies above 10,000 employees GitHub Copilot leads with 56% (https://newsletter.pragmaticengineer.com/p/ai-tooling-2026). Stack Overflow 2026: among users of coding agents, Claude Code 66% and GitHub Copilot 59% (https://survey.stackoverflow.co/2026/ai). Both are self-selected samples.
- Thoughtworks Radar Vol. 35 has Codex and OpenCode in Adopt ([research.md 5.1](../bildungsgutschein/research.md#51-agentic-engineering)). OpenCode is nearly absent from postings.

What this supports: Claude Code as the base tool is in line with both the postings and the surveys. A single tool is not what employers describe. The existing decision to word outcomes without tool names and repeat a workflow in a second agent in week 14 fits the data. Large German employers are more likely to be on GitHub Copilot if the Pragmatic Engineer size split holds for Germany, which is **unknown**.

## 6. Trends

From the corpus *(computed)*:

| Scrape | Postings | Named tool | Practice phrase | Either | "AI-native"-type title |
|---|---:|---:|---:|---:|---:|
| 4 Feb | 895 | 8.8% | 8.3% | 12.8% | 1.7% |
| 27 Feb | 870 | 9.0% | 8.7% | 12.2% | 2.1% |
| 27 Mar | 680 | 11.2% | 10.4% | 16.0% | 2.6% |
| 22 Apr | 645 | 13.5% | 14.9% | 20.2% | 4.0% |
| 29 May | 919 | 14.6% | 14.1% | 20.0% | 4.6% |
| 25 Jun | 888 | 17.0% | 19.1% | 25.8% | 4.7% |
| 22 Jul | 846 | 14.8% | 17.1% | 22.3% | 4.8% |
| 25 Aug | 1,222 | 14.0% | 19.1% | 23.9% | 4.0% |
| 23 Sep | 1,086 | 13.7% | 18.4% | 24.1% | 4.1% |
| 6 Nov | 1,709 | 13.8% | 20.5% | 25.1% | 4.0% |

- The rise was fast from February to June and has been flat to slightly up since. It is not a straight line, and the November scrape is much larger than the others, so the mix of employers may have shifted.
- By role type, using the Field Guide's classification: AI-first roles 20.7% over the period (12.6% in the first three scrapes, 25.4% in the last three), AI-support roles 25.1% (18.6%, then 25.7%), classical-ML roles 5.0%. Earlier in the year the expectation was stronger in support roles such as platform, frontend and backend; the AI-first roles have caught up.
- By region, first three scrapes against last three: USA 13.7% to 23.8%, India 11.7% to 21.5%, UK 16.4% to 33.2%, Germany 17.3% to 38.7%, Netherlands 6.7% to 32.7%. The German figure rests on 81 and 106 postings and on few employers: of 85 German postings with a signal, 13 are from Wolters Kluwer and 6 from AutoScout24, 49 employers in all. It shows the wording exists in Berlin postings. It is not a German market estimate.
- Seniority in the title: signal postings are 32.0% senior, 25.7% staff, principal, lead or above, 1.5% junior. The rest of the corpus is 27.3%, 21.1% and 2.1%. The whole corpus has almost no junior roles, which the Field Guide also reports (`role/07-trends.md`).
- Interviews: the Field Guide records employers that test how a candidate works with AI tools (an AI-assisted round followed by a round without AI at Microsoft; "AI-First Proficiency" at Miro), and one that requires the tools on the job and bans them in the interview (`interview/05-trends.md`). This supports assessing both with and without AI.

From the public sources already catalogued:

- Tool leadership changed within eight months in 2025–2026, and Stanford's CS146S was largely rewritten between its 2025 and 2026 runs ([research.md 4.1](../bildungsgutschein/research.md#41-track-a), [5.1](../bildungsgutschein/research.md#51-agentic-engineering)).
- 2026 syllabi added background agents, issue-to-pull-request pipelines, agent-ready codebases, cost and measurement; they dropped the separate prompting week and "vibe coding" as a framing.
- Whether teams get faster is not settled. METR is redesigning its study (https://metr.org/blog/2026-02-24-uplift-update/). Faros reports more throughput together with more bugs and slower review, from vendor telemetry (https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways). Postings nevertheless frame the skill as productivity in 45% of cases.
- German labour market: Bitkom reports unfilled IT jobs down from 149,000 in 2023 to 79,000, and 63% of companies expecting AI skills to be needed in all IT jobs (https://www.bitkom.org/Presse/Presseinformation/IT-Fachkraeftemangel-in-den-letzten-drei-Jahren-halbiert). No German study on coding-agent skills in software jobs was found ([research.md section 3](../bildungsgutschein/research.md#3-comparable-programmes-in-germany)).

## 7. Implications for variant A

What the data supports as it stands:

| Decision in the syllabus | Support |
|---|---|
| Audience: people who already program | Postings attach the requirement to engineering roles with experience; 1.5% junior |
| One supervised agent first, review and safety before automation (weeks 2–10, then 11–14) | Review, testing and security are the themes postings name most; same order as the 2026 syllabi |
| A full week on reviewing agent-generated changes (week 7) and one on testing and debugging (week 6) | The strongest point of agreement across postings, practitioners and syllabi |
| Outcomes without tool names, Claude Code as base, a second agent in week 14 | 58% of tool-naming postings name several tools; leadership moved within the year |
| Checkpoints without AI (weeks 2, 6, 9) | Employers interview both with and without AI; the Anthropic trial |
| Full-stack product with CI/CD, deployment and observability (weeks 4–5, 8, 10) | Signal postings ask for ordinary delivery skill at least as often as other postings |
| The factory week states its limits (week 14) | Unattended factories are disputed among practitioners and rare in postings |

Adjustments the data suggests. These are my recommendations, not decisions.

1. **Bring team enablement into the core.** 28.6% of signal postings ask the engineer to teach, champion or set standards, and the enablement role is a distinct shape with German examples (taleroo, GetYourGuide, Payrails, AutoScout24 "AI Enabler"). In the syllabus this is only extension week X3. A lighter option: make "write the team's working agreement and instruction files for someone else's repository" an assessed output in week 11 or 14.
2. **Add measurement as an outcome.** Postings ask for KPIs, cycle time, review latency and escaped defects (14.3% near the mention). Practitioners agree only on what not to count. A short unit in week 13 or 14 on measuring a workflow before and after would cover it, with the dispute stated.
3. **Use the employers' words in the outward description.** "AI-assisted software development", "coding agents", "review and validate AI-generated code", "acceptance criteria" are what postings say. "Software factory", "harness" and "loop" are practitioner terms that are nearly absent from postings. They can stay in the module content; the course goal and the labour-market section should use the first set.
4. **Show a second tool earlier, briefly.** Week 14 is late if a participant interviews before the end. One comparison exercise in week 1 or 2 (the same small task in Claude Code and in one other agent) would let participants say truthfully that they have used more than one. For large German employers the second tool is plausibly GitHub Copilot; that is an inference from one survey, not a finding.
5. **Be explicit about the entry level in the funding argument.** The postings do not show a junior market for this skill. For career changers the realistic claim from the data is "an existing developer or adjacent technical professional updates how they work", not "a beginner becomes an agentic engineer". This matches the entry check already planned, and it should shape how the course goal is worded for the Agentur für Arbeit.

Material from this analysis that can be reused later, after re-checking: the German posting examples in [data/coding-agent-signals.json](data/coding-agent-signals.json) (`germany.examples`) as illustrations of employer wording, and the quotes in section 3.2.

## 8. What the available data cannot support

- **Demand in ordinary software jobs.** The corpus was collected with the search "AI Engineer"; 9,705 of 9,760 titles contain an AI-related word (AI, ML, LLM, agent, applied and similar). The audience of variant A mostly applies to jobs without one. The share of general developer postings that ask for coding-agent skills is **unknown**.
- **Germany.** 323 German postings over nine months, from one job board that is not a main German board, in English. No StepStone, Indeed, LinkedIn or BA Jobbörse data is in the repository. Provider-quoted StepStone counts in the notes are unverified and are about AI-engineer titles.
- **Hiring outcomes and salaries.** Nothing available links these skills to getting hired or to pay.
- **Requirement strength.** I counted wording near the mention, not whether a requirement is mandatory. The split of 54% "required"-type against 39% "preferred"-type wording is rough.
- **Theme shares.** They are keyword matches inside a text window. "Workflow" and "quality" are common words.
- **Trend as market change.** Each scrape is a new cross-section of a job board. Changes can come from which employers post, and the last scrape is twice the size of the early ones.
- **Practitioner evidence.** Mostly English-language, vocal, tool-forward authors and vendors. Reddit and X are not covered. Developer surveys are self-selected.
- **Productivity.** No clean measurement exists yet.
- **Demand for the course.** No survey responses, interviews or pilot results exist ([../README.md](../README.md)).
- **Role shapes in section 3.2.** A reading of samples, not a classification of all postings.

What would close the main gaps is the work that the t3267u-D plan is meant to scope: a corpus of ordinary software engineering postings, including a German sample, classified for these signals. Nothing of that was started here.

## 9. Forms and templates

No form or template was required to write this analysis, and none was invented. For the record, these documents that the Bildungsgutschein application will need are not in the repository:

- The certifier's course-documentation form. The notes describe TÜV NORD form A601F113 and link its PDF ([germany-azav-programmes.md section 3.3](../bildungsgutschein/research-notes/germany-azav-programmes.md)); the form itself is not stored here, and no certifier has been chosen.
- A formal German course concept, a certificate format, assessment rubrics and the entry exercise. They are listed as missing in the [AZAV checklist](../bildungsgutschein/README.md#azav-checklist).

## 10. Reproduce

```bash
python3 scripts/coding_agent_signals.py /path/to/ai-engineering-field-guide data/coding-agent-signals.json
```

Needs Python 3 with PyYAML. Reads the Field Guide checkout only; about one minute. The output in [data/coding-agent-signals.json](data/coding-agent-signals.json) was produced on 13 November 2026 from Field Guide commit `d48b83e5`. It holds all counts used above, the German examples, and 123 sampled sentences with job IDs and URLs.

## 11. Sources

In this repository:

- [../bildungsgutschein/research.md](../bildungsgutschein/research.md) and the catalogues in [../bildungsgutschein/research-notes/](../bildungsgutschein/research-notes/)
- [../bildungsgutschein/variante-a-agentic-engineering.md](../bildungsgutschein/variante-a-agentic-engineering.md)
- [../research.md](../research.md), [../materials/survey.en.md](../materials/survey.en.md), [../README.md](../README.md)

AI Engineering Field Guide, https://github.com/alexeygrigorev/ai-engineering-field-guide, commit `d48b83e5`:

- `job-market/data_raw/`, `job-market/data_structured/` (ten scrape folders, 2026-02-04 to 2026-11-06)
- `job-market/README.md`, `job-market/_internal/PIPELINE.md`, `job-market/_internal/scrapers/scrape_builtin_requests.py`
- `role/02-skills.md`, `role/07-trends.md`, `role/08-trends-appendix.md`, `interview/03-get-hired.md`, `interview/05-trends.md`

Public pages, all taken from the 12 November 2026 catalogue and not fetched again:

- https://aishippingblog.com/p/trends-in-agentic-engineering
- https://simonwillison.net/guides/agentic-engineering-patterns/
- https://newsletter.pragmaticengineer.com/p/ai-tooling-2026
- https://survey.stackoverflow.co/2026/ai
- https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways
- https://metr.org/blog/2026-02-24-uplift-update/
- https://www.anthropic.com/research/AI-assistance-coding-skills
- https://www.thoughtworks.com/radar/techniques
- https://themodernsoftware.dev/
- https://www.bitkom.org/Presse/Presseinformation/IT-Fachkraeftemangel-in-den-letzten-drei-Jahren-halbiert

Job postings quoted in section 3.2, as stored in the corpus (Built In, scrape dates 2026-02-27 to 2026-11-06); not re-checked for being open:

- https://builtin.com/job/senior-fullstack-engineer-ai-native-dri-native-german-m-w-d/9763092
- https://builtin.com/job/senior-software-engineer-ai-native-development/11894527
- https://builtin.com/job/junior-ai-native-software-engineer-all-genders/11369908
- https://builtin.com/job/senior-ai-enablement-engineer/8990334
- https://www.builtinla.com/job/ai-native-software-engineer/11426154
- https://www.builtinla.com/job/staff-or-senior-software-engineer-ai-native-sdlc/10911459
- https://builtin.com/job/ai-enablement-engineer/9586468 (Payrails, read but not quoted)
