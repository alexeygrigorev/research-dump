# Variante B: AI engineering

**13 November 2026.** Course description and syllabus for track B from the survey, [materials/survey.en.md](../materials/survey.en.md), question 1. Rebased on the **AI Engineering Field Guide** (`alexeygrigorev/ai-engineering-field-guide`, commit `ab21b128`, 9,760 real job postings from Feb–Nov 2026) alongside Alexey's own courses. Evidence and sources: [research.md](research.md). Draft only; not submitted anywhere.

Basis:
- **FG** = AI Engineering Field Guide (`github.com/alexeygrigorev/ai-engineering-field-guide`, commit `ab21b128`, 9,760 builtin.com postings Feb–Nov 2026: `role/02-skills.md`, `role/03-responsibilities.md`, `role/04-use-cases.md`, `role/07-trends.md`).
- **LLMZ** = [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp).
- **Buildcamp** = Maven course [AI Engineering Buildcamp: From RAG to Agents](https://maven.com/alexey-grigorev/from-rag-to-agents) (public code: https://github.com/alexeygrigorev/ai-engineering-buildcamp-code).

## Market basis (AI Engineering Field Guide, 9,760 jobs)

Every module and technology choice in this syllabus reflects what employers require in 9,760 AI Engineer job postings (Feb–Nov 2026):

- **Applied integrator role, not model research**: 97.4% of postings are applied/production (only 2.6% research). Within AI-First roles (68.9% of the market, 6,721 jobs), the **integrator stack** (RAG, agents, APIs) rose from 80.0% in February to **91.7%** in November, while the trainer stack fell from 37.5% to 27.2% (pure-integrator roles: 50.9% → **66.8%**). Fine-tuning is a primary responsibility in only **3.2%** of AI-First roles and absent from responsibilities in **86.0%** (overall fine-tuning share fell 17.1% → 9.4%). Fine-tuning and model training from scratch are therefore left out of the 16-week core.
- **Full-stack beyond GenAI (86.9%)**: **Python** is mandatory (71.6% overall, **75.9%** AI-First), followed by **GenAI + Ops** (**71.0%** of AI-First: **CI/CD** 36.9%, **Docker** 24.2%, **Kubernetes** 23.6%, **Observability** 20.7% / 23.6% AI-First), **GenAI + Web** (**59.2%**: APIs 2,515 jobs, REST APIs 1,630, **FastAPI** 928, React 1,373; backend 61.0%, frontend 30.8%), **Databases** (**Vector Databases** 2,201 jobs, **PostgreSQL** 1,020 jobs, **SQL** 14.6% rising 11.1% → 14.9%), and **Cloud** (**AWS** 39.3% overall / 41.8%–45.4% AI-First > Azure 29.7% > GCP 29.1%).
- **RAG + Agents are the core**: **Agents (any)** appear in **56.2%** of all jobs (**74.0%** AI-First; responsibilities +10.1 pp to 55.8% in Nov) and **RAG** in **40.1%** (**56.0%** AI-First). Jobs requiring *both* RAG and agents jumped from 33.1% to **51.0%** of AI-First postings (3,183 jobs).
- **Standard agent & retrieval stack**: **LangChain** (21.1% overall, 76.8% of framework adopters) and **LangGraph** (14.4% overall, climbing 7.4% → 15.2% and 37.7% → **71.0%** among framework adopters) are the #1 co-occurring pair (3.5x lift, 1,030 jobs). **MCP** (15.6%) is the fastest-rising named skill (9.9% → **20.4%**, +0.94 pp/scrape), followed by **Function Calling** (15.1%, 9.6% → **18.5%**).
- **Evaluation & guardrails are the differentiator**: **61.8%** of AI-First roles require evaluation-related skills, rising from 55.9% to **69.3%** in November ("Evaluation and Testing" appears in **79.0%** of November responsibilities, +9.6 pp). Inside that group: **LLM Evaluation** (33.5% AI-First), **Observability** (23.6%), **Guardrails** (19.8% AI-First; 10.2% → **17.5%** overall), and **Monitoring** (15.4%). LLM-native eval tooling (`LangSmith`, `Langfuse`, `Guardrails`, `LLM Evaluation`) rose 26.7% → **34.5%** while classic MLOps (`MLflow`, `Kubeflow`) fell 19.9% → 14.5%.
- **Enterprise automation & document workflows lead use cases**: **Automating manual workflows** (58.8% of jobs), **Internal operational efficiency** (57.5%), **Agentic systems** (49.9%), **Finding information in company data** (43.8%), and **Document processing** (rising 13.3% → 16.0%) dominate, while customer-facing Q&A fell **-13.8 pp** (44.7% → 30.9%).

## Course description

**Title.** AI Engineering: Build, Evaluate and Run LLM Applications
German working title: *KI-Anwendungsentwicklung mit Large Language Models: RAG, Agenten, Evaluation und Betrieb*

**In one sentence (survey).** Learn to build and run applications that use language models to answer questions or take actions.

**Target group**

- Developers and other technical professionals who can program, use APIs and work with a repository: software, data and ML roles (survey question 8). Note from FG: employers overwhelmingly hire mid and senior engineers into AI Engineering roles (junior/entry-level stayed at 0.8%–1.5% across all 10 scrapes), so the programme targets working developers transitioning into AI engineering rather than complete beginners.
- Career changers with verifiable programming experience, if they pass the entry check.
- For the Bildungsgutschein: people who are unemployed or at risk of unemployment, where the Agentur für Arbeit confirms the training is necessary (§ 81 SGB III).

**Learning goals.** By the end, participants can (survey wording):

1. Build an assistant in Python using an LLM API.
2. Use retrieval-augmented generation (RAG) and document processing over company data.
3. Give the assistant tools, function calling and MCP connections to look up information or call an API.
4. Define what it can do on its own and when it needs human approval, with multi-step agentic control flow.
5. Use realistic questions and tasks to evaluate answers and tool use; compare prompts, models and retrieval methods; check for regressions.
6. Deploy the application to the cloud and trace its model and tool calls.
7. Track quality, latency and cost, and handle failures safely with guardrails.

**Final project (survey + FG use cases).** Build and deploy an AI assistant for a concrete enterprise or operational use case — such as an internal knowledge, document-processing and workflow-automation assistant that retrieves cited answers from messy company documents, executes tool/MCP actions with human approval, and runs behind an API. Show where it works, where it fails and how you measured that.

**Prerequisites**

- comfortable programming, preferably in Python
- command line, Git and basic Docker
- able to follow technical teaching and work in English (survey question 6)

No machine-learning background, advanced mathematics or GPU is needed. These are the LLM Zoomcamp's prerequisites. Readiness is checked before admission with a short coding exercise and a documented conversation.

**Format**

- Live teaching, online from Germany or in person in Berlin (Prenzlauer Berg, near S+U Schönhauser Allee). English.
- 1 UE = 45 minutes. 8 UE a day, Monday to Friday 09:00–16:00 including breaks. All UE are taught or actively accompanied by the teacher.
- A 40-UE week: 4 UE review and recall quiz, 8 UE teaching and live demonstration, 12 UE guided exercise, 12 UE accompanied project work, 4 UE code review, demo and oral check. Capstone weeks have less teaching and more project work. Reasons: [research.md](research.md#62-what-i-derived-from-it-my-recommendations).
- Stack: Python. Each concept is first built by hand, then with the market-standard framework (**LangChain + LangGraph**, with **PydanticAI** compared as a typed-agent alternative). Tools and versions are listed in a dated annex that is reviewed before every cohort.
- One application grows through the programme. Each week adds a capability and a way to check it. Example: an internal operations and documentation assistant that starts with cited answers over company documents, then looks up tickets/issues via MCP and APIs, then executes multi-step workflow actions for human approval.
- Coding assistants (`Claude Code`, `GitHub Copilot`, `Cursor` — listed in 13.6% of Nov postings, up from 7.6%) are allowed after a concept has been coded by hand once.
- Taught by Alexey Grigorev. No subcontractors. The LLM Zoomcamp units taught by partners (orchestration, data ingestion) are not reused; their topics are taught in-house.

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

- Weekly: the assessed output in the table below, plus a live walkthrough.
- Three checkpoints without AI (weeks 2, 5 and 10): write a retrieval function, trace a tool-call loop by hand, label a set of outputs.
- Midterm (week 7): deployed assistant with cited answers and one tool, three peer reviews and a teacher review (week 8).
- Hiring prep and interviews (80 UE total, not two consecutive weeks): Week 13 (40 UE full week) covers hiring loops, CV/LinkedIn/GitHub, a first algorithm-style coding round without AI (now asked even for QA roles), a timed take-home assignment with review, presenting the midterm/assistant project, and first peer mock interviews, plus capstone scoping. Weeks 14–16 spread the second 40 UE of interview practice (~13–14 UE/week: timed algorithm and live-coding drills without AI, peer mock interviews in squads, project-talk rehearsals) alongside the 80 UE individual capstone. Training and interview practice only; no job-placement promises.
- Career consultations (outside the 80 UE block, scheduled during project/studio time from the existing career-coach line so total stays 640 UE): three individual 45-minute sessions plus one written review of CV and profile per participant (session 1 in weeks 4–5 on target role, market positioning and CV/profile gaps; session 2 in week 13 on application plan and first mock feedback; session 3 in weeks 15–16 on debriefing real interviews, gaps and salary).
- Final (weeks 14–16, 80 UE capstone): deployed assistant, evaluation report, technical defence in week 16. The rubric starts from the LLM Zoomcamp project criteria ([project.md](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/project.md)) and adds criteria it lacks: tools, agent evaluation, tests, guardrails and deployment.

**Certificate.** Provider certificate "AI Engineering" listing the modules with UE, the assessment forms and the result. The AZAV format still has to be created.

## Syllabus: core, 640 UE

"LLMZ" is the LLM Zoomcamp repository. "Buildcamp" is the Maven course; its public code is at https://github.com/alexeygrigorev/ai-engineering-buildcamp-code. "FG" is the AI Engineering Field Guide (`ab21b128`, 9,760 jobs). "Write" means no teaching material exists yet.

| Wk | Module | UE | Learning outcomes | Topics | Practice and assessed output | Field Guide & course basis |
|---:|---|---:|---|---|---|---|
| 1 | B01 Agentic engineering basics (8 UE) + A Python service on an LLM API (32 UE) | 40 | Set up a safe coding-agent baseline on day 1; call an LLM from Python with typed, validated output and error handling | **Day 1 (8 UE):** coding-agent basics (`Claude Code`, `Cursor`) — project context file, permissions, cost control, basic plan-edit-review loop. **Days 2–5 (32 UE):** `uv`, Git, Docker, OpenAI/Anthropic APIs, messages, system prompts, streaming, structured output (`pydantic`), tokens and cost | Entry check. Working agent-ready environment, plus a small API that returns validated structured answers and survives a failed call | **FG**: Python 71.6% (75.9% AI-First), OpenAI API 14.6%, Prompt Eng 34.8% · Buildcamp week 1 · LLMZ [unit 1](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/01-agentic-rag) · Cross-module (`t109u`/`t113u`) |
| 2 | B02 Retrieval, document processing and indexing | 40 | Build a reproducible ingestion pipeline over company documents and answer with cited sources by hand | Indexing a document set, keyword search (`minsearch`), parsing PDFs/Markdown/tables, chunking, metadata, repeatable incremental updates, prompt with citations | Knowledge/FAQ assistant with a one-command ingestion pipeline that answers with sources. Checkpoint without AI: write a retrieval function | **FG**: RAG 40.1% (56.0% AI-First), Document processing 13.3% → 16.0%, Data & pipelines 29.7% · LLMZ unit 1 · Buildcamp weeks 1–3 · **Write** for in-house pipeline |
| 3 | B03 Vector and hybrid search | 40 | Choose between keyword, vector and hybrid search for a dataset. Show good and bad retrieval | Embeddings, vector search in SQLite and PostgreSQL (`pgvector`), hybrid search and rank fusion, reranking, query rewriting | Three retrieval variants on the project data, with examples of where each fails | **FG**: Vector DBs 2,201 jobs, Embeddings 16.3% (23.2% AI-First), PostgreSQL 1,020 jobs, SQL 14.6% (11.1% → 14.9%) · LLMZ [unit 2](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/02-vector-search) and [unit 6](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/06-best-practices) (2024, to refresh) · [SQLiteSearch](https://aishippingblog.com/p/how-i-built-sqlitesearch-a-lightweight) |
| 4 | B04 Evaluating retrieval | 40 | Build a realistic question set. Measure retrieval and tune it | Ground truth by hand and generated, Hit Rate, MRR, comparing variants, parameter tuning | Retrieval evaluation of the project with a chosen configuration and the reason for it | **FG**: Eval & Testing 79.0% Nov responsibilities (+9.6 pp), Eval skills 69.3% AI-First · LLMZ [unit 4](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/04-evaluation) |
| 5 | B05 Agentic engineering workflow (32 UE) + Tools, function calling and the agent loop (8 UE) | 40 | Run the full agentic workflow on the project repo; give the assistant a tool and write the tool-call loop by hand | **Mon–Thu (32 UE):** full agentic engineering workflow on the squad/project repo — spec to tasks, tests as the contract, reviewing agent diffs, CI, parallel agents. **Fri (8 UE):** function calling, tool contracts, the agent loop, stop conditions | Project repo configured with specs, tests and CI using the agent workflow, plus an assistant that calls an API through a tool. Checkpoint without AI: trace a tool-call loop | **FG**: Agents (any) 56.2% (74.0% AI-First), Function Calling 15.1% (9.6% → 18.5%), RAG+Agents 51.0% AI-First · Cross-module (`t109u`/`t113u`) · LLMZ unit 1 (agentic part) · Buildcamp week 3 |
| 6 | B06 Agent frameworks, MCP and context | 40 | Rebuild the agent with a framework and say what it adds. Connect a tool through MCP. Keep the context small | **LangChain + LangGraph** as primary orchestration stack (with **PydanticAI** compared). MCP client and server. Conversation history, memory, compaction | Assistant on LangGraph with one MCP tool and a tested limit on context size (plus PydanticAI comparison note) | **FG**: LangChain 21.1% (76.8% of adopters), LangGraph 14.4% (71.0% of adopters, 3.5x lift), MCP 15.6% (9.9% → 20.4%, #1 riser) · Buildcamp week 3 · **Write** for LangGraph/MCP/memory |
| 7 | B07 Serving and cloud deployment · midterm | 40 | Serve the assistant as an API. Package and deploy it to the cloud | FastAPI, streaming responses, REST API contracts, Docker Compose, cloud deployment (**AWS** primary), secrets, setup instructions | **Midterm:** deployed assistant with cited answers and one tool, README and test access | **FG**: GenAI+Web 59.2% (APIs 2,515, FastAPI 928), Docker 24.2%, AWS 39.3% (41.8% AI-First, #1 cloud) · LLMZ [unit 7](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/07-project-example) (2024, to refresh) · **Write** for AWS/FastAPI deployment |
| 8 | B08 Agentic workflows and human approval · midterm review | 40 | Define which actions run automatically and which need approval. Handle denied and failed actions. Keep long tasks resumable | Workflows versus agents (LangGraph state/interrupts). Read and write actions, approval steps, permissions in code. State that survives a restart | An internal workflow action that waits for human approval and handles refusal. Three peer reviews of midterm projects | **FG**: Automating workflows 58.8%, Internal operations 57.5%, Agentic workflows 32.8% · [Building an AI Book Generator](https://aishippingblog.com/p/building-an-ai-book-generator-with) · **Write** (human approval is thin in both sources) |
| 9 | B09 Testing LLM applications and CI/CD | 40 | Write tests for answers and tool calls. Run them in CI. Catch regressions when a prompt or model changes | `pytest` for LLM code, tests on tool calls, judge-based assertions, test models, CI/CD pipelines | Regression suite for the project running in CI/CD | **FG**: CI/CD 36.9% (36.7% AI-First), Eval & Testing 79.0% Nov responsibilities · Buildcamp week 4 · **Write** for CI/CD |
| 10 | B10 Evaluating answers and agents | 40 | Find failure types by reading outputs. Build a judge and check it against human labels. Compare prompts, models and retrieval methods | Error analysis, golden/labelled reference sets, LLM-as-judge alignment, hallucination checks, trajectory checks for tool use, synthetic data | Evaluation report comparing two configurations, with the failure cases explained. Checkpoint without AI: label outputs | **FG**: LLM Evaluation 33.5% AI-First (20.3% → 26.6% overall), Eval & Testing 79.0% · Buildcamp week 6 · LLMZ unit 4 · [How to Do Evals in 2026](https://aishippingblog.com/p/how-to-do-evals-in-2026) |
| 11 | B11 Tracing, monitoring, cost and latency | 40 | Trace model and tool calls, monitor quality and drift, and reduce cost and latency without losing quality | OpenTelemetry, LLM-native observability (`Langfuse`/`LangSmith`/`Logfire`), Grafana dashboards; token accounting, prompt/semantic caching, routing, timeouts, retries and fallbacks | Traces, monitoring dashboard, and cost/latency report with one measured improvement and a tested fallback | **FG**: Observability 20.7%, Monitoring 15.4%, Deploy/production 78.3% · LLMZ [unit 5](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/05-monitoring) · Buildcamp week 5 · **Write** |
| 12 | B12 Safety: guardrails, injection and compliance | 40 | Explain prompt injection and limit its damage. Add and test guardrails. Name the obligations that apply to the product | Input and output guardrails, least privilege for tools, keeping credentials out of reach, OWASP lists for LLM and agentic applications, personal data, the EU AI Act's dates and duties for engineers. 4 UE reserve for what changed | Threat sketch, tested guardrails and a short list of compliance points for the project | **FG**: Guardrails 19.8% AI-First (10.2% → 17.5% overall), Security/Safety/Compliance 37.5% Nov responsibilities · **Write** (prompt injection is missing in both sources; guardrails exist as a workshop) |
| 13 | B13 Technical interviews and hiring prep (full week) | 40 | Prepare systematically for AI/LLM and QA-automation interviews, solve algorithm-style coding rounds without AI, deliver scoped take-home assignments, present AI systems and run first peer mocks | How hiring loops work and how to prepare; CV, LinkedIn and GitHub; algorithm-style coding rounds without AI (asked even for QA roles); timed take-home assignment with review; presenting the midterm/assistant project; first peer mock interviews; individual capstone scoping. Plus career consultation 2 (application plan and first mock feedback) during studio time. No job-placement promises | Solved algorithm-style coding drills (without AI), a documented take-home/test assignment, a 5-minute project presentation, first peer mock interviews with written feedback, and capstone scope | [AI Engineering Field Guide: Interview](https://github.com/alexeygrigorev/ai-engineering-field-guide/tree/main/interview) (`01-interview-process.md`, `03-get-hired.md`, `05-trends.md`) · **Write** |
| 14 | B14 Capstone I + interview practice | 40 | Build the core of the individual AI assistant capstone (~27 UE) while continuing timed coding drills and peer mock interviews (~13 UE) | Capstone build and integration for one enterprise workflow/document use case; timed algorithm and live-coding practice without AI; peer mock interviews in squads | Working capstone assistant core with tests, plus weekly coding drills and peer mock interview notes | **FG**: Integrator stack 91.7% AI-First, RAG+Agents 51.0% · LLMZ [project](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/project.md) · Buildcamp capstone |
| 15 | B15 Capstone II + interview practice | 40 | Evaluate, measure and improve the capstone assistant (~27 UE) alongside mock interviews and project-talk rehearsals (~13 UE) | Test users, evaluation on realistic tasks, documented improvement; squad mock interviews and project-talk rehearsals. Career consultation 3 (debrief of real interviews, gaps, salary; weeks 15–16) during studio time | Evaluation evidence and improved capstone assistant, plus mock interview and project-talk rehearsal notes | **FG**: Eval 69.3%, Ops 71.0% · LLMZ project · Buildcamp capstone |
| 16 | B16 Capstone III + final defence and interview practice | 40 | Finalise, deploy and defend the 80 UE capstone (~26 UE) and complete final interview practice and rehearsals (~14 UE) | Final deployment, peer review, technical defence, demo; final algorithm/live-coding drills, peer mocks and project-talk rehearsals. No job-placement promises | **Final:** deployed assistant, evaluation report, technical defence, and completed 80 UE interview-prep portfolio | **FG**: Production & Eval focus · LLMZ project criteria · Buildcamp demo day |
| | **Total** | **640** | | | | |

### Extension weeks

Each is 40 UE and is placed before the capstone. They are added in this order. Each has its own content reason, because duration has to be justified by the course goal.

| Module | Learning outcomes | Topics | Assessed output | Why (Field Guide & course basis) |
|---|---|---|---|---|
| X1 Multi-step and multi-agent systems | Choose a pattern for a task and justify it against a single agent | Routing, pipelines, plan-then-execute, evaluator loops, orchestrator and workers (`LangGraph` multi-agent, `CrewAI`/`AutoGen` comparison), their costs | One pattern added to the project and compared with the single-agent version | **FG**: Agent builder is the #1 archetype (29.9%); `LangGraph` (71.0% of framework adopters), `CrewAI` (26.2%), `AutoGen` (25.1%) all grew sharply; Buildcamp has optional material ([research.md](research.md#42-track-b)) |
| X2 Retrieval beyond text chunks | Handle documents and questions that simple retrieval fails on | Complex PDFs, tables and images, iterative and agent-driven search, file-system search, long context versus retrieval | A hard subset of project questions with a measured improvement | **FG**: Document processing grew 13.3% → 16.0%; plain chunk-and-embed retrieval lost its default status in 2026 ([research.md](research.md#52-ai-engineering)) |
| X3 Production operations and Kubernetes | Release and run the assistant like other software | CI/CD for prompts and models, **Kubernetes** deployment, infrastructure as code (`Terraform`), staged rollout, rollback, load and queues | The project released through a pipeline with a rollback test on container/Kubernetes infra | **FG**: GenAI + Ops is 71.0% of AI-First (CI/CD 36.9%, Docker 24.2%, Kubernetes 23.6% rising 18.6% → 23.8%); cloud deployment and CI/K8s are gaps in both source courses |
| X4 Capstone: second iteration | Run a second measured cycle with users | Second test round, before-and-after comparison | Second release with evidence | The survey's final project asks to show where it works, where it fails and how that was measured |

## Coverage of the survey's learning goals

| Survey goal | Weeks |
|---|---|
| Assistant in Python on an LLM API | 1 |
| RAG & document processing | 2, 3 |
| Tools & MCP | 5, 6 |
| What it does alone and what needs approval | 8 |
| Evaluation, comparison, regressions | 4, 9, 10 |
| Deployment and tracing | 7, 11 |
| Quality, latency, cost, safe failure | 11, 12 |
| Final project (80 UE capstone) | 14–16 |
| Technical interviews and hiring prep (80 UE) | 13 (40 UE), 14–16 (40 UE) |

## Why this order

- Retrieval comes first and agents second, as in both source courses — matching FG's two largest AI-First archetypes (RAG app builder 26.6% and Agent builder 29.9%) and the 51.0% of AI-First jobs requiring both. The 40 UE agentic engineering cross-module (`t109u`/`t113u`: 8 UE week 1 day 1 for agent basics + 32 UE Mon–Thu of week 5 for the full agent workflow on the project/squad repo) leaves the LLM Zoomcamp retrieval backbone in weeks 2–4 untouched (in the 13-week 520 UE AZAV variant, squad project shifts from 200 to 168 UE).
- Evaluation starts in week 4, before agents. The newest international courses move evaluation forward, and FG confirms evaluation-related skills are required in 69.3% of AI-First roles (79.0% of November responsibilities).
- Deployment is in week 7, so the midterm is a running service on FastAPI/Docker/AWS and weeks 8–12 work on something real.
- Control, tests, evaluation, monitoring, cost and safety take five weeks. These are the survey's goals 4 to 7, the highest-momentum FG areas (`Guardrails`, `LLM Evaluation`, `Observability`, `CI/CD`), and where the source courses are thinnest.
- Fine-tuning and model training are left out of the core. FG shows 97.4% of roles are applied/production, the integrator stack reached 91.7% of AI-First jobs, and fine-tuning is absent from responsibilities in 86.0% of postings (primary responsibility in only 3.2%).
- Weeks 13–16 combine 80 UE of interview preparation (40 UE full week 13 + 40 UE spread across weeks 14–16) with an 80 UE capstone (weeks 14–16), plus three individual 45-minute career consultations and a written CV/profile review scheduled during studio time. Starting interview prep in week 13 lets participants apply and interview while they still have instructor and career-coach support.

## Stable and fast-moving parts

| Stable: taught as the core | Fast-moving: in the dated annex, reviewed before each cohort |
|---|---|
| Calling a model and validating its output | Model names, prices and limits |
| Search: keyword, vector, hybrid | Vector stores (`pgvector`, Pinecone, Weaviate) and embedding models |
| Tool contracts and the agent loop | Framework APIs (`LangChain`, `LangGraph`, `PydanticAI`) |
| Control flow and permissions in code | MCP protocol version |
| Human approval for actions with consequences | Observability products (`Langfuse`, `LangSmith`, `Logfire`) and attribute names |
| Evaluation from error analysis, checked judges | Evaluation libraries |
| Tracing, cost and latency measurement | Caching and routing features of providers |
| Limiting damage from prompt injection | Lists and legal dates (OWASP, EU AI Act) |

Refresh rules and the open question about reporting changes to the certifier: [research.md](research.md#8-staying-current-what-is-stable-and-what-moves).

## Material to write

Existing material is recorded video, notebooks and text lessons. Every week needs a live lesson plan, exercises and a rubric. New content is needed for:

- week 2 (in-house document-processing and ingestion pipeline)
- week 6 (LangGraph orchestration, MCP client/server, memory)
- week 7 (FastAPI + Docker + AWS cloud deployment, refresh of the 2024 recordings)
- week 8 (human approval, resumable LangGraph state)
- week 9 (CI/CD for LLM tests)
- week 11 (monitoring, cost, latency, model choice)
- week 12 (prompt injection, guardrails, compliance)
- weeks 13–16 (80 UE interview prep: algorithm-style coding drills, take-home briefs, mock-interview rubrics, project-talk rehearsals)
- the extended capstone rubric
- all extension weeks (including X3 Kubernetes/IaC)
