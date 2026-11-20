# 16. AI Engineering Capstone

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 6. Capstone. 7 lessons, 2-3 hours.

## Summary

Learners build an accounts payable assistant that checks incoming invoices against purchase orders and supplier agreements. It produces a review record with cited payment terms and reasons for any discrepancies. Learners package the assistant as a FastAPI service and verify its behavior with tests, evaluations and traces.

## Learning objectives

- Define the inputs, decisions and outputs for an invoice review workflow
- Extract invoice fields, retrieve agreement clauses and check discrepancies in a LangGraph workflow
- Add guardrails, `pytest`/judge tests, OpenTelemetry monitoring and a FastAPI/Streamlit interface
- Package, deploy and document the application so that someone else can run it

## Why here

This is a transfer exercise. Learners apply the extraction, retrieval, testing, and release workflow they practiced with conference support to a new task with financial records and explicit review rules.

## Transformation

From "I know the individual techniques" to "I can own an applied AI system from data ingestion to evaluated production deployment."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

PDF extraction with page metadata, typed invoice fields, agreement retrieval, purchase order lookup over MCP, deterministic reconciliation checks, LangGraph approval, `pytest` and evaluation, OpenTelemetry tracing, FastAPI, Docker and a README

### How it's used in the exercises

The learner receives fictional invoice PDFs, supplier agreements a purchase order CSV, and a seeded ledger of previously reviewed invoices. They extract the invoice number, supplier ID, purchase order ID, amount, currency and dates into a typed record. They select the agreement effective for the supplier and invoice date, then retrieve payment terms with agreement and page citations and run deterministic checks for duplicate supplier–invoice pairs, missing purchase orders, total or currency mismatches, and inconsistent payment terms.

The assistant returns a JSON review record with the extracted fields, cited evidence, discrepancy reasons and a review status. Incomplete evidence is flagged for review. The workflow prepares a draft and submits the approved version to a sandbox at most once.

### Model / release

Python 3.13; reuse the earlier courses’ dependencies (`minsearch>=0.1.0`, `sentence-transformers>=5.5.0`, `langchain`, `langgraph`, `openai>=2.38.0`, `fastapi`, `pytest`, `pymupdf>=1.26.7`, `mcp`, `opentelemetry-sdk`, `streamlit>=1.58.0`, `pandas>=3.0.3`). Model chosen by the learner and justified by evaluation.

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): Integrator stack 91.7% AI-First, GenAI + Ops 71.0%, Evaluation 69.3% Nov, Automating Manual Workflows 58.8%, Internal Operational Efficiency 57.5%, Agentic Systems 49.9%
- **FG learning paths / portfolio** (`learning-paths/README.md`, `portfolio/`, commit `1556dcb2`): portfolio signals used as the capstone checklist (real user and problem, realistic inputs, clear output, tests, evaluation, logging, reproducible setup, README with decisions and trade-offs); 86.9% of AI-First roles need skills beyond GenAI and 71.0% need production/ops skills (`portfolio/01`); top domains finance 3,877, healthcare 2,380, legal/regulatory 1,798 mentions (`portfolio/02`); finance candidates such as invoice extraction and reconciliation (`portfolio/07`).
- **LZ**: LLM Zoomcamp (`github.com/DataTalksClub/llm-zoomcamp`) Module 7 End-to-End Project (`project.md`)
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 7: End-To-End Project Example; Project guidelines, Evaluation criteria, Documentation tips

### Notes

For the 2–3 hour guided build, supply a starter with the web shell, tool adapters, deployment manifest, and fixture runner already wired. Learners implement field extraction, evidence selection, reconciliation, and the approval gate. Bundle 20–50 cases and reserve a held-out subset for final checks. Grade field accuracy, citations, discrepancy decisions, and approval behavior separately. The deployment check runs locally, with a kind manifest and saved rollout output as a fallback.

## Exercise adapted from the Buildcamp

Use My Daily Tasks to show how tools, an agent, tests, tracing, evaluation, and a service fit together. For the assessed build, give learners a fresh invoice and agreement dataset and ask them to extract invoice fields, retrieve matching payment terms, and flag discrepancies for review. Require a runnable container, a trace of a sample run, and a short evaluation report covering field accuracy, citation correctness, and tool choice.

[Buildcamp Week 7 source](https://github.com/alexeygrigorev/ai-bootcamp/blob/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/07-project-bonus/03-complete-example/01-intro-overview.md)

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 16.1 | Workflow Design | LZ `07-project-example/01-intro.md`; `project.md`; FG Use Cases |
| 16.2 | Extraction and Retrieval | LZ `07-project-example/07-chunking.md`, `02-evaluating-retrieval.md` |
| 16.3 | Checks and Approvals | BC `v2/07-project-bonus/03-complete-example/03-tools.md`, `04-agent.md` |
| 16.4 | Testing and Evaluation | LZ `03-evaluating-rag.md`; BC `03-complete-example/06-testing.md`, `07-test-judges.md`, `09-evals-otel.md` |
| 16.5 | FastAPI Integration | LZ `04-interface.md`; BC `03-complete-example/05-creating-app.md` |
| 16.6 | Workflow Tracing | LZ `05-monitoring.md`; BC `03-complete-example/08-logfire.md` |
| 16.7 | Deployment and Documentation | BC `03-complete-example/10-deployment.md`; `v2/07-project-bonus/02-project-work/04-documentation-tips.md`; LZ `06-summary.md` |

## Detailed lesson outline

### 16.1 Workflow Design

Inspect an invoice for 1,250 USD against a purchase order for 1,200 USD and an agreement that specifies Net 30. Examine the expected review record before coding. Define the fields, discrepancy reason, and evidence references needed for a reviewer to act.

**Check.** Classify a clean invoice, a mismatch, and a missing-evidence case.

### 16.2 Extraction and Retrieval

Extract typed invoice fields. Choose the supplier agreement applicable on the invoice date, then retrieve its payment clause and evidence.

**Check.** Verify each extracted field against the invoice and the cited terms against the agreement on a development fixture. Reserve held-out cases for the final evaluation.

### 16.3 Checks and Approvals

Compare normalized invoice values with purchase orders and the invoice ledger. Include two suppliers that reuse the same invoice number. Draft a proposed review ticket locally. Require approval of that exact draft before submitting it to the sandbox.

**Check.** Verify the flagged discrepancy and supporting evidence, then show that a rejected or changed draft creates no ticket and an approved retry creates only one.

### 16.4 Testing and Evaluation

Write tests for deterministic comparisons and run offline evaluation across clean, missing-evidence, duplicate, and mismatch cases.

**Check.** Report field accuracy, citation correctness, and tool and approval behavior.

### 16.5 FastAPI Integration

Connect the workflow to the supplied FastAPI endpoint and review view. Render a review record with discrepancy reasons and the cited evidence.

**Check.** Submit a fixture and confirm a reviewer can inspect the reasons for each flag.

### 16.6 Workflow Tracing

Trace PDF extraction, retrieval, comparison, and the approval gate with OpenTelemetry and inspect a run in Langfuse.

**Check.** Use the trace to explain why a development invoice was flagged.

### 16.7 Deployment and Documentation

Use the supplied CI and deployment templates to package the passing revision. Smoke-test that version on kind or use the fixture runtime when cluster access is unavailable. Document setup, checks, and known limitations in the project README.

**Check.** Reproduce a sample review from the documented commands. Attach the final version’s held-out evaluation report and retain the sample record and trace.
