# Variante A: Agentic engineering

**Draft · 12 November 2026.** Course description and syllabus for track A from the survey, [materials/survey.en.md](../materials/survey.en.md), question 1. Size: 640 UE, as recommended in the [README](README.md#recommendation-option-5). Not submitted anywhere.

## Course description (Kursbeschreibung)

**Title.** Agentic Engineering: Build, Test and Ship Software with Coding Agents
German working title (from [curriculum-options.md](../curriculum-options.md)): *KI-gestützte Softwareentwicklung mit Coding-Agenten*

**In one sentence (survey).** Learn to use coding agents to build, test and ship software.

**Target group**
- People who already write code: software developers, QA/test automation engineers, data/ML practitioners, technical analysts and adjacent roles (survey question 8).
- Career changers, if they can show the programming prerequisites below. The survey notes say: "Career changer does not mean no programming experience".
- For Bildungsgutschein: people who are unemployed or at risk of unemployment, where the Agentur für Arbeit confirms the training is necessary (§ 81 SGB III).

**Learning goals.** By the end, participants can (survey wording):
1. Turn a product idea into a spec and a set of small tasks.
2. Build a full-stack feature across the interface, API and database.
3. Work in an existing codebase, debug, and review agent-generated changes.
4. Automate tests and releases with CI/CD.
5. Deploy the application and use logs and metrics to investigate failures.
6. Connect agents to tools through MCP and create reusable workflows for implementation and code review.
7. Set up and configure an agentic software factory.

**Final project (survey).** Ship a working web application for a real user task. Have people try it, improve it from their feedback, and show how you tested and released the changes.

**Prerequisites** (survey: "Both tracks assume some programming experience"; detail from [curriculum-options.md](../curriculum-options.md)). The learner can:
- run a small repository and find the relevant logic
- read and explain a short function
- use basic Git
- call an API and work with ordinary data structures
- run and explain a simple test
- follow technical teaching and work in English (survey question 6)

No prior experience with a particular coding agent is needed. Readiness is checked with a short practical exercise and a documented consultation before admission.

**Format**
- Live, synchronous teaching, either online from Germany or in person in Berlin (Prenzlauer Berg, near S+U Schönhauser Allee). English only.
- 1 UE = 45 minutes. Teaching day per [schedule-and-capacity.md](../schedule-and-capacity.md#proposed-teaching-day): 2 UE teaching and demonstration, 2 UE guided exercise, 2 UE supervised project work, 2 UE project review, debugging and discussion. So each 40-UE week = 10 + 10 + 10 + 10.
- One primary teaching stack for the cohort (Python or TypeScript, chosen after reviewing applicants).
- One product built across the whole programme, using the Product Shipping milestones (brief, first version, testers, feedback, launch).
- Taught by Alexey Grigorev. No subcontractors. AI Shipping Labs sessions are optional and outside the UE count.

**Duration**
- **640 UE.**
- Full-time: 16 weeks × 40 UE, Monday–Friday 09:00–16:00 incl. breaks.
- Part-time: 32 weeks × 20 UE, Monday–Friday 09:00–12:30. Each full-time week below = 2 part-time weeks.

**Assessment** (from [curriculum-options.md](../curriculum-options.md)). AI use is allowed. Participants have to show they can:
1. explain the requirement and why the implementation meets it
2. identify which parts were generated or assisted by AI
3. reproduce the relevant checks and discuss their limits
4. diagnose a failure or an incomplete suggestion
5. explain an important design choice and an alternative
6. present the work to another engineer in a review or interview

Assessment points:
- weekly assessed outputs (table below)
- midterm: deployed first version with peer and instructor review (Product Shipping midterm)
- final: product, launch report, technical defence

**Certificate.** Provider certificate "Agentic Engineering" listing the modules with their UE, the assessment forms and the result. AZAV format, still to create.

## Syllabus (640 UE)

| Wk FT (PT) | Module | UE | Learning outcomes | Topics | Practice and assessed output | Material |
|---|---|---:|---|---|---|---|
| 1 (1–2) | A0 Setup and baseline | 40 | Run the course repository and stack; use a coding agent safely on it | Environment, Git, Docker, coding-agent installation and permissions, course platform | Entry check; working environment; first agent-assisted change | Buildcamp "Environment Preparation"; [curriculum-options](../curriculum-options.md) weeks 1–2 |
| 2 (3–4) | A1 Working in an existing codebase | 40 | Build a project map; give agents the right context and instructions; ship a small verified change | Reading an unfamiliar repository, context selection, agent instructions, small pull requests | A small change, a verified pull request and an explanation of the affected code | curriculum-options weeks 1–2; **material to write** |
| 3 (5–6) | A2 From idea to spec and small tasks | 40 | Choose a user and one main task; write a spec with acceptance criteria; split it into small agent tasks | Task people need to complete, choosing a problem, defining and checking the first version, organising the project, giving AI small tasks | Product brief, acceptance criteria and task list for the course product | [Product Shipping](../../product-shipping) Module 1; Module 2 "Organize the project and give AI small tasks" |
| 4 (7–8) | A3 Full-stack feature I: API and database | 40 | Define what the interface needs from the API; build the backend and data storage with an agent | API design from screens, backend, storing data | Backend and database for the main task, with tests | Product Shipping Module 2 ("Define what the screens need from the API", "Build the backend and store data") |
| 5 (9–10) | A4 Full-stack feature II: interface, end to end | 40 | Connect interface, API and database for the main task | Connecting the main task end to end; agent-generated web interface | An end-to-end feature with explicit scope and testable completion criteria | Product Shipping Module 2 ("Connect the main task from start to finish"); Buildcamp "Build a clone of Lovable.dev" (Django) |
| 6 (11–12) | A5 Debugging and regression prevention | 40 | Reproduce a failure, fix it with justification, and add tests that tell correct from incorrect behaviour | Debugging with and without agents, independent verification, regression tests | A reproduced failure, a justified fix and regression tests | curriculum-options weeks 5–6; Product Shipping Module 2 "Test changes and automate checks"; **material to write** for debugging |
| 7 (13–14) | A6 Reviewing agent-generated changes | 40 | Review agent changes for correctness, security, secrets and dependencies | Code review, AI-written code checks, secrets, dependency risks; code-reviewer agent | Review record for a set of agent changes; own code-reviewer agent | curriculum-options weeks 7–8; Buildcamp code reviewer / code evaluator agent |
| 8 (15–16) | Midterm: first version deployed | 40 | Deploy the first version with setup instructions and test access | Deployment, README, known limitations, pre-submission check | Midterm submission: repository, commit hash, README, free test access | Product Shipping "Midterm: Submit your first version"; Module 2 "Deploy the product and write setup instructions" |
| 9 (17–18) | Midterm review and tester preparation | 40 | Test peer products; turn feedback into a plan; prepare reviewer access | Peer testing (3 products), review checklist, removing postponable features, test instructions | 3 peer reviews, instructor review, improvement plan | Product Shipping midterm feedback; Module 3 |
| 10 (19–20) | A7 CI/CD: automated tests and releases | 40 | Run tests automatically on every change; release in a repeatable way; recover from a bad release | Automated checks, release pipeline, recovery procedure | A release with a review record, operational checks and a recovery procedure | curriculum-options weeks 7–8; Product Shipping "Test changes and automate checks"; **material to write** for release pipelines |
| 11 (21–22) | A8 Logs, metrics and investigating failures | 40 | Use logs, traces and metrics to find failures; track errors and service limits | Logging, metrics, Grafana, OpenTelemetry, Pydantic Logfire, error and service-limit tracking | Monitoring for the product; a failure investigated from its logs | Product Shipping Module 5 ("Track errors and service limits"); Buildcamp "Monitoring"; LLM Zoomcamp Module 5 |
| 12 (23–24) | A9 Connecting agents to tools through MCP | 40 | Connect agents to tools through MCP with documented access and limits | MCP servers and clients, tool permissions, when MCP is useful | Project tools exposed and used via MCP | Buildcamp "Agentic Flows" (MCP); curriculum-options weeks 9–10 |
| 13 (25–26) | A10 Reusable workflows for implementation and code review | 40 | Create reusable agent workflows with bounded delegation and verification | Reusable skills, subagents, permissions, bounded delegation, review workflow | A repeatable agent workflow with documented access, limits and verification | curriculum-options weeks 9–10; Buildcamp code-reviewer agent; **material to write** |
| 14 (27–28) | A11 Agentic software factory | 40 | Set up and configure an agentic software factory: spec → tasks → agent build → tests → review → release | Combining A1–A10 into one configured set-up | Configured factory used on the course product | Survey topic; built on A1–A10; **material to write** |
| 15 (29–30) | Capstone: users, feedback, improvement | 40 | Have people try the product; separate problems from feature requests; ship tested improvements; track usage | Tester feedback vs requests, prioritising fixes, changelog, usage tracking, where people stop | Improved product released through the pipeline, with a changelog | Product Shipping Modules 4 and 5 |
| 16 (31–32) | Capstone: release, defence, launch | 40 | Present the product and its testing/release evidence; launch and record the response | Peer review, technical defence, portfolio and interview-style discussion, launch report | Final assessment: product, launch report, defence | Product Shipping Module 6 and final project; curriculum-options weeks 11–12 |
| | **Total** | **640** | | | | |

**Why 16 weeks instead of 12.** The 12-week draft in [curriculum-options.md](../curriculum-options.md) has five 80-UE blocks and a capstone. That leaves no room for the survey's final project: people trying the app, feedback, improvement, and evidence of testing and release. The 16-week plan keeps those blocks and adds the Product Shipping midterm review (week 9), a separate CI/CD week before the feedback cycle (week 10), a separate software-factory week (week 14) and a feedback-driven capstone iteration (week 15).

**Material gaps.** Weeks 2, 6, 10, 13 and 14 cover survey topics that have no existing course material. AI Dev Tools Zoomcamp is listed in curriculum-options.md as a source for track A, but it was not in the content scope for this draft. Decide whether to use it or to write the material.
