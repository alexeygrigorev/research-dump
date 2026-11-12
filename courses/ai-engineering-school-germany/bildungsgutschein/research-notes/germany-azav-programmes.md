# Comparable Bildungsgutschein/AZAV programmes in Germany: agentic engineering and AI engineering

Research date: 2026-11-12. All URLs below were fetched on 2026-11-12 unless marked "search snippet only".

## How to read this file

- **[F]** = I fetched the page/PDF and the figures come from it. Web pages were read through a summarising fetch tool, so wording is paraphrased unless in quotes; PDFs marked **[F-PDF]** were downloaded and read as raw text with `pdftotext` (highest confidence).
- **[S]** = from a search-result snippet only; not verified on the source page.
- **[KURSNET-mirror]** = studysmarter.de pages that republish the Bundesagentur für Arbeit course catalogue ("Katalog der Bundesagentur für Arbeit, Stand 07/2026"). They give price *bands* and duration *bands*, not exact figures, and explicitly leave AZAV status of the specific Maßnahme "to be confirmed".
- "not published" = the fetched page did not state it.
- Anything I calculated myself is labelled **(my arithmetic)**.
- Not reachable: genaumeinkurs.de (HTTP 403 on every page), digitalcareerinstitute.org (403), techstarter.de (HTTP 522), codersbay.de (TLS certificate error), Turing College Notion pages (render empty), MSIT syllabus PDFs (over 10 MB fetch limit). mein-now.de / KURSNET itself was not queried directly (JS search app); the studysmarter mirror was used instead.

---

## 1. Comparison table

| # | Provider / course | Lang | Format | Duration / UE | Price (as stated) | AZAV / BGS (as stated) | Entry level | Main subject | Src |
|---|---|---|---|---|---|---|---|---|---|
| 1 | IfaDW – AI Engineer | not published (page German) | live online, Mon-Fri 8-16 | 30 weeks, 1,050 UE | 14,658.00 EUR | AZAV, cert. M-26-26532-1 (GUTcert), valid to 03.02.2029 | basic maths/stats, basic IT | Python DA -> ML -> DL -> NLP/GenAI -> Big Data -> MLOps | [F] |
| 2 | IfaDW – KI-Entwickler | not published | live online | 25 weeks, 875 UE | 12,600.00 EUR | AZAV (GUTcert) | same | same minus Big Data | [F] |
| 3 | IfaDW – KI-Anwendungsentwickler | not published | live online | 15 weeks, 525 UE | 7,413.00 EUR | AZAV, cert. M-26-26532-2 (GUTcert), valid to 19.05.2029 | same | Python DA -> ML -> NLP/GenAI | [F] |
| 4 | Turing College – AI Engineering (BGS version) | DE or EN | live online, fixed timetable | "3 months", 520 UE on certificate; 30 h/week = "40 academic hours" | 0 EUR with BGS; self-funded 3,500 EUR upfront or 1,055 EUR x 4 | AZAV-certified | >= 1 year Python or JS | LLM apps: prompt eng., LangChain/RAG, agents, capstone | [F] |
| 5 | Turing College – Building with AI Agents (BGS version) | DE or EN | live online, fixed timetable | 3 months, 520 UE | 0 EUR with BGS; self-paid 2,000 EUR upfront (regular 3,500 EUR) or 625 EUR x 4 | AZAV-certified | no coding experience | building tools with Claude Code (non-developers) | [F] |
| 6 | neue fische / Spiced – Agentic Machine Learning Engineer | EN | live online, ~15 participants, Mon-Fri 9:00-18:30 | 14 weeks; UE not published | not published | "AZAV- & HZA-zertifiziert" | strong Python, SQL, stats/linear algebra | classical ML -> DL -> LLM/RAG -> agents -> evals/safety -> capstone | [F] + [F-PDF] |
| 7 | neue fische / Spiced – Agentic AI: Build and Deploy AI Agents | EN | live online full-time | 8 weeks; UE not published | not published | "eligible for funding with an education voucher" (PDF); AZAV not stated on the Spiced page | solid Python, Git, CLI, LLM/API understanding, admissions test | agents only; 3-week capstone | [F] + [F-PDF] |
| 8 | neue fische / Spiced – AI Engineering (DS + MLE) | EN & DE | live online | 32 weeks; UE not published | not published; KURSNET-mirror band "über 10.000 €" for a neuefische "AI Engineer" listing | AZAV & HZA | programming knowledge (Python preferred) | DS -> ML -> DL -> GenAI -> MLOps -> LLMOps; IHK cert | [F] + [F-PDF] |
| 9 | neue fische / Spiced – Software Development with AI | DE & EN | live online | 16 weeks; UE not published | not published | "100% eligible for funding with an education voucher" (PDF) | none (beginners) | web dev + "Agentic Coding (Claude Code)" block | [F] + [F-PDF] |
| 10 | neue fische – Advanced Software Development with AI | DE | live online | 16 weeks; UE not published | not published | AZAV & HZA | HTML/CSS/JS experience | TypeScript/NestJS/Next.js/Docker + "AI-Driven Development"; 5-week capstone | [F] + [F-PDF] |
| 11 | WBS Coding School – AI Software Development | EN or DE | live online, Mon-Fri 9:00-17:30 | 17 weeks; UE not published | 0 EUR with BGS; self-funded 9,900 EUR | AZAV-certified | beginners; B2 language | MERN + TypeScript, 1 week GenAI, 1 week "Agentic AI & Developer Workflows", 3-week project | [F] |
| 12 | WBS Coding School – AI Agents & Automations | EN or DE | live online | 12 weeks | 0 EUR with BGS; self-funded 7,500 EUR | AZAV-certified | no prior experience | n8n + Python automations, agents | [F] |
| 13 | WBS Coding School – AI Automation Engineering | EN and DE | live online | 10 months, "40-week curriculum" | not published | BGS funding advertised; AZAV not stated on page | none | n8n -> Python -> agent backends -> MCP/RAG; 4-week final project | [F] (page truncated after module 3) |
| 14 | alfatraining – AI Engineer | DE | live online (alfaview), Mon-Fri 8:30-15:35 | 16 weeks (4 x ~20 days); UE not published | not published | AZAV-certified | Python + SQL; degree in CS/maths or comparable | Data Eng -> ML -> DL -> Reinforcement Learning | [F] |
| 15 | alfatraining – Agentische Softwareentwicklung mit Claude Code | DE | live online | 2 weeks (~10 days); UE not published | not published | AZAV-certified, BGS | agentic-AI knowledge, one programming language, Git | **Claude Code as main subject** | [F] |
| 16 | Viona / IBB – Softwareentwicklung mit KI-Tools (course VZ-E-4683-1) | DE | virtual live, full-time | 4 weeks (20 days); UE not published | "€ 0,00" (flyer shows funded price only) | provider "zugelassener Träger nach der AZAV", BGS 100% | one programming language; German B2 | **AI-assisted coding as main subject** (tool-agnostic) | [F-PDF] |
| 17 | Digitale Leute School – AI Software Engineering Bootcamp | EN | full-time / part-time / video, remote | 3 months (12 weeks on overview page); UE not published | not published; KURSNET-mirror band "5.000–10.000 €" for sibling listings | "AZAV-zertifiziert"; "BGS möglich" for full-time | some dev experience | product skills + AI-assisted engineering + agentic AI | [F] |
| 18 | Digitale Leute School – Vibe Coding Bootcamp | DE | full-time / part-time / video, remote | 3 months (12 weeks) | not published | AZAV-certified | no programming | vibe coding for founders/PMs/designers | [F] |
| 19 | Ironhack – Remote AI Engineering Bootcamp | EN | live online | 9 weeks full-time / 24 weeks part-time; hours not published; 40 h prework | 8,500 EUR | "AZAV-certified under SGB III"; BGS "up to 100% funded, subject to approval" | none | Python -> ML/DL -> GenAI/LLMs/agents | [F] |
| 20 | Le Wagon Berlin – AI Software (web dev) | not published | in person or online | "9 Intensive Weeks", 400h + 40h prework | not published | "certified and recognized by the government"; BGS "is possible" (AZAV word not on page) | none | Ruby/Rails web dev, 40h AI building blocks, 8h AI-assisted coding, 80h project | [F] |
| 21 | Masterschool / MSIT – AI Engineering; GenAI Engineering; AI Systems Backend Engineering | EN (IHK exam DE) | online | not published | not published ("100% funded") | AZAV-certified | none | Python from zero, LLM APIs, prompting; IHK certificate | [F] |
| 22 | SkillSprinters – Digitalisierungsmanager für Prozessautomatisierung und KI | DE | live Zoom, Mon-Fri 8-16 | ~4 months full-time (80 days), 720 UE | 10,548.00 EUR | "nach AZAV zugelassen (DEKRA)" | not captured | no-code automation + LLMs (not a developer course) | [F] (vendor blog) |
| 23 | COMCAVE – KI-Engineering: KI-Agenten und Workflow-Automatisierung | DE | full-time 8:00-16:45 or part-time | ca. 4 weeks | not published | "nach AZAV durch die Cert-IT ... zugelassen" | Ausbildung/Studium, good PC skills | Copilot/ChatGPT/Claude prompting, Power Automate/Zapier/Make | [F-PDF] |
| 24 | WBS Training – AI Engineer – Effizient arbeiten mit Power KI-Tools | DE | full-time | 71 days (7 x 10-day modules + intro) | not published | BGS listed | no programming needed | Python basics, prompt engineering, agents, n8n | [F-PDF] |

Unit economics for the four programmes that publish both price and UE (**my arithmetic**): IfaDW AI Engineer 14,658 / 1,050 = 13.96 EUR/UE; IfaDW KI-Entwickler 12,600 / 875 = 14.40 EUR/UE; IfaDW KI-Anwendungsentwickler 7,413 / 525 = 14.12 EUR/UE; SkillSprinters 10,548 / 720 = 14.65 EUR/UE. All four sit between the 2026 B-DKS for "Softwareentwicklung – Spezialist" (13.24 EUR) and "– Experte" (15.46 EUR), see section 3.

---

## 2. Per-programme detail

### 2.1 IfaDW Institut für angewandte Datenwissenschaft – AI Engineer [F]
- URL: https://www.ifadw.de/ai-engineer/ (overview: https://www.ifadw.de/)
- Format: "100 % remote", daily live teaching Mon-Fri 8-16; morning expert input, afternoon guided tutorials and independent programming. Max group size 12.
- Duration: 30 weeks, 1,050 UE. Six modules of five weeks each. UE per module is not stated on this page; the standalone module "Angewandtes Maschinelles Lernen" is listed at 175 UE, which matches 6 x 175 = 1,050 (inference by the fetch, not stated per module).
- Price: 14,658.00 EUR "Lehrgangskosten"; 0 EUR with Bildungsgutschein; page states there is no self-payer offer.
- AZAV: Träger W-26-26532 (GUTcert, valid to 18.01.2031); Maßnahme certificate M-26-26532-1 (valid to 03.02.2029). § 81 and § 82 SGB III.
- Prerequisites: basic maths and statistics, basic IT skills, interest in AI applications, internet-capable computer; individual intake consultation documented under § 179 SGB III.
- Target group: job seekers, career starters, career changers, specialists from IT/maths/science/business.
- Modules: (1) Datenanalyse mit Python, weeks 1-5; (2) Angewandtes Maschinelles Lernen, 6-10; (3) Deep Learning, 11-15; (4) NLP & Generative AI, 16-20 (NLTK, spaCy, TF-IDF, Word2Vec, BERT, GPT, Hugging Face, prompt engineering, LangChain, Ollama, RAG, vector DBs, agentic AI, fine-tuning); (5) Big Data Engineering, 21-25 (Spark, Airflow, SQL/NoSQL, ETL); (6) MLOps & Deployment, 26-30 (Linux, Docker, MLflow, CI/CD, GitHub Actions, unit tests, FastAPI, monitoring, portfolio preparation).
- Assessment: the last week of every module is an individual project with results presentation; no formal exam mentioned. Certificate "AI Engineer" "gemäß AZAV" after all six modules plus a Teilnahmebescheinigung with competence record per module.
- Start dates: 30.11.2026, 18.01.2027, 22.02.2027; starts roughly every five weeks.

### 2.2 IfaDW – KI-Entwickler [F]
- URL: https://www.ifadw.de/ki-entwickler/
- 25 weeks, 875 UE, 12,600.00 EUR. Five modules of five weeks: Datenanalyse mit Python; Angewandtes ML; Deep Learning; NLP & Generative AI; MLOps & Deployment. Same prerequisites, group size 12, free laptop that becomes the participant's property.
- Caveat: the fetch reported certificate number M-26-26532-2 for this course, the same number as for KI-Anwendungsentwickler. One of the two is probably a mis-read; check the page before quoting the number.
- KURSNET-mirror cross-check: https://www.studysmarter.de/s/weiterbildung/k/ki-entwickler-ifadw-institut-fuer-angewand/ lists price band "über 10.000 €" and start dates 26.10.2026, 30.11.2026, 18.01.2027.

### 2.3 IfaDW – KI-Anwendungsentwickler [F]
- URL: https://www.ifadw.de/ki-anwendungsentwickler/
- 15 weeks, 525 UE, 7,413.00 EUR. Three modules of five weeks: Datenanalyse mit Python; Angewandtes ML; NLP & Generative AI. Certificate M-26-26532-2 (GUTcert), valid to 19.05.2029.
- Structural point: IfaDW sells one 175-UE/5-week module block and stacks 3, 5 or 6 of them into three differently named and priced Maßnahmen.

### 2.4 Turing College – AI Engineering (Bildungsgutschein version) [F]
- URL: https://www.turingcollege.com/ai-engineering-bildungsgutschein
- Language German or English; funded version live online with fixed timetable (self-funded version is self-paced).
- Duration: three months full time; 30 hours per week described as "40 academic hours of 45 minutes each"; certificate records 520 academic hours (UE).
- Price: 0 EUR with approved BGS; self-funded 3,500 EUR upfront or 1,055 EUR x 4.
- Prerequisites: at least 1 year Python or JavaScript; B2 German or English; 30 focused hours per week.
- Target group: developers who want to build, evaluate and deploy LLM applications and agents.
- Modules (hours per module not published): (1) Foundations of LLM application development (OpenAI, Anthropic, Gemini APIs, prompt engineering, ethics); (2) Building applications with LangChain and RAG (ChromaDB, Streamlit or Next.js); (3) AI agents (LangGraph, short/long-term memory, MCP); (4) Capstone.
- Tools: Python, JavaScript, LangChain, LangGraph, Streamlit, Next.js, OpenAI, Gemini, Llama, Claude, Claude Code via a Claude Team Premium seat, ChromaDB, MCP.
- Assessment: four AI applications each with technical feedback; self-designed deployed capstone; Turing College certificate; no exam stated.
- Vendor-blog cross-check: https://www.turingcollege.com/blog/best-ai-bootcamps-germany-2026 and https://www.turingcollege.com/blog/bildungsgutschein-ai-training-germany-2026 (the second says "AZAV-certified, listed in Mein NOW").

### 2.5 Turing College – Building with AI Agents (Bildungsgutschein version) [F]
- URL: https://www.turingcollege.com/building-with-ai-bildungsgutschein
- 3 months, 520 UE, 30 h/week; German or English; live online fixed timetable.
- Price: 0 EUR with BGS; self-paid 2,000 EUR upfront (regular price 3,500 EUR) or 625 EUR x 4 (regular 990 EUR x 4).
- Prerequisites: no coding experience; B2 language. Target group: non-technical professionals (consulting, marketing, product, sales, finance, operations).
- Sprints: (1) Your first web tool, live online; (2) A tool your team can log into; (3) An AI tool that knows your data; (4) A mobile app, payments and automations; (5) Capstone: your own idea, built and launched.
- Tools: Claude Code, Git, GitHub, Next.js, Supabase, Vercel, OpenAI API, OpenRouter, LangChain, MCP, Figma, Expo, Playwright, Google Cloud, Stripe; Claude Team Premium seat included.
- Relevance: this is an AZAV course with Claude Code as its primary tool, but aimed at non-programmers, not at developers.

### 2.6 neue fische / Spiced – Agentic Machine Learning Engineer [F] + [F-PDF]
- URLs: https://www.neuefische.de/bootcamp/agentic-machine-learning-engineering ; https://www.neuefische.de/en/bootcamp/agentic-machine-learning-engineering ; curriculum PDF https://nf-strapi.s3.eu-central-1.amazonaws.com/NFSP_Curriculum_AGENTIC_MACHINE_LEARNING_ENGINEERING_da4335d0c4.pdf
- English; remote live online, ca. 15 participants; full-time 14 weeks, Mon-Fri 09:00-18:30. UE not published. Price not published ("Selbstzahlerrate oder Stipendium" available).
- Funding: "Förderbar durch die Agentur für Arbeit (AZAV- & HZA-zertifiziert)".
- Prerequisites: good Python, databases and SQL, solid statistics/analysis/linear algebra.
- Nine phases (web page): Python Foundations; Classical ML; Deep Learning & Transfer Learning; LLMs & Prompt Engineering; RAG & Knowledge Systems; Agent Architecture & Stateful Workflows; Multi-Agent Systems; Evaluation, Safety & Compliance; Capstone: Build & Deploy. Weeks per phase not published.
- PDF topic list (verbatim headings): Foundations (command line & version control, Python & numerical computing); Data Science Core (project: real dataset analysis); Classical Machine Learning (three projects: classification, regression, advanced method on business data); Deep Learning (project: image classification); NLP & LLMs (transformers, LLM APIs & prompt engineering, RAG, fine-tuning concepts, project: LLM-powered tool); Agentic AI Systems (tool-calling & structured outputs, agent loop & ReAct, agent frameworks, state/routing/checkpointing, streaming & interruption, human-in-the-loop & idempotency, embeddings/vector stores/chunking, RAG as a tool, adaptive RAG, memory architectures, tool protocols & custom tool servers, hooks & subagent patterns, multi-agent patterns); Observability & Production Engineering (observability & tracing, type-safe production agents, integration patterns, cost-latency engineering, eval-driven development & LLM-as-judge); Safety & Governance (safety in production, AI governance & EU AI Act); Capstone Project.
- Extras: Claude Pro subscription during the course "& $270 API credits"; voucher for NVIDIA Certified Associate – Generative AI LLMs (NCA-GENL). Certificate: "Agentic Machine Learning Engineer Zertifikat".
- The PDF's own labour-market page cites: Bitkom 79,000 unfilled IT positions; StepStone September 2026 postings: Data Scientist 370, Machine Learning Engineer 313, AI Engineer 582, Agentic AI Engineer 366; Glassdoor 2,575 ML postings in Germany (September 2026). These are the provider's numbers, not independently checked.

### 2.7 neue fische / Spiced – Agentic AI: Build and Deploy AI Agents [F] + [F-PDF]
- URLs: https://www.spiced-academy.com/en/program/agentic-ai ; PDF https://assets.ctfassets.net/zrf6ycylsmg6/5pwoQJcuHiPymxmcIPeF3B/4793ef0e9ef3c8a6f046b18ebb02c973/NFSP_Curriculum_AGENTIC_AI_8W_.pptx.pdf
- English; full-time remote; 8 weeks / 2 months; Mon-Fri 9:00-18:00 with 45-minute lunch break. Price and UE not published. Next start listed on Spiced homepage: Feb 1, 2027.
- Prerequisites: solid Python, basic Git/GitHub, command line, working understanding of LLMs and APIs, module-specific admissions test. Target group: "software developers and tech professionals".
- Week structure: (1) Foundations of Agentic AI (ReAct loop in pure Python, OpenAI Agents SDK, Modal sandboxes, Langfuse logging); (2) Stateful Workflows & Observability (LangGraph, human-in-the-loop, idempotency, self-hosted Langfuse); (3) Agentic Knowledge: RAG & Memory; (4) Tool Integration & the Modern Agent Stack (custom MCP servers, Claude Agent SDK, Pydantic AI); (5) Multi-Agent Orchestration & Production Discipline (orchestrator-worker, supervisor, swarm; cost/latency; safety; EU AI Act); (6) Capstone: Discovery & Foundation; (7) Capstone: Implementation & Midterm; (8) Capstone: Production & Graduation.
- Split: 5 taught weeks + 3 capstone weeks (PDF: "A three-week capstone project").
- Tools: Python, LangGraph, OpenAI Agents SDK, Claude Agent SDK, Pydantic AI, Langfuse, DeepEval, Llama Guard 4, Modal, LlamaIndex, Anthropic API credits; Claude Pro subscription.
- This is the closest existing German funded offer to track B's agent portion, and it is aimed at people who already program.

### 2.8 neue fische / Spiced – AI Engineering: Data Science and Machine Learning Engineering [F] + [F-PDF]
- URLs: https://www.neuefische.de/en/bootcamp/ai-engineering-data-science-and-machine-learning ; PDF https://nf-strapi.s3.eu-central-1.amazonaws.com/NFSP_Curriculum_AI_ENGINEERING_541161248f.pdf
- English & German; remote; "Full-time: 32 weeks / 8 months". Price and UE not published. AZAV and HZA certified.
- Nine phases: Orientation & Python fundamentals; Data sourcing & management; EDA & advanced Python; Classical ML; Intermediate data project; Advanced DL & computer vision; GenAI, LLMs & sequential data; ML engineering & modern MLOps; Final capstone.
- PDF project structure: "Project 1: Exploratory Data Analysis", "Project 2: Predictive Modeling", "Data Science & AI Capstone Project (4 weeks)"; then "4 mini projects: Refactoring & API, Data Pipeline, Model deployment, MLOPs", "3 medium projects: RAG, Agent, LLM Deployment", "Machine Learning Capstone Project (4 weeks)".
- PDF LLM content: "Building AI Systems" (LLM foundations & embeddings; prompt engineering and context engineering; RAG pipelines & fine tuning; building custom agents & MCP) and "LLMOPs: Deploying AI Systems" (serving LLMs with FastAPI; deploying containerized LLMs; monitoring & observability for LLM services). MLOps tooling named: dbt, Prefect, MLflow, Prometheus, Grafana, Evidently, Docker.
- Certificates: IHK "Fachkraft AI Engineering (IHK)"; neue fische certificates; CompTIA "Cloud Essentials" voucher; Claude Pro subscription.
- KURSNET-mirror: https://www.studysmarter.de/s/weiterbildung/k/ai-engineer-weiterbildung-und-data-science-konzepte-neuefische-gmbh/ lists a neuefische "AI Engineer weiterbildung und Data Science Konzepte" at "über 10.000 €", 3–6 months.

### 2.9 neue fische / Spiced – Software Development with AI [F] + [F-PDF]
- URLs: https://www.spiced-academy.com/en/program/full-stack-web-development ; PDF https://assets.ctfassets.net/zrf6ycylsmg6/3KnmEExZow7bd6rezseGqe/496983a1f4f1c1c1ccb9053c9d59d8a6/NFSP_Curriculum_SOFTWARE_DEVELOPMENT_WITH_AI.pdf
- "Full-time: 16 weeks / 4 months", DE & EN, remote. Beginners. Price not published.
- PDF tech stack, first block "AI & Language Models": "Agentic Coding (Claude Code)", "Agentic developer workflows", "Skills", "MCP's", "Context Management". Then HTML, CSS, JavaScript, TypeScript, React, Backend (Node.js, Express, testing, auth), DevOps (deployment, CI & CD), capstone (project planning, version control, debugging, final demo).
- Web page: an "Agentic Development" phase starts in week 9 (Claude Code, agentic workflows, prompting, context management, task delegation, critical evaluation of AI output). Certificate: "Junior JavaScript Exam" voucher; Claude Code access.
- Target job titles in PDF include "Agentic AI Developer".

### 2.10 neue fische – Advanced Software Development with AI [F] + [F-PDF]
- URLs: https://www.neuefische.de/en/bootcamp/advanced-web-development-bootcamp ; PDF https://nf-strapi.s3.eu-central-1.amazonaws.com/2027_NFSP_Curriculum_ADVANCED_SOFTWARE_DEVELOPMENT_WITH_AI_8dca945491.pdf
- German (good English required); remote; 16 weeks, Mon-Fri 09:00-18:00. AZAV and HZA certified. Price not published.
- Prerequisites: "Experience in software and front-end development, including HTML, CSS, and JavaScript."
- Phases: Welcome, Basics & AI Tooling (1 week); TypeScript; Express, SQL & Clean Architecture; NestJS, Auth & Testing; DevOps, Docker & Cloud Deployment; Next.js, Zustand & Testing; Full-Stack Integration & Real-Time WebSockets; AI Integration & Augmented Coding; Capstone & Career Launch.
- PDF: "In the final five weeks, you put everything into practice in a large-scale capstone project. Over five agile sprints with sprint planning, daily standups, reviews and individual coaching". So 11 taught weeks + 5 capstone weeks.
- "AI-Driven Development" block: working with AI APIs; integrating AI into applications; prompt engineering; AI-powered tools & services; augmented coding with AI tools; AI security & data privacy. Claude Pro subscription "for 5 Months"; W3Schools Academy certificate voucher.
- This is the closest existing funded analogue to a developer-level track, but the AI-coding content is one block, not the spine.

### 2.11 WBS Coding School – AI Software Development [F]
- URLs: https://www.wbscodingschool.com/ai-software-development/ ; WBS Training listing https://www.wbstraining.de/weiterbildung-full-stack-web-und-app-development-english-full-time ; catalogue https://www.wbscodingschool.com/
- English or German; 100% online live; 17 weeks; Mon-Fri 9:00-17:30. Price: 0 EUR with BGS, self-funded 9,900 EUR. AZAV-certified.
- Prerequisites: aimed at beginners and career changers; B2 in language of instruction.
- Modules: Primer 2 weeks (HTML, CSS, Git, GitHub, AI coding assistants from day one); JavaScript 3 weeks; React 2 weeks; TypeScript 2 weeks; Backend & Full-Stack 3 weeks (MongoDB, Node/Express); Generative AI Integration 1 week (LLM integration, prompt engineering, structured output, n8n); Agentic AI & Developer Workflows 1 week (OpenAI SDK, MCP, AI-assisted test generation, documentation, refactoring); Final Project 3 weeks.
- Tools: Claude, Claude Code, Anthropic API, OpenAI API/SDK, Gemini API, GitHub Copilot, n8n, MCP. WBS Training listing [S]: every participant gets Claude with Claude Code for the full 17 weeks plus Anthropic API credits in selected modules.
- Certificate: WBS Coding School certificate; optional PCEP exam paid by school.

### 2.12 WBS Coding School – AI Agents & Automations [F]
- URL: https://www.wbscodingschool.com/ai-agents-automations-course/
- 12 weeks; 0 EUR with BGS, self-funded 7,500 EUR; AZAV-certified; no prior experience.
- Modules: Foundations of AI 2 weeks; Generative AI and LLMs 3 weeks; Automations with n8n and Python 4 weeks; AI Agents & Safety 2 weeks; Final Project 1 week.

### 2.13 WBS Coding School – AI Automation Engineering [F, truncated]
- URL: https://www.wbscodingschool.com/ai-automation-engineering-course/
- 10 months full-time, "40-week curriculum"; price not published.
- Modules seen: (1) Automation, AI and programming foundations 11 weeks (n8n, Python from scratch, APIs, SQL, vector storage); (2) Advanced automation and agent backends 6 weeks (human-in-the-loop, tool calling, agent memory and guardrails, A2A protocol, FastAPI, automated testing); (3) Agentic architecture and knowledge integration 7 weeks (MCP servers/clients, RAG). Modules 4–6 not captured. Four-week final project; one automation system is built and hardened across all modules.
- Tools named: n8n, Python, Claude Code, Pydantic, OpenAI Agents SDK, FastAPI, MCP, Microsoft Foundry on Azure.

### 2.14 alfatraining – AI Engineer [F]
- URL: https://en.alfatraining.de/kurse/weiterbildung-ai-engineer
- German; live via alfaview; 16 weeks; Mon-Fri 8:30-15:35; 6–25 participants. Price not published. AZAV-certified.
- Prerequisites: Python and SQL; target group people with CS/business informatics/maths degree or comparable.
- Four 20-day blocks, each with its own certificate: Data Engineer (project ~5 days), Machine Learning (project ~4 days), Deep Learning (project ~3 days), Reinforcement Learning (project ~3 days). LLM/RAG/agents get about 1 day inside Deep Learning plus about 2 days of LLM/GenAI overview inside Machine Learning.
- Exam form: "Praxisbezogene Projektarbeiten mit Abschlusspräsentationen".

### 2.15 alfatraining – Agentische Softwareentwicklung mit Claude Code [F]
- URL: https://en.alfatraining.de/kurse/weiterbildung-claude-code
- German; live via alfaview; 2 weeks; AZAV-certified; price not published.
- Prerequisites: knowledge of agent-based AI systems, at least one programming language, Git. Target group: IT apprentices, IT specialists, programmers.
- Content: Claude Code Basics (approx. 1 day); working with code bases – CLAUDE.md, multi-file refactoring, planning mode, slash commands (approx. 2 days); Tools, Skills and MCP integration – MCP servers, custom skills, sub-agents, hooks (approx. 2 days); Automation of development and business processes – CI/CD integration, automated reviews/tests, scheduled tasks (approx. 2 days); Security, governance and team operations – permission models, sandboxing, logging/auditing, review processes, cost management (approx. 2 days); project work (approx. 1 day).
- Exam: "Praxisbezogene Projektarbeit mit Abschlusspräsentation". Start dates: 16.11.2026, 23.11.2026, 14.12.2026, 21.12.2026, 18.01.2027.
- The alfatraining site also lists (search snippet only, not fetched) "Python and artificial intelligence (AI) for software developers" https://en.alfatraining.de/kurse/weiterbildung-python-kuenstliche-intelligenz-ki-softwareentwickler and "AI Agents and Process Automation" https://en.alfatraining.de/kurse/weiterbildung-ki-agenten-prozessautomatisierung [S].

### 2.16 Viona (IBB Institut für Berufliche Bildung) – Softwareentwicklung mit KI-Tools [F-PDF]
- URL: https://pdf.viona.online/kursflyer/E-4683.pdf (course number VZ-E-4683-1)
- 4 weeks (20 days) full-time; virtual live teaching in small groups; attendance at a partner site or at home with funder's consent. Price shown "€ 0,00". Certificate: "Trägerinternes Zertifikat bzw. Teilnahmebescheinigung".
- Content list: Grundlagen zu KI; Erstellen guter Anfragen; Assistenten für Code und Arbeitsschritte; Fehlersuche; Erstellen und Pflegen verständlicher Beschreibungen; Planen von Datenstrukturen und Abfragen mit KI; Automatisieren von Aufgaben; Nutzung von Schnittstellen; Einsatz fortgeschrittener Werkzeuge; Risiken erkennen, verantwortlich handeln, Qualität sichern. Summary text adds debugging, refactoring, testing, documentation, local LLMs, APIs, RAG/Text-to-SQL, with examples in HTML/CSS, JavaScript, Python, Java, C# or C++.
- Prerequisites: "sicherer Umgang mit mindestens einer Programmiersprache"; German B2; good English. Target group: frontend/backend/full-stack developers, QA, DevOps, sysadmins, data/ML engineers.
- No tool brand is named in the flyer.

### 2.17 Digitale Leute School – AI Software Engineering Bootcamp [F]
- URLs: https://school.digitale-leute.de/weiterbildung/ai-software-engineering ; overview https://school.digitale-leute.de/
- English (course), remote; full-time, part-time or video course; "In drei Monaten"; overview page says 12 Wochen, start 28.10.2026. Price and UE not published. AZAV-certified; "BGS möglich" for full-time.
- Prerequisites: ideally some practical software development experience; Python not required.
- Modules by number of sessions: Product Skills für Engineers (5); AI Software Engineering Foundations (4); Software Engineering with AI (8: modern AI stack, prompt engineering, rapid prototyping, MVP, deployment & monitoring, code quality/refactoring); Agentic AI Engineering (5: directing agentic AI, workflow automation, context engineering & multi-agent orchestration, LLMs/MCP/LangChain/vector integrations, building an AI product); Career Coaching (2). 24 sessions in total (my arithmetic).
- Tools named: Claude Code, Cursor, GitHub Copilot, Windsurf, Lovable, Replit, MCP, LangChain, Pinecone, Weaviate, n8n, Docker, Grafana.
- KURSNET-mirror siblings from the same provider (price band "5.000–10.000 €", duration band "1–3 Monate" full-time): "Künstliche Intelligenz in der Softwareentwicklung" https://www.studysmarter.de/s/weiterbildung/k/kuenstliche-intelligenz-in-der-softwareentwicklung-digitale-leute-school/ (tools: Cursor, GitHub Copilot, ChatGPT, Claude, LangChain, Python, Docker); "Vom Programmierer zum AI Engineer" https://www.studysmarter.de/s/weiterbildung/k/vom-programmierer-zum-ai-engineer-digitale-leute-school/ (LangChain, LangGraph, MCP, Cursor, Pinecone, FastAPI; full-time 28.10.2026–19.01.2027, part-time to 13.04.2027); "Softwareprogrammierung für Vibe Coder" https://www.studysmarter.de/s/weiterbildung/k/softwareprogrammierung-fuer-vibe-coder-digitale-leute-school/ (KURSNET-Datensatz-ID 99102685).

### 2.18 Digitale Leute School – Vibe Coding Bootcamp [F]
- URL: https://school.digitale-leute.de/weiterbildung/vibe-coding
- German; 3 months; AZAV-certified; no programming skills required; target founders, PMs, designers.
- Modules: Creative Foundations (4 sessions); Technical Foundations (4); Prompt Engineering (5); System Flow & Automation (4); Agentic AI Engineering (5); Career Coaching (2). Tools: Claude Code, Lovable, Replit, n8n.

### 2.19 Ironhack – Remote AI Engineering Bootcamp [F]
- URL: https://www.ironhack.com/de-en/artificial-intelligence/remote
- English; live online; full-time 9 weeks (Mon-Fri 09:00-18:00) or part-time 24 weeks. Total hours not published. Price 8,500 EUR. "AZAV-certified under SGB III"; BGS "up to 100% funded, subject to approval".
- No prior experience; 40 hours prework; aptitude test.
- Modules: Prework (40 hours); Python and AI Engineering Essentials; Machine Learning, Deep Learning and Model Fine-Tuning; Generative AI, LLMs and Agents (LLM APIs, agents and RAG with LangChain). Weeks per module not published.
- Separate one-year product: https://lp.ironhack.com/de-en/ai-software-engineering-program [F] – "One-Year AI Software Engineering Program", English, Berlin or remote, "Covered 100% by the Agentur für Arbeit", five modules (MERN full-stack; AI and ML; software testing and QA; project management; Java and SQL), "5 real-life projects". A 2024 Ironhack blog gives 226 working days / 1,582 instructional hours [S, https://www.ironhack.com/us/blog/learn-ai-software-engineering-in-1-year-with-ironhack-germany].

### 2.20 Le Wagon Berlin – AI Software Development bootcamp [F]
- URL: https://www.lewagon.com/berlin/web-development-course
- In person or online; full-time Mon-Fri 9am-6pm; "9 Intensive Weeks"; 400h course time plus 40h preparation work. Price not published. Page says certified and government-recognised; BGS funding "is possible".
- Module hours as reported by the fetch: prep 40h; Foundation & Programming Fundamentals (Ruby, terminal, Git, MVC) 96h; Store and extract data (SQL) 24h; Design dynamic websites 80h; Build complete web applications (Rails) 40h; Code with AI building blocks (LLMs, OpenAI, WebSockets) 40h; Code faster with AI assistance 8h; Build your own AI web app (final project) 80h. Caveat: the fetch flagged that mapping 40h to the AI building-blocks module was its own inference, and that listed hours total 408h including prep versus the stated 400h.
- Tools: Ruby, Rails, JavaScript, SQL, OpenAI, Claude Code, Heroku, Figma. Final project in teams of 3 or 4.

### 2.21 Masterschool / MSIT (Master School Institute of Technology) [F]
- URLs: https://learn.joinmsit.de/ai-engineering-germany-bg-3 (redirect from learn.masterschool.com); https://learn.joinmsit.de/genai-engineering-germany-bg-en ; https://learn.joinmsit.de/ai-systems-germany-bg-en
- English instruction ("The IHK exam is in German"); online; AZAV-certified; "100% funded"; no prior knowledge required. Duration, UE and price not published on any of the three pages.
- GenAI Engineering topics: integration of AI models in Python; AI-supported project; fundamentals of AI and LLMs; prompting techniques; API integration of ChatGPT and Gemini; exam preparation. Certificate "Generative AI Expert (IHK)" via IHK Akademie München und Oberbayern; PCEP/PCAP.
- Syllabus PDFs exist but exceeded the fetch size limit: https://joinmsit.de/wp-content/uploads/2026/04/GenAI-Engineer-ENG-v0.pdf and https://joinmsit.de/wp-content/uploads/2026/07/AI-Backend-Engineer-ENG-v1.pdf (not read).
- [S] genaumeinkurs.de lists Masterschool courses "LLM Engineering" (9.900 € per snippet) and "KI für Softwareentwickler"; pages returned 403 so not verified.

### 2.22 SkillSprinters – Digitalisierungsmanager für Prozessautomatisierung und KI [F, vendor blog]
- URL: https://skill-sprinters.de/blog/foerderung/ki-weiterbildung-bildungsgutschein-anbieter-vergleich/ (page states it is "nicht neutral"; figures as of 20.10.2026)
- 720 UE; full-time about 4 months (80 Unterrichtstage), part-time 144 days "rund 29 Wochen"; live via Zoom Mon-Fri 8-16; 10.548,00 Euro; "nach AZAV zugelassen (DEKRA)"; 13 modules; at least 80 percent attendance for the certificate; TÜV Rheinland PersCert exam.
- Not a developer course, but it is a published data point of a >10,000 EUR, ~16-week, 720-UE Maßnahme. 80 days x 9 UE/day = 720 (my arithmetic).
- Same page gives: fbs future education "KI-Manager" 410 UE in 17 weeks; alfatraining "KI-Experte" 12 weeks; WBS "KI-Manager:in (DEKRA)" 41 days.

### 2.23 COMCAVE – KI-Engineering: KI-Agenten und Workflow-Automatisierung [F-PDF]
- URL: https://media.comcave.de/broschuere/Kursinformation_KI_Engineering_KI-Agenten_Workflow-Automatisierung.pdf
- "ca. 4 Wochen"; full-time Mon-Fri 8:00-16:45 or part-time 8:30-12:35; 6–25 participants; "Die Maßnahme ist nach AZAV durch die Cert-IT als fachkundige Stelle zugelassen"; Abschlussart "Trägerzertifikat"; start dates 13.11.2026, 15.12.2026, 25.01.2027.
- Content: prompting for Microsoft Copilot, ChatGPT and Claude; Power Automate, Zapier, Make; cloud flows; own AI-supported workflow as project. Admission requires an internal selection interview rated "gut geeignet". Not a coding course despite "Engineering" in the title.

### 2.24 WBS Training – AI Engineer – Effizient arbeiten mit Power KI-Tools [F-PDF]
- URL: https://www.wbstraining.de/kurse/weiterbildung/ai-engineer-effizient-arbeiten-mit-power-ki-tools.pdf (PDF "Erstellt am 12.11.2026")
- 71 days full-time; WBS-Zertifikat; dates 25.01.2027–07.05.2027 etc. Seven 10-day modules: Die Programmiersprache Python; Funktionen und Module in Python; KI-Klassifizierung; KI-Methoden; Prompt-Engineering; Automatisiertes Prompting; KI & Datenmanagement. "Spezifische KI-Vorkenntnisse oder Programmierkenntnisse sind nicht erforderlich."
- The flyer has an explicit "Lernziele" section written as "Du entwickelst ...", "Du setzt ... ein" statements, a useful format example for an AZAV-style course sheet.

### 2.25 Other providers checked
- **StackFuel** [F-PDF] https://downloads.stackfuel.com/curricula/StackFuel_Curriculum_KI-Fachmann_KI-Fachfrau.pdf (version 27/10/26): "KI-Fachkraft", 6 modules, office users, CustomGPT final project; platform self-study with coaching; states StackFuel is part of Multiverse since January 2026. KURSNET-mirror https://www.studysmarter.de/s/weiterbildung/k/ki-agenten-koordinator-stackfuel-gmbh/ lists "KI-Agenten Koordinator" (n8n, MCP servers, RAG pipelines, ReAct/Plan-and-Execute/Reflection, multi-agent), price band "über 10.000 €", 3–6 months, start 19.10.2026. No developer-level AI engineering course found.
- **Constructor Academy (ex Propulsion)** [KURSNET-mirror] https://www.studysmarter.de/s/weiterbildung/k/data-science-ai-intense-program-constructor-academy-gmbh/ : "Data Science & AI Intense Program", Munich or online, price band 5.000–10.000 €, classical DS/ML/DL/NLP + company team project. No LLM-engineering Maßnahme found.
- **velpTEC** [KURSNET-mirror] https://www.studysmarter.de/s/weiterbildung/k/data-science-ai-assistant-development-velptec-gmbh/ : "Data Science & AI-Assistant Development", 1–3 months, band 1.000–5.000 €; custom GPTs/Claude assistants, RAG, testing/monitoring of assistants.
- **A-Leecon** [KURSNET-mirror] https://www.studysmarter.de/s/weiterbildung/k/programmieren-mit-kuenstlicher-intelligenz-vibe-coding-mit-agents-a-leecon-gmbh/ : "Programmieren mit Künstlicher Intelligenz – Vibe Coding mit Agents", up to 1 month full-time, band 1.000–5.000 €; VS Code, Cursor, Replit, ChatGPT, Claude; beginner web development.
- **Developer Akademie** [KURSNET-mirror] https://www.studysmarter.de/s/weiterbildung/k/ki-beim-programmieren-developer-akademie-gmbh/ : "KI beim Programmieren", part-time 3–6 months, band 1.000–5.000 €; ChatGPT, prompt engineering, AI-supported project, Scrum.
- **StartSteps** [F] https://www.startsteps.org/ : AZAV-certified organisation; "AI Automation Specialist" only; no AI engineering or AI coding course.
- **ReDI School** [F] https://www.redi-school.org/ : free evening courses; no Bildungsgutschein/AZAV mention; no AI-engineering course listed.
- **cimdata** [F] https://www.cimdata.de/weiterbildung/ : course list loads dynamically; only category pages visible (https://cimdata.de/lernen-mit-ki); no data.
- **GFN** [S]: KI-Grundlagen, Azure AI-900, KI Data Analyst (4 weeks); nothing developer/agent-focused in snippets.
- **DCI** [S]: "Business Automatisierung mit KI", 12 months, 30.243 € (genaumeinkurs snippet; page 403). Site itself 403.
- **Techstarter, Coders.Bay**: sites unreachable; nothing relevant in search.
- **Data Science Institute (Fabian Rappert), Hamburg Coding School**: no relevant result in search; not found.
- **IU Akademie** [S]: "AI Engineering" Weiterbildung 2.495 € (fernstudi.net snippet).

### 2.26 Direct answer: is there a German AZAV course whose main subject is coding agents?
Yes, but only short or beginner-level ones. I found no programme of 400+ UE for experienced developers.
- Main subject is a coding agent, for developers: alfatraining "Agentische Softwareentwicklung mit Claude Code", 2 weeks [F]; Viona/IBB "Softwareentwicklung mit KI-Tools", 4 weeks [F-PDF].
- Main subject is AI-assisted building, for non-programmers: Turing College "Building with AI Agents", 520 UE [F]; Digitale Leute "Vibe Coding Bootcamp", 3 months [F]; A-Leecon "Vibe Coding mit Agents", up to 1 month [KURSNET-mirror].
- Mixed product/engineering, some dev experience: Digitale Leute "AI Software Engineering Bootcamp", 3 months, 24 sessions [F].
- Coding agents as one block inside a web-dev bootcamp: neue fische/Spiced Software Development with AI (Claude Code from week 9), neue fische Advanced Software Development with AI, WBS Coding School AI Software Development (1 week), Le Wagon (8h).
- Outside AZAV [S]: Haufe Akademie 2-day "Vibecoding – KI-gestützte Softwareentwicklung in der Praxis" (Copilot, Cursor, Lovable, MCP); Fast Lane "Master Class: Agentic Software Engineering using Claude Code (ASECC)".

---

## 3. What an AZAV Maßnahme curriculum/concept must contain

### 3.1 AZAV text [F]
- URLs: https://www.gesetze-im-internet.de/azav/BJNR050400012.html and https://www.gesetze-im-internet.de/azav/__3.html
- § 3 Abs. 1: a Maßnahme lets successful participation be expected when (1) "Ziele, Dauer und Inhalte der Maßnahme jeweils auf die Voraussetzungen der Zielgruppe" and the Maßnahmeziel are matched, and (2) "sie aktuelle Entwicklungen des Ausbildungs- und Arbeitsmarktes berücksichtigt."
- § 3 Abs. 2: BA publishes average cost rates every two years. § 3 Abs. 3: cost check looks at concept and calculation; for group measures "eine Gruppengröße von zwölf Teilnehmenden zu Grunde zu legen". § 3 Abs. 4: special expenses (above-average staffing, special rooms/technology/content, accessibility, justified smaller group) can be recognised. § 3 Abs. 6: BA consent to above-average costs depends on special labour-market interest plus proof of necessary above-average expenses. § 3 Abs. 8: individual Maßnahmebausteine can be approved.
- § 2 Abs. 5: contracts must provide a "Teilnahmebescheinigung mit Angaben zum Inhalt, zeitlichen Umfang und Ziel der Maßnahme".
- § 2 Abs. 4 (Träger QM system): documented methods for supporting individual learning processes and for evaluating measures.
- The AZAV text itself does not spell out Lernerfolgskontrolle, UE per module or certificate format; those come from the Beirat recommendations and the certifiers' checklists below.

### 3.2 Empfehlungen des Beirats nach § 182 SGB III, Stand 10.09.2024 [F-PDF]
- URL fetched: https://certqua.de/pdf/ueber-uns/downloads/offener-bereich/_Empfehlungen des Beirats_20240910.pdf (copy hosted by certifier Certqua; I did not locate the same version on arbeitsagentur.de. An older edition is at https://www.arbeitsagentur.de/datei/dok_ba025935.pdf [S, not read]. Check whether a newer edition than 10.09.2024 exists.)
- Recommendation "Zulassung von Maßnahmen der beruflichen Weiterbildung nach §§ 179, 180 SGB III i.V.m. §§ 3, 4 AZAV" (page 33). The Träger must submit documentation including:
  - "Maßnahmekonzeption mit konkreter Definition des Maßnahmeziels, der Zielgruppe der Maßnahme, der Maßnahmeinhalte sowie der Materialien ihrer Vermittlung"
  - "Methodisch-didaktisches Konzept zur Umsetzung der Maßnahmekonzeption, Organisation des Lehrbetriebs (fachbereichsbezogene Qualifikation der Dozenten ..., Vertretungsregelungen, konzeptionelle und technische Unterstützung der Dozenten/des Personals, Teilnahmekontrolle)"
  - "Konzept zur Maßnahmeerfolgskontrolle"
  - targeted Maßnahmeerfolg, or results of previous runs with the same or similar concept
  - check that a prospective participant belongs to the target group and can reach the Maßnahmeziel
  - assessment of the measure's usefulness given the state and development of the labour market
  - rooms, staff and technical equipment; occupational safety; data protection
  - calculation principles; cost assessment against B-DKS
  - duration: "Maßnahmeteile, die nicht zwingend für das Erreichen des Bildungsziels erforderlich sind, dürfen nicht zu einer Verlängerung der Maßnahme führen."
  - for § 3 Abs. 1 Nr. 2 AZAV: information sources and contacts for labour-market knowledge, concrete contacts with companies where needed, and how those findings are implemented in the measure.
- Cost rule (page 33): exceeding the B-DKS can be justifiable if necessary and special; "Übersteigen die Maßnahmekosten die durchschnittlichen Kostensätze um mehr als 25 Prozent, kann die Maßnahme ... nicht zugelassen werden, es sei denn, die innerhalb der Bundesagentur zuständige Stelle stimmt den erhöhten Maßnahmekosten zu." Classification of the measure to KldB 2010 must be correct.
- Group size (page 21): twelve participants is the calculation norm; the group size is part of the approval and is noted on the certificate.
- Delivery forms (page 26): "Digitale (virtuelle) Maßnahme" means exclusively digital, with teacher and participants connected in a virtual room, teaching carried out by the teacher "während der gesamten Dauer", "synchroner Informationsaustausch", group and project work possible. Fernunterricht under FernUSG is separate and needs ZFU approval.
- Maßnahmebausteine (page 34): each Baustein must be individually usable on the labour market, have its own KldB position and cost rate, and meet all requirements on its own.
- Model Maßnahme certificate fields (Anlage 3, FbW): Maßnahmetitel; KldB 2010 classification; Maßnahme vs Baustein; Präsenz / digital / kombiniert; Abschluss ("zu erreichender Abschluss und prüfende Stelle"); Teilnehmerzahl; Unterrichtsstunden; Stunden für betriebliche Lernphase; Gesamtkosten per participant; Unterrichtskostensatz per participant per Unterrichtsstunde; Kostenzustimmung; Standorte; Zulassungszeitraum; certificate number.

### 3.3 Certifier guidance: TÜV NORD CERT form A601F113 "Dokumentation der Maßnahmezulassung", Rev. 08/03.26 [F-PDF]
- URL: https://www.tuev-nord.de/fileadmin/Sites/TUEV_NORD/Dienstleistungen/Certification/Files/PDFs_Managementsystems/AZAV/20260402_A601F113_Dokumentation_zur_Ma%C3%9Fnahmezulassung.pdf (download area: https://www.tuev-nord.de/de/dienstleistungen/auditierung-und-zertifizierung/azav/downloadbereich-azav/ [S])
- The auditor checks that the "Maßnahmekonzept liegt mit mind. folgenden Inhalte vor":
  1. "Maßnahmeziel ist konkret definiert"
  2. "Zielgruppe mit Zugangsvoraussetzungen ist beschrieben und auch wie die Zugangsvoraussetzungen überprüft und die Ergebnisse dokumentiert werden"
  3. how participants are advised before the start
  4. full-time or part-time
  5. presence, digital or hybrid delivery; for hybrid and digital, description of the technical implementation
  6. "Methodisch-didaktisches Konzept" covering theory teaching and teaching of practical skills, plus organisation of teaching (lecturer qualification, substitution rules, support for lecturers, attendance control)
  7. "Inhalten/Lehrplan/Curriculum – UE-Umfang pro Woche / Dauer gesamt in Wochen → Erläuterung warum die Dauer so gewählt wurde – Themen/Inhalte aufgegliedert"
  8. forms of documenting delivered content (e.g. Klassenbuch)
  9. "Beschreibung, ob und wie Lernerfolgskontrollen stattfinden"
  10. how participants are supported in the individual learning process
  11. Fehlzeitenkonzept
  12. betriebliche Lernphasen/Praktika (placement, duration, supervision)
  13. "Beschreibung der arbeitsmarktlichen Notwendigkeit der Maßnahme (Arbeitsmarkt/Vernetzung/Vermittlungsaktivitäten)"
- Also checked: Teilnahmebescheinigung/Zertifikat (content, time volume, goal); participant contract (free withdrawal until start, free termination on taking a job, costs shown but no cost to participant, right to a Teilnahmebescheinigung even if the goal is not reached); staff list; rooms; "Quantitative Angaben in der Kalkulation stimmen mit den quantitativen Angaben im Konzept/Lehrplan überein"; evidence for cost positions 1–7.
- Stammdaten include whether the calculated rate "Teilnehmer je UE" is at or below B-DKS: "nein → Achtung: bei >25% Zustimmung der BA notwendig".
- Other certifier pages found but not read [S]: GUTcert AA157 https://www.gut-cert.de/files/content/download/qms/AA157_Massnahmenzulassung.pdf ; DQS https://www.dqsglobal.com/de/uber-uns/azav-dokumente ; Kiwa info sheet; BA-Prüfdienst criteria at GUTcert https://www.gut-cert.de/files/content/download/AZAV/Kriterien%20BA-Prüfdienst.pdf (scanned image, unreadable without OCR; snippet says the Lehrplan should show hours and sequence in detail and that regular Lernerfolgskontrollen with test evidence are expected).

### 3.4 Bundes-Durchschnittskostensätze (B-DKS) FbW 2026 [F-PDF]
- URL: https://www.gut-cert.de/files/content/download/AZAV/b-dks_fbw_2026.pdf (BA document "Stand: 01. Juli 2026", hosted by GUTcert; valid from 1 July 2026; basis: approved measures 01.01.2024–31.12.2025)
- Relevant rows (EUR per participant per Unterrichtsstunde): 43412 Softwareentwicklung – Fachkraft 11,82; 43413 Softwareentwicklung – Spezialist 13,24; 43414 Softwareentwicklung – Experte 15,46; 43423 Programmierung – Spezialist 13,25; 43102 Informatik (o. S.) – Fachkraft 11,82; 43103 – Spezialist 13,00; 43104 – Experte 15,35.
- Implication for the target of 640 UE above 10,000 EUR (**my arithmetic**): 640 x 15.46 = 9,894.40 EUR at the Experte rate; 640 x 13.24 = 8,473.60 EUR at the Spezialist rate. Reaching 10,000 EUR at exactly 15.46 needs 647 UE. 10,000 / 640 = 15.63 EUR/UE, i.e. about 1% above the Experte B-DKS and 18% above the Spezialist B-DKS; both are inside the 25% band, but any excess over B-DKS needs justification to the fachkundige Stelle. The 25% ceiling without BA Kostenzustimmung is 19.33 EUR/UE x 640 = 12,368 EUR (Experte) or 16.55 x 640 = 10,592 EUR (Spezialist). The KldB level assigned to the Maßnahme therefore decides whether >10,000 EUR at 640 UE is routine or needs a justification.

### 3.5 Checklist for the two syllabi (derived from 3.1–3.3)
Maßnahmetitel; KldB 2010 position; Maßnahmeziel; Zielgruppe; Zugangsvoraussetzungen and how they are tested and documented (entry test/interview); pre-start counselling; full-time/part-time; delivery form and platform; total UE, UE per week, weeks, and a reason for the duration; module list with UE and topics per module; Lernziele per module; methodisch-didaktisches Konzept (theory vs practice); Lernerfolgskontrollen per module and overall; individual learning support; Fehlzeitenkonzept; documentation (Klassenbuch); certificate/Teilnahmebescheinigung content; labour-market necessity with evidence; trainer qualifications; group size (12 as calculation basis); cost calculation consistent with UE in the Lehrplan.

---

## 4. Labour-market data 2025–2026 (demand for AI skills among developers)

- **Bitkom, "IT-Fachkräftemangel in den letzten drei Jahren halbiert", press release 3 September 2026** [F] https://www.bitkom.org/Presse/Presseinformation/IT-Fachkraeftemangel-in-den-letzten-drei-Jahren-halbiert (study PDF, not read: https://www.bitkom.org/sites/main/files/2026-09/bitkom-studienbericht-arbeitsmarkt-it-fachkraefte-2026.pdf [S]). Two representative Bitkom Research surveys of 853 and 602 companies with 3+ employees, telephone, calendar weeks 18–25 of 2026.
  - Unfilled IT positions: 149,000 (2023), 109,000 (2025), 79,000 (2026).
  - 78% see an IT skills shortage; 76% expect it to worsen; 97% of companies with IT vacancies have trouble filling them; 33% say applicants lack knowledge of the latest technologies; 43% cite insufficient qualification.
  - 42% of companies with IT positions already use AI in IT work; 36% plan to.
  - 63% expect AI knowledge and tools to be needed in all IT jobs; 74% expect strategic control of AI to gain importance; 61% expect more pressure for continuous training; 55% expect entry-level tasks to decline; 38% expect AI to largely replace some IT roles.
  - 49% expect AI to increase demand for IT staff with AI knowledge; 48% expect no additional demand; 12% of companies with vacancies seek AI specialists; 17% seek software development and architecture (second after IT administration at 26%).
  - AI already used for software testing and error analysis by 9%, considered by 16%.
  - Among AI-using companies 10% have cut some IT jobs; 32% expect AI-driven cuts.
  - Read for the Maßnahme rationale: the shortage is shrinking, so the labour-market argument has to rest on the skills shift (63% / 33% figures), not on raw vacancy counts.
- **Bitkom, "Softwarewelt 2036", 22 June 2026** [F] https://www.bitkom.org/presse/presseinformation/ki-bringt-geschaeftsmodelle-softwarebranche-wanken (report PDF, not read: https://www.bitkom.org/sites/main/files/2026-06/22062026-bitkom-studienbericht-software-2036.pdf [S]). Qualitative interviews, explicitly not representative; press page has no figures on AI in development.
- **BearingPoint study reported by ingenieur.de, 15 September 2026** [F, secondary] https://www.ingenieur.de/karriere/arbeitsleben/ki-veraendert-kompetenzprofile-ersetzt-entwickler-aber-nicht/ : 112 executives in DACH. 91% already use AI in software development; 18% have it firmly integrated; 73% use it selectively; uses: documentation 77%, code generation 76%, QA and code reviews 74%; 81% report higher development speed; challenges: security and compliance 70%, choosing tools 61%, process integration 58%; 59% want to expand AI expertise; 27% plan more junior and 27% more senior developers. Original BearingPoint report not fetched.
- **index Anzeigendaten, reported by e-fellows.net, 8 May 2026** [F, secondary] https://www.e-fellows.net/skills/die-ki-skills-suchen-arbeitgeber : Q1 2026 job ads in Germany. Machine Learning "rund 12.000 Nennungen"; Bayern "über 9.000" ads with AI skills; Berlin +"42 Prozent" versus Q4 2025; IT is the top sector. AI development tools named in ads: Cursor, Claude Code, GitHub Copilot (no counts). Totals per quarter not published, so no shares.
- **Stifterverband** [S only]: 2026 study "Welche Future Skills fehlen in deutschen Unternehmen?" presented 22 September 2026 with Haufe Akademie, 1,001 managers (reported by https://skill-sprinters.de/blog/news/stifterverband-future-skills-studie-ki-kompetenzluecke-2026/ ; not fetched, no figures confirmed). Earlier Stifterverband/McKinsey study of January 2025: 79 percent of managers said employees lack basic AI competencies (https://www.stifterverband.org/sites/default/files/2025-01/ki-kompetenzen_in_deutschen_unternehmen.pdf , not fetched).
- **Bitkom AI usage** [S only]: release of 14 September 2026 reportedly says 57 percent of companies use AI and 66 percent rate employees' AI competencies as low (https://www.bitkom.org/Presse/Presseinformation/Erstmals-nutzt-Mehrheit-Unternehmen-KI , not fetched). Note the neue fische PDF quotes a different Bitkom figure (41% in 2026); I did not resolve the discrepancy.
- **IAB / BA**: no 2025–2026 IAB publication on AI-skill demand for software developers found; only the IAB-Vorhabenplanung 2026 (https://doku.iab.de/grauepap/2026/IAB-Vorhabenplanung_2026.pdf [S]) announcing research. Providers cite the BA Entgeltatlas for salary bands (e.g. https://web.arbeitsagentur.de/entgeltatlas/beruf/15260 in the neue fische PDF), not fetched.
- **PwC** [S only]: share of AI-related job ads in Germany reached 1.3% in 2025 (t3n snippet); not fetched.
- Provider-quoted posting counts (unverified, from the neue fische PDFs in 2.6/2.8/2.10): StepStone Sept 2026 AI Engineer 582, Agentic AI Engineer 366; Glassdoor Oct 2026 Software Engineer 6,408 and Software Developer 2,105 postings in Germany; Glassdoor July 2026 4,317 AI engineering listings.

---

## 5. Patterns

### 5.1 Typical module sequence
- **"AI Engineer" in Germany mostly means data science/ML plus an LLM block.** IfaDW, alfatraining, neue fische AI Engineering and Ironhack all run Python/data analysis -> classical ML -> deep learning -> NLP/GenAI -> MLOps. LLM application work is 1 of 4–6 blocks (IfaDW: one 5-week module of six; alfatraining: about 3 days of 80).
- **LLM-application-first sequence** (Turing AI Engineering, neue fische Agentic AI 8-week): LLM APIs and prompting -> RAG -> agents (tool calling, state, memory, MCP) -> multi-agent -> evals/observability/safety -> capstone. Only these two assume the learner already codes.
- **Web-dev bootcamps with AI bolted on** (WBS, Le Wagon, neue fische Software Development with AI): HTML/CSS/JS -> React/TypeScript -> backend -> 1–2 weeks GenAI integration and coding agents -> project.
- **Coding-agent courses** (alfatraining Claude Code): tool basics -> context management and large codebases -> tools/skills/MCP/sub-agents/hooks -> CI/CD and process automation -> security/governance/team rollout -> project.

### 5.2 Typical UE and time split
- Full-time day is 8–9 UE: IfaDW 1,050 UE / 30 weeks = 35 UE/week; SkillSprinters 720 UE / 80 days = 9 UE/day; Turing "40 academic hours" per week, 520 UE over 3 months; fbs 410 UE in 17 weeks (my arithmetic on stated figures).
- 16 weeks x 40 UE = 640 UE is consistent with what Turing (40/week) reports; IfaDW-style 35/week would give 560 UE in 16 weeks (my arithmetic).
- Modules come in fixed blocks so they can be approved and combined as Bausteine: IfaDW 5 weeks/175 UE; alfatraining 4 weeks/20 days; WBS Training 10 days.
- Most bootcamp brands publish weeks only and no UE; IfaDW, Turing and SkillSprinters are the exceptions.
- Published prices above 10,000 EUR: IfaDW 12,600 and 14,658; SkillSprinters 10,548. Comparable-length bootcamps publish 8,500 (Ironhack, 9 weeks), 9,900 (WBS, 17 weeks), 7,500 (WBS, 12 weeks). Turing's 520-UE courses list a self-pay price of 3,500 EUR; its Maßnahme price for the voucher is not published.

### 5.3 How projects are handled
- **Project in the last week of every module** with presentation, used as the Lernerfolgskontrolle (IfaDW; alfatraining ~3–5 days of each 20-day block). No formal exam.
- **Capstone at the end**: 1 week of 12 (WBS agents), 3 of 17 (WBS AI Software Dev), 3 of 8 (neue fische Agentic AI), 4 of 32 twice (neue fische AI Engineering), 5 of 16 run as five agile sprints (neue fische Advanced), 80h of 400h in teams of 3–4 (Le Wagon).
- **Graduated projects**: neue fische AI Engineering uses 4 mini + 3 medium + capstone; Turing uses four reviewed applications; WBS AI Automation Engineering extends one system through every module.
- External certificate vouchers are common add-ons: NVIDIA NCA-GENL, PCEP/PCAP, IHK certificate (neue fische, Masterschool), CompTIA, TÜV Rheinland PersCert, W3Schools.
- Tool subscriptions are now a selling point: Claude Pro / Claude Code / Claude Team seats and API credits at neue fische, WBS Coding School and Turing.

### 5.4 What none of them cover (gaps relevant to tracks A and B)
Based on the published curricula above; absence from a marketing page does not prove absence from the classroom.
- **No long-form (400+ UE) programme on agentic software engineering for experienced developers.** The developer-level offers are 2 weeks (alfatraining) and 4 weeks (Viona); the long ones are for beginners or non-programmers.
- **Multi-tool coverage is missing.** Claude Code dominates; Cursor and Copilot appear only at Digitale Leute and WBS; no curriculum names Codex or compares agents.
- **Working in existing/legacy codebases, code review of agent output at scale, test strategy for agent-written code, spec- or plan-driven workflows, parallel agents/worktrees, and measuring productivity or cost** are named only in the 2-week alfatraining course (review processes, cost management) or not at all.
- **Evals are thin in "AI Engineer" tracks.** Only neue fische agentic courses name eval-driven development, LLM-as-judge, DeepEval and Langfuse; IfaDW, alfatraining, Ironhack and Masterschool pages list none. Turing's page says "evaluate" in the target-group text but lists no eval module.
- **Production monitoring of LLM apps** is named only by neue fische (observability/tracing, LLMOps) and Digitale Leute (deployment & monitoring); elsewhere "monitoring" means classical MLOps.
- **Guardrails/security for agents** (prompt injection, sandboxing, permissions) appear only at neue fische (Llama Guard, safety in production) and alfatraining Claude Code.
- **English-language developer-level offers** are limited to Turing AI Engineering (520 UE) and neue fische Agentic AI (8 weeks) / Agentic ML Engineer (14 weeks, half of it classical ML).
- **Almost nobody requires prior programming.** Exceptions: Turing AI Engineering (>= 1 year), neue fische agentic courses, alfatraining, Viona. That makes "for people who already program" a real differentiator, and it means the Zugangsvoraussetzung and its test (required by the TÜV NORD checklist item 2) must be designed explicitly.

### 5.5 Caveats
- Web pages were read via a summarising fetch; exact wording and some numbers (especially IfaDW certificate numbers and Le Wagon module hours) should be re-checked on the page before being quoted in an application.
- Provider pages are marketing; AZAV status of the specific Maßnahme (not just the Träger) was only explicit for IfaDW (certificate numbers), COMCAVE and SkillSprinters.
- Spiced Academy's site lists the same catalogue and uses the same "NFSP" curriculum PDFs as neue fische; I treated them as one provider family (inference from file names and identical course lists).
- KURSNET / mein-now.de was not searched directly.
