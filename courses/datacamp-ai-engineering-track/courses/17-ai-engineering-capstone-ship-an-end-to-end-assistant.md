# 17. AI Engineering Capstone: Ship an End-to-End Assistant

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 6. Capstone. 7 lessons, 2-3 hours.

## Summary

Learners build an accounts payable assistant that checks incoming invoices against purchase orders and supplier agreements. It produces a review record with cited payment terms and reasons for any discrepancies. Learners package the assistant as a FastAPI service and verify its behavior with tests, evaluations and traces.

## Learning objectives

- Define the inputs, decisions and outputs for an invoice review workflow
- Extract invoice fields, retrieve agreement clauses and check discrepancies in a LangGraph workflow
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

PDF extraction with page metadata, typed invoice fields, agreement retrieval, purchase order lookup over MCP, deterministic reconciliation checks, LangGraph approval, `pytest` and evaluation, OpenTelemetry tracing, FastAPI, Docker and a README

### How it's used in the exercises

The learner receives fictional invoice PDFs, supplier agreements and a purchase order CSV. They extract the invoice number, supplier ID, purchase order ID, amount, currency and dates into a typed record. They retrieve the applicable payment terms with agreement and page citations and run deterministic checks for duplicate invoices, missing purchase orders, total or currency mismatches, and inconsistent payment terms.

The assistant returns a JSON review record with the extracted fields, cited evidence, discrepancy reasons and a review status. Incomplete evidence is flagged for review. The workflow can write a draft review ticket to a sandbox after human approval.

### Model / release

Python 3.13; reuse the earlier courses’ dependencies (`minsearch>=0.1.0`, `sentence-transformers>=5.5.0`, `langchain`, `langgraph`, `openai>=2.38.0`, `fastapi`, `pytest`, `pymupdf>=1.26.7`, `mcp`, `opentelemetry-sdk`, `streamlit>=1.58.0`, `pandas>=3.0.3`). Model chosen by the learner and justified by evaluation.

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): Integrator stack 91.7% AI-First, GenAI + Ops 71.0%, Evaluation 69.3% Nov, Automating Manual Workflows 58.8%, Internal Operational Efficiency 57.5%, Agentic Systems 49.9%
- **FG learning paths / portfolio** (`learning-paths/README.md`, `portfolio/`, commit `1556dcb2`): portfolio signals used as the capstone checklist (real user and problem, realistic inputs, clear output, tests, evaluation, logging, reproducible setup, README with decisions and trade-offs); 86.9% of AI-First roles need skills beyond GenAI and 71.0% need production/ops skills (`portfolio/01`); top domains finance 3,877, healthcare 2,380, legal/regulatory 1,798 mentions (`portfolio/02`); finance candidates such as invoice extraction and reconciliation (`portfolio/07`).
- **LZ**: LLM Zoomcamp (`github.com/DataTalksClub/llm-zoomcamp`) Module 7 End-to-End Project (`project.md`)
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 7: End-To-End Project Example; Project guidelines, Evaluation criteria, Documentation tips

### Notes

Bundle 20–50 evaluation cases with clean invoices, duplicates, mismatches, missing evidence, and out-of-scope requests. Keep a held-out subset for final checks. Grade field accuracy, cited evidence, discrepancy classification and approval behavior. Record token usage and latency from sample traces and document the setup and trade-offs in the README.

## Exercise adapted from the Buildcamp

Use My Daily Tasks to show how tools, an agent, tests, tracing, evaluation, and a service fit together. For the assessed build, give learners a fresh invoice and agreement dataset and ask them to extract invoice fields, retrieve matching payment terms, and flag discrepancies for review. Require a runnable container, a trace of a sample run, and a short evaluation report covering field accuracy, citation correctness, and tool choice.

[Buildcamp Week 7 source](https://github.com/alexeygrigorev/ai-bootcamp/blob/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/07-project-bonus/03-complete-example/01-intro-overview.md)

## Lesson outline and source map

FG = AI Engineering Field Guide, LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. `'new'` = no lesson in LZ or BC.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 17.1 | Define the invoice review workflow | LZ `07-project-example/01-intro.md`; `project.md`; FG Use Cases |
| 17.2 | Extract invoice fields and retrieve agreement clauses | LZ `07-project-example/07-chunking.md`, `02-evaluating-retrieval.md` |
| 17.3 | Check purchase orders and gate review ticket creation | BC `v2/07-project-bonus/03-complete-example/03-tools.md`, `04-agent.md` |
| 17.4 | Tests and offline evaluation | LZ `03-evaluating-rag.md`; BC `03-complete-example/06-testing.md`, `07-test-judges.md`, `09-evals-otel.md` |
| 17.5 | FastAPI service and UI | LZ `04-interface.md`; BC `03-complete-example/05-creating-app.md` |
| 17.6 | OpenTelemetry traces and Langfuse | LZ `05-monitoring.md`; BC `03-complete-example/08-logfire.md` |
| 17.7 | Docker deployment and documentation | BC `03-complete-example/10-deployment.md`; `v2/07-project-bonus/02-project-work/04-documentation-tips.md`; LZ `06-summary.md` |

## Detailed lesson outline

### 17.1 Define the invoice review workflow

Inspect sample invoices, supplier agreements, and the purchase-order CSV. Define a typed review record and decide when evidence is insufficient.

**Check.** Classify a clean invoice, a mismatch, and a missing-evidence case.

### 17.2 Extract invoice fields and retrieve agreement clauses

Extract typed invoice fields and retrieve the payment terms from the matching agreement.

**Check.** Check field accuracy and the cited agreement section against a held-out fixture.

### 17.3 Check purchase orders and gate review ticket creation

Compare invoice values with purchase-order records and require approval before drafting a review ticket.

**Check.** Verify the flagged discrepancy, supporting evidence, and behavior when approval is rejected.

### 17.4 Tests and offline evaluation

Write tests for deterministic comparisons and run offline evaluation across clean, missing-evidence, duplicate, and mismatch cases.

**Check.** Report field accuracy, citation correctness, and tool and approval behavior.

### 17.5 FastAPI service and UI

Expose invoice review through FastAPI and add a view of the review record and cited evidence.

**Check.** Submit a fixture and confirm a reviewer can inspect the reasons for each flag.

### 17.6 OpenTelemetry traces and Langfuse

Trace PDF extraction, retrieval, comparison, and the approval gate with OpenTelemetry and inspect a run in Langfuse.

**Check.** Use the trace to explain why a held-out invoice was flagged.

### 17.7 Docker deployment and documentation

Build and run the container, and document setup, checks, and known limitations in the project README.

**Check.** Reproduce a sample review from the documented commands and preserve the resulting record and trace evidence.
