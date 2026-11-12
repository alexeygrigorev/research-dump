# Variante B: AI engineering

**12 November 2026.** Course description and syllabus for track B from the survey, [materials/survey.en.md](../materials/survey.en.md), question 1. Evidence and sources: [research.md](research.md). Not submitted anywhere.

Basis, as Alexey specified: his [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) and his Maven course [AI Engineering Buildcamp: From RAG to Agents](https://maven.com/alexey-grigorev/from-rag-to-agents).

## Course description

**Title.** AI Engineering: Build, Evaluate and Run LLM Applications
German working title: *KI-Anwendungsentwicklung mit Large Language Models: RAG, Agenten, Evaluation und Betrieb*

**In one sentence (survey).** Learn to build and run applications that use language models to answer questions or take actions.

**Target group**

- Developers and other technical professionals who can program, use APIs and work with a repository: software, data and ML roles (survey question 8).
- Career changers, if they pass the entry check.
- For the Bildungsgutschein: people who are unemployed or at risk of unemployment, where the Agentur für Arbeit confirms the training is necessary (§ 81 SGB III).

**Learning goals.** By the end, participants can (survey wording):

1. Build an assistant in Python using an LLM API.
2. Use retrieval-augmented generation (RAG).
3. Give the assistant tools to look up information or call an API.
4. Define what it can do on its own and when it needs human approval.
5. Use realistic questions and tasks to evaluate answers and tool use; compare prompts, models and retrieval methods; check for regressions.
6. Deploy the application and trace its model and tool calls.
7. Track quality, latency and cost, and handle failures safely.

**Final project (survey).** Build and deploy an AI assistant for a concrete use case, such as answering questions from technical documentation and drafting support replies. Show where it works, where it fails and how you measured that.

**Prerequisites**

- comfortable programming, preferably in Python
- command line, Git and basic Docker
- able to follow technical teaching and work in English (survey question 6)

No machine-learning background, advanced mathematics or GPU is needed. These are the LLM Zoomcamp's prerequisites. Readiness is checked before admission with a short coding exercise and a documented conversation.

**Format**

- Live teaching, online from Germany or in person in Berlin (Prenzlauer Berg, near S+U Schönhauser Allee). English.
- 1 UE = 45 minutes. 8 UE a day, Monday to Friday 09:00–16:00 including breaks. All UE are taught or actively accompanied by the teacher.
- A 40-UE week: 4 UE review and recall quiz, 8 UE teaching and live demonstration, 12 UE guided exercise, 12 UE accompanied project work, 4 UE code review, demo and oral check. Capstone weeks have less teaching and more project work. Reasons: [research.md](research.md#62-what-i-derived-from-it-my-recommendations).
- Stack: Python. Each concept is first built by hand, then with one framework, which is how both source courses teach. Tools and versions are listed in a dated annex that is reviewed before every cohort.
- One application grows through the programme. Each week adds a capability and a way to check it. Example: a documentation assistant that starts with cited answers, then looks up issues, then drafts support replies for human approval.
- Coding assistants are allowed after a concept has been coded by hand once.
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
- Three checkpoints without AI (weeks 2, 6 and 11): write a retrieval function, trace a tool-call loop by hand, label a set of outputs.
- Midterm (week 8): deployed assistant with cited answers and one tool, three peer reviews and a teacher review.
- Final (week 16): deployed assistant, evaluation report, technical defence. The rubric starts from the LLM Zoomcamp project criteria ([project.md](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/project.md)) and adds criteria it lacks: tools, agent evaluation, tests, guardrails and deployment.

**Certificate.** Provider certificate "AI Engineering" listing the modules with UE, the assessment forms and the result. The AZAV format still has to be created.

## Syllabus: core, 640 UE

"LLMZ" is the LLM Zoomcamp repository. "Buildcamp" is the Maven course; its public code is at https://github.com/alexeygrigorev/ai-engineering-buildcamp-code. "Write" means no teaching material exists yet.

| Wk | Module | UE | Learning outcomes | Topics | Practice and assessed output | Based on |
|---:|---|---:|---|---|---|---|
| 1 | B01 A Python service on an LLM API | 40 | Call a model from a Python service. Get typed, validated output. Handle errors and retries | Environment with `uv`, Git, Docker. Model APIs, messages, system prompts, streaming. Structured output and validation. Tokens and cost per call | Entry check. A small API that returns validated structured answers and survives a failed call | Buildcamp week 1 · LLMZ [unit 1](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/01-agentic-rag) |
| 2 | B02 First assistant with retrieval | 40 | Explain the RAG flow. Build search and an answer with sources by hand | Indexing a document set, keyword search, building the prompt, citing sources | FAQ assistant that answers with sources. Checkpoint without AI: write a retrieval function | LLMZ unit 1 · Buildcamp week 1 · [Minsearch](https://aishippingblog.com/p/minsearch-the-small-search-library) |
| 3 | B03 Ingestion and indexing | 40 | Load real documents into a reproducible index. Choose a chunking approach and justify it | Parsing documents, chunking, metadata, a repeatable pipeline, incremental updates | Documentation assistant with an index that can be rebuilt with one command | Buildcamp weeks 1–3 (chunking) · **Write** for the in-house pipeline |
| 4 | B04 Vector and hybrid search | 40 | Choose between keyword, vector and hybrid search for a dataset. Show good and bad retrieval | Embeddings, vector search in SQLite and Postgres (pgvector), hybrid search and rank fusion, reranking, query rewriting | Three retrieval variants on the project data, with examples of where each fails | LLMZ [unit 2](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/02-vector-search) and [unit 6](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/06-best-practices) (2024, to refresh) · [SQLiteSearch](https://aishippingblog.com/p/how-i-built-sqlitesearch-a-lightweight) |
| 5 | B05 Evaluating retrieval | 40 | Build a realistic question set. Measure retrieval and tune it | Ground truth by hand and generated, Hit Rate, MRR, comparing variants, parameter tuning | Retrieval evaluation of the project with a chosen configuration and the reason for it | LLMZ [unit 4](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/04-evaluation) |
| 6 | B06 Tools and the agent loop | 40 | Give the assistant a tool. Write the tool-call loop by hand. Let the assistant decide when to search | Function calling, tool descriptions and contracts, the agent loop, search as a tool, stop conditions | Assistant that looks up information or calls an API through a tool. Checkpoint without AI: trace a tool-call loop | LLMZ unit 1 (agentic part) · Buildcamp week 3 |
| 7 | B07 Frameworks, MCP and context | 40 | Rebuild the agent with a framework and say what it adds. Connect a tool through MCP. Keep the context small | One agent framework (PydanticAI). MCP client and server. Conversation history, memory, compaction | Assistant on a framework with one MCP tool and a tested limit on context size | Buildcamp week 3 · **Write** for MCP and memory (thin in both sources) |
| 8 | B08 Serving and deployment · midterm | 40 | Serve the assistant as an API. Package and deploy it | FastAPI, streaming responses, Docker Compose, a cloud deployment, secrets, setup instructions | **Midterm:** deployed assistant with cited answers and one tool, README and test access | LLMZ [unit 7](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/07-project-example) (2024, to refresh) · **Write** for cloud deployment |
| 9 | B09 What the assistant may do alone · midterm review | 40 | Define which actions run automatically and which need approval. Handle denied and failed actions. Keep long tasks resumable | Workflows versus agents. Read and write actions, approval steps, permissions in code. State that survives a restart | An action that waits for human approval and handles refusal. Three peer reviews of midterm projects | [Building an AI Book Generator](https://aishippingblog.com/p/building-an-ai-book-generator-with) · **Write** (human approval is thin in both sources) |
| 10 | B10 Testing LLM applications | 40 | Write tests for answers and tool calls. Run them in CI. Catch regressions when a prompt or model changes | pytest for LLM code, tests on tool calls, judge-based assertions, test models, CI | Regression suite for the project running in CI | Buildcamp week 4 · **Write** for CI |
| 11 | B11 Evaluating answers and agents | 40 | Find failure types by reading outputs. Build a judge and check it against human labels. Compare prompts, models and retrieval methods | Error analysis, a labelled reference set, judge alignment, trajectory checks for tool use, synthetic data | Evaluation report comparing two configurations, with the failure cases explained. Checkpoint without AI: label outputs | Buildcamp week 6 · LLMZ unit 4 · [How to Do Evals in 2026](https://aishippingblog.com/p/how-to-do-evals-in-2026) |
| 12 | B12 Tracing and monitoring | 40 | Trace model and tool calls. Monitor quality in production. Collect user feedback | OpenTelemetry, Pydantic Logfire, storing traces, feedback, online judging, Grafana dashboards. 4 UE reserve for what changed | Traces and a dashboard for the deployed assistant | LLMZ [unit 5](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/05-monitoring) · Buildcamp week 5 |
| 13 | B13 Cost, latency and model choice | 40 | Measure cost and latency per request. Reduce both without losing quality. Choose a model by measurement | Token accounting, caching, batching, routing between models, small and open models, timeouts, retries and fallbacks | Cost and latency report with one measured improvement and a tested fallback | LLMZ unit 5 (cost records) · **Write** |
| 14 | B14 Safety: guardrails and prompt injection | 40 | Explain prompt injection and limit its damage. Add and test guardrails. Name the obligations that apply to the product | Input and output checks, least privilege for tools, keeping credentials out of reach, OWASP lists for LLM and agentic applications, personal data, the EU AI Act's dates and duties for engineers. 4 UE reserve for what changed | Threat sketch, tested guardrails and a short list of compliance points for the project | **Write** (prompt injection is missing in both sources; guardrails exist as a workshop) |
| 15 | B15 Capstone: build and measure | 40 | Build the final assistant for one concrete use case. Show where it works and where it fails | Scoping, test users, evaluation on realistic tasks | Capstone build with evaluation evidence | LLMZ [project](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/project.md) · Buildcamp capstone |
| 16 | B16 Capstone: improve, review and defend | 40 | Improve from measurements and feedback. Defend design and measurement choices | A documented improvement, peer review, technical defence, demo | **Final:** deployed assistant, evaluation report, defence | LLMZ project criteria · Buildcamp demo day |
| | **Total** | **640** | | | | |

### Extension weeks

Each is 40 UE and is placed before the capstone. They are added in this order. Each has its own content reason, because duration has to be justified by the course goal.

| Module | Learning outcomes | Topics | Assessed output | Why |
|---|---|---|---|---|
| X1 Multi-step and multi-agent systems | Choose a pattern for a task and justify it against a single agent | Routing, pipelines, plan-then-execute, evaluator loops, orchestrator and workers, their costs | One pattern added to the project and compared with the single-agent version | Agent patterns are in most international syllabi; the Buildcamp has optional material ([research.md](research.md#42-track-b)) |
| X2 Retrieval beyond text chunks | Handle documents and questions that simple retrieval fails on | Tables, PDFs and images, iterative and agent-driven search, file-system search, long context versus retrieval | A hard subset of project questions with a measured improvement | Plain chunk-and-embed retrieval lost its default status in 2026 ([research.md](research.md#52-ai-engineering)) |
| X3 Production operations | Release and run the assistant like other software | CI/CD for prompts and models, infrastructure as code, staged rollout, rollback, load and queues | The project released through a pipeline with a rollback test | Cloud deployment and CI are gaps in both source courses |
| X4 Capstone: second iteration | Run a second measured cycle with users | Second test round, before-and-after comparison | Second release with evidence | The survey's final project asks to show where it works, where it fails and how that was measured |

## Coverage of the survey's learning goals

| Survey goal | Weeks |
|---|---|
| Assistant in Python on an LLM API | 1 |
| RAG | 2, 3, 4 |
| Tools | 6, 7 |
| What it does alone and what needs approval | 9 |
| Evaluation, comparison, regressions | 5, 10, 11 |
| Deployment and tracing | 8, 12 |
| Quality, latency, cost, safe failure | 12, 13, 14 |
| Final project | 15, 16 |

## Why this order

- Retrieval comes first and agents second, as in both source courses.
- Evaluation starts in week 5, before agents. The newest international courses move evaluation forward, and practitioners name it as the skill teams lack most ([research.md](research.md#42-track-b), [5.2](research.md#52-ai-engineering)).
- Deployment is in week 8, so the midterm is a running service and weeks 9–14 work on something real.
- Control, tests, evaluation, monitoring, cost and safety take six weeks. These are the survey's goals 4 to 7, and they are where the source courses are thinnest.
- Fine-tuning and model training are left out. Alexey's own definition of the role and the 2026 surveys agree that most teams do not fine-tune ([research.md](research.md#52-ai-engineering)).

## Stable and fast-moving parts

| Stable: taught as the core | Fast-moving: in the dated annex, reviewed before each cohort |
|---|---|
| Calling a model and validating its output | Model names, prices and limits |
| Search: keyword, vector, hybrid | Vector stores and embedding models |
| Tool contracts and the agent loop | Framework and its API |
| Control flow and permissions in code | MCP protocol version |
| Human approval for actions with consequences | Observability products and attribute names |
| Evaluation from error analysis, checked judges | Evaluation libraries |
| Tracing, cost and latency measurement | Caching and routing features of providers |
| Limiting damage from prompt injection | Lists and legal dates (OWASP, EU AI Act) |

Refresh rules and the open question about reporting changes to the certifier: [research.md](research.md#8-staying-current-what-is-stable-and-what-moves).

## Material to write

Existing material is recorded video, notebooks and text lessons. Every week needs a live lesson plan, exercises and a rubric. New content is needed for:

- week 3 (in-house ingestion pipeline)
- week 7 (MCP, memory)
- week 8 (cloud deployment, refresh of the 2024 recordings)
- week 9 (human approval, resumable state)
- week 10 (CI)
- week 13 (cost, latency, model choice)
- week 14 (prompt injection, compliance)
- the extended capstone rubric
- all extension weeks
