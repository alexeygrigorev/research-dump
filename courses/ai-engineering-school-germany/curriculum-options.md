# Curriculum options to test

Updated: 2026-11-09.

These are proposed learning outcomes and structures for audience research. No course, price, timetable or accreditation is represented as approved. The first iteration would be taught by Alexey personally. Both tracks assume some programming experience. Assess career changers by their current skills.

## Two tracks

| Offer | Learner starting point | Main outcome |
| --- | --- | --- |
| **A. AI-assisted Software Engineering / Agentic Development** | Already writes and understands code | Develop, debug, test, review and ship software using coding agents responsibly |
| **B. Applied AI Engineering** | Programming plus basic API/software experience | Build an AI application with retrieval or tools, evaluate it and operate it reliably |

Offer A concerns **how software is developed**. Offer B concerns **AI functionality in the product**. Coding agents may be used in both, but that does not make the learning goals identical.

Choose the first track after reviewing learner demand and readiness.

## Existing material to reuse

- [AI Dev Tools Zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp) and its [current curriculum](https://datatalksclub.github.io/docs/courses/ai-dev-tools-zoomcamp/curriculum/) support offer A.
- [Maven Product Shipping with AI](https://maven.com/alexey-grigorev/product-shipping) adds the product brief, tester access, feedback and launch milestones to Agentic Engineering.
- [Maven AI Engineering Buildcamp: From RAG to Agents](https://maven.com/alexey-grigorev/from-rag-to-agents) provides the RAG, tool use, evaluation and monitoring sequence for AI Engineering.
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

Plan for about 12 teaching weeks, full-time and taught in English. The current scenario is Monday to Friday, 09:00 to 16:00 Berlin time, with breaks. It gives 30 synchronous clock hours per full week, including supervised projects, and an illustrative total of 480 UE. See the [teaching day](schedule-and-capacity.md#proposed-teaching-day) for the assumptions. Confirm the actual unit allocation once the track and activities are chosen.

BA defines the teaching unit as 45 minutes and distinguishes asynchronous components, which do not increase the synchronous-unit denominator used in the relevant cost calculation. See [BA implementation note 1/2026](https://www.arbeitsagentur.de/datei/umsetzungshinweis-01-2026_ba055638.pdf).

### Proposed syllabus

| Teaching weeks | Synchronous UE | Focus | Assessed output |
| --- | ---: | --- | --- |
| 1–2 | 80 | Existing repository, environment, baseline, project map, context and instructions for agents | A small change, a verified pull request and an explanation of the affected code |
| 3–4 | 80 | Problem definition, specification, acceptance criteria, APIs and data | An end-to-end feature with explicit scope and testable completion criteria |
| 5–6 | 80 | Debugging, regression prevention and independent verification | A reproduced failure, justified fix and tests that distinguish correct from incorrect behaviour |
| 7–8 | 80 | Review, security, secrets, dependencies, CI/CD, deployment and observability | A release with a review record, operational checks and a recovery procedure |
| 9–10 | 80 | Reusable skills, MCP/tools when useful, subagents, permissions and bounded delegation | A repeatable agent workflow with documented access, limits and verification |
| 11–12 | 80 | Capstone completion and professional application | A working project, technical defence, portfolio narrative and interview-style discussion |
| **Total** | **480** | | |

### Teaching method

Start with an existing repository and ship reviewed changes. Then use the Maven product milestones to define a user task, deploy a first version, collect peer or user feedback and improve the product. Assess the deployment and the evidence of testing and review.

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

### Proposed syllabus

| Teaching weeks | Synchronous UE | Focus | Assessed output |
|---|---:|---|---|
| 1–2 | 80 | Python service, LLM APIs, structured outputs and a baseline | A working API with typed responses, validation and failure handling |
| 3–4 | 80 | Ingestion, indexing, search and RAG with sources | A document assistant with a reproducible index and examples of good and poor retrieval |
| 5–6 | 80 | Function calling, tool contracts, MCP and approval steps | An assistant that can use an external tool and handle denied or failed actions |
| 7–8 | 80 | Evaluation datasets, retrieval metrics, answer quality and regression tests | An evaluation report comparing two configurations and explaining the failure cases |
| 9–10 | 80 | Deployment, tracing, latency, cost, security and fallbacks | A deployed service with useful traces, cost measurements and a tested fallback |
| 11–12 | 80 | Capstone, user testing and technical defence | A working AI service, a reproducible evaluation suite and evidence of improvements |
| **Total** | **480** | | |

Use the [Maven Buildcamp](https://maven.com/alexey-grigorev/from-rag-to-agents) sequence for the AI system and draw on its RAG, tool-use, evaluation and monitoring exercises. Build one application across the programme. Each milestone should add a capability and a way to check it. For example, a documentation assistant can start with cited answers, then add issue lookup and draft support replies for human review.

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

Choose the first programme from matched demand, observed readiness, founder capacity, necessary approvals and viable economics. Use one track and a common baseline for the first cohort. The survey's purpose is to discover which coherent offer can be delivered well.
