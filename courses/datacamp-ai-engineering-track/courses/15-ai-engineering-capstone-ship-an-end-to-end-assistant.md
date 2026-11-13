# 15. AI Engineering Capstone: Ship an End-to-End Assistant

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 6. Capstone. 7 lessons, 2–3 hours.

## Summary

Learners build one complete enterprise workflow & document-processing assistant from a new dataset—combining the full **integrator stack** (91.7% of AI-First roles), **evaluation** (69.3% in Nov), and **production ops** (71.0% GenAI+Ops). Each lesson adds one layer: ingestion, hybrid retrieval, LangGraph agent with MCP/action tools, guardrails, `pytest` and evaluation table, FastAPI/UI, OpenTelemetry monitoring, and Docker deployment.

## Learning objectives

- Plan an applied AI system from a real-world enterprise workflow/knowledge problem and dataset
- Build the hybrid retrieval pipeline and LangGraph agent and justify the design with evaluation results
- Add guardrails, `pytest`/judge tests, OpenTelemetry monitoring and a FastAPI/Streamlit interface
- Package, deploy and document the application so that someone else can run it

## Why here

Final course: it combines every earlier stage on a new enterprise automation and document-processing problem (the top real-world use cases in the field guide).

## Transformation

From "I know the individual techniques" to "I can own an applied AI system from data ingestion to evaluated production deployment."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Everything from courses 1–14: ingestion and chunking, hybrid retrieval, LangGraph agent with MCP/action tools, guardrails, `pytest` and judge tests, evaluation table, OpenTelemetry logging and dashboard, FastAPI + Docker, README

### How it's used in the exercises

The learner receives an enterprise workflow/document dataset and a problem statement and builds the application layer by layer with decreasing guidance. Each lesson ends with a check (retrieval metric above a threshold, tests passing, evaluation gate met, dashboard showing traffic, container running).

### Model / release

Python 3.13; same packages as courses 2–13 (`minsearch>=0.1.0`, `sentence-transformers>=5.5.0`, `langchain`, `langgraph`, `openai>=2.38.0`, `fastapi`, `pytest` TBC, `streamlit>=1.58.0`, `pandas>=3.0.3`). Model chosen by the learner and justified by evaluation.

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): Integrator stack 91.7% AI-First, GenAI + Ops 71.0%, Evaluation 69.3% Nov, Automating Manual Workflows 58.8%, Internal Operational Efficiency 57.5%, Agentic Systems 49.9%
- **LZ**: LLM Zoomcamp (`github.com/DataTalksClub/llm-zoomcamp`) Module 7 End-to-End Project (`project.md`)
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 7: End-To-End Project Example; Project guidelines, Evaluation criteria, Documentation tips

### Notes

Use a different dataset from the running example of courses 2–11 (focused on enterprise workflow automation and document processing) so the learner cannot copy earlier code. The LLM Zoomcamp project evaluation criteria can be reused as the checklist.

## Lesson outline and source map

FG = AI Engineering Field Guide, LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. `'new'` = no lesson in LZ or BC.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 15.1 | The problem, the dataset and the plan | LZ `07-project-example/01-intro.md`; `project.md`; FG Use Cases |
| 15.2 | Ingestion and hybrid retrieval | LZ `07-project-example/07-chunking.md`, `02-evaluating-retrieval.md` |
| 15.3 | The LangGraph agent, MCP and guardrails | BC `v2/07-project-bonus/03-complete-example/03-tools.md`, `04-agent.md` |
| 15.4 | Tests and offline evaluation | LZ `03-evaluating-rag.md`; BC `03-complete-example/06-testing.md`, `07-test-judges.md`, `09-evals-otel.md` |
| 15.5 | FastAPI service and UI | LZ `04-interface.md`; BC `03-complete-example/05-creating-app.md` |
| 15.6 | OpenTelemetry monitoring and dashboard | LZ `05-monitoring.md`; BC `03-complete-example/08-logfire.md` |
| 15.7 | Docker deployment and documentation | BC `03-complete-example/10-deployment.md`; `v2/07-project-bonus/02-project-work/04-documentation-tips.md`; LZ `06-summary.md` |
