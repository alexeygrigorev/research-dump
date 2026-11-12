# Variante A: Agentic engineering

**12 November 2026.** Course description and syllabus for track A from the survey, [materials/survey.en.md](../materials/survey.en.md), question 1. Evidence and sources: [research.md](research.md). Not submitted anywhere.

Basis, as Alexey specified:

- his [AI Dev Tools Zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp) and his Substack articles (list in [research.md](research.md#22-track-a-substack-articles))
- the audience is developers who write code and have tried AI only a little
- the first module starts like the first AI Dev Tools cohort: an overview of the tools, then environment and tool installation
- Claude Code is the base tool throughout

## Course description

**Title.** Agentic Engineering: Build, Test and Ship Software with Coding Agents
German working title: *Agentische Softwareentwicklung: Software mit Coding-Agenten entwickeln, testen und ausliefern*

**In one sentence (survey).** Learn to use coding agents to build, test and ship software.

**Target group**

- Developers who write code today and have used AI tools only a little: some chat-assistant or autocomplete use, no agent-based workflow.
- Also QA and test-automation engineers, data and ML practitioners and technical analysts who program (survey question 8).
- Career changers, if they pass the entry check.
- For the Bildungsgutschein: people who are unemployed or at risk of unemployment, where the Agentur für Arbeit confirms the training is necessary (§ 81 SGB III).

**Learning goals.** By the end, participants can (survey wording):

1. Turn a product idea into a spec and a set of small tasks.
2. Build a full-stack feature across the interface, API and database.
3. Work in an existing codebase, debug, and review agent-generated changes.
4. Automate tests and releases with CI/CD.
5. Deploy the application and use logs and metrics to investigate failures.
6. Connect agents to tools through MCP and create reusable workflows for implementation and code review.
7. Set up and configure an agentic software factory.

**Final project (survey).** Ship a working web application for a real user task. Have people try it, improve it from their feedback, and show how you tested and released the changes.

**Prerequisites.** The participant can:

- write basic code in Python, JavaScript, TypeScript or a similar language
- use the command line and basic Git and GitHub
- read and explain a short function, and run a simple test
- follow technical teaching and work in English (survey question 6)

No prior experience with a coding agent is needed. This is the AI Dev Tools Zoomcamp's own prerequisite ([README](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/blob/main/README.md)). Readiness is checked before admission with a short practical exercise and a documented conversation.

**Format**

- Live teaching, online from Germany or in person in Berlin (Prenzlauer Berg, near S+U Schönhauser Allee). English.
- 1 UE = 45 minutes. 8 UE a day, Monday to Friday 09:00–16:00 including breaks. All UE are taught or actively accompanied by the teacher.
- A 40-UE week: 4 UE review and recall quiz, 8 UE teaching and live demonstration, 12 UE guided exercise, 12 UE accompanied project work, 4 UE code review, demo and oral check. Capstone weeks have less teaching and more project work. Reasons: [research.md](research.md#62-what-i-derived-from-it-my-recommendations).
- Stack: Python and FastAPI for the backend, a web frontend, Postgres, Docker, GitHub Actions. This is the Zoomcamp's stack.
- Base tool: Claude Code. Outcomes are worded without tool names, and week 14 repeats one workflow in a second agent. The tools and versions are listed in a dated annex that is reviewed before every cohort.
- Two codebases run through the programme: the participant's own product, built from week 3, and a prepared existing repository used for brownfield, debugging and review work.
- Taught by Alexey Grigorev. No subcontractors.

**Duration**

- **Core: 640 UE, 16 weeks full-time** (40 UE a week). Part-time: 32 weeks at 20 UE.
- Four defined extension weeks bring it to 680, 720 or 800 UE. Which version is submitted depends on the cost rate the certifier accepts.

| Version | UE | Weeks | Rate per UE | Price per participant *(computed)* |
|---|---:|---:|---|---:|
| Core at the 25% ceiling | 640 | 16 | €19.32 | €12,364.80 |
| Core + X1 | 680 | 17 | €19.32 | €13,137.60 |
| Core + X1–X2 | 720 | 18 | €17.00 | €12,240.00 |
| Core + X1–X4 | 800 | 20 | €15.46 | €12,368.00 |

  16 weeks is the shortest course that reaches €12,000 without BA consent, and only with the full 25% surcharge. Analysis and risks: [research.md](research.md#7-price-and-duration).

**Assessment.** AI use is allowed and has to be disclosed.

- Weekly: the assessed output in the table below, plus a live walkthrough in which the participant explains the change, shows the checks and answers questions.
- Three checkpoints without AI (weeks 2, 6 and 9): read code, find a bug, review a diff. Reason: in Anthropic's 2026 trial the AI group scored lower on a follow-up quiz, most of all in debugging ([research.md](research.md#61-what-the-sources-say)).
- Midterm (week 8): first version deployed, with three peer reviews and a teacher review.
- Final (week 16): product, launch report, technical defence. The rubric starts from the Zoomcamp's 12 project criteria ([project/README.md](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/blob/main/project/README.md)).

**Certificate.** Provider certificate "Agentic Engineering" listing the modules with UE, the assessment forms and the result. The AZAV format still has to be created.

## Syllabus: core, 640 UE

"ADTZ" is the AI Dev Tools Zoomcamp repository. "Write" means no teaching material exists yet.

| Wk | Module | UE | Learning outcomes | Topics | Practice and assessed output | Based on |
|---:|---|---:|---|---|---|---|
| 1 | A01 AI development tools: overview and setup | 40 | Tell the tool categories apart and say what each is for. Install and configure a coding agent. Explain how an agent works: a model calling tools in a loop | Chat applications, coding assistants and IDEs, project bootstrappers, agents. Installing Claude Code, account and plan, Git, GitHub, Docker. Permission modes and a safe working directory. The agent loop, tools, context window | Entry check. Working environment. The same small game built in a chat application and in the agent, with a comparison. First agent-made commit | ADTZ [2025 module 1](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/tree/main/cohorts/2025/01-overview) · [How to Set Up Your Coding Agent](https://aishippingblog.com/p/how-to-set-up-your-coding-agent-a) · [Free and Affordable AI-Native Development](https://aishippingblog.com/p/free-and-affordable-ai-native-development) |
| 2 | A02 Working in a session and in an existing codebase | 40 | Map an unfamiliar repository with an agent. Steer a session: explore, plan, change, commit. Keep context small and relevant | Reading a repository. Plan mode, compaction, new session per task. Instruction files (`AGENTS.md`, `CLAUDE.md`). Small commits and pull requests | A small change in the prepared repository as a verified pull request, with an explanation of the affected code. Checkpoint without AI: read and explain code | **Write** (ADTZ has no existing-codebase material) · context part of [AI-Native Development](https://aishippingblog.com/p/ai-native-development-specifications) |
| 3 | A03 From idea to spec, backlog and small tasks | 40 | Turn an idea into a written plan. Write tasks with checkable acceptance criteria. Keep a backlog an agent can work from | Interview-style brainstorming, `_docs/plan.md`, choosing a stack you can review. Tasks with Goal, Acceptance criteria, Out of scope, Constraints. GitHub issues as the backlog, grooming | Product brief, groomed backlog and first empty project with a passing test for the participant's own product | ADTZ [module 1](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/tree/main/01-ai-native-workflow) · [AI-Native Development](https://aishippingblog.com/p/ai-native-development-specifications) · [How We Built AI Shipping Labs Website](https://aishippingblog.com/p/how-we-built-ai-shipping-labs) |
| 4 | A04 Full-stack feature I: interface and API contract | 40 | Build the interface against a mocked service layer. Derive an API contract from it | Frontend first, one services layer with a mock, manual two-session test, OpenAPI as the contract between frontend and backend | Working interface on mocks and an OpenAPI specification | ADTZ [module 2](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/tree/main/02-development) · [Build and Ship a Full-Stack App](https://aishippingblog.com/p/build-and-ship-a-full-stack-app-with) |
| 5 | A05 Full-stack feature II: backend and database | 40 | Implement the contract in a backend. Store data. Connect interface, API and database | FastAPI, modules, authentication basics, SQLite with an ORM, database-agnostic design, Makefile, asking the agent for options before a technology choice | The main user task working end to end, with backend tests | ADTZ module 2 · [From Idea to Production in 28 Prompts](https://aishippingblog.com/p/from-idea-to-production) (prompts 1–10) |
| 6 | A06 Testing, verification and debugging | 40 | Write tests that tell correct from incorrect behaviour. Give the agent a way to check its own work. Reproduce and fix a failure | Unit, integration and end-to-end tests with Playwright. Red/green test-first work. Acceptance criteria as tests that run. Spotting tests that prove nothing. Debugging: reproduce, isolate, fix, regression test | Test suite for the product. A seeded bug in the prepared repository reproduced, fixed and covered. Checkpoint without AI: find a bug | ADTZ [module 3](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/tree/main/03-deployment) (tests) · **Write** for debugging and test quality |
| 7 | A07 Reviewing agent-generated changes | 40 | Review a change for correctness, security and maintainability. Set up a second agent as reviewer. Move repeated review comments into automatic checks | Risk-based review depth. Reviewer in a fresh context, implementer and reviewer with shared written rules. Linters, type checks, hooks. Secrets, dependencies, common security flaws in generated code | Review record for a set of agent changes. A reviewer workflow and at least two automatic checks added to the product | [Trends in Agentic Engineering](https://aishippingblog.com/p/trends-in-agentic-engineering) · [Dark Software Factories](https://aishippingblog.com/p/dark-software-factories) · **Write** for human review and security checks |
| 8 | A08 Containers, CI/CD and deployment · midterm | 40 | Package the application. Run tests on every change. Deploy through the pipeline | Two-stage Docker build, Postgres, Compose, infrastructure as code, GitHub Actions, OIDC instead of stored keys, health checks, migrations and rollback | **Midterm:** first version deployed through CI, with README and test access | ADTZ module 3 · [Deploy a Full-Stack App](https://aishippingblog.com/p/deploy-a-full-stack-app-with-ai-coding) · **Write** for migrations and rollback |
| 9 | A09 Permissions, sandboxing and safe operation · midterm review | 40 | Limit what an agent can reach. Explain prompt injection and when it becomes dangerous. Keep agents away from production | Permission modes and their limits, sandboxed environments, hooks that block destructive commands, separate cloud account with temporary credentials, deployment only through CI. Case study: a deleted production database | Threat sketch and guardrails for the product. Three peer reviews of midterm products and an improvement plan. Checkpoint without AI: review a diff | [How I Dropped Our Production Database](https://aishippingblog.com/p/how-i-dropped-our-production-database) · [AWS Access Without Keys](https://aishippingblog.com/p/the-system-i-built-for-aws-access) · **Write** for sandboxing and prompt injection |
| 10 | A10 Environments, logs, metrics and an on-call agent | 40 | Run separate dev and prod environments. Use logs, metrics and traces to find a failure. Have an agent respond to an alert | Build once and promote the same image, manual promotion to prod. OpenTelemetry, Prometheus, Loki, Tempo, Grafana. Product metrics, alerts on user impact, headless agent as first responder | Dashboards and one alert for the product. A failure investigated from telemetry. On-call agent tested with an injected bug | ADTZ [module 4](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/tree/main/04-devops) · [DevOps and Observability for an AI-Built App](https://aishippingblog.com/p/devops-and-observability-for-an-ai) |
| 11 | A11 Reusable workflows: skills, subagents and hooks | 40 | Turn a task done once into a reusable workflow. Use subagents to isolate context. Automate checks around the agent | Skills (`SKILL.md`), global and project scope, subagent definitions, hooks, sharing as plugins. Workflows for implementation and for code review | An implementation workflow and a code-review workflow packaged for reuse and used on the product | ADTZ [module 5](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/tree/main/05-agent-capabilities) · [Coding Agent Building Blocks](https://aishippingblog.com/p/coding-agent-building-blocks-reusable) · [My PyPI Release Pipeline](https://aishippingblog.com/p/my-pypi-release-pipeline-for-python) · **Write** for hooks and plugins |
| 12 | A12 Connecting agents to tools through MCP | 40 | Connect an agent to external tools. Build a small tool server. Decide between MCP, a command-line tool and a skill | MCP clients and servers, local and remote, permissions and security. Building a server for a project tool. Current protocol version. 4 UE reserve for what changed | Product tools exposed through MCP and used by the agent, with documented access and limits | ADTZ [2025 module 3](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/tree/main/cohorts/2025/03-mcp), to be updated to the 2026 protocol · **Write** |
| 13 | A13 Agent teams, loops and parallel work | 40 | Define agent roles and how work moves between them. Run a loop with a checkable stop condition. Run tasks in parallel without conflicts | Orchestrator, PM, engineer, QA and on-call roles. Goal loops and stop conditions. Git worktrees. Headless and background runs, issue-to-pull-request in CI. Cost of the process compared with a single session | A backlog batch worked through by an agent team, with QA verdicts on the issues. One task run headless in CI | ADTZ modules 1 and 5 · [I Built an AI Agent Team](https://aishippingblog.com/p/i-built-an-ai-agent-team-for-software) · [My Experiments with Claude Code](https://aishippingblog.com/p/my-experiments-with-claude-code) · **Write** for agents in CI |
| 14 | A14 The agentic software factory | 40 | Set up and configure a factory: spec, tasks, build, tests, review, release. Define when it stops and asks a person. Keep it maintainable | Assembling weeks 3–13 into one configured setup. Escalation rules. Factory maintenance, comprehension debt. Usage limits, model choice and cost. Auditing a repository for agent readiness. The same workflow in a second agent. 4 UE reserve for what changed | Configured factory on the product, a written operating guide, and one task repeated in a second agent with notes on the differences | [Dark Software Factories](https://aishippingblog.com/p/dark-software-factories) · [Six Projects That Didn't Make It](https://aishippingblog.com/p/six-projects-that-didnt-make-it) · [Trends in Agentic Engineering](https://aishippingblog.com/p/trends-in-agentic-engineering) · **Write** |
| 15 | A15 Capstone: users, feedback, improvement | 40 | Have people try the product. Separate problems from feature requests. Ship tested improvements | Test sessions with real users, feedback triage, prioritising, changelog, usage tracking | Improved product released through the pipeline, with a changelog and the evidence of testing | ADTZ [project](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/blob/main/project/README.md) · [AI Design for Non-Designers](https://aishippingblog.com/p/ai-design-for-non-designers) |
| 16 | A16 Capstone: release, evidence and defence | 40 | Present the product and show how changes were tested and released. Defend design decisions | Peer review, launch report, technical defence, interview-style discussion | **Final:** product, launch report, defence | ADTZ project criteria |
| | **Total** | **640** | | | | |

### Extension weeks

Each is 40 UE and is placed before the capstone. They are added in this order. Each has its own content reason, because duration has to be justified by the course goal.

| Module | Learning outcomes | Topics | Assessed output | Why |
|---|---|---|---|---|
| X1 Brownfield project I | Deliver a real change to a larger existing codebase | Choosing an issue in an open-source project, reading the code and its conventions, a plan the maintainers can accept | Accepted plan and a first pull request | Survey goal 3. No German programme covers work in existing codebases, and Stanford's CS146S grades open-source contributions at 30% in 2026 ([research.md](research.md#41-track-a)) |
| X2 Brownfield project II | Take a change through review to merge | Responding to review, tests in someone else's suite, documentation | Pull request merged or ready to merge, with the review history | Same |
| X3 Agents in a team | Use agents where several people work on one codebase | Shared instruction files and checks, review load, branch and merge policy, usage budgets, measuring results without counting lines | Team working agreement applied in a group exercise | Review is reported as the bottleneck in teams ([research.md](research.md#51-agentic-engineering)) |
| X4 Capstone: second feedback round | Run a second cycle with users | A second test round, comparison with the first, release | Second release with before-and-after evidence | The survey's final project asks for improvement from feedback |

## Coverage of the survey's learning goals

| Survey goal | Weeks |
|---|---|
| Spec and small tasks | 3 |
| Full-stack feature | 4, 5 |
| Existing codebase, debugging, review | 2, 6, 7 (X1, X2) |
| Tests and releases with CI/CD | 6, 8 |
| Deploy, logs and metrics | 8, 10 |
| MCP and reusable workflows | 11, 12 |
| Agentic software factory | 13, 14 |
| Final project | 15, 16 |

## Why this order

- Week 1 opens the way the first AI Dev Tools cohort did, because the audience has little AI experience.
- Weeks 2–10 teach one supervised agent first: context, specs, build, tests, review, deployment, safety, operation. International syllabi follow the same path from a supervised session to a configured repository to unattended work ([research.md](research.md#41-track-a)).
- Review (week 7) and safety (week 9) come before any unattended work. Practitioners agree that verification and sandboxing are the durable skills, and they disagree about how far unattended factories work ([research.md](research.md#51-agentic-engineering)).
- Weeks 11–14 then extend and automate: workflows, MCP, agent teams, the factory.
- The factory week includes its limits. Alexey's own posts say the full process costs more time and tokens and that a simple loop is often enough.

## Stable and fast-moving parts

| Stable: taught as the core | Fast-moving: in the dated annex, reviewed before each cohort |
|---|---|
| Writing specs and checkable acceptance criteria | Which coding agent, its plan, commands and modes |
| Decomposing work into small tasks | Instruction-file and skill formats |
| Managing what the agent knows | MCP protocol version and available servers |
| Tests and checks as the feedback loop | Hook and plugin mechanisms |
| Review, and who is accountable | Model names, limits and prices |
| Git, CI/CD, deployment, observability | Cloud services used in the labs |
| Limiting what an agent can reach | Tooling for background and parallel agents |
| Separating the one who builds from the one who checks | The vocabulary of the year |

Refresh rules and the open question about reporting changes to the certifier: [research.md](research.md#8-staying-current-what-is-stable-and-what-moves).

## Material to write

Existing material is recorded video and articles. Every week needs a live lesson plan, exercises and a rubric. New content is needed for:

- week 2 (existing codebase, session steering)
- week 6 (debugging, test quality)
- week 7 (human review, security checks)
- week 8 (migrations, rollback)
- week 9 (sandboxing, prompt injection)
- week 11 (hooks, plugins)
- week 12 (MCP on the 2026 protocol)
- week 13 (agents in CI)
- week 14 (factory operation, cost, agent readiness)
- the prepared repository with seeded bugs
- all extension weeks
