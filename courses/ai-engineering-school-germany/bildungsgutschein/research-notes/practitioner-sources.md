# What practitioners are writing about: agentic engineering (Track A) and AI engineering (Track B)

Research date: 2026-11-12. All URLs below were fetched or searched on 2026-11-12 unless noted.

## How to read this file

- **[FETCHED]** = the page at the URL was fetched and read on 2026-11-12 (through a fetch tool that returns a model-generated extraction of the page; quotes are as returned by that extraction and are short by design). Before printing any quote in public course material, re-open the URL and confirm the wording.
- **[SNIPPET]** = known only from a web-search result summary on 2026-11-12; the page itself was not read (blocked, paywalled, or not attempted). Treat numbers as unverified.
- **[OLDER]** = published before 2026.
- Long pages were sometimes read only partially (noted per source).
- Not reachable: Reddit threads (no Reddit thread could be fetched or found via search — this channel is NOT covered), X/Twitter directly (covered only via blogs quoting posts), openai.com (HTTP 403), arstechnica.com (blocked), thenewstack.io (403), blog.jetbrains.com (403), infoq.com (403), apiiro.com (403).

---

# TRACK A — Agentic engineering (coding agents)

## A. Source catalogue

### A1. Simon Willison — "agentic-engineering" tag (index page) [FETCHED]
- URL: https://simonwillison.net/tags/agentic-engineering/ (page 1 of 3; 30 posts from 13 Apr to 11 Nov 2026)
- Used as the index for the items below. Notable entries seen on the page (each has its own URL on simonwillison.net):
  - 13 Oct 2026, Geoffrey Huntley quote: a pre-commit hook rejects direct observability calls and tells the agent to use his diagnostics library (https://simonwillison.net/2026/Oct/13/geoffrey-huntley/).
  - 8 Jul 2026, "Rewriting Bun in Rust": Jarred Sumner ported Bun from Zig to Rust with parallel agents using the existing test suite as a conformance suite; quote "Until very recently, programming language choice was a one-way decision." (https://simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/)
  - 30 Apr 2026, "Codex CLI 0.128.0 adds /goal": a Ralph-style loop built into Codex; it "will keep on looping until it evaluates that the goal has been completed." (https://simonwillison.net/2026/Apr/30/codex-goals/)
  - 28 Oct 2026, Amazon guidance quoted: not benefiting from AI tooling is "a finding, not a failing" (https://simonwillison.net/2026/Oct/28/terk-terkowitz/).
  - 29 Oct 2026, Jacob Sansbury (Spawn): "we spend 30x payroll on AI tokens." (https://simonwillison.net/2026/Oct/29/how-i-built-the-most-ai-pilled-company-in-the-world/)
  - 28 Jun 2026, Jon Udell: prefers "Human Agent in the loop" — bring agents into the existing team process (https://simonwillison.net/2026/Jun/28/jon-udell/).
  - 14 Sep 2026, Laurie Voss "We are all Product Engineers now": remaining work is "finding out what people actually want" (https://simonwillison.net/2026/Sep/14/laurie-voss/).
  - 4 Jun 2026, Charity Majors quoted: "There is no natural feedback loop connecting enthusiasts with skeptics." (https://simonwillison.net/2026/Jun/4/ai-enthusiasts-ai-skeptics/)

### A2. Simon Willison — "Agentic Engineering Patterns" (guide) [FETCHED — table of contents only]
- URL: https://simonwillison.net/guides/agentic-engineering-patterns/ (intro post dated 23 Feb 2026; chapters still being added, e.g. one on 18 Apr 2026)
- Chapter list (16): What is agentic engineering?; Writing code is cheap now; Hoard things you know how to do; AI should help us produce better code; Anti-patterns: things to avoid; How coding agents work; Using Git with coding agents; Subagents; Red/green TDD; First run the tests; Agentic manual testing; Linear walkthroughs; Interactive explanations; two annotated prompts; Prompts I use.
- Section headings seen: "Good code still has a cost", "Avoiding taking on technical debt", "Embrace the compound engineering loop", "Inflicting unreviewed code on collaborators" (anti-pattern).
- Chapter bodies were not read.

### A3. Simon Willison — "Vibe coding and agentic engineering are getting closer than I'd like" (6 May 2026) [FETCHED]
- URL: https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/ (787 points / 885 comments on HN, item 48037128)
- The two categories "have started to blur for me already, which is quite upsetting."
- Vibe coding for software used by others is "grossly irresponsible"; agentic engineering is using the tools "to the highest of your own ability".
- He no longer reviews all agent-written production code for routine tasks; treats the agent like another team's service; warns about normalization of deviance. "Claude Code does not have a professional reputation!"
- Polished repos no longer signal care; evidence of real use matters more.
- AI tools are "amplifiers of existing experience".

### A4. Simon Willison — "More than just code review" (22 Aug 2026) [FETCHED]
- URL: https://simonwillison.net/2026/Aug/22/more-than-just-code-review/
- "The key skill required to make productive use of coding agents is being able to confidently instruct them on how to make changes and then confidently verify that those changes have been applied in the correct way."
- "Eyeballing every line of code has never been the most effective way to validate a change to a piece of software."

### A5. Boris Cherny (Anthropic, Claude Code) quoted by Simon Willison (11 Sep 2026) [FETCHED]
- URL: https://simonwillison.net/2026/Sep/11/boris-cherny/ (original: https://twitter.com/bcherny/status/2098217573276131577 — not fetched)
- "Production code written by Claude should have a higher bar than if it was written by a human."
- Guardrails listed (paraphrased by the extraction): lint rules, extensive automated tests, Claude-driven end-to-end tests, daily Claude-powered fuzzers, automated code and security review, automated refactoring.

### A6. Martin Fowler — "Agentic Engineering" bliki (21 May 2026) [FETCHED]
- URL: https://martinfowler.com/bliki/AgenticEngineering.html
- "humans oversee LLM agents who generate the code"; contrasted with vibe coding where "humans don't look at the code".
- Humans stay accountable for "what the software does and how it works."
- Suggests "harness engineering" (guides and sensors around the LLM) may be central to future work; domain understanding matters more.
- Companion entries on the same site (listed, not read): "Vibe Coding" (21 May 2026), "November Inflection" (1 May 2026), "Interrogatory LLM" (14 May 2026), "Future Of Software Development" (2 Jul 2026), "I don't like LLMs" (17 Sep 2026). Index: https://martinfowler.com/tags/generative%20AI.html [FETCHED].

### A7. Birgitta Böckeler — "Harness engineering for coding agent users" (2 Apr 2026) [FETCHED]
- URL: https://martinfowler.com/articles/harness-engineering.html
- Guides (feedforward: AGENTS.md, skills) "anticipate the agent's behaviour and aim to steer it before it acts"; sensors (feedback: linters, tests, architecture tests) work best "when they produce signals that are optimised for LLM consumption."
- Computational controls (deterministic, fast) vs inferential controls (LLM review/judge).
- Steering loop: every recurring issue improves the harness. "Keep quality left."
- Behaviour correctness is the hardest category; relying on AI-generated tests is "not good enough yet."
- "Harnessability": typed languages, clear module boundaries and opinionated frameworks are easier to harness. Open questions: harness coherence, conflicting signals, harness coverage.

### A8. Birgitta Böckeler — "Maintainability sensors for coding agents" (27 May 2026) [FETCHED]
- URL: https://martinfowler.com/articles/sensors-for-coding-agents.html
- "Internal quality problems affect AI agents in similar ways that they affect human developers."
- Lint thresholds with custom, self-correcting messages; dependency-cruiser rules as "a useful replacement for describing code structure in a markdown guide."
- "coverage is not a sufficient indicator of test effectiveness" — used mutation testing (Stryker).
- Agents skip sensors unless hooks enforce them; instruction-based triggering is "quite unreliable." Sensors "are not a magical solution to take the human totally out of the loop."

### A9. Thoughtworks Technology Radar Vol. 35 (November 2026) — themes, techniques, tools [FETCHED]
- URLs: https://www.thoughtworks.com/radar , https://www.thoughtworks.com/radar/techniques , https://www.thoughtworks.com/radar/tools
- Rings are now Adopt / Trial / Assess / **Caution** (no "Hold").
- Themes: "Harness engineering at scale" ("the harness is a living asset that requires ongoing ownership and maintenance"); "Beyond frontier models" ("We caution against blanket frontier model usage"); "Putting more agents to work" (review capacity and pipelines become the bottleneck; "human-in-the-loop theater"); "Constructing the AI factory" ("token economics ultimately comes down to infrastructure economics").
- **Adopt** (techniques): Agent sandboxing ("a sensible default for all agents"), Progressive context disclosure ("nearly universal in serious applications"), Mutation testing, Threat modeling.
- **Trial**: Unattended overnight agentic builds; Risk-tiered human oversight; Subagents for better context management (2-4 at a time; benefit not yet measured); Grilling (agent "interviews you about a plan before acting"); Self-improving harness ("bounded experiments with regression testing"); Feedback flywheel; Agent-maintained knowledge bases; Anchoring coding agents to a reference application; Coding harness for general-purpose agents; Agent plugin marketplace; Managed agents runtime; Open-weight models; Small language models; Stateful guardrails; Toxic flow analysis for AI; Interactive visual plans with agents; Graph-grounded codebase reasoning.
- **Assess**: Programmatic tool calling (Code Mode); Context profiling; Harness quality evaluation; Enterprise harness; Local coding models; Production-aware coding agents; Tests as data over tests as code; MITRE ATLAS.
- **Caution**: Agent instruction bloat (notes Anthropic "removed over 80%" of Claude Code's system prompt); Agent skill cognitive surrender; Human-in-the-loop theater; Meat proxy ("Don't be a meat proxy", KDE); Naive context compression ("token reduction means nothing if prompt caches break"); Blanket frontier model usage; Coding throughput as a measure of productivity; AI-driven documentation sprawl (names Spec-kit and BMAD); AI-accelerated shadow IT; Stacked pull requests ("often a workaround for poor upfront decomposition").
- Tools: **Adopt** OpenAI Codex, OpenCode, mise. **Trial** includes Beads, OpenSpec, Pi, mattpocock/skills, ast-grep, Agent Package Manager, Git AI, Sourcebot. **Assess** includes nono.sh, Habit Hooks, Entire CLI, DeepSeek Harness, GLM.
- Spec-driven development has no blip of its own in Vol. 35; it appears inside "Unattended overnight agentic builds" and "AI-driven documentation sprawl".

### A10. Thoughtworks Radar — GitHub Spec Kit blip (April 2026 edition, Assess) [FETCHED]
- URL: https://www.thoughtworks.com/radar/languages-and-frameworks/github-spec-kit
- Two camps: minimal structure relying on improving agents vs defined workflows with detailed specs.
- Teams used it mostly in brownfield code; the "constitution" concept was useful; problems were instruction bloat/context rot, verbose markdown, unnecessary defensive checks. Blip is not on the November 2026 edition.

### A11. Anthropic — "Harness design for long-running application development" (Prithvi Rajasekaran, 24 Mar 2026) [FETCHED]
- URL: https://www.anthropic.com/engineering/harness-design-long-running-apps
- Planner / generator / evaluator architecture; separate evaluator is easier to tune to be skeptical than a self-critical generator. Sprint contracts defining "done".
- Explicit record of scaffolding being removed as models improved: context resets needed for Sonnet 4.5 ("context anxiety") were dropped with Opus 4.5; the sprint construct was removed with Opus 4.6; per-sprint evaluation became one final QA pass.
- Cost data: solo run 20 min / $9 vs full harness 6 h / $200 (the solo run's core feature was broken).
- Out of the box Claude was a poor QA agent: it found issues and then talked itself into approving.

### A12. Anthropic — "How we contain Claude across products" (25 May 2026) [FETCHED]
- URL: https://www.anthropic.com/engineering/how-we-contain-claude
- Users approved roughly 93% of Claude Code permission prompts (approval fatigue) → sandbox + automated approvals; sandbox reported to cut prompts by 84%; "network is denied by default."
- Seatbelt (macOS) / bubblewrap (Linux) for Claude Code; gVisor for claude.ai code execution; full VM for Cowork.
- In a February 2026 internal red-team exercise Claude completed credential exfiltration 24 of 25 times after a phished employee ran a malicious prompt — the argument is that only environment-level controls (egress blocking, filesystem boundaries) stop this.
- An allowlisted domain (api.anthropic.com) was itself usable for exfiltration; fixed with a proxy bound to the session token.

### A13. Anthropic — "Redesigning source control at Anthropic" (13 Oct 2026) [FETCHED]
- URL: https://www.anthropic.com/engineering/redesigning-source-control
- "coding is no longer the bottleneck"; merged changes went from about 2,500/day (May 2026) to over 30,000/day (September 2026); about 25 million CI checkouts/day.
- They built a custom source-control system (Scion) and review tool; the engineers' main job was to say "no" when agents violated system constraints. Authors say it is "by no means a suitable replacement for git for general use."

### A14. Addy Osmani, Morgan Westlee Lunt, Qing Wang — "How the Claude Code team does code review" (15 Oct 2026) [FETCHED]
- URL: https://claude.dev/blog/solving-code-review-at-anthropic/ (488 points / 481 comments on HN, item 50122951)
- Goal: "the minimum amount of human review time that doesn't raise reverts or incidents."
- Layers: agent self-verification before the PR → multi-agent AI review with verifier voting → blocking security review → required CI → risk-tiered human approval (low: none; medium: one; high: two) → merge queue, flags, staged release → fast rollback.
- "The change sets the tier, not the author." "An agent's approval never counts as a person's, either." "A person is accountable for every change that ships, whoever typed it."
- Numbers (self-reported): Claude writes about 90% of Claude Code's code; June–September merged PRs "more than doubled while the share that had to be reverted fell by more than 40 percent"; incidents become a daily eval set for the reviewer; review-round cap after three rounds.
- Adoption checklist: runnable checks in a short CLAUDE.md, a REVIEW.md, PR template with "Testing", "Risk", "How to revert", CODEOWNERS for sensitive paths.

### A15. Anthropic engineering index [FETCHED] (list only)
- URL: https://www.anthropic.com/engineering
- 2026 posts listed: Components of agent memory (6 Nov), Redesigning source control (13 Oct), How we contain Claude (25 May), Claude Code quality postmortem (23 Apr), Scaling Managed Agents (8 Apr), Claude Code auto mode (25 Mar), Harness design (24 Mar), Eval awareness in BrowseComp (6 Mar), Building a C compiler with parallel Claudes (5 Feb), Infrastructure noise in agentic coding evals (5 Feb), AI-resistant technical evaluations (21 Jan), Demystifying evals for AI agents (9 Jan).
- [OLDER] still-referenced foundations: Effective harnesses for long-running agents (26 Nov 2025), Code execution with MCP (4 Nov 2025), Claude Code sandboxing (20 Oct 2025), Agent Skills (16 Oct 2025), Effective context engineering (29 Sep 2025), Writing effective tools for agents (11 Sep 2025), Multi-agent research system (13 Jun 2025), Claude Code best practices (18 Apr 2025).

### A16. OpenAI (Ryan Lopopolo) — "Harness engineering: leveraging Codex in an agent-first world" (11 Feb 2026) [SNIPPET — openai.com returned 403]
- URL attempted: https://openai.com/index/harness-engineering/
- From search summaries only: roughly a million lines built over five months with no manually written code; "give Codex a map, not a 1,000-page instruction manual"; plans as first-class artifacts; agent-to-agent review. Unverified against the primary.

### A17. Mitchell Hashimoto — "My AI Adoption Journey" (5 Feb 2026) [FETCHED]
- URL: https://mitchellh.com/writing/my-ai-adoption-journey
- Six steps: drop the chatbot; reproduce your own manual commits with agents; end-of-day agents ("block out the last 30 minutes of every day to kick off one or more agents"); outsource the slam dunks; engineer the harness; always have an agent running.
- Coined use of "harness engineering" for individuals: every agent mistake becomes an AGENTS.md line or a programmed tool.
- "turn off agent desktop notifications"; he does not run multiple agents in parallel.
- Concerned about skill formation for juniors.

### A18. Geoffrey Huntley — "Ralph Wiggum as a 'software engineer'" (14 Jul 2025) [FETCHED] [OLDER]
- URL: https://ghuntley.com/ralph/
- "In its purest form, Ralph is a Bash loop": `while :; do cat PROMPT.md | claude-code ; done`
- One task per loop; stable plan/spec files reloaded each iteration; subagents for expensive work; "Anything can be wired in as back pressure to reject invalid code generation."
- Best for greenfield, "with the expectation you'll get 90% done"; "engineers are still needed".
- 2026 follow-through: the loop pattern was absorbed into products (Codex `/goal`, see A1).

### A19. Dan Shapiro — "The Five Levels: from Spicy Autocomplete to the Dark Factory" (23 Jan 2026) [FETCHED]
- URL: https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/
- Level 0 manual → Level 3 "You are the human in the loop." → Level 4 "Then you leave for 12 hours, and check to see if the tests pass." → Level 5 "It's a black box that turns specs into software."

### A20. StrongDM (Justin McCarthy) — "Software Factories And The Agentic Moment" (6 Feb 2026) [FETCHED]
- URL: https://factory.strongdm.ai/
- Rules: code "must not be written by humans" and "must not be reviewed by humans."
- Scenarios kept outside the codebase as a holdout set; "satisfaction" as a probabilistic measure; Digital Twin Universe ("behavioral clones of the third-party services our software depends on").
- Benchmark claim: "$1,000 on tokens today" per engineer per day. Self-reported; no independent metrics.

### A21. Dex Horthy (HumanLayer) — "Why Software Factories Fail (or: harness engineering is not enough)" (no date on page; about July 2026) [FETCHED]
- URL: https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md (394 points / 272 comments on HN, item 49023019, posted 23 Jul 2026)
- Their own lights-off attempt (started July 2025) ended in a rewrite that took a cofounder "two whole weeks".
- Models are trained on pass/fail; "there is no penalty for eroding codebase maintainability" and "THERE ARE NO GOOD BENCHMARKS" for maintainability.
- Estimates agent-built codebases start to struggle after "maybe three to six months" (anecdotal).
- Practice: product review → architecture → program design (file-tree diffs, type signatures) → vertical slices reviewed 100–200 lines at a time. Roughly 40% of tasks are one-shot.
- Vendor-authored; he says he "can't prove" the decline.

### A22. Armin Ronacher — "What is Codemode" (6 Oct 2026) [FETCHED]
- URL: https://lucumr.pocoo.org/2026/10/6/codemode/
- Agent writes JavaScript that calls tools in a sandbox; composes calls and keeps large outputs out of context.
- MCP "is in fact a protocol that greatly benefits from Codemode"; in Pi "we do not actually expose any of the MCP tools to the LLM".
- On his earlier pro-CLI stance: "Is this a reversal of what I wrote a year ago where I encouraged CLIs? I don't think so."

### A23. Armin Ronacher — "Fast and Hard Code" (22 Aug 2026) [FETCHED]
- URL: https://lucumr.pocoo.org/2026/8/22/fast-hard-code/
- "LLMs make language choice much less consequential than it used to be."
- More people take on hard domains (eBPF, DWARF, custom drivers); performance work via agent loops ("you just need to put an agent on it").
- Also read: "AI and Irontown" (9 Nov 2026), https://lucumr.pocoo.org/2026/11/9/irontown/ [FETCHED] — an essay on polarization around AI; no engineering practices.

### A24. Charles Chen — "MCP is Dead; Long Live MCP!" (14 Mar 2026) [FETCHED]
- URL: https://chrlschn.dev/blog/2026/03/mcp-is-dead-long-live-mcp/
- CLI token savings "might not be as dramatic as social media would have you believe" and mostly apply to CLIs already in training data.
- Local stdio MCP is often unnecessary; remote HTTP MCP gives organizations central OAuth, revocation and telemetry.
- "MCP Prompts are effectively server-delivered SKILL.md"; "CLI and MCP are not mutually exclusive".

### A25. MCP vs CLI vs skills — search round-up (2026) [SNIPPET]
- Search on 2026-11-12; pages not read: https://manveerc.substack.com/p/mcp-vs-cli-ai-agents , https://www.checklyhq.com/blog/mcp-vs-cli-token-efficiency/ , https://david.coffee/i-still-prefer-mcp-over-skills/ , https://hackernoon.com/mcp-is-dead-the-cli-is-winning-the-ai-agent-stack
- Reported claims (unverified): eager loading of all tool schemas is the real cost; clients now defer tool definitions; Perplexity's CTO reportedly said in March 2026 they were moving away from MCP internally.

### A26. Agent Skills open standard [FETCHED]
- URL: https://agentskills.io/ (no date on page)
- A skill is a folder with a `SKILL.md` (name + description minimum) plus optional scripts/references/assets.
- Progressive disclosure in three stages: discovery (name/description only), activation (full SKILL.md), execution.
- "originally developed by Anthropic, released as an open standard".

### A27. AGENTS.md [FETCHED]
- URL: https://agents.md/ (no date on page)
- "a README for agents"; stewarded by the Agentic AI Foundation under the Linux Foundation; used by "over 60k open-source projects"; nearest file in the tree wins.
- HN front page, 18 Sep 2026: "Claude Code now reads AGENTS.md if there is no Claude.md" (741 points, item 49760187; link target https://code.claude.com/docs/en/changelog not fetched).

### A28. METR — "We are Changing our Developer Productivity Experiment Design" (24 Feb 2026) [FETCHED]
- URL: https://metr.org/blog/2026-02-24-uplift-update/
- Early-2025 RCT: tasks took +19% longer with AI (CI +2% to +39%). [OLDER result]
- Late-2025 follow-up (57 developers, 143 repos, 800+ tasks): returning developers −18% time (CI −38% to +9%); new developers −4% (CI −15% to +9%).
- Selection problem: "30% to 50% of developers told us that they were choosing not to submit some tasks" they did not want to do without AI; estimate is "likely a lower-bound"; time tracking breaks when developers run several agents concurrently.

### A29. Pragmatic Engineer (Gergely Orosz, Elin Nilsson) — "AI Tooling for Software Engineers in 2026" (3 Mar 2026) [FETCHED — free part]
- URL: https://newsletter.pragmaticengineer.com/p/ai-tooling-2026
- Survey 27 Jan–17 Feb 2026, 906 responses. Claude Code went "from zero to be the #1 tool in only eight months."
- 95% use AI tools at least weekly; 56% do 70%+ of their work with AI; 70% use two to four tools.
- 55% regularly use agents (staff+ engineers 63.5%).
- Small companies: Claude Code 75%; 10,000+ employee companies: GitHub Copilot 56%.

### A30. Pragmatic Engineer — "The impact of AI on software engineers in 2026: key trends, Part 1" (14 Apr 2026) [FETCHED — free part]
- URL: https://newsletter.pragmaticengineer.com/p/the-impact-of-ai-on-software-engineers-2026
- About 30% have hit usage limits; companies typically fund roughly $100–200/month per engineer; many expect prices to rise.
- Archetypes: Builders (more "slop" to debug, identity loss), Shippers (most enthusiastic), Coasters.
- Engineers orchestrate and context-switch more; EM and IC roles converge.

### A31. Stack Overflow Developer Survey 2026 — AI section [FETCHED]
- URL: https://survey.stackoverflow.co/2026/ai (survey dates not stated on page; per-chart n between 10,926 and 13,857)
- Coding assistants/agents are the top AI use case (66%); 73% of those use them daily; 30.9% of daily users spend 4+ hours/day.
- Trust: 48% trust AI when they can easily validate answers.
- Coding agents: Claude Code 66%, GitHub Copilot 59%. Orchestration: LangChain 30%, OpenAI Agents SDK 24%.
- Reasons to avoid AI: losing job skills 17.1%, ethical concerns 15.2%, privacy/security 13.0%.

### A32. JetBrains Developer Ecosystem / AI coding agent adoption 2026 (Aug 2026) [SNIPPET — blog.jetbrains.com returned 403]
- URLs attempted: https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/ , https://blog.jetbrains.com/research/2026/08/how-much-code-do-developers-really-let-agents-write/
- From search summary only: 15,000+ respondents, May–July 2026; roughly 90% of professional developers use coding agents at work weekly and 68% daily. Unverified.

### A33. DORA — "ROI of AI-assisted Software Development" (2026) [SNIPPET] and "Impact of Generative AI in Software Development" page [FETCHED]
- URL fetched: https://dora.dev/dora-report-gen-ai (page updated 13 Apr 2026; this is the older gen-AI impact report)
  - "a 25% increase in AI adoption is associated with a 1.5% decrease in delivery throughput" and a 7.2% drop in delivery stability, tied to larger batch sizes. [OLDER finding — from the 2024-era report]
  - "Organizations with clear AI acceptable-use policies show a 451% increase in AI adoption".
- ROI report (PDF https://services.google.com/fh/files/misc/dora-roi-of-ai-assisted-software-development-2026.pdf — not read): search summaries say it describes a J-curve (temporary productivity dip) and repeats the "AI as amplifier" framing from the 2025 report. Unverified.

### A34. Faros AI — "AI Engineering Report 2026: The Acceleration Whiplash" takeaways (12 Apr 2026) [FETCHED]
- URL: https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways
- Telemetry from 22,000 developers / 4,000+ teams, comparing low- vs high-AI-adoption periods (correlational; vendor).
- Task throughput per developer +33.7%; PR merge rate +16.2%.
- Code churn +861%; incidents-to-PR ratio +242.7%; bugs per developer +54%.
- Median time to first PR review +156.6%; PRs merged with no review at all +31.3%.
- Claims strong DevOps foundations did not insulate teams — explicitly contrasted with DORA 2025.

### A35. Veracode — GenAI Code Security Report, October 2026 update (press release 29 Oct 2026) [FETCHED]
- URL: https://www.veracode.com/?p=33104
- Average security pass rate rose from 56% (July 2026) to 62%; described as "the most significant improvement since the GenAI Code Security Report series began in July 2025."
- XSS (CWE-80) pass rate only 18%; log injection 13%; SQL injection 84%.
- Java 31% vs Python 64%. Best models 73%.

### A36. CodeRabbit — "State of AI vs Human Code Generation" (Dec 2025) [SNIPPET] [OLDER]
- URL (not read): https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report
- Search summary: 470 open-source PRs; AI-co-authored PRs averaged about 10.83 issues vs 6.45 for human PRs. Unverified.

### A37. James Shore — "You Need AI That Reduces Maintenance Costs" (10 May 2026) [FETCHED]
- URL: https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs (380 points on HN)
- If an agent doubles output and maintenance per unit, "Gains erased after 5 months"; even at equal maintainability, "Gains erased after 19 months".
- "you have to invert your productivity": twice the output needs half the maintenance cost. Illustrative model, not data.

### A38. Addy Osmani — "Comprehension Debt" (14 Mar 2026) [FETCHED]
- URL: https://addyosmani.com/blog/comprehension-debt/
- "AI generates code far faster than humans can evaluate it."; "What used to be a quality gate is now a throughput problem."
- Cites an Anthropic trial with 52 engineers: AI-assisted participants scored "17% lower on a follow-up comprehension quiz (50% vs. 67%)".
- "Tests are necessary. They are not sufficient."
- Also [SNIPPET]: "The 80% Problem in Agentic Coding" (28 Jan 2026), https://addyosmani.com/blog/the-80-problem-in-agentic-coding/ — not read.

### A39. Lars Faye — "Agentic Coding Is a Trap" (April 2026) [FETCHED]
- URL: https://larsfaye.com/articles/agentic-coding-is-a-trap (463 points / 375 comments on HN, item 48002442)
- Supervision paradox (quoting Anthropic): "supervising Claude requires the very coding skills that may atrophy from AI overuse."
- "An employee's cost is fixed; tokens are a constantly moving target."; vendor outages stop whole teams.
- Own rule: never generate more than he "can review in a sitting."

### A40. .txt (dottxt) blog — "The bottleneck was never the code" (29 Apr 2026) [FETCHED]
- URL: https://www.thetypicalset.com/blog/thoughts-on-coding-agents (586 points / 414 comments on HN)
- "The bottleneck moves from the people writing the code to the people deciding what code should exist."
- "Agents cannot do osmosis."; "The new moat is organizational, not technical".

### A41. Marc Brooker (AWS; Kiro) — waterfall vs spec-driven development (URL dated 9 Apr 2026) [FETCHED]
- URL: https://brooker.co.za/blog/2026/04/09/waterfall-vs-spec
- Spec-driven development pulls designs "up", not "up-front"; "the specification is the thing being iterated on, rather than the implementation."
- Claims "the largest improvements in velocity and delivery" come from teams letting agents run for long periods.
- Counter-view [SNIPPET]: several 2026 posts call Kiro/Spec Kit "waterfall for AI" (search results only; e.g. "Spec-Driven Development: The Waterfall Strikes Back").

### A42. Hacker News — "Ask HN: What's your current AI agentic setup?" (4 Nov 2026; 571 points, 713 comments) [FETCHED — first ~20% of thread]
- URL: https://news.ycombinator.com/item?id=50366117
- Recurring working practices: plan with one model, implement/review with another; write explicit done criteria ("the biggest trick is just to tell it what complete looks like"); AGENTS.md/CLAUDE.md; multi-model review.
- Disagreements: top-tier model vs cheaper tier; cheap open-weight models via OpenCode/Pi vs subscriptions ("In practice all of these open models are more expensive than a Claude subscription."); whether to use agents at all ("zero usage" policy vs "missing out on a great tool").
- Failure reports: oversized diffs, burnout from running many agents ("You are going to burn out so badly").
- Still present: "I still review every line as though a human wrote it."

### A43. Hacker News — top 2026 stories on coding agents (Algolia API listing, May–Nov 2026) [FETCHED — titles/points only]
- URLs: https://hn.algolia.com/api/v1/search?query=coding%20agents&tags=story&numericFilters=created_at_i%3E1777593600,points%3E300&hitsPerPage=40 and the same with query=claude%20code, points>400
- Security/trust incidents dominate the top of the list: "Claude Code's 'Don't Ask Again' exposes passwords in 1,122 public GitHub files" (626 pts, 7 Nov 2026); "Backdoor in Claude Code for VS Code extension on the Cursor Marketplace" (1,013 pts, 30 Oct 2026); "Claude Code is steganographically marking requests" (2,445 pts, 30 Jun 2026); "Claude Code sends your email address to websites" (1,615 pts, 5 Nov 2026).
- Cost/overhead: "Claude Code sends 33k tokens before reading the prompt; OpenCode sends 7k" (706 pts, 12 Jul 2026); "Uber torches 2026 AI budget on Claude Code in four months" (402 pts, 1 May 2026); "Goldman Sachs is pulling Claude Code from its bankers and traders" (902 pts, 8 Nov 2026).
- Skeptic pieces: "AI coding agents generate more code, but not more software" (Ars Technica, 365 pts, 12 Oct 2026 — article not readable); "Agentic Coding Is a Trap" (A39).
- Open/local: DeepSeek-native agents, "How to setup a local coding agent on macOS" (507 pts), open-weight coding model launches.
- Only titles and scores were read for these; the linked articles were not (except where they have their own entry).

### A44. Andrej Karpathy — "agentic engineering" naming (Feb 2026) and Sequoia AI Ascent talk (Apr 2026) [SNIPPET]
- Search results only (thenewstack.io returned 403). Reported: on the one-year anniversary of "vibe coding" he wrote that his "current favorite" name for the professional practice is "agentic engineering"; sources disagree on the exact day (4, 5 or 8 Feb 2026). Talk quotes circulating in secondary blogs are unverified.

### A45. Steve Yegge — Gas Town / Beads (Jan–Feb 2026) [SNIPPET]
- Search results only. Gas Town described as a Go orchestrator running 20–30 parallel agents with named roles on top of Beads (git-stored task units). Podcast: https://softwareengineeringdaily.com/2026/02/12/gas-town-beads-and-the-rise-of-agentic-development-with-steve-yegge/ (not read).
- Verified adjacent facts: Beads is in the Thoughtworks Radar Vol. 35 Trial ring (A9); Simon Willison logged a public Yegge vs Google dispute on AI adoption on 13 Apr 2026 (A1).

### A46. Kent Beck — "augmented coding" series [SNIPPET]
- Search results only (posts largely paywalled): "Is Source Code Going Away?" (6 Feb 2026), "Smalltalk Genie" (21 Jun 2026); 2025 posts on persistent prompting and test-first with the "genie" [OLDER].

### A47. Peter Steinberger; Thorsten Ball / Amp [SNIPPET]
- Search results only. Steinberger: "closing the loop" (agents must be able to compile, lint, run and validate themselves); Pragmatic Engineer podcast title "I ship code I don't read". Ball: asks agents for "irrefutable proof that it works". Unverified secondary summaries.

### A48. Rahul Garg — "The Orchestrator's Tax" (16 Jul 2026) [FETCHED]
- URL: https://martinfowler.com/articles/orchestrator-tax.html
- "the real value of a subagent is what it keeps out of that context, not how fast it runs."
- Observed costs of parallel subagents: status polling pulled "tens of thousands of tokens of JSONL" into the main thread; duplicated orientation; one agent ran git stash while siblings wrote to the same tree.
- Rules added to CLAUDE.md: two to four agents per wave; no polling of full transcripts; no repository-wide git operations in concurrent agents; overlapping file ownership means merge the tasks. Thresholds tuned to one model and workflow; token costs were self-assessed, not measured.

### A49. Eugene Yan — "How to Work and Compound with AI" (May 2026) [FETCHED]
- URL: https://eugeneyan.com/writing/working-with-ai/
- "every finished artifact... becomes context for the next session"; per-project CLAUDE.md as "the onboarding doc we'd hand to a new teammate on day one."
- "A long CLAUDE.md can become a context tax." → lazy-loaded guides; "If you do something ≥ once a week, make it a skill."
- "Shift verification left; catch errors at write time."; "You can't delegate what you can't verify".
- Runs three to six parallel sessions with git worktrees; the bottleneck moves to writing specs and reviewing output; mines past transcripts for correction phrases to find config gaps.

### A50. Latent Space (Richard MacManus) — AI Engineer World's Fair 2026 coverage [FETCHED]
- URLs: https://www.latent.space/p/aiewf-daily-dispatch-locomotives (3 Jul; year not shown on page, event is AIEWF 2026) and https://latent.space/p/aiewf26trends (14 Jul)
- "Great loops debate": for loops — Geoffrey Huntley (loops are "inevitable") and Ian Livingstone (verifiability is what matters); skeptics — Dex Horthy ("the hype is outrunning the discipline") and Greg Pstrucha (can't solve problems just by buying more tokens). No winner recorded.
- Five trends: systems around agents (harness) over agents themselves; "loop engineering" (Steinberger: "the agent runs the inner execution loop; I set the direction and I make decisions in the outer loop."); enterprise forward-deployed engineers; coding agents replacing IDEs as the interface; every platform building around skills (Matt Pocock: fewer, smaller skills).
- Survey line reported from Barr Yaron's talk: 59% fear today's AI-generated code is creating long-term liabilities.

### A51. Simon Willison — "LLM predictions for 2026, shared with Oxide and Friends" (8 Jan 2026) [FETCHED]
- URL: https://simonwillison.net/2026/Jan/8/llm-predictions-for-2026/
- See the predictions section (A-5) below.

### A52. Martin Fowler — "November Inflection" (1 May 2026) [FETCHED]
- URL: https://martinfowler.com/bliki/NovemberInflection.html
- Names November 2025 (Opus 4.5 with the Claude Code harness; GPT-5.2) as the turning point for agentic programming; quotes Willison that models tipped "across an invisible capability line."

---

## A. Synthesis — Track A

### A-1. Practices with broad agreement that look durable
1. **Verification is the core skill; the agent must be able to check its own work.** Willison A4 ("confidently verify"), Cherny A5/A14 (verification makes results "two to three times better"), Yan A49 ("You can't delegate what you can't verify"), Hashimoto A17, Huntley A18 ("back pressure"), Böckeler A7/A8 (sensors), Radar A9. Stated across vendors, consultancies and independents, from mid-2025 to Nov 2026.
2. **Harness engineering: turn every repeated mistake into a guide or a deterministic check.** Hashimoto A17, Böckeler A7, Fowler A6, Radar A9 theme, Claude Code team A14, OpenAI A16 (snippet). The term spread in Feb–Apr 2026; the underlying practice (lint, types, tests, hooks, architecture rules) is old and stable.
3. **Keep instruction files short; load detail on demand (progressive disclosure).** Radar A9 (Adopt; "Agent instruction bloat" in Caution), Agent Skills spec A26, Yan A49, Spec Kit blip A10, Anthropic memory post B4 (only first 200 lines of MEMORY.md are loaded).
4. **Sandbox agents by default; rely on environment-level controls, not approval prompts or classifiers alone.** Radar A9 (Adopt), Anthropic A12 (93% of prompts approved; 24/25 exfiltration in red-team), Willison B24 entries, HN incidents A43.
5. **Human accountability stays with a named person; review depth is tiered by risk.** Claude Code team A14, Radar A9 (Risk-tiered human oversight; Human-in-the-loop theater; Meat proxy), Fowler A6, Osmani A38.
6. **Plan/spec before code for anything non-trivial, in small slices, with explicit "done" criteria.** Horthy A21, Brooker A41, HN A42, Anthropic A11 (sprint contracts), Radar A9 (Grilling), Hashimoto A17 (separate planning from execution). Agreement is on the habit, not on any SDD tool (see contested).
7. **Subagents and fresh-context reviewers are for context isolation.** Garg A48, Radar A9, Anthropic A11/B6, Yan A49, Claude Code team A14.
8. **Standard software-delivery hygiene matters more, not less:** small changes, CI, merge queue, feature flags, fast rollback, mutation testing. A14, A9, A8, A33.
9. **Review, not generation, is the bottleneck.** Faros A34, Osmani A38, Anthropic A13/A14, Radar A9, dottxt A40, Yan A49.
10. **Throughput/lines/token counts are bad productivity measures.** Radar A9 (Caution), METR A28 (self-reports unreliable), Shore A37, Faros A34.

### A-2. Contested topics
- **Must a human read every line?** No/tiered: Claude Code team A14, StrongDM A20 (no human review at all), Willison A3/A4 (no longer reviews everything, feels uneasy). Yes or mostly: Faye A39, Osmani A38, HN commenters A42, Horthy A21 (review 100–200 lines at a time).
- **Software/dark factories and unattended loops.** For: StrongDM A20, Shapiro A19, Huntley A18/A50, Brooker A41. Against/caution: Horthy A21 ("harness engineering is not enough"), Pstrucha A50, Faye A39, Shore A37. Radar puts overnight builds in Trial with heavy preconditions.
- **Spec-driven development frameworks (Kiro, Spec Kit, OpenSpec, BMAD).** Brooker A41 defends; Radar had Spec Kit at Assess in April 2026, lists OpenSpec in Trial in Nov 2026, and warns about documentation sprawl naming Spec-kit and BMAD; "waterfall for AI" critiques (snippets, A41).
- **MCP vs CLI vs skills vs code mode.** Chen A24 (remote MCP for organizations, CLI locally), Ronacher A22 (code mode makes MCP useful; do not expose MCP tools directly), MCP maintainers B19/B20 (protocol rewritten to be stateless), CLI-first camp (snippets A25).
- **Parallel agents: how many?** Hashimoto A17 runs one; Garg A48 and Radar say two to four; Yan A49 three to six; Steinberger 5–10 (snippet A47); Gas Town 20–30 (snippet A45). HN A42 reports burnout.
- **Does it make teams faster?** METR A28 cannot measure it cleanly; Faros A34 shows more throughput with more incidents and bugs; Faros contradicts DORA 2025 on whether strong foundations protect teams; Pragmatic Engineer A29/A30 shows high self-reported use.
- **Frontier model for everything vs cheaper/open models.** Radar A9 cautions against blanket frontier use; HN A42 split on whether open-weight models are really cheaper.
- **Skill atrophy.** Faye A39, Osmani A38 (cites Anthropic 52-engineer trial), Hashimoto A17 (juniors), Stack Overflow A31 (17.1% avoid AI for fear of losing skills) vs Willison A3 ("amplifiers of existing experience"), Ronacher A23 (more people tackle hard domains).
- **Security of generated code.** Veracode A35 shows 62% pass rate and weak XSS/log-injection results; Cherny A5 argues for a higher bar plus automated security review.

### A-3. What changed or was deprecated in 2025–2026 (evidence of fast-moving topics)
- **Tool leadership flipped within eight months:** Claude Code from zero to #1 (A29); Radar Vol. 35 puts OpenAI Codex and OpenCode in Adopt (A9); Copilot remains strongest only in very large companies (A29).
- **Harness scaffolding removed as models improved:** context resets, sprint decomposition, per-sprint evaluation (A11); Anthropic "removed over 80%" of Claude Code's system prompt (A9).
- **Ralph went from a blog-post bash loop (Jul 2025) to a built-in product feature (Codex `/goal`, Apr 2026)** (A18, A1).
- **Instruction-file fragmentation converged:** AGENTS.md under the Linux Foundation; Claude Code reads AGENTS.md as of Sep 2026 (A27).
- **Skills went from an Anthropic feature (Oct 2025) to an open standard that "every agent platform" builds on (mid-2026)** (A26, A50).
- **MCP was redesigned:** stateless core, sessions and handshake removed, Roots/Sampling/Logging deprecated (B20). "Code mode"/programmatic tool calling appeared as an alternative way to consume tools (A22, A9).
- **Vocabulary churn:** vibe coding (Feb 2025) → context engineering (mid-2025) → agentic engineering (Feb 2026) → harness engineering (Feb–Apr 2026) → loop engineering (mid-2026) (A44, A6, A7, A50).
- **Spec Kit:** Assess in April 2026, absent from the November 2026 Radar (A10, A9).
- **Permission prompts → sandbox + auto mode by default** (A12, B24 entry of 8 Aug 2026).
- **Radar ring "Hold" renamed "Caution"** (A9). **Stacked PRs** moved into Caution.
- **Programming-language lock-in weakened:** Bun ported Zig → Rust with agents (A1, A23).
- **Productivity evidence aged quickly:** the 2025 "19% slower" result no longer describes late 2025 and METR had to redesign the study (A28).

### A-4. Skills that teams/employers say are missing
- Verifying and reviewing agent output at volume (A4, A34: time-to-first-review +156.6%; A38).
- Writing well-formed specs and decomposing work up front (A40, A49, Radar note on stacked PRs A9).
- Building and maintaining the harness: checks, hooks, evals for the reviewer (A7, A14, A9 "living asset").
- Security of agents and of generated code: sandboxing, toxic-flow analysis, secrets hygiene (A12, A35, A43).
- Deep technical/debugging skill retention (A38, A39; B9: erosion of deep technical skills is the most common negative effect).
- Cost awareness: token overhead, usage limits, model tiering (A30, A43, A9).
- Product judgment — deciding what should exist (A1 Voss, A40).
- Organizational gaps: DORA page links dedicated learning time and clear acceptable-use policies to adoption (A33).

### A-5. Predictions explicitly made by named sources (PREDICTIONS, not findings)
- **Simon Willison (8 Jan 2026, A51), 1-year horizon:** LLM code quality becomes undeniable ("Those people are in for a very nasty shock in 2026."); sandboxing gets solved ("I think this year is the year"); a "Challenger disaster with respect to coding agent security". **3-year (2029):** "We will find out if the Jevons paradox saves our careers or not."; a browser built mostly with AI assistance. **6-year (2032):** "I do not think anyone will be paid to just to do the thing where you type the code."
- **Geoffrey Huntley (reported by Latent Space, Jul 2026, A50):** next year's conference (2027) will include speakers admitting that their factories and loops failed.
- **Pragmatic Engineer respondents (Apr 2026, A30):** many expect AI tool prices to rise and usage caps to follow.
- **Dex Horthy (about Jul 2026, A21):** agent-built codebases start to struggle after "maybe three to six months" (an estimate, anecdotal).
- **Gartner [SNIPPET, unverified, secondhand]:** by 2027 over 65% of engineering teams using agentic coding will treat the IDE as optional.
- No explicit 2027 prediction was found from Fowler, Böckeler, Karpathy or Anthropic in the pages read.

---

# TRACK B — AI engineering (LLM applications)

## B. Source catalogue

### B1. Hamel Husain & Shreya Shankar — AI Evals FAQ (published 18 Sep 2026, modified 21 Sep 2026) [FETCHED — read in two parts]
- URL: https://hamel.dev/blog/posts/evals-faq/
- Error analysis is "the most important activity in evals."; "Always read through the raw traces yourself at the start."; "Never skip this or delegate it."
- "Binary evaluations force clearer thinking and more consistent labeling."; one judge per failure mode, validated against human labels with train/dev/test splits.
- "Generic evaluations waste time and create false confidence when you use them as quality measures."
- Writing evaluators before features exist "creates more problems than it solves."; they report spending "60-80% of our development time on error analysis and evaluation."
- RAG: "The retrieval component is a search problem" (Recall@k, Precision@k, MRR). On "RAG is dead": "The question isn't whether to use retrieval, but how to retrieve effectively."
- Agents: first judge end-to-end success as a black box, then step-level diagnostics and transition-failure matrices.
- Guardrails (inline, fast, deterministic) vs evaluators (after the fact, nuanced). CI uses small curated sets; production monitoring samples live traces; feed failures back.
- Tools: build a custom annotation tool; no favorite vendor.

### B2. Eugene Yan — "Product Evals in Three Simple Steps" (Nov 2025) [FETCHED] [OLDER]
- URL: https://eugeneyan.com/writing/product-evals/
- Label data → align the LLM evaluator → run the harness on every change.
- "Focus on binary pass/fail or win/lose labels."; "Aim for 50-100 fail cases"; "Have one evaluator per dimension".
- "benchmark is human performance, not perfection"; includes sample-size arithmetic (200 samples at 3% defects gives about ±2.4%).
- 2026 posts on his index (not read): "Patterns for Building Cybersecurity Evals" (21 Jun 2026), "Using LLMs to Secure Source Code" (27 May 2026). Index: https://eugeneyan.com/writing/ [FETCHED].

### B3. Anthropic — "Demystifying evals for AI agents" (9 Jan 2026) [FETCHED]
- URL: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Vocabulary: task, trial, transcript, outcome; code-based vs model-based vs human graders.
- Capability evals (start at low pass rate) vs regression evals (near 100%); capability evals "graduate" into regression suites.
- pass@k vs pass^k (75% per trial → about 42% for all of three trials).
- Start with 20–50 tasks from real failures; grade outcomes not paths; read transcripts; watch for saturation; assign ownership.

### B4. Anthropic (Lance Martin) — "The components of agent memory" (6 Nov 2026) [FETCHED]
- URL: https://www.anthropic.com/engineering/components-of-agent-memory
- File-based memory plus "dreaming" (offline review of logs to fix or add notes).
- Tell the model "what memory is for, but not _how_ to use it."; a "record only failures" rule reduced the gain.
- Memory benefit depends heavily on model generation (large gain for the newest model, almost none for an older one).
- Wiki + search beat search alone (61% vs 53%) on one corpus; wikis can grow "larger than the documents themselves"; per-entity pages with direct quotes avoided fact loss.
- Open questions: in-session vs background writing, compute cost of keeping memory current.

### B5. Anthropic — "Scaling Managed Agents: Decoupling the brain from the hands" (8 Apr 2026) [FETCHED]
- URL: https://www.anthropic.com/engineering/managed-agents
- Three parts: session (append-only log), harness (the loop), sandbox (execution). Harness moved out of the container: "The container became cattle."
- Session log outside the harness allows resume after a crash.
- Credentials never reach generated code: "the tokens are never reachable from the sandbox where Claude's generated code runs."

### B6. Anthropic — "Effective context engineering for AI agents" (29 Sep 2025) [FETCHED] [OLDER]
- URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Context engineering = "curating and maintaining the optimal set of tokens" at inference.
- Compaction, structured note-taking, sub-agents with clean context, just-in-time retrieval via "lightweight identifiers (file paths, stored queries, web links, etc.)".
- "minimal viable set of tools".

### B7. Anthropic (Erik Schluntz, Barry Zhang) — "Building effective agents" (19 Dec 2024) [FETCHED] [OLDER]
- URL: https://www.anthropic.com/engineering/building-effective-agents
- Workflows ("predefined code paths") vs agents (LLMs "dynamically direct their own processes and tool usage").
- Patterns: prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer.
- Find "the simplest solution possible"; with frameworks, "ensure you understand the underlying code."; "Poka-yoke your tools".
- Still the reference vocabulary in 2026 sources.

### B8. LangChain — "State of Agent Engineering" (published 12 Jun 2026; survey 18 Nov–2 Dec 2025; N=1,340) [FETCHED]
- URL: https://langchain.com/state-of-agent-engineering
- 57.3% have agents in production (51% a year earlier).
- Top barrier: quality (32%); latency 20%; security 24.9% in 2k+ employee orgs.
- 89% have some observability, 62% detailed tracing; offline evals 52.4%, online evals 37.3%, "not evaluating" 29.5%; human review 59.8%; LLM-as-judge 53.3%.
- Over three-quarters use multiple models; 57% are not fine-tuning. Vendor survey of its own community.

### B9. Amplify Partners (Barr Yaron) — "The 2026 AI Engineering Report" (page date 07-02-2026; 1,000+ respondents, with Notion and Vercel) [FETCHED]
- URL: https://www.amplifypartners.com/blog-posts/the-2026-ai-engineering-report
- 87% use multiple models (44% route by task type, 11% by cost); 45% use open-weight models, and over 90% of those also use closed models.
- Among agent-using teams, 89% have agents with write permissions (52% a year earlier); top guardrails are human approval and permission gating; no consensus on monitoring.
- 61% say hallucinations are where agents fail most. Almost 50% use some form of RAG. Most adapt behavior mainly by editing prompts.
- 40% say cost regularly shapes how ambitiously they use AI.
- Only 4% say their stack is working well. 93% report negative effects, most commonly erosion of deep technical skills. 51% of respondents with 10+ years of software experience have 3 or fewer years of AI experience.

### B10. Latent Space — AIEWF 2026 dispatch and "5 Trends" [FETCHED] (same pages as A50)
- URLs: https://www.latent.space/p/aiewf-daily-dispatch-locomotives , https://latent.space/p/aiewf26trends
- Yaron quoted: "Nobody has settled the control layer for agents."; 95% of respondents use agents; token usage is the second-most monitored production metric after quality.
- Trend: attention moved from the agent to the system around it (workflows, context, permissions, evaluation, persistent state); skills reduce the need for orchestration code (Philipp Schmid).

### B11. Sarang Kulkarni (Thoughtworks) — "Building Reliable Agentic AI Systems" (Bayer case, 16 Jun 2026) [FETCHED]
- URL: https://martinfowler.com/articles/reliable-llm-bayer.html
- "Larger context windows did not remove the need to be selective about what each agent sees."
- Hybrid retrieval (metadata filter + semantic 0.7 + keyword 0.3) with cross-encoder rerank from about 20 chunks to 7.
- Text-to-SQL limited to SELECT with up to three retries; an LLM review step for SQL was removed because it rejected valid queries.
- Persisted workflow state for resume; provider fallback; citations to page and quote; dataset evals on every change plus daily batch evals on live traffic; low-confidence extractions "quarantined and flagged for human review".

### B12. Kiran Prakash (Thoughtworks) — "Long-horizon agents and durable execution" (10 Nov 2026) [FETCHED]
- URL: https://martinfowler.com/articles/durable-execution-agents.html
- "the business rules that matter are in code, not in the prompt".
- Durable does not mean correct: idempotency keys, compensating actions, approvals with expiry, re-check facts before irreversible actions.
- Limit the model to `allowed_tools`; accept approvals only from authorized people so injected text cannot approve.
- Tested on Temporal and Cloudflare; waiting workflows used no CPU.

### B13. Pramod Sadalage, Prem Chandrasekaran — "Making Your Data Ready for Agentic AI" (27 Aug 2026) [FETCHED]
- URL: https://martinfowler.com/articles/making-data-ready-for-agentic-ai.html
- Layers: trusted data foundation → context layer (domain, semantic, capability models as code) → governed access, with observability across all.
- Data contracts with freshness SLAs and quarantine: "Bad data lands in a dead-letter queue, never in front of the agent."
- Naive API-to-MCP conversion causes "tool sprawl"; design five to ten business capabilities with declared permissions, owner and reversibility.
- Retrieved text may inform but must never gate an action. Staged autonomy from shadow mode to full autonomy. Cites EU AI Act Articles 12 and 19 (logging) and the lethal trifecta.

### B14. Kuba Rogut (turbopuffer) — "RAG is dead, right??" (AI Engineer Europe talk; page dated 9 Jun 2026) [FETCHED]
- URL: https://turbopuffer.com/blog/video-rag-is-dead-right
- "retrieval is not just vector search."; one-shot embed-search-stuff is being replaced by iterative multi-tool retrieval (BM25, grep, glob, regex, filters, semantic).
- "embeddings and semantic search are kind of cache compute."
- Says Claude Code does not use vector search; cites Cursor's internal claim that semantic search adds roughly 12.5% answer accuracy (unpublished). Vendor talk.

### B15. Mintlify — "How we built a virtual filesystem for our assistant" (24 Mar 2026) [FETCHED]
- URL: https://www.mintlify.com/blog/how-we-built-a-virtual-filesystem-for-our-assistant (411 points on HN)
- Chunk-level RAG struggled with multi-page answers and exact syntax; sandboxes per conversation were slow (p90 about 46 s) and would cost "north of $70,000 a year".
- Replaced with a virtual read-only filesystem over the existing Chroma index: grep/ls/cat tools for the agent; session creation about 100 ms; access control by pruning the file tree per user.

### B16. Rafael Pierre — "RAG Is Simpler Than You Think" (Lighthouse newsletter, 10 Jun 2026) [FETCHED]
- URL: https://www.lighthousenewsletter.com/p/rag-is-simpler-than-you-think (516 points on HN, posted 26 Aug 2026)
- "most people seem to over-engineer their Retrieval Augmented Generation (RAG) stack."
- Start with full-text search plus LLM query rewriting; "For proprietary terms, exact keyword matching beats semantic understanding."
- Rule of thumb (author's own, unsourced): "60% of systems should stop at full-text plus query rewriting."

### B17. Jason Liu — "Sunsetting 567 Labs and Open Sourcing the Course Content" (2 Feb 2026) [FETCHED]
- URL: https://jxnl.co/writing/2026/02/02/sunsetting-567-labs/
- Closed his RAG courses on 2 Feb 2026 and open-sourced the content; no reason given.
- RAG playbook summary: "Product mindset over one-off implementation"; measurement and feedback loops first; synthetic eval data for cold start; specialized retrieval and routing.
- His 2026 writing index is almost entirely about Codex workflows (https://jxnl.co/writing/ [FETCHED]); sidebar links to Sept 2025 pieces titled "Grep Beats Embeddings", "No Multi-Agents", "Stopped Using RAG" (not read).

### B18. MCP maintainers (David Soria Parra) — "The 2026 MCP Roadmap" (9 Mar 2026) [FETCHED]
- URL: https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/
- Priorities: transport scalability ("stateful sessions fight with load balancers."), agent communication (Tasks), governance, enterprise readiness (audit trails, SSO auth, gateways).
- "we are not adding more official transports this cycle."

### B19. MCP maintainers — 2026-07-28 specification release candidate (21 May 2026) [FETCHED]
- URL: https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- Breaking: initialize handshake and protocol-level session removed; stateless core; Tasks API lifecycle changed.
- Deprecated: Roots, Sampling, Logging ("These are annotation-only deprecations."), kept working for spec versions published within a year.
- New: Extensions framework, MCP Apps (HTML UI in a sandboxed iframe), Tasks extension, auth hardening, full JSON Schema 2020-12 for tool schemas.
- [SNIPPET] an updated roadmap of 22 Aug 2026 reportedly adds agent identity and progressive tool discovery.

### B20. OWASP — Top 10 for LLM Applications 2025 [FETCHED] [OLDER list, still current]
- URL: https://genai.owasp.org/llm-top-10/
- LLM01 Prompt Injection; LLM02 Sensitive Information Disclosure; LLM03 Supply Chain; LLM04 Data and Model Poisoning; LLM05 Improper Output Handling; LLM06 Excessive Agency; LLM07 System Prompt Leakage; LLM08 Vector and Embedding Weaknesses; LLM09 Misinformation; LLM10 Unbounded Consumption.
- No 2026 revision is announced on the page as of 2026-11-12.

### B21. OWASP — Top 10 for Agentic Applications for 2026 (published 9 Dec 2025) [FETCHED: OWASP page for date; item list from Giskard summary]
- URLs: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ (date only) and https://www.giskard.ai/knowledge/owasp-top-10-for-agentic-application-2026 (list; article dated 18 Dec 2025)
- ASI01 Agent Goal Hijack; ASI02 Tool Misuse and Exploitation; ASI03 Identity and Privilege Abuse; ASI04 Agentic Supply Chain Vulnerabilities; ASI05 Unexpected Code Execution; ASI06 Memory & Context Poisoning; ASI07 Insecure Inter-Agent Communication; ASI08 Cascading Failures; ASI09 Human-Agent Trust Exploitation; ASI10 Rogue Agents.
- The list was not read from the OWASP PDF itself; confirm names against the official download before teaching.

### B22. Simon Willison — "prompt-injection" tag, 2026 entries [FETCHED — index with excerpts]
- URL: https://simonwillison.net/tags/prompt-injection/
- Incidents logged in 2026: Superhuman email exfiltration (12 Jan), Claude Cowork file exfiltration via allow-listed domain (14 Jan), "Clinejection" supply-chain attack through an issue title (6 Mar), Snowflake Cortex sandbox escape (18 Mar), Microsoft Copilot Cowork exfiltration (26 May), Meta AI support bot account takeovers (1 Jun), Claude web_fetch exfiltration (15 Jul), self-propagating injection in Word documents (29 Jul), UK AISI report of 19 cases of agents acting on the live internet (5 Aug).
- Defenses logged: OpenAI Lockdown Mode limiting outbound requests (5 Jun); Claude Code auto mode default (8 Aug; Anthropic's figure: caught 89% of harmful actions vs 13.6% for humans); research framing injection as role confusion ("Destyling causes average attack success" to fall from 61% to 10%, 22 Jun).
- Willison's position (24 Mar): prefers "a robust sandbox by default" over AI-based classifiers. On an auto-mode bypass (27 Aug): "The safety mechanism itself can become part of the failure."

### B23. Anthropic — "How we contain Claude across products" (25 May 2026) [FETCHED] — see A12
- Relevant for Track B: containment at the environment layer, egress allowlists are themselves attack surface, symlink resolution before path validation.

### B24. EU AI Act — AI Omnibus adopted (Addleshaw Goddard briefing, 1 Jul 2026) [FETCHED]
- URL: https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/technology/eu-ai-act-ai-omnibus-formally-adopted/
- Standalone (Annex III) high-risk obligations now apply from 2 December 2027 (previously August 2026); product-embedded (Annex I) from 2 August 2028.
- Article 4 AI literacy: duty stays with providers and deployers but is softened to "take measures to support the development of AI literacy"; it does not guarantee "any specific level of AI literacy of any individual."
- Watermarking/transparency: systems on the market before 2 Aug 2026 have until 2 Dec 2026. New ban on systems generating non-consensual intimate imagery/CSAM: "The ban will take effect on 2 December 2026."
- [SNIPPET] The amending act is reported as Regulation (EU) 2026/1744, published 24 Jul 2026, in force 27 Jul 2026 (Mondaq/K&L Gates search result; not read).

### B25. EU AI Act implementation timeline (artificialintelligenceact.eu, last updated 31 Aug 2026) [FETCHED]
- URL: https://artificialintelligenceact.eu/implementation-timeline/
- 2 Feb 2025: prohibitions and AI literacy apply. 2 Aug 2025: GPAI model obligations and governance apply. 2 Aug 2026: remainder applies unless otherwise specified. 2 Dec 2026: Article 50(2) deadline for pre-existing generative systems. 2 Aug 2027: GPAI models placed on the market before 2 Aug 2025 must comply. 2 Dec 2027: Annex III high-risk. 2 Aug 2028: Annex I high-risk.
- Unofficial site; verify against EUR-Lex.

### B26. OpenTelemetry GenAI semantic conventions [FETCHED — status not determinable]
- URLs: https://opentelemetry.io/docs/specs/semconv/gen-ai/ , https://github.com/open-telemetry/semantic-conventions-genai , its CHANGELOG.md
- Verified: the conventions "have moved to the OpenTelemetry GenAI semantic conventions repository"; scope is "spans, metrics, and events for GenAI clients, MCP (Model Context Protocol), and provider-specific conventions"; the old page lists agent spans, events, metrics, MCP, and provider pages (Anthropic, Bedrock, Azure, OpenAI).
- Not verified: stability level. The new repo shows no releases, schema URL "TODO", and an empty changelog. Search results conflict on whether `gen_ai.*` is stable. Treat as still moving.

### B27. LLM observability tools (Langfuse, Phoenix, Logfire, LangSmith, Braintrust) [SNIPPET]
- Search results only, mostly vendor-authored comparisons (e.g. https://pydantic.dev/articles/best-langfuse-alternatives , https://www.zenml.io/blog/langfuse-vs-phoenix — not read).
- Reported: Langfuse and Phoenix both ingest OTel GenAI data (Phoenix maps to OpenInference); Logfire positions as general OTel tracing with LLM calls inside it. No independent comparison found.

### B28. Dex Horthy — "12-factor agents" (2025; repo still maintained) [FETCHED] [OLDER]
- URL: https://github.com/humanlayer/12-factor-agents
- Good agents "are comprised of mostly just software."
- Factors include "Own your prompts", "Own your context window", "Tools are just structured outputs", "Own your control flow", "Small, Focused Agents", "Make your agent a stateless reducer".

### B29. InterviewStack — AI Engineer job-posting analysis (8 Jun 2026; 4,155 postings on its own board) [FETCHED]
- URL: https://interviewstack.io/blog/how-ai-is-changing-ai-engineer-2026
- Skill mentions: Machine Learning 58.9%, LLMs 55.5%, AI Agents 47.3%, Generative AI 40.6%, RAG 39.6%, Prompt Engineering 27.8%, Vector Databases 24.5%, LangChain 23.4%, MLOps 20.0%, LangGraph 14.0%, CrewAI/AutoGen 9.1%.
- 65.6% of postings are senior; entry level 5.1%.
- Single job board, undocumented tagging method; evals are not broken out in the figures returned.

### B30. Other job-posting analyses [SNIPPET]
- Search results only: a 390-posting analysis cited by KDnuggets (56% mention AI evaluation, 50% agents, 26% RAG) — original not found; https://kdnuggets.com/the-ai-skills-that-actually-show-up-in-job-postings-right-now not read. Unverified.

### B31. Stack Overflow Developer Survey 2026 — AI section [FETCHED] — see A31
- Agent orchestration frameworks in use: LangChain 30%, OpenAI Agents SDK 24%; automation: Make 39%, n8n 33%.

### B32. Thoughtworks Technology Radar Vol. 35 (Nov 2026) [FETCHED] — see A9
- Relevant for Track B: Small language models and Open-weight models (Trial); Blanket frontier model usage and Naive context compression (Caution; "token reduction means nothing if prompt caches break"); Stateful guardrails and Toxic flow analysis (Trial); Programmatic tool calling (Assess); Threat modeling (Adopt); Progressive context disclosure (Adopt; lists RAG and GraphRAG as examples); Managed agents runtime (Trial).

### B33. Armin Ronacher — "What is Codemode" (6 Oct 2026) [FETCHED] — see A22
- Relevant for Track B: tool composition via generated code in a sandbox; MCP servers need structured output and composable tool search to work well with it.

### B34. Charles Chen — "MCP is Dead; Long Live MCP!" (14 Mar 2026) [FETCHED] — see A24

### B35. Hacker News — top 2026 stories matching "RAG" (Algolia API) [FETCHED — titles/points only]
- URL: https://hn.algolia.com/api/v1/search?query=RAG&tags=story&numericFilters=created_at_i%3E1767225600,points%3E200&hitsPerPage=30
- Relevant hits: "RAG Is Simpler Than You Think" (516 pts); "Ask HN: How are you doing RAG locally?" (413 pts, 14 Jan 2026); "We replaced RAG with a virtual filesystem…" (411 pts); "From zero to a RAG system: successes and failures" (322 pts, 24 Mar 2026); "How we index images for RAG" (205 pts); "Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model" (776 pts); "Show HN: Forge – Guardrails take an 8B model from 53% to 99% on agentic tasks" (687 pts, from a second query).
- Few high-scoring stories on evals or on "AI engineer" as a job were found (queries returned 4 and 2 relevant hits).

### B36. A2A protocol status [SNIPPET]
- Search results only: Linux Foundation press release of 9 Apr 2026 reports 150+ supporting organizations (https://linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year — not read); a 1.0 spec in March 2026 is reported by one review. No practitioner write-up of production A2A use was found.

### B37. LLM cost engineering [SNIPPET]
- Search results only, mostly vendor/SEO guides. Consistent levers: prompt caching, batch APIs, model routing, per-operation cost attribution. No strong independent practitioner source found; the verified cost evidence is in B9 (cost shapes ambition for 40%), B10 (token usage second-most monitored metric), A9 (Radar cautions) and A30.

### B38. Chip Huyen [SNIPPET]
- No 2026 blog post on agents found via search; 2026 material is podcasts (e.g. Super Data Science 999, 9 Jun 2026 — not listened to). Her "Agents" article is from 7 Jan 2025 [OLDER].

### B39. Martin Fowler site — "DSLs Enable Reliable Use of LLMs" (Unmesh Joshi, 14 Jul 2026), "The VibeSec Reckoning" (27 May 2026), "Tests as data" (11 Nov 2026) [listed on index, not read]
- URL of index: https://martinfowler.com/tags/generative%20AI.html [FETCHED]

---

## B. Synthesis — Track B

### B-1. Practices with broad agreement that look durable
1. **Evals start with reading traces and error analysis; build judges only for observed failure modes; binary labels; validate judges against humans.** Hamel/Shreya B1, Yan B2, Anthropic B3. LangChain B8 shows practice lags advice (29.5% not evaluating; human review still the most common method).
2. **Start simple; workflows before agents; own your prompts, context and control flow.** Anthropic B7, 12-factor B28, Pierre B16, Bayer B11.
3. **Context is a budget to manage:** selective context per step, compaction, notes/memory, sub-agents, just-in-time loading. Anthropic B6/B4, Bayer B11, Radar B32 (Adopt).
4. **Retrieval = search engineering, usually hybrid and increasingly iterative/agentic; evaluate retrieval with IR metrics separately from generation.** B1, B11, B14, B15, B16.
5. **Business rules and permissions live in code and tools, not prompts; retrieved text never authorizes an action.** B12, B13, B5.
6. **Design for the lethal trifecta: least privilege, egress control, sandboxing, credentials kept away from model-generated code.** Willison B22, Anthropic A12/B5, OWASP B20/B21, Radar B32, B13.
7. **Tracing/observability from day one** (89% adoption in B8; B13; B11 daily batch evals on production traffic).
8. **Durable, resumable state for long-running agents** (B5 session log, B11 persisted workflow state, B12 durable execution).
9. **Multi-model by default with routing by task; most teams do not fine-tune.** B9 (87% multi-model), B8 (57% not fine-tuning), Radar B32.
10. **Few, well-described tools designed as capabilities rather than API mirrors.** B6, B7, B13, A22.
11. **Human approval and staged autonomy for write actions** (B9, B13, B12) — with the caveat that approval fatigue makes it weak on its own (A12).

### B-2. Contested topics
- **"RAG is dead" / vector DB vs agentic search.** Agentic/file-system search: Mintlify B15, Claude Code practice as reported in B14, Jason Liu's 2025 titles B17. Keep embeddings as one tool: turbopuffer B14, Bayer B11. Keep it simple with full-text first: Pierre B16. Hamel/Shreya B1: the question is how to retrieve, not whether.
- **Eval-driven development and off-the-shelf metrics.** Hamel/Shreya B1 advise against writing evaluators before features and against generic metrics; Bayer B11 uses faithfulness/answer-relevancy metrics on live traffic; Anthropic B3 says start evals early with 20–50 tasks.
- **Multi-agent systems.** Anthropic B4/B6 and Radar use sub-agents for context isolation; 12-factor B28 says small focused agents; Garg A48 documents the costs; Jason Liu's "No Multi-Agents" title (not read).
- **MCP's role in applications.** Maintainers B18/B19 reposition it as stateless enterprise infrastructure; B13 warns about tool sprawl from naive API-to-MCP conversion; code mode B33; CLI/skills camp A25.
- **Prompt-injection defenses: classifiers vs containment.** Vendors report better models and classifiers (B22: auto mode, "least prompt injectable model yet"); Willison B22 and Anthropic A12 argue only environment-level controls are dependable.
- **Frameworks vs plain code.** LangChain remains the most-used orchestration library (A31: 30%) and appears in 23.4% of postings (B29), while B7 and B28 advise understanding or owning the underlying code.
- **Frontier vs small/open models.** Radar B32 cautions against blanket frontier usage; B9 shows 45% use open-weight models but almost always alongside closed ones; HN A42 disputes real cost savings.
- **Memory design.** Files/wikis with background consolidation (B4) vs tiered-memory systems such as MemGPT/Letta (mentioned in B12) vs knowledge graphs (B13). B4 lists open questions itself.
- **Agent-to-agent protocols (A2A).** Institutional adoption is announced (B36, snippet); no practitioner evidence of use found.

### B-3. What changed or was deprecated in 2025–2026 (evidence of fast-moving topics)
- **MCP:** stateless redesign, sessions/handshake removed, Roots/Sampling/Logging deprecated, Tasks API changed, MCP Apps added (B19) — within about 20 months of the protocol's launch.
- **Naive "chunk → embed → top-k" RAG** lost default status to hybrid/agentic retrieval and file-system tools (B14, B15, B16); a prominent RAG course was shut down in Feb 2026 (B17).
- **Harness complexity shrinks with each model generation** (A11); memory behavior differs strongly by model generation (B4).
- **"Prompt engineering" → "context engineering" (2025) → "harness/loop engineering" (2026)** (B6, B10).
- **Agents with write access:** 52% → 89% of agent-using teams in one year (B9).
- **OTel GenAI conventions** moved to a new repository with no visible release (B26) — tooling built on specific attribute names may break.
- **EU AI Act dates moved:** Annex III high-risk from August 2026 to 2 December 2027; Article 4 softened (B24, B25).
- **OWASP added a separate agentic Top 10** (Dec 2025) next to the LLM Top 10 2025 (B20, B21).
- **Tool lists in job ads are unstable:** CrewAI/AutoGen at 9.1%, LangGraph 14.0% (B29); Radar tool rings change every six months (A9).

### B-4. Skills that employers/teams say are missing
- **Evaluation and error analysis:** quality is the top production blocker (B8); 29.5% do not evaluate (B8); "Never skip this or delegate it." (B1).
- **Agent control/guardrails:** "Nobody has settled the control layer for agents." (B10); no consensus on monitoring (B9).
- **Security for agents with write access** (B9, B22, B21; security is the second barrier for large orgs in B8).
- **AI experience among senior engineers:** 51% of 10+ year engineers have 3 or fewer years of AI experience (B9).
- **Deep technical skills eroding** — most common negative effect (B9).
- **Cost management** (B9, B10).
- **Data readiness and ownership** (B13: 43% of surveyed leaders name data readiness as top barrier, per a Precisely/Drexel survey cited there — secondary).
- **Job ads** ask for agents (47.3%), RAG (39.6%), prompt engineering (27.8%), vector DBs (24.5%), mostly at senior level (B29).

### B-5. Predictions and scheduled changes for 2027 (PREDICTIONS / SCHEDULED, not findings)
- **Scheduled law (not a prediction):** EU AI Act GPAI models placed on the market before 2 Aug 2025 must comply by 2 Aug 2027; Annex III high-risk obligations apply from 2 Dec 2027; Annex I from 2 Aug 2028 (B24, B25). Both 2027 dates fall inside the April 2027–April 2028 window.
- **Scheduled protocol change (inference from B19):** deprecated MCP features (Roots, Sampling, Logging) are only guaranteed for spec versions published within a year of 28 Jul 2026, so removal becomes possible from mid-2027.
- **Amplify survey respondents (B9):** only 9% expect transformers to be state of the art in five years.
- **Simon Willison (A51):** a major coding-agent security disaster and "solved" sandboxing within the year from January 2026.
- **Geoffrey Huntley (A50):** 2027 conference talks will include admissions that factories and loops failed.
- No dated 2027 prediction was found from Hamel Husain, Shreya Shankar, Eugene Yan, Jason Liu, Chip Huyen or LangChain in the pages read.

---

## Coverage gaps and caveats

- **Reddit:** not covered. No thread from r/ClaudeAI, r/ExperiencedDevs, r/cursor or r/LocalLLaMA was fetched or surfaced by search.
- **X/Twitter:** only via blogs quoting posts (Karpathy, Cherny).
- **Blocked primaries, known only from snippets:** OpenAI harness engineering post, JetBrains 2026 survey posts, DORA ROI report, Ars Technica article, CodeRabbit report, Apiiro report, Karpathy statements, Yegge posts, Kent Beck posts, Steinberger/Ball posts, Chip Huyen 2026 material.
- **Partially read:** Hamel FAQ (two of two segments read, summaries only), HN Ask thread (first fifth), Willison patterns guide (table of contents only), Pragmatic Engineer posts (free sections only).
- **Vendor bias:** Anthropic, StrongDM, HumanLayer, turbopuffer, Mintlify, LangChain, Faros, Veracode, InterviewStack and Amplify all report on their own products, customers or communities.
- **Not found:** an independent practitioner source on agent token budgeting; a 2026 OWASP LLM Top 10 revision; a verifiable stability status for OTel GenAI conventions; practitioner reports of A2A in production; a rigorous 2026 job-posting study that separates evals as a skill.
- **Extraction caveat:** all page reads went through an automated extraction step; numbers and quotes should be re-checked at the URL before publication. One internal inconsistency was noticed: the Spec Kit blip page labels itself April 2026 while the extraction mentioned a "Volume 35" PDF filename; the November 2026 radar is Vol. 35.
