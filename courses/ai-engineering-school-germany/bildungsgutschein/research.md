# Research behind the two syllabi

**12 November 2026.** This file is the evidence for [variante-a-agentic-engineering.md](variante-a-agentic-engineering.md) and [variante-b-ai-engineering.md](variante-b-ai-engineering.md). All web pages were fetched on 12 November 2026. Nothing was sent to anyone and no certifier (fachkundige Stelle, FKS) or BA office was contacted.

## 1. How to read this

- Every claim carries a URL, or points to a numbered entry in one of the detailed source catalogues in [research-notes/](research-notes/). Those catalogues hold the per-source notes, quotes and fetch status:

| Catalogue | Content |
|---|---|
| [research-notes/pricing.md](research-notes/pricing.md) | Official cost rules, B-DKS table, premium comparables, minimum-length arithmetic |
| [research-notes/germany-azav-programmes.md](research-notes/germany-azav-programmes.md) | 24 Bildungsgutschein programmes in Germany, AZAV curriculum requirements, labour-market data |
| [research-notes/international-syllabi.md](research-notes/international-syllabi.md) | 17 international syllabi per track, with module lists |
| [research-notes/practitioner-sources.md](research-notes/practitioner-sources.md) | 52 sources on agentic engineering and 39 on AI engineering, 2026 |
| [research-notes/curriculum-design.md](research-notes/curriculum-design.md) | Curriculum design frameworks, teaching evidence, AI and learning, keeping content current |

- *(computed)* marks my own arithmetic. **Unknown** marks something no source settled.
- Limits of the research:
  - Web pages were read through a tool that returns an extraction of the page. Quotes and figures should be re-checked at the URL before they go into an application. PDFs (laws, BA documents, the B-DKS table) were read as raw text.
  - **Reddit was not covered.** No thread could be fetched or found. X/Twitter is covered only through blogs that quote posts.
  - Some primary pages were blocked and are known from search snippets only (OpenAI's harness-engineering post, the JetBrains 2026 survey, the DORA ROI report, Karpathy, Yegge, Kent Beck, Chip Huyen's 2026 material). The catalogues mark each one.
  - The BA's own course search shows price bands only, so exact prices exist for few providers.
  - Alexey's unpublished drafts and private course repositories were read for planning, but only published material is cited here.

## 2. Alexey's own material

### 2.1 Track A: AI Dev Tools Zoomcamp

Repository: https://github.com/DataTalksClub/ai-dev-tools-zoomcamp (last commits October 2026). The 2026 course is four weekly modules plus a fifth module and a project of about 20 hours. Lectures are recorded. The teaching text lives in `articles/`, which are the Substack posts in section 2.2.

| Module | Content | Source |
|---|---|---|
| 2025 cohort, module 1 | Overview of tool categories (chat applications, coding assistants and IDEs, project bootstrappers, agents), installing Claude Code, a Snake game example | [cohorts/2025/01-overview](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/tree/main/cohorts/2025/01-overview) |
| 1 AI-native workflow | Spec-driven development, backlog in GitHub issues, `AGENTS.md` and modular `_docs/`, PM / engineer / QA agent roles, `/goal` loops, orchestrator | [01-ai-native-workflow](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/tree/main/01-ai-native-workflow) |
| 2 Build a full-stack app | Mocked frontend, OpenAPI contract, FastAPI, SQLite and SQLAlchemy | [02-development](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/tree/main/02-development) |
| 3 Test, containerize, deploy | Two-stage Dockerfile, Postgres, Compose, Playwright end-to-end tests, AWS with CloudFormation, GitHub Actions with OIDC | [03-deployment](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/tree/main/03-deployment) |
| 4 DevOps and observability | Dev and prod promotion, build once, OpenTelemetry with Prometheus, Loki, Tempo and Grafana, alerting, headless on-call agent | [04-devops](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/tree/main/04-devops) |
| 5 Agent capabilities | Skills (`SKILL.md`), subagents, orchestrator, parallel git worktrees | [05-agent-capabilities](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/tree/main/05-agent-capabilities) |
| 2025 cohort, module 3 | MCP: servers, workflows, local and remote, security | [cohorts/2025/03-mcp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/tree/main/cohorts/2025/03-mcp) |
| Project | 12 criteria, 24 points, pass at 10, three peer reviews | [project/README.md](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/blob/main/project/README.md) |

Stated audience: "developers and technical data professionals who want to learn disciplined AI-assisted software development", with basic programming, command line and Git, and no prior AI-tool experience ([README](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/blob/main/README.md)). This matches Alexey's audience note for track A.

What the repository does not teach, so the bootcamp has to write it:

- work in a large existing codebase (the course uses two small starters)
- human review of agent diffs and a pull-request workflow
- systematic debugging
- steering a session (plan mode, compaction, rewind)
- permissions, sandboxing, secrets and prompt injection (goals and research notes only)
- MCP, hooks and plugins in the 2026 version (module 5's README lists them, only skills and subagents have content)
- migrations, rollback and staging (promised in module 3, not in the article)
- cost, tokens and model choice
- agents in CI and background agents
- a capstone larger than 20 hours

### 2.2 Track A: Substack articles

All 63 published posts on https://aishippingblog.com were read. 26 are about agentic engineering. The ones the syllabus uses:

| Theme | Posts |
|---|---|
| Setup and tool choice | [How to Set Up Your Coding Agent](https://aishippingblog.com/p/how-to-set-up-your-coding-agent-a) · [Free and Affordable AI-Native Development](https://aishippingblog.com/p/free-and-affordable-ai-native-development) · [My Experiments with Claude Code](https://aishippingblog.com/p/my-experiments-with-claude-code) |
| Specs, backlog, context, loops, agent roles | [AI-Native Development: Specifications, Loop and Graph Engineering](https://aishippingblog.com/p/ai-native-development-specifications) · [I Built an AI Agent Team for Software Development](https://aishippingblog.com/p/i-built-an-ai-agent-team-for-software) · [How We Built AI Shipping Labs Website using AI Tools](https://aishippingblog.com/p/how-we-built-ai-shipping-labs) |
| Build, deploy, operate | [Build and Ship a Full-Stack App](https://aishippingblog.com/p/build-and-ship-a-full-stack-app-with) · [Deploy a Full-Stack App](https://aishippingblog.com/p/deploy-a-full-stack-app-with-ai-coding) · [DevOps and Observability for an AI-Built App](https://aishippingblog.com/p/devops-and-observability-for-an-ai) · [From Idea to Production in 28 Prompts](https://aishippingblog.com/p/from-idea-to-production) · [My PyPI Release Pipeline](https://aishippingblog.com/p/my-pypi-release-pipeline-for-python) |
| Skills, subagents, worktrees | [Coding Agent Building Blocks](https://aishippingblog.com/p/coding-agent-building-blocks-reusable) |
| Safety and access | [How I Dropped Our Production Database](https://aishippingblog.com/p/how-i-dropped-our-production-database) · [The System I Built for AWS Access Without Keys](https://aishippingblog.com/p/the-system-i-built-for-aws-access) · [The System I Built to Ship Code From a Phone](https://aishippingblog.com/p/the-system-i-built-to-ship-code-from) |
| Review and the factory | [Trends in Agentic Engineering](https://aishippingblog.com/p/trends-in-agentic-engineering) · [Dark Software Factories](https://aishippingblog.com/p/dark-software-factories) · [Six Projects That Didn't Make It](https://aishippingblog.com/p/six-projects-that-didnt-make-it) · [Aplexer](https://aishippingblog.com/p/aplexer-why-i-stopped-using-tmux) |
| Design | [AI Design for Non-Designers](https://aishippingblog.com/p/ai-design-for-non-designers) |

Practices that recur across the posts and that the syllabus teaches:

1. Spec first. Dictate the idea, let the assistant "Ask me one question at a time", save the plan, only then code.
2. A groomed backlog. Each task has Goal, Acceptance criteria, Out of scope and Constraints. GitHub issues are the only active backlog. A `human` tag marks what needs a person.
3. Four levels: prompt, context (`AGENTS.md` plus documents loaded on demand), loop (a goal with a checkable stop condition) and graph (who does what when there are several agents).
4. Separate roles. "When the same agent writes and judges the code, it's grading its own homework." An orchestrator coordinates, a PM grooms and accepts, an engineer implements, QA reports PASS or FAIL and never fixes, an on-call engineer watches CI.
5. Implementer and reviewer share written rules and iterate until the reviewer accepts.
6. Skills and subagents are the two building blocks. Do the task once, then "Save this as a skill".
7. Build order with a testable result at each step: mocked frontend, OpenAPI contract, backend, SQLite, Postgres.
8. Verify by tests and behaviour: Playwright end-to-end tests against Compose, QA against acceptance criteria, screenshots as evidence.
9. Ship through CI with OIDC. Dev deploys automatically, prod only after a manual action, the same image is promoted.
10. Operate with OpenTelemetry, alerts on user impact and a headless on-call agent.
11. "An agent should never have a path to production": sandbox account, temporary credentials, a hook that blocks destructive commands.
12. A factory needs maintenance and escalation rules. "The more work I delegate, the more carefully I have to design the specifications, checks, and escalation paths around it."

Tensions in his own writing that the syllabus keeps visible instead of hiding:

- The Zoomcamp text says "We look at the code". [Dark Software Factories](https://aishippingblog.com/p/dark-software-factories) says he stopped reading agent code routinely. Section 5.1 shows the field is split on the same question. The syllabus teaches review first and treats "not reading every line" as a decision that depends on risk.
- He writes that the multi-agent process "takes significantly more time and tokens" and that "Often, a simple prompt or loop is enough."
- Running several agent teams is unsolved by his own account: "I still haven't made a department of teams work reliably."
- No post covers MCP, hooks or plugins on their own, and brownfield work appears only in anecdotes.

### 2.3 Track B: LLM Zoomcamp

Repository: https://github.com/DataTalksClub/llm-zoomcamp (last commit September 2026). Free, recorded, 10 weeks. Stack: OpenAI Responses API, `uv`, Jupyter.

| Unit | Teacher | Status | Content |
|---|---|---|---|
| [1 Agentic RAG](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/01-agentic-rag) | Alexey | 2026 | RAG from scratch with minsearch and sqlitesearch, function calling and the agent loop by hand |
| [2 Vector search](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/02-vector-search) | Alexey | 2026 | sentence-transformers, numpy, sqlitesearch, pgvector |
| [3 Orchestration](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/03-orchestration) | Kestra (partner) | 2026 | YAML flows, RAG and agents in Kestra |
| dlt workshop | dltHub (partner) | 2026 | Pipelines over agent traces |
| [4 Evaluation](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/04-evaluation) | Alexey | 2026 | Synthetic ground truth, Hit Rate, MRR, tuning, LLM judge, one agent-trajectory lesson |
| [5 Monitoring](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/05-monitoring) | Alexey | 2026 | Cost, token and latency records in Postgres, feedback, online judge, Grafana, Compose; homework on OpenTelemetry |
| [6 Best practices](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/06-best-practices) | not stated | recorded 2024 | Hybrid search and reciprocal rank fusion on Elasticsearch |
| [7 Project example](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/07-project-example) | not stated | recorded 2024 | Fitness assistant with Flask, Postgres, Grafana |
| [Project](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/project.md) | | | Nine criteria at 0–2 points plus best-practice and bonus points, peer review |

Because the bootcamp uses no subcontractors, units 3 and the dlt workshop cannot be reused as they are. Their topics (ingestion, pipelines) are taught in-house in the syllabus.

Gaps for a 2027 programme: tests and CI for LLM applications, prompt injection and guardrails, human approval, cloud deployment (the rubric calls it "not covered in the course"), FastAPI serving, streaming and caching. MCP, frameworks, reranking and query rewriting are named only. The project rubric has no criteria for tools, agent evaluation, tests, guardrails or deployment.

### 2.4 Track B: Maven course

[AI Engineering Buildcamp: From RAG to Agents](https://maven.com/alexey-grigorev/from-rag-to-agents). Recorded lessons with a weekly office hour and a demo day. Public code: https://github.com/alexeygrigorev/ai-engineering-buildcamp-code. The course's own overview describes nine weeks; the Maven page says six. I use the nine-week structure and treat the difference as unresolved.

| Weeks | Content |
|---|---|
| 1–3 | Responses API, RAG with minsearch, chunking, structured output, a hand-written tool-call loop, PydanticAI |
| 4 | Testing with pytest: tool-call tests and LLM-judge tests |
| 5 | Monitoring with Pydantic Logfire |
| 6 | Offline evaluation: a judge aligned with human labels, synthetic data, trajectory checks |
| 7–9 | Capstone (33-point rubric, pass at 12, three peer reviews), demo day |

Coverage for track B:

- Strong: LLM API basics, structured output, RAG, chunking, tool calling, the agent loop, PydanticAI, tests, judges, answer and trajectory evaluation, tracing, capstone.
- Optional and uneven: vector search, multi-agent patterns, other frameworks, cost.
- Thin: MCP, guardrails, retrieval evaluation, human approval, latency, deployment.
- Missing: prompt injection, CI, reranking.

Related posts used for track B: [How to Do Evals in 2026](https://aishippingblog.com/p/how-to-do-evals-in-2026), [Trends in AI Engineering](https://aishippingblog.com/p/trends-in-ai-engineering), [What Is an AI Engineer?](https://aishippingblog.com/p/what-is-an-ai-engineer-my-perspective), [What 1,000+ Job Descriptions Reveal](https://aishippingblog.com/p/what-1000-job-descriptions-reveal), [Minsearch](https://aishippingblog.com/p/minsearch-the-small-search-library), [(Re)Building a FAQ System](https://aishippingblog.com/p/rebuilding-a-faq-system-for-datatalksclub), [How CRISP-DM Still Applies](https://aishippingblog.com/p/how-crisp-dm-still-applies-to-ai), [Building an AI Book Generator](https://aishippingblog.com/p/building-an-ai-book-generator-with).

The split between the tracks is his own: "AI engineering - AI is part of the product" and "Agentic engineering - agents help you build the product" ([Trends in Agentic Engineering](https://aishippingblog.com/p/trends-in-agentic-engineering)).

## 3. Comparable programmes in Germany

Details: [research-notes/germany-azav-programmes.md](research-notes/germany-azav-programmes.md).

**Is there a long Bildungsgutschein programme on coding agents for people who already program? None was found.** What exists:

| Provider and course | Length | For whom | Source |
|---|---|---|---|
| alfatraining, "Agentische Softwareentwicklung mit Claude Code" | 2 weeks, German | programmers | https://en.alfatraining.de/kurse/weiterbildung-claude-code |
| Viona / IBB, "Softwareentwicklung mit KI-Tools" | 4 weeks, German | one programming language required | https://pdf.viona.online/kursflyer/E-4683.pdf |
| Turing College, "Building with AI Agents" | 520 UE | non-coders | https://www.turingcollege.com/building-with-ai-bildungsgutschein |
| Digitale Leute School, "AI Software Engineering" | 12 weeks | | https://school.digitale-leute.de/weiterbildung/ai-software-engineering |
| Turing College, "Agentic Engineering" | 13 weeks, BA price band €1,000–5,000 | | BA listing, see [pricing notes](research-notes/pricing.md) section 2.2 |

Elsewhere, coding agents are a one- or two-week block inside a beginner web-development bootcamp.

**Closest to track B:**

| Provider and course | Length | Notes | Source |
|---|---|---|---|
| Turing College, AI Engineering | 3 months, 520 UE | Requires a year of Python or JavaScript. LLM APIs, then LangChain and RAG, then agents with LangGraph and MCP, then a capstone. Self-pay €3,500 | https://www.turingcollege.com/ai-engineering-bildungsgutschein |
| neue fische / Spiced, "Agentic AI: Build and Deploy AI Agents" | 8 weeks, English | For developers. Names evals, LLM-as-judge, Langfuse, MCP and the EU AI Act | https://www.spiced-academy.com/en/program/agentic-ai |
| neue fische, "Agentic Machine Learning Engineer" | 14 weeks, English | About half classical ML | https://www.neuefische.de/bootcamp/agentic-machine-learning-engineering |
| IfaDW, KI-Anwendungsentwickler | 15 weeks, 525 UE, €7,413 | LLM content is one of three five-week modules | https://www.ifadw.de/ki-anwendungsentwickler/ |

Patterns:

- "AI Engineer" in Germany usually means data science and machine learning with one LLM block.
- Almost no programme requires prior programming. "For people who already program" is a real difference, and it means the entry requirement and its test have to be designed explicitly.
- Topics no curriculum covers in depth: work in existing codebases, review and testing of agent-written code, evaluation and monitoring of LLM applications (outside neue fische).

**What an AZAV course concept has to contain.** § 3 AZAV: goals, duration and content match the target group and take current labour-market developments into account; 12 participants as the calculation basis (https://www.gesetze-im-internet.de/azav/__3.html). The TÜV NORD documentation form asks for a concrete course goal, the target group with entry requirements and how they are tested, UE per week and total weeks with a reason for the duration, topics, learning checks, an absence concept and labour-market necessity (form A601F113, [Germany notes](research-notes/germany-azav-programmes.md) section 3.3).

**Labour market.** Bitkom, 3 September 2026: unfilled IT jobs fell from 149,000 in 2023 to 79,000; 63% of companies expect AI skills to be needed in all IT jobs; 33% say applicants lack the latest technologies (https://www.bitkom.org/Presse/Presseinformation/IT-Fachkraeftemangel-in-den-letzten-drei-Jahren-halbiert). No IAB study on AI skills of software developers was found.

## 4. Comparable programmes internationally

Details and module lists: [research-notes/international-syllabi.md](research-notes/international-syllabi.md).

### 4.1 Track A

Read: Stanford CS146S "The Modern Software Developer" in its Fall 2025 and Fall 2026 versions (https://themodernsoftware.dev/), Anthropic's courses (https://anthropic.skilljar.com/claude-code-in-action, https://anthropic.skilljar.com/claude-code-101), DeepLearning.AI short courses, the Hugging Face MCP course, "Elite AI Assisted Coding" (https://maven.com/agentic-ventures/ai-coding), "AI Coding for Real Engineers" (https://www.aihero.dev/cohorts/ai-coding-for-real-engineers-m0k0w), and university courses at Michigan (https://eecs498-aase.github.io/syllabus.html), UT Austin (https://www.cs.utexas.edu/~witchel/378AC/schedule.html), Maryland, Paderborn (https://www.hni.uni-paderborn.de/en/sse/lehre/ase) and Brown, plus the GitHub Copilot certification, OpenAI's Codex guide and Simon Willison's patterns guide (https://simonwillison.net/guides/agentic-engineering-patterns/).

| | Topics |
|---|---|
| In most syllabi | How a coding agent works (model plus tools in a loop) · context engineering and guidance files · plan before code, specs, task decomposition · MCP · skills and subagents · tests as the feedback loop · code review of agent output and by AI reviewers · Git, worktrees, parallel work · permissions, hooks, sandboxing · security (prompt injection, secrets, static analysis) |
| Only in 2026 syllabi | Background and unattended agents, issue-to-PR pipelines · "software factory" and "loop engineering" as named topics · agent-ready codebases · harness engineering · verifying unsupervised runs · gateways, model routing, cost · plugins and headless runs · graded open-source contributions (30% in CS146S 2026) |
| Dropped since 2025 | A separate prompting week · "AI IDE" and "modern terminal" weeks · one-prompt app builders · "vibe coding" as the framing |

Usual order: agent internals, context and specs, MCP, skills, repository customisation, testing and review, security, background agents and CI, team and cost, factory.

CS146S was largely rewritten between its two years; the week lists are in the notes. That is direct evidence of how fast this track's tool layer moves.

### 4.2 Track B

Read: Hugging Face Agents Course, Berkeley Agentic AI MOOC, Stanford CS224G, DeepLearning.AI "Agentic AI" and RAG courses, "AI Evals for Engineers & PMs" (https://maven.com/parlance-labs/evals, $4,500, 8 weeks), Anthropic "Building with the Claude API" (https://anthropic.skilljar.com/claude-with-the-anthropic-api), OpenAI's agents guide, Microsoft "AI Agents for Beginners" (https://github.com/microsoft/ai-agents-for-beginners), Turing College, Ironhack (9 weeks, £8,000), "End-to-End AI Engineering Bootcamp" (https://maven.com/swirl-ai/end-to-end-ai-engineering, $2,200, 8 weeks), and Chip Huyen's book contents. Stanford CS329Z and CMU 11-768 are known from a third-party write-up only.

| | Topics |
|---|---|
| In most syllabi | LLM API basics, structured output, prompting · RAG (chunking, embeddings, hybrid search, reranking) · tool use · agent patterns, workflows versus agents · evaluation (error analysis, LLM judge, component and trajectory checks) · tracing and monitoring · guardrails and security · deployment, cost, latency · a deployed capstone |
| Only in 2026 syllabi | MCP as a standard lesson · context engineering replacing prompt engineering · agent memory as its own unit · "build an agentic harness" as homework · evaluation first and in CI · sandboxing and credential management · coding agents as the development workflow |
| Dropped | Fine-tuning as core · classical ML prerequisites · framework tours · the "LLMOps" label |

Assessment in bootcamps and project courses: a graded project per sprint, ending in a demo day.

### 4.3 How these courses stay current

- CS146S: "weekly updates" and guest speakers.
- Elite AI Assisted Coding: "The curriculum is revised quarterly, materials are refreshed for each cohort".
- GitHub's certification publishes a dated "skills measured" list with a change log (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300).
- Ed Donner and Microsoft stamp an edition on the material ("refreshed version from Summer 2026", "Version 3").
- Several courses describe themselves as vendor-agnostic so that a tool change does not change the outcomes.

## 5. What practitioners write

Details, with one entry per source: [research-notes/practitioner-sources.md](research-notes/practitioner-sources.md).

### 5.1 Agentic engineering

**Broad agreement, looks durable:**

| Practice | Sources |
|---|---|
| Verification is the core skill, and the agent needs a way to check its own work | Willison, https://simonwillison.net/2026/Aug/22/more-than-just-code-review/ · Claude Code team, https://claude.dev/blog/solving-code-review-at-anthropic/ |
| Every repeated mistake becomes a guide or a deterministic check ("harness engineering") | Böckeler, https://martinfowler.com/articles/harness-engineering.html · Hashimoto, https://mitchellh.com/writing/my-ai-adoption-journey |
| Short instruction files, detail loaded on demand | Thoughtworks Radar Vol. 35, https://www.thoughtworks.com/radar/techniques · https://agentskills.io/ · https://agents.md/ |
| Sandbox by default. Anthropic reports users approved about 93% of permission prompts, so prompts alone are weak | https://www.anthropic.com/engineering/how-we-contain-claude |
| A named person stays accountable; review depth follows risk | Radar Vol. 35 · Claude Code team (above) |
| Plan before code, in small slices with explicit "done" criteria | Radar Vol. 35 · Hashimoto (above) |
| Subagents are for context isolation, not speed | https://martinfowler.com/articles/orchestrator-tax.html |
| Review is the bottleneck, not generation. Faros reports time to first review up 156.6% and bugs per developer up 54% | https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways |

**Contested:**

- Must a human read every line? The Claude Code team and StrongDM (https://factory.strongdm.ai/) say no or tiered. Others say yes.
- Dark factories and unattended loops. For: StrongDM, Huntley. Against: Dex Horthy, "Why Software Factories Fail" (https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md).
- Spec-driven frameworks. The Radar had Spec Kit at Assess in April 2026 and now warns about documentation sprawl.
- MCP versus command-line tools versus skills versus "code mode" (https://lucumr.pocoo.org/2026/10/6/codemode/, https://chrlschn.dev/blog/2026/03/mcp-is-dead-long-live-mcp/).
- How many parallel agents: from one (Hashimoto) to two to four (Radar) to dozens.
- Whether teams get faster. METR could not measure it cleanly and is redesigning its study (https://metr.org/blog/2026-02-24-uplift-update/).

**Changed during 2025–2026:**

- Claude Code went from new to the most-used tool in eight months (https://newsletter.pragmaticengineer.com/p/ai-tooling-2026). The Radar now has Codex and OpenCode in Adopt.
- Anthropic removed harness scaffolding as models improved (https://www.anthropic.com/engineering/harness-design-long-running-apps).
- The "Ralph" bash loop became a built-in goal feature.
- `AGENTS.md` converged as the instruction-file standard.
- Permission prompts gave way to sandbox plus auto mode.
- The vocabulary moved: vibe coding, context engineering, agentic engineering, harness engineering, loop engineering.

**Skills reported as missing:** verifying and reviewing at volume, writing specs and decomposing work, building the checks, security of agents and of generated code, keeping deep debugging skill, cost awareness.

### 5.2 AI engineering

**Broad agreement, looks durable:**

| Practice | Sources |
|---|---|
| Evaluation starts with error analysis on real traces, binary labels, judges validated against humans | https://hamel.dev/blog/posts/evals-faq/ · https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents |
| Start simple; workflows before agents; own the prompts and control flow | https://www.anthropic.com/engineering/building-effective-agents (2024) |
| Retrieval is search engineering, usually hybrid, increasingly iterative | https://martinfowler.com/articles/reliable-llm-bayer.html |
| Business rules and permissions live in code, not prompts; long-running agents need resumable state | https://martinfowler.com/articles/durable-execution-agents.html |
| Design against the "lethal trifecta": least privilege, egress control, credentials out of reach | https://simonwillison.net/tags/prompt-injection/ |
| Tracing from day one. 89% have observability, 29.5% still do not evaluate | https://langchain.com/state-of-agent-engineering |
| Several models with routing; most teams do not fine-tune (87% use several models) | https://www.amplifypartners.com/blog-posts/the-2026-ai-engineering-report |

**Contested:**

- "RAG is dead": agentic or filesystem search (https://www.mintlify.com/blog/how-we-built-a-virtual-filesystem-for-our-assistant) versus embeddings as one tool among several (https://turbopuffer.com/blog/video-rag-is-dead-right) versus full-text first (https://www.lighthousenewsletter.com/p/rag-is-simpler-than-you-think).
- Generic evaluation metrics and evaluation-first development.
- Prompt-injection defence by classifiers versus by containment.
- Multi-agent designs, frameworks versus plain code, memory architecture.

**Changed during 2025–2026:**

- The MCP specification of 28 July 2026 is a stateless redesign with sessions removed and several features deprecated (https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/).
- Plain chunk, embed and top-k retrieval lost its default status.
- Agents with write access rose from 52% to 89% of agent-using teams in a year (Amplify report above).
- OWASP added a separate Top 10 for agentic applications in December 2025.

**Fixed dates inside the course window:** EU AI Act high-risk obligations under Annex III now apply from 2 December 2027; general-purpose models placed on the market before 2 August 2025 must comply by 2 August 2027 (https://artificialintelligenceact.eu/implementation-timeline/, https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/technology/eu-ai-act-ai-omnibus-formally-adopted/).

**Skills reported as missing:** evaluation and error analysis, control and guardrails for agents, agent security, cost management. One job-board analysis finds agents in 47.3% and RAG in 39.6% of AI-engineer postings, mostly senior (https://interviewstack.io/blog/how-ai-is-changing-ai-engineer-2026; single board, not representative).

### 5.3 AI Engineering Field Guide (9,760 jobs, Feb–Nov 2026)

Alexey's own corpus in `alexeygrigorev/ai-engineering-field-guide` (commit `ab21b128`, 9,760 builtin.com postings across 10 monthly scrapes Feb–Nov 2026; `role/02-skills.md`, `role/03-responsibilities.md`, `role/04-use-cases.md`, `role/07-trends.md`) provides direct empirical grounding for Track B ([variante-b-ai-engineering.md](variante-b-ai-engineering.md)):

- **Applied integrator role, not model research:** 97.4% of postings are applied/production (only 2.6% research). Within AI-First roles (68.9% of the market), the integrator stack (RAG, agents, APIs) rose from 80.0% to **91.7%** (pure-integrator: 50.9% → **66.8%**), while the trainer stack fell from 37.5% to 27.2%. Fine-tuning is a primary responsibility in only **3.2%** of AI-First roles and absent from responsibilities in **86.0%**.
- **RAG + Agents + MCP + LangChain/LangGraph:** Agents (any) appear in **56.2%** of all jobs (**74.0%** AI-First) and RAG in **40.1%** (**56.0%** AI-First); jobs requiring *both* rose from 33.1% to **51.0%** of AI-First postings. **LangChain** (21.1% overall, 76.8% of framework adopters) and **LangGraph** (14.4%, climbing 37.7% → **71.0%** among adopters) are the #1 co-occurring pair (3.5x lift). **MCP** (15.6%) is the fastest-rising named skill (9.9% → **20.4%**, +0.94 pp/scrape), followed by **Function Calling** (15.1%, 9.6% → **18.5%**).
- **Evaluation & guardrails:** Evaluation-related skills appear in **61.8%** of AI-First roles, rising to **69.3%** in November ("Evaluation and Testing" in **79.0%** of November responsibilities). **Guardrails** rose from 10.2% to **17.5%** (19.8% AI-First); LLM-native eval/observability (`LangSmith`, `Langfuse`, `Guardrails`, `LLM Evaluation`) rose 26.7% → **34.5%** while classic MLOps (`MLflow`, `Kubeflow`) fell 19.9% → 14.5%.
- **Full-stack & Ops beyond GenAI (86.9%):** Python (71.6% / **75.9%** AI-First), GenAI + Ops (**71.0%** AI-First: **CI/CD** 36.9%, **Docker** 24.2%, **Kubernetes** 23.6%, **Observability** 20.7%), GenAI + Web (**59.2%**: APIs 2,515, **FastAPI** 928, React 1,373), Vector DBs (2,201), PostgreSQL (1,020), SQL (14.6%, rising 11.1% → 14.9%), and Cloud (**AWS** 39.3% / 41.8% AI-First > Azure 29.7% > GCP 29.1%).
- **Enterprise use cases:** Automating manual workflows (58.8%), internal operational efficiency (57.5%), agentic systems (49.9%), finding information in company data (43.8%), and document processing (13.3% → 16.0%) lead, while customer-facing Q&A fell **-13.8 pp** (44.7% → 30.9%). Junior/entry-level postings stayed at **0.8%–1.5%**, confirming the target group is working developers rather than beginners.

## 6. How to plan the curriculum

Details: [research-notes/curriculum-design.md](research-notes/curriculum-design.md).

### 6.1 What the sources say

- **Order of design.** Backward design (Wiggins and McTighe, https://files.ascd.org/staticfiles/ascd/pdf/siteASCD/publications/UbD_WhitePaper0312.pdf), constructive alignment (Biggs, https://www.herdsa.org.au/herdsa-review-higher-education-vol-1/5-22) and Teaching Tech Together (https://teachtogether.tech/en/index.html) agree: outcomes first, then assessments, then content.
- **German vocational framing.** The KMK guide derives learning fields from job tasks, names them as actions, sizes them at 40, 60 or 80 hours, and fills only 80% of the time (https://www.kmk.org/fileadmin/veroeffentlichungen_beschluesse/2021/2021_06_17-GEP-Handreichung.pdf).
- **What counts as a teaching unit.** The Beirat recommendations of 17 June 2026 count only time in which a teacher runs or actively accompanies the session and direct interaction is possible at any moment. Accompanied project and group work counts if the concept shows how interaction and learning checks happen. Self-study and homework do not count (https://www.arbeitsagentur.de/datei/dok_ba032840.pdf).
- **Teaching evidence.** Active learning beats lecturing (Freeman et al. 2014, PNAS, DOI 10.1073/pnas.1319030111; abstract only). Explicit guidance suits new material, and its advantage fades as expertise grows (https://www.aft.org/sites/default/files/Clark.pdf). Peer instruction cut fail rates from 20% to 7% in four computer-science courses (https://files.software-carpentry.org/training-course/2012/08/porter-halving-fail-peer-instruction-2013.pdf).
- **Bootcamps.** Thayer and Ko's interviews found cohorts split by prior experience and uneven access to teachers (https://faculty.washington.edu/ajko/papers/Thayer2017CodingBootcamps.pdf).
- **AI and learning.** In Anthropic's 2026 trial with 52 engineers, the AI group scored 50% against 67% on a follow-up quiz, with the largest gap in debugging; use aimed at understanding preserved learning (https://www.anthropic.com/research/AI-assistance-coding-skills, https://arxiv.org/abs/2601.20245). ACM's task force reports that 68% of surveyed educators changed assessment, toward oral defences, in-person checks and larger projects (https://acm-education-genai-task-force.github.io/ACM_Taskforce_GenAI_Report_16Feb26.pdf).
- **Skill half-life.** No primary source was found for the often-quoted "2.5 years". The citable figure is from the WEF: 39% of skill sets change between 2025 and 2030 (https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf).
- **Changing an approved course.** The provider must report "wesentliche" changes without delay: substantial changes of content, concept or organisation, or any with financial effect (Beirat recommendations above; https://www.dqsglobal.com/de/entdecken/blog/aenderungen-bei-zugelassenen-massnahmen-sind-mitteilungspflichtig). No source gives examples or thresholds. § 3 AZAV also requires the course to follow current labour-market developments, so updating is expected.
- **Update practice elsewhere.** The Carpentries use life-cycle labels and advisory committees (https://docs.carpentries.org/resources/curriculum/lesson-life-cycle.html). Zoomcamps and Stanford courses freeze each past run and keep one current version.

### 6.2 What I derived from it (my recommendations)

1. Start from the survey's learning bullets as the job tasks. Each becomes a programme competence with one verb.
2. Fix the assessments before the modules: a weekly artefact with a live walkthrough, a midterm, a capstone with an oral defence.
3. Word outcomes without tool names. Name the tools in a dated toolchain annex.
4. Use 40-UE modules, one per week, each ending in an assessed output.
5. A 40-UE week:

| Block | UE |
|---|---:|
| Review of last week and short recall quiz | 4 |
| Teaching and live demonstration | 8 |
| Guided exercise | 12 |
| Accompanied project work | 12 |
| Code review, demo, oral check | 4 |

   No study tests a specific ratio for bootcamps, so these numbers are a judgement. In capstone weeks teaching shrinks and project work grows. All 40 UE are live with the teacher present, which is what the Beirat definition requires.
6. AI is allowed and logged. A few checkpoints are done without AI, because the Anthropic trial shows the debugging gap.
7. Refresh policy in section 8.

## 7. Price and duration

Details and all sources: [research-notes/pricing.md](research-notes/pricing.md).

### 7.1 What the Agentur für Arbeit funds

- The reference is the Bundes-Durchschnittskostensatz (B-DKS) for the occupation line of the course goal. Table valid from 1 July 2026: **43414 Softwareentwicklung – Experte, €15.46 per UE per participant** (https://www.arbeitsagentur.de/datei/tabelle-der-kosten-fuer-massnahmen-der-beruflichen-weiterbildung-2024_ba049411.pdf; the file name says 2024, the content is the 2026 table). No new table is announced for 2027, so an April 2027 course is priced against this one.
- Other IT expert lines are €15.29–15.98. The only one above 43414 that is not a management line is 43154 Medieninformatik at €15.98, which does not fit the content. Specialist level is lower (43413: €13.24).
- **There is no absolute cap.** The BA page says: "Der Bundes-Durchschnittskostensatz stellt keine Kostenobergrenze dar." (https://www.arbeitsagentur.de/institutionen/bildungstraeger/akkreditierung-zulassung).
- Three tiers (§ 179 SGB III, https://www.gesetze-im-internet.de/sgb_3/__179.html; § 3 AZAV; BA directive on cost consent, https://www.arbeitsagentur.de/datei/fachliche-weisung-kostenzustimmung-p-179_ba056279.pdf):

| Rate | Who decides | Condition |
|---|---|---|
| up to €15.46 | FKS alone | costs properly calculated |
| €15.47 to €19.32 (up to +25%) | FKS alone | the excess comes from named, justified and evidenced special costs |
| above €19.32 | FKS, after consent from the BA's Operativer Service Sachsen-Anhalt | proven special costs **and** a special labour-market interest; processing time not published |

- Accepted special costs: above-average staffing (the directive's own example is a trainer with a necessary special qualification on an expert-level course), special rooms, special technical equipment, special content, accessibility, and a justified group below 12. Overheads do not count.
- **Correction to the earlier draft:** 15.46 × 1.25 = 19.325. Rates have two decimals, so €19.33 is already above 25%. The highest rate the FKS can approve alone is **€19.32** *(computed)*. How an FKS rounds is unknown.
- Price = rate × synchronous UE. Nothing is priced on top. Laptops, tool subscriptions, exam fees and coaching are cost lines inside the rate. Self-study hours and internships are not UE.
- No maximum weekly UE and no holiday rule for long courses was found in the Beirat recommendations or the BA directives. The earlier draft's note about holiday rules for courses over six months is therefore **unverified**.
- Duration must be limited to what the course goal needs (§ 179(1) no. 3 SGB III). Every extra week needs a content reason.
- VAT: no BA document mentions it. Whether AZAV approval is enough for the exemption under § 4 no. 21 UStG is **unverified**; ask the accountant.

### 7.2 Courses priced at €12,000 or more

Programmes where both price and UE could be read on a page:

| Provider, course | Price | UE | Weeks | €/UE *(computed)* | Source |
|---|---:|---:|---:|---:|---|
| IfaDW, AI Engineer | €14,658.00 | 1,050 | 30 | 13.96 | https://www.ifadw.de/ai-engineer/ |
| SkillSprinters, ISB (approval pending) | €13,404.60 | 990 | 22 | 13.54 | https://skill-sprinters.de/llms-full.txt |
| IfaDW, KI-Entwickler | €12,600.00 | 875 | 25 | 14.40 | https://www.ifadw.de/ki-entwickler/ |
| IfaDW, Data Scientist | €12,127.50 | 875 | 25 | 13.86 | https://www.ifadw.de/data-scientist/ |
| SkillSprinters, Digitalisierungsmanager KI | €10,548.00 | 720 | 16 | 14.65 | https://skill-sprinters.de/digitalisierungsmanager/ |
| IfaDW, Machine Learning Engineer | €9,450.00 | 700 | 20 | 13.50 | https://www.ifadw.de/machine-learning-engineer/ |
| IfaDW, KI-Anwendungsentwickler | €7,413.00 | 525 | 15 | 14.12 | https://www.ifadw.de/ki-anwendungsentwickler/ |

How they reach the price:

- **More UE at a rate 5–13% below the B-DKS.** Every verified price of €12,000 or more belongs to a course of 22–30 weeks.
- **Heavier days.** IfaDW runs 7 UE a day, alfatraining 8, SkillSprinters 9, DCI states 10.
- **No premium surcharge was found.** Laptops, exam vouchers, tool access and career services sit inside the normal rate. No programme with more than €19 per UE was found.
- **No verified course of 16 weeks or less at €12,000 or more.** Two unverified candidates: Data Science Retreat Berlin (14 weeks, "€14,414" on https://datascienceretreat.com/, UE and price type not published) and Karriere Tutor's Data & Machine Learning Specialist (16 weeks, "13.348,80 €" from a search snippet).
- The BA search does list full-time courses of 11–16 weeks in the "über 10.000 €" band (Talentspring, IntelliLearn, neuefische, alfatraining), without exact prices or UE.

So the €12–13k Berlin courses Alexey has seen are consistent with what could be verified only at 22–25 weeks. Shorter ones may exist, but their rate could not be confirmed from public pages.

### 7.3 Minimum duration for €12,000–13,000

At line 43414 and 40 UE a week *(computed)*:

| Rate | Decided by | UE and weeks for €12,000 | Price at that length | UE and weeks for €13,000 | Price at that length |
|---|---|---|---:|---|---:|
| €15.46 (no surcharge) | FKS | 800 UE, 20 weeks | €12,368.00 | 880 UE, 22 weeks | €13,604.80 |
| €17.00 (+10%) | FKS | 720 UE, 18 weeks | €12,240.00 | 800 UE, 20 weeks | €13,600.00 |
| **€19.32 (+25%, the ceiling)** | **FKS** | **640 UE, 16 weeks** | **€12,364.80** | **680 UE, 17 weeks** | **€13,137.60** |
| above €19.32 | BA consent | fewer than 16 weeks | | | |

- **The minimum without BA consent is 16 weeks for €12,000 and 17 weeks for €13,000.** Both need the full 25% surcharge.
- At 640 UE, exactly €12,000 needs €18.75 per UE, which is 21.3% above the B-DKS *(computed)*.
- The 12 weeks from the survey (480 UE) would need €25.00 per UE for €12,000, which is 61.7% above and needs BA consent *(computed)*.
- With 9-UE days (45 a week) the same UE fit into fewer weeks, but one teacher then has about 34 clock hours of live teaching a week, and the day no longer ends at 16:00.

### 7.4 What this means for the plan

**Decision used in the syllabi: a 16-week core of 640 UE, plus four defined extension weeks.**

| Version | UE | Weeks | Rate | Price per participant *(computed)* | Risk |
|---|---:|---:|---|---:|---|
| Core at the ceiling | 640 | 16 | €19.32 (+25%) | €12,364.80 | Best case. No verified comparable uses this rate. Every euro of the surcharge needs evidence |
| Core + 1 week at the ceiling | 680 | 17 | €19.32 (+25%) | €13,137.60 | Same |
| Core + 2 weeks | 720 | 18 | €17.00 (+10%) | €12,240.00 | Moderate. A surcharge of this size has indirect support in the band data |
| Core + 4 weeks | 800 | 20 | €15.46 | €12,368.00 | Lowest. Matches how verified comparables price |
| Core, no surcharge | 640 | 16 | €15.46 | €9,894.40 | Fallback if neither surcharge nor extension is accepted |

Why this shape:

- It is the minimum Alexey asked for, and each longer version is the same course with named weeks added, so the FKS conversation decides the version without a rewrite.
- A surcharge has to be earned with costs. Candidates that the rules recognise: a justified group below 12 (the plan is 8 participants), per-participant coding-agent, LLM and cloud usage as special technical equipment, and an expert-level teacher as above-average staffing. The amounts are **unknown** until there is a costing with quotes.
- A smaller certified group raises the price per participant, not the revenue per cohort: 8 × €12,364.80 = €98,918.40, while 12 × €9,894.40 = €118,732.80 *(computed)*.
- On the evidence, 18–20 weeks is what an FKS is most likely to accept at €12,000. 16 weeks at the full 25% is legally open and unproven.

Questions only an FKS can answer:

1. Which occupation line and level it would assign (43414 expert or 43413 specialist).
2. Whether €19.33 counts as inside the 25%.
3. How it treats the owner-teacher's own time as a cost.
4. Whether it accepts a certified group of 8–10, and how much surcharge its rules allow for that.
5. Whether it accepts 9 UE a day for a live course taught by one person.
6. Which per-participant tool costs and exam fees it accepts.
7. Its experience with the duration of BA cost consent.
8. Whether it applies a holiday or weekly-hours convention of its own.

## 8. Staying current: what is stable and what moves

**Stable** (supported by the durable lists in section 5 and by what survived between the 2025 and 2026 syllabi in section 4):

- Track A: specifying work and acceptance criteria, decomposing tasks, managing context, verification through tests and checks, review, Git and CI/CD, deployment and observability, permissions and blast radius, separating the roles of implementer and verifier.
- Track B: calling a model and validating its output, search and retrieval, tool contracts, control flow in code, human approval for write actions, evaluation from error analysis, tracing, cost and latency measurement, containment against prompt injection.

**Fast-moving** (supported by the "changed during 2025–2026" lists): which coding agent leads, its features and commands, MCP protocol details, skill and plugin formats, model names and prices, framework APIs, observability attribute names, the vocabulary.

**Refresh policy (my recommendation):**

| What | Rule |
|---|---|
| Pinned in the approved concept | Course goal, target group, module titles and UE, learning outcomes (worded without tool names), assessment forms |
| Reviewed before every cohort | The dated toolchain annex, lab instructions, example repositories, reading lists, model and price tables |
| Reserve | 4 UE in each of the last two taught modules are held for "what changed since the syllabus was written" |
| Triggers for an unscheduled change | A tool the labs depend on is discontinued or changes its terms; a protocol release breaks a lab; a named technique moves to the Radar's Caution ring; a law date arrives |
| Change classes | Patch: fixes and version bumps. Minor: one tool replaced under an unchanged outcome. Major: an outcome, module UE or assessment form changes. Only major is reported to the FKS as substantial |
| Record | A changelog in Git and a frozen snapshot of the material per cohort |
| Outside view | Twice a year, ask two or three practitioners or hiring managers to review the outcomes |

Whether replacing a tool under an unchanged outcome is "wesentlich" is **not settled by any source**. Get the FKS's answer in writing before relying on the "minor" class.

Claude Code is the base tool for track A, as Alexey decided. It is named in the toolchain annex, not in the outcomes, and week 14 has participants run the same workflow in a second agent. The evidence for that caution: tool leadership changed within eight months in 2025–2026 (section 5.1).

## 9. Not verified or not found

- Any long AZAV programme on coding agents for experienced developers (none found; absence is not proof).
- Exact prices and UE for most bootcamps (Le Wagon, Ironhack, neuefische, Spiced, WBS Coding School, Masterschool, DCI, StackFuel, alfatraining).
- A verified course of 16 weeks or less at €12,000 or more, and any rate above €19 per UE.
- Whether a tool swap counts as a substantial change.
- VAT treatment.
- The 2026 day-by-day content of Google's agents intensive, Stanford CS329Z and CMU 11-768 from their own sites.
- Reddit and X discussions.
- Demand for either track: no survey responses exist yet ([README](../README.md)).
