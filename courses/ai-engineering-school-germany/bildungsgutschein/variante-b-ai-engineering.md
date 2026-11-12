# Variante B: AI engineering

**Draft · 12 November 2026.** Course description and syllabus for track B from the survey, [materials/survey.en.md](../materials/survey.en.md), question 1. Size: 640 UE, as recommended in the [README](README.md#recommendation-option-5). Not submitted anywhere.

## Course description (Kursbeschreibung)

**Title.** AI Engineering: Build, Evaluate and Run LLM Applications
German working title (proposal): *KI-Anwendungsentwicklung mit Large Language Models (RAG, Agenten, Evaluation, Betrieb)*

**In one sentence (survey).** Learn to build and run applications that use language models to answer questions or take actions.

**Target group**
- Developers and adjacent technical professionals who can write code, use APIs and work with a repository ([curriculum-options.md](../curriculum-options.md)). This includes software, data and ML roles (survey question 8; LLM Zoomcamp and Buildcamp audiences).
- Career changers, if they show the programming prerequisites.
- For Bildungsgutschein: people who are unemployed or at risk of unemployment, where the Agentur für Arbeit confirms the training is necessary (§ 81 SGB III).

**Learning goals.** By the end, participants can (survey wording):
1. Build an assistant in Python using an LLM API.
2. Use retrieval-augmented generation (RAG).
3. Give the assistant tools to look up information or call an API.
4. Define what it can do on its own and when it needs human approval.
5. Use realistic questions and tasks to evaluate answers and tool use; compare prompts, models and retrieval methods; check for regressions.
6. Deploy the application and trace its model and tool calls.
7. Track quality, latency and cost, and handle failures safely.

**Final project (survey).** Build and deploy an AI assistant for a concrete use case, such as answering questions from technical documentation and drafting support replies. Show where it works, where it fails and how you measured that.

**Prerequisites** (survey: "Both tracks assume some programming experience"; LLM Zoomcamp prerequisites; Buildcamp page)
- comfortable programming, preferably in Python
- command line, Git and Docker basics
- no prior ML/LLM experience, advanced maths, GPU or degree needed
- able to follow technical teaching and work in English (survey question 6)

Readiness is checked with a short coding exercise and a documented consultation before admission.

**Format**
- Live, synchronous teaching, either online from Germany or in person in Berlin (Prenzlauer Berg, near S+U Schönhauser Allee). English only.
- 1 UE = 45 minutes. Teaching day per [schedule-and-capacity.md](../schedule-and-capacity.md#proposed-teaching-day): 2 UE teaching and demonstration, 2 UE guided exercise, 2 UE supervised project work, 2 UE project review, debugging and discussion. So each 40-UE week = 10 + 10 + 10 + 10.
- One application built across the programme. Each milestone adds a capability and a way to check it. Example from [curriculum-options.md](../curriculum-options.md): a documentation assistant that starts with cited answers, then adds issue lookup, then drafts support replies for human review.
- Recorded LLM Zoomcamp/Buildcamp videos are optional extra material and do not count as UE.
- Taught by Alexey Grigorev. No subcontractors. LLM Zoomcamp's orchestration module is taught in-house. AI Shipping Labs sessions are optional and outside the UE count.

**Duration**
- **640 UE.**
- Full-time: 16 weeks × 40 UE, Monday–Friday 09:00–16:00 incl. breaks.
- Part-time: 32 weeks × 20 UE, Monday–Friday 09:00–12:30. Each full-time week below = 2 part-time weeks.

**Assessment**
- Formative: assessed weekly outputs (table below), plus LLM Zoomcamp/Buildcamp homework where it fits.
- Midterm: deployed assistant with cited answers and one tool, 3 peer reviews and an instructor review (LLM Zoomcamp project.md; Product Shipping midterm).
- Final: the deployed capstone, graded against the LLM Zoomcamp project criteria: problem description, retrieval flow, retrieval evaluation, LLM evaluation, interface, ingestion, monitoring, containerisation, reproducibility, best practices. Also an evaluation report showing where it works and fails, and a technical defence.

**Certificate.** Provider certificate "AI Engineering" listing the modules with their UE, the assessment forms and the result. AZAV format, still to create.

## Syllabus (640 UE)

| Wk FT (PT) | Module | UE | Learning outcomes | Topics | Practice and assessed output | Material |
|---|---|---:|---|---|---|---|
| 1 (1–2) | B0 Setup and a Python LLM service | 40 | Set up the environment; call an LLM API from a Python service; get typed, validated output | Python, uv, Docker, Git, LLM providers and alternatives, structured output, failure handling | Entry check; a working API with typed responses, validation and failure handling | LLM Zoomcamp prerequisites; Buildcamp "Environment Preparation", 01-foundation (03-structured-output, 05-alternatives); [curriculum-options](../curriculum-options.md) weeks 1–2 |
| 2 (3–4) | B1 First assistant with RAG | 40 | Explain the RAG flow; build a keyword-search RAG assistant with sources | LLM and RAG basics, FAQ dataset, minsearch, prompt building | FAQ assistant answering with sources | LLM Zoomcamp Module 1; Buildcamp 01-foundation/02-rag |
| 3 (5–6) | B2 Ingestion, indexing and use cases | 40 | Ingest and index real documents reproducibly; adapt RAG to different sources | dlt ingestion, Kestra workflows, sqlitesearch, use cases: FAQ, YouTube transcripts, book/documentation Q&A | Documentation assistant with a reproducible index | Buildcamp 02-rag-usecases-tech; LLM Zoomcamp Module 3 + dlt workshop |
| 4 (7–8) | B3 Vector and hybrid search | 40 | Choose between keyword, vector and hybrid search; show good and bad retrieval | Embeddings, sentence-transformers, PostgreSQL + pgvector, hybrid search, reranking (RRF), query rewriting | Examples of good and poor retrieval on the project data | LLM Zoomcamp Module 2 and Module 6 (2024, to refresh); curriculum-options weeks 3–4 |
| 5 (9–10) | B4 Tools and agents | 40 | Give the assistant tools to look up information or call an API; build an agent loop | Function calling, tool contracts, agent loop, web-research agent | Assistant with an issue-lookup or API tool | LLM Zoomcamp Module 1 (agentic part); Buildcamp 03-agents (02-agent-basics, 04-web-research) |
| 6 (11–12) | B5 Frameworks, MCP and human approval | 40 | Define what the assistant does on its own and what needs approval; handle denied or failed actions | PydanticAI, OpenAI Agents SDK, MCP, approval steps, denied and failed tool calls | An assistant that uses an external tool and handles denied or failed actions | Buildcamp 03-agents/03-agent-frameworks, "Agentic Flows"; curriculum-options weeks 5–6 |
| 7 (13–14) | Midterm: deployed first version | 40 | Deliver a working assistant with cited answers and one tool | Scoping, README, deployment, test access | Midterm submission | LLM Zoomcamp project.md; Product Shipping "Midterm: Submit your first version" |
| 8 (15–16) | Midterm review | 40 | Review peer projects; plan improvements from feedback | Peer testing (3 projects), review checklist, separating failures from feature requests | 3 peer reviews, instructor review, improvement plan | Product Shipping midterm feedback, Module 4 |
| 9 (17–18) | B6 Evaluating retrieval | 40 | Build a realistic ground-truth set; measure and tune retrieval | Offline vs online evaluation, LLM-generated ground truth, Hit Rate, MRR, parameter tuning | Retrieval evaluation of the project | LLM Zoomcamp Module 4 |
| 10 (19–20) | B7 Evaluating answers and tool use; regressions | 40 | Evaluate answers and tool use on realistic tasks; compare prompts, models and retrieval; catch regressions | LLM-as-a-judge, agent trajectory evaluation, synthetic users, unit tests, trace replay, Evidently, LangWatch | An evaluation report comparing two configurations and explaining the failure cases; regression suite | Buildcamp 04-testing, documentation-agent (evals, tests, trace_replay); curriculum-options weeks 7–8 |
| 11 (21–22) | B8 Deployment | 40 | Package and deploy the assistant reproducibly | FastAPI/Flask API, Docker Compose, ingestion pipeline in production, setup instructions | Deployed, containerised service | LLM Zoomcamp Module 7 (2024, to refresh); Product Shipping Module 2 "Deploy the product" |
| 12 (23–24) | B9 Tracing, quality, latency and cost | 40 | Trace model and tool calls; track quality, latency and cost | OpenTelemetry, Pydantic Logfire, Grafana, logging to PostgreSQL, user feedback, token and cost tracking | Dashboard with traces, latency and cost measurements | LLM Zoomcamp Module 5; Buildcamp "Monitoring" |
| 13 (25–26) | B10 Handling failures safely | 40 | Add guardrails and fallbacks; test them; handle misuse and service limits | Guardrails, fallbacks, security, errors and service limits | A deployed service with a tested fallback | Buildcamp "Monitoring" (guardrails); Product Shipping Module 5; curriculum-options weeks 9–10 |
| 14 (27–28) | Capstone: build for a concrete use case | 40 | Build the final assistant end to end for one concrete use case | E.g. answering from technical documentation and drafting support replies for human review | Capstone build with consultations | LLM Zoomcamp project.md; Buildcamp Capstone, ai-buildcamp-project-starter |
| 15 (29–30) | Capstone: measure and improve | 40 | Show where it works and where it fails; improve from measurements and tester feedback | Evaluation suite, tester feedback, changelog | Evaluation evidence and a documented improvement | Buildcamp 04-testing; Product Shipping Module 4 |
| 16 (31–32) | Final review and defence | 40 | Defend design and measurement choices; present the deployed assistant | Peer review, technical defence, final test, demo | Final assessment: deployed assistant, reproducible evaluation suite, evidence of improvements | LLM Zoomcamp peer review and criteria; Product Shipping Module 6; curriculum-options weeks 11–12 |
| | **Total** | **640** | | | | |

**Why 16 weeks instead of 12.** The 12-week draft in [curriculum-options.md](../curriculum-options.md) fits each capability into two weeks and has a 2-week capstone. To show where the assistant works, where it fails and how that was measured, the programme also needs a midterm review (week 8), separate retrieval and answer/tool evaluation weeks (9–10), a separate safe-failure week (13) and a measured capstone iteration (15).

**Material notes.** LLM Zoomcamp Modules 6–7 are 2024 recordings and need refreshing. All existing material is recorded or self-paced, so every week needs live lesson, exercise and review plans (the teacher pack in [curriculum-options.md](../curriculum-options.md)).
