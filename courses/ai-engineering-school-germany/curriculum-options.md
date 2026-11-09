# Curriculum options to test

Updated: 2026-11-09.

These are proposed learning outcomes and structures for audience research. No course, price, timetable or accreditation is represented as approved. The first iteration would be taught by Alexey personally. Beginners and career changers remain part of the research; only one coherent first programme should be selected after the evidence is reviewed.

## Three offers

| Offer | Learner starting point | Main outcome |
| --- | --- | --- |
| **A. AI-assisted Software Engineering / Agentic Development** | Already writes and understands code | Develop, debug, test, review and ship software using coding agents responsibly |
| **B. Applied AI Engineering** | Programming plus basic API/software experience | Build an AI application with retrieval or tools, evaluate it and operate it reliably |
| **C. Programming Foundations with AI** | Needs stronger coding foundations | Build a small application while learning to understand, debug and verify its code |

Offer A concerns **how software is developed**. Offer B concerns **AI functionality in the product**. Coding agents may be used in both, but that does not make the learning goals identical.

The working preference for A is an inference from existing content and solo-delivery constraints. It is not a finding that demand for A exceeds demand for B or C.

## Existing material to reuse

- [AI Dev Tools Zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp) and its [current curriculum](https://datatalksclub.github.io/docs/courses/ai-dev-tools-zoomcamp/curriculum/) support offer A.
- [AI Engineering Buildcamp](https://aishippinglabs.com/courses/ai-buildcamp) supports offer B.
- [AI Shipping Labs](https://aishippinglabs.com/) provides potential supplementary building sessions, trend discussions and career activities.

Map existing exercises to outcomes before commissioning new content. Check rights and participant access for jointly owned, licensed or member-only materials before placing them in a commercial programme.

## A. AI-assisted Software Engineering with Coding Agents

German working description: **KI-gestützte Softwareentwicklung mit Coding-Agenten**.

### Proposed audience and prerequisites

The learner should be able to:

- Run a small repository and find the relevant logic.
- Read and explain a short function.
- Use basic Git operations.
- Call an API and work with ordinary data structures.
- Run and explain a simple test.

The cohort would use one primary teaching stack, selected after reviewing applicants. Python or TypeScript are possible starting points; promising to support every stack would increase preparation and troubleshooting work.

Prior experience with a particular coding agent is not a prerequisite. Technical readiness should be demonstrated with a small exercise, rather than inferred solely from a job title or years of experience.

### Working format

- Twelve **teaching weeks** of volume.
- Four live mornings per week, provisionally Monday–Thursday, 09:00–12:15 Europe/Berlin.
- A 15-minute break each morning.
- Three clock hours of live teaching per morning = four 45-minute UE.
- Sixteen synchronous UE per week; **192 UE total = 144 live clock hours**.
- Approximately eight clock hours of independent practice per week, described separately.

The resulting student workload is around 20 active hours per teaching week. These are hypotheses to test with learners and the certifier, not requirements imposed by law or an approved offer. Public holidays and any breaks must be reflected in the actual dated schedule.

BA defines the teaching unit as 45 minutes and distinguishes asynchronous components, which do not increase the synchronous-unit denominator used in the relevant cost calculation. See [BA implementation note 1/2026](https://www.arbeitsagentur.de/datei/umsetzungshinweis-01-2026_ba055638.pdf).

### Proposed syllabus

| Teaching weeks | Synchronous UE | Focus | Assessed output |
| --- | ---: | --- | --- |
| 1–2 | 32 | Existing repository, environment, baseline, project map, context and instructions for agents | A small change, a verified pull request and an explanation of the affected code |
| 3–4 | 32 | Problem definition, specification, acceptance criteria, APIs and data | An end-to-end feature with explicit scope and testable completion criteria |
| 5–6 | 32 | Debugging, regression prevention and independent verification | A reproduced failure, justified fix and tests that distinguish correct from incorrect behaviour |
| 7–8 | 32 | Review, security, secrets, dependencies, CI/CD, deployment and observability | A release with a review record, operational checks and a recovery procedure |
| 9–10 | 32 | Reusable skills, MCP/tools when useful, subagents, permissions and bounded delegation | A repeatable agent workflow with documented access, limits and verification |
| 11–12 | 32 | Capstone completion and professional application | A working project, technical defence, portfolio narrative and interview-style discussion |
| **Total** | **192** | | |

### Teaching method

Use one continuing application or prepared codebase where possible. Each module introduces a constrained engineering problem, demonstrates a method and requires participants to verify an outcome.

Mix short explanations with supervised practice and review. When a lab is declared synchronous teaching, the teacher actively supports it. A Slack channel or the possibility of a later answer is not a substitute for a taught live unit; the organisation must match the approved concept. See the [BA Beirat recommendations](https://www.arbeitsagentur.de/datei/dok_ba014848.pdf).

Avoid using a long list of frameworks as the course's value proposition. Teach transferable skills: task decomposition, context selection, independent tests, debugging, review, permissions, deployment and accountability. Demonstrate tool substitution when it clarifies the underlying method.

### Assessment

Assess more than a polished demo. A participant should be able to:

1. Explain the requirement and why the implementation meets it.
2. Identify which parts were generated or assisted by AI.
3. Reproduce relevant checks and discuss their limits.
4. Diagnose a failure or incomplete suggestion.
5. Explain an important design choice and an alternative.
6. Present the work to another engineer in a review or interview.

AI use is allowed. The assessment should establish understanding and judgement, not reward hiding tools.

The final project can be public or reviewed privately. Use sample data and a prepared repository when employer confidentiality or access would otherwise prevent assessment. Public portfolio publication should not be an unannounced requirement.

## B. Applied AI Engineering

### Proposed audience

Developers or adjacent technical professionals who can write code, use APIs and work with a repository. The detailed prerequisites may differ from offer A, particularly if Python is the common implementation language.

### Learning sequence to validate

| Area | Practical outcome |
| --- | --- |
| LLM APIs and structured outputs | A small application with explicit input/output contracts and failure handling |
| Retrieval and RAG | A retrieval pipeline with examples showing where it succeeds and fails |
| Tool use and agent workflows | A bounded workflow with clear tool permissions and escalation conditions |
| Testing and evaluation | A reproducible evaluation set and a process for investigating regressions |
| Deployment and observability | A running service with useful logs, traces or metrics |
| Cost, security and reliability | Documented limits, safeguards and trade-offs |
| Capstone and professional application | A working AI service, evaluation evidence and a technical explanation |

Existing Buildcamp material can supply many exercises, but the duration and synchronous teaching volume must be designed for the selected audience. Do not copy the 192-UE structure merely because it exists for offer A, and do not extend the programme solely to justify a desired price.

## C. Programming Foundations with AI

### Research remains open

The user explicitly wants to understand this segment's demand. Include people without coding experience and people partway through a career transition in the survey and learner interviews.

The first question is what outcome they need: basic coding confidence, preparation for a later technical programme, ability to build a small product, or a longer transition into a new profession. These are different educational commitments.

### Candidate foundation sequence

- One programming language and a workable environment.
- Reading code, variables, control flow, functions and ordinary data structures.
- Files, APIs and simple data persistence.
- Git and reproducible project setup.
- Debugging, tests and checking AI-generated suggestions.
- A small independently explained application.

The duration, supervision and funding suitability remain unresolved. A twelve-week transition from no programming to AI-engineer employment is **not** promised. If this segment leads the research, run a separate small introductory experiment to measure support needs before specifying a full programme.

People with some programming may be able to use an existing preparation route and then demonstrate readiness for A or B. Treat this as an individual readiness decision, not an automatic short bridge for every beginner.

## Shared AI Shipping Labs activities

Prepare a case once and use it at appropriate levels:

- Required course teaching: structured explanation, practice and assessment.
- Existing Labs event: a trend discussion, advanced case, demonstration or career conversation.
- Public material: a reusable article, example repository or summary, with appropriate permissions.

For the first iteration, a shared Labs session should be optional and outside the required synchronous UE unless the arrangement has been explicitly incorporated and accepted. The core course must remain complete without an additional mandatory membership purchase. Attendance at an optional session must not become a hidden completion condition.

A future proposal to count mixed-audience events as required teaching needs a clear learning goal, teacher involvement, attendance process, access arrangement and compatible cost calculation. This is a design question for the FKS, not an automatic entitlement based on sharing a calendar event.

## What to build while delivering the first cohort

Create a teacher pack alongside the first iteration:

- Objective and prerequisites for each session.
- Preparation checklist and demonstration steps.
- Exercise, reference solution and typical mistakes.
- Assessment rubric and examples of acceptable work.
- Known setup problems and troubleshooting notes.
- Backup exercise and recovery plan if a tool fails.
- Notes about what actually took longer than expected.

This enables later delegation. After the first cohort, interested graduates may apply for paid TA work. Selection should include technical competence, a short teaching demonstration and the ability to give useful feedback. Successful course completion alone does not establish readiness to lead the next programme.

## Selection rule

Choose the first programme from matched demand, observed readiness, founder capacity, necessary approvals and viable economics. Do not combine all three audiences merely to fill seats. The survey's purpose is to discover which coherent offer can be delivered well.
