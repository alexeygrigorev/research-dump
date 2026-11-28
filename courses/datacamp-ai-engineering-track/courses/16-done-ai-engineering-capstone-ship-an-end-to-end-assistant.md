# 16. AI Engineering Capstone - DONE

Part of the [DataCamp AI Engineering track plan](../README.md). Stage: 6. Capstone. 7 lessons, 2-3 hours. Each lesson is designed for approximately 20-25 minutes.

## Summary

Learners combine the preceding courses in a guided invoice-review application. They complete selected parts of document extraction, retrieval, agent tools, validation, and observability in a supplied project. They test and evaluate the completed workflow, then verify its local release and deployment.

## Learning objectives

- Combine structured extraction, retrieval, and agent tools in one workflow
- Apply tests, guardrails, and approval to the application
- Use traces and evaluation results to explain a quality decision
- Verify a reproducible local release and deployment

## Why here

Transfers the preceding skills to a new dataset and checks that learners can connect them into one application.

## Transformation

From "I can implement the individual techniques" to "I can complete, verify, and explain an end-to-end AI application."

## Theory or application

Theory and application

## Coverage of preceding courses

| Course | Required capstone work | Evidence |
| :---- | :---- | :---- |
| 1. LLM APIs | Call the model with instructions, extract typed fields, and stream an answer. | Validated extraction, API request, and a completed response stream. |
| 2. RAG | Chunk agreements with source metadata and answer from retrieved passages. | Keyword baseline and answers with agreement/page citations. |
| 3. Embeddings and vector search | Embed agreement chunks, persist the vector index, and compare retrieval with the keyword baseline. | Saved index, retrieval comparison, and a successful restart. |
| 4. PDF processing | Recover invoice fields and table rows, handle continued text, and process independent documents in parallel. | Source-linked records and extraction checks. |
| 5. Agent basics | Inspect a model-selected tool call and its result through the agent loop. | A trace connecting the request, tool arguments, result, and answer. |
| 6. Agent frameworks | Register typed read/write tools and structured output with LangChain. | Validated tool schemas, review drafts, and updates by draft ID. |
| 7. MCP | Discover and call purchase-order lookup through an MCP server. | Discovered schema, successful call, and a handled missing-order result. |
| 8. Multi-agent patterns | Coordinate extraction and agreement specialists with LangGraph state. | Worker findings joined into a review; comparison with a supplied single-agent baseline. |
| 9. Python applications | Build importable modules, load assets, serve FastAPI, lock dependencies, and containerize. | A clean setup, API requests, and a runnable image. |
| 10. Testing | Test reconciliation, tool behavior, output quality, and follow-up changes. | Passing tests and a regression caught by a failed assertion. |
| 11. Monitoring | Trace runs in Langfuse, inspect tokens and costs, collect feedback, and review a failed run. | Linked trace, feedback, and a human correction. |
| 12. Evaluation | Score reviewed runs, check the judge against human labels, compare versions, and add synthetic coverage. | Quality report, paired comparison, and reviewed synthetic cases. |
| 13. Guardrails | Check inputs, outputs, tool permissions, and approval before submission. | Allowed, denied, rejected, changed-draft, and approved-retry results. |
| 14. CI/CD | Run tests and budgeted live-model evaluations before building a commit-tagged image. | Passing pipeline, blocked regression, and matching report/image commit IDs. |
| 15. Kubernetes | Deploy the image, configure it, verify readiness, and practice update and rollback. | Manifests, successful smoke requests, and restored image after rollback. |

## Build details

### Syntax / functionality involved

PDF extraction, Pydantic schemas, keyword and vector retrieval, a persistent index, LangChain tools, LangGraph state and specialist agents, an MCP client/server, guardrails and approval, pytest, Langfuse tracing and datasets, LLM judges, FastAPI, uv, Docker, CI workflow YAML, and Kubernetes manifests.

### How it's used in the exercises

Provide an integrated starter with the API shell, tool adapters, tracing backend, local pipeline, and cluster manifests prepared. Learners complete focused code sections for extraction, retrieval, tool coordination, validation, and approval; they then run the provided tests, evaluate real model outputs, inspect a trace, and verify a deployment. Each lesson reuses the same project and produces evidence for the next step.

### Model / release

Python 3.13. `openai==3.57.0`, `pydantic==2.14.4`, `python-dotenv==1.2.4`, `minsearch==0.2.0`, `sentence-transformers==6.3.0`, `numpy==2.5.5`, `sqlitesearch==0.3.0`, `mcp==1.30.0`, `langchain==1.5.2`, `langchain-openai==1.8.5`, `langgraph==1.2.24`, `langchain-mcp-adapters==0.3.2`, `fastapi==0.165.0`, `uvicorn==0.54.0`, `pytest==9.2.0`, `httpx==0.28.1`, `langfuse==5.2.0`, `pandas==3.1.1`, `uv==0.13.9`, `PyYAML==6.0.4`, `PyMuPDF==2.1`. Use DataCamp-funded model API calls. Select the lowest-cost available model that meets the exercise criteria; no fixed model release is required. Docker and local runtime tools are supplied by the exercise workspace; see [Runtime requirements](../runtime.md).

### Source material

- Courses 1-15 provide the implementation patterns and required skills listed in the coverage map.
- **BC Week 7** supplies the integrated project pattern, tests, monitoring, and documentation. [Complete example](https://github.com/alexeygrigorev/ai-bootcamp/tree/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/07-project-bonus/03-complete-example).
- **LZ** supplies project and evaluation guidance. [Project requirements](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/project.md).
- **FG portfolio guidance**, commit `1556dcb2`, supplies the expectations for realistic inputs, reproducibility, tests, evaluation, logging, and documented trade-offs.

### Notes

Seven guided lessons of approximately 20-25 minutes, completed in 2-3 hours. The starter includes the infrastructure and routine wiring; learners complete the assessed decisions and code sections. Use fictional invoices, agreements, purchase orders, and reviewed examples. Keep the dataset small enough for the supplied model-call budget.

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 16.1 | Planning the Application | Courses 1-15 coverage map; FG portfolio; BC project guidelines |
| 16.2 | Processing and Retrieving Documents | Courses 1 and 4; BC structured extraction; Courses 2 and 3; LZ document retrieval |
| 16.3 | Connecting Agents and Tools | Courses 5-8; BC tools and agents |
| 16.4 | Serving the Application | Course 9; BC creating the app |
| 16.5 | Testing and Guardrails | Courses 10 and 13; BC tests and approval |
| 16.6 | Monitoring and Evaluation | Courses 11 and 12; BC monitoring and evaluations |
| 16.7 | CI/CD and Deployment | Courses 14 and 15; BC deployment and documentation |

## Detailed lesson outline

### 16.1 Planning the Application

Inspect a clean invoice, a mismatch, and a missing-evidence case. Define the review schema, specialist responsibilities, tool permissions, and approval boundary. Set quality and cost criteria before building. Reserve held-out case families and map the required skills to the project deliverables.

**Check.** Explain the expected outcome for each example and identify the artifact that will demonstrate each course's contribution.

**Guided scope.** Complete the specified function or configuration in the supplied starter, then run the provided check. Infrastructure and routine integration are preconfigured.

### 16.2 Processing and Retrieving Documents

Extract text and table rows from PDFs, join continued sections across pages, and process independent invoices in parallel. Use the model to extract typed fields and retain source/page references. Save records for reuse and handle absent fields explicitly.

**Check.** Recover an invoice amount from a table, preserve a field continued on another page, and trace every assessed field to its source. Keep duplicate invoice numbers from different suppliers distinct.

Chunk supplier agreements with document, page, supplier, and effective-date metadata. Build a keyword baseline, then embed chunks and persist a vector index. Apply supplier and date filters and return cited payment terms from the relevant agreement.

**Check.** Compare retrieval on paraphrased queries, reload the index in a fresh process, and verify the cited clause belongs to the correct agreement version.

**Guided scope.** Complete the specified function or configuration in the supplied starter, then run the provided check. Infrastructure and routine integration are preconfigured.

### 16.3 Connecting Agents and Tools

Register typed read/write tools with LangChain. Discover purchase-order lookup through MCP and connect the extraction and agreement specialists in a LangGraph workflow. Combine their outputs with deterministic reconciliation and create an editable review draft. Inspect a tool call through its full request/result loop and compare the specialist workflow with the supplied single-agent baseline.

**Check.** Follow evidence IDs into the final review, handle a missing purchase order, update a draft by ID, and compare supported decisions, calls, and cost across the two architectures.

**Guided scope.** Complete the specified function or configuration in the supplied starter, then run the provided check. Infrastructure and routine integration are preconfigured.

### 16.4 Serving the Application

Organize the workflow into importable Python modules and load its index, embedding model, and tool clients at startup. Expose review and approval routes with FastAPI and stream a read-only explanation. Lock dependencies with uv and build the container with the required assets.

**Check.** Start from a clean checkout, send a request from another process, reconstruct a streamed answer, and run the container without mounting the source checkout.

**Guided scope.** Complete the specified function or configuration in the supplied starter, then run the provided check. Infrastructure and routine integration are preconfigured.

### 16.5 Testing and Guardrails

Test deterministic reconciliation, tool arguments, citations, output quality, and follow-up draft edits. Add input and output checks and enforce permissions before tool execution. Require approval for the exact draft submitted. Test rejection, edits after approval, and retries with the same operation ID.

**Check.** Catch a seeded reconciliation regression. Show zero submissions for denied, rejected, or changed drafts and one submission for an approved retry. Verify that a malicious instruction in a document cannot authorize a write.

**Guided scope.** Complete the specified function or configuration in the supplied starter, then run the provided check. Infrastructure and routine integration are preconfigured.

### 16.6 Monitoring and Evaluation

Trace extraction, retrieval, agent/tool calls, and approval with Langfuse. Inspect token usage and cost, attach feedback to the correct run, and record a human correction. Use reviewed traces to define evaluation criteria and check the judge against human labels. Compare baseline and candidate quality on the reserved cases, then generate and review a few questions for uncovered cases.

**Check.** Explain one failure from its trace and produce a versioned quality/cost report. Keep generated cases separate from the held-out comparison and preserve links to source traces.

**Guided scope.** Complete the specified function or configuration in the supplied starter, then run the provided check. Infrastructure and routine integration are preconfigured.

### 16.7 CI/CD and Deployment

Complete the workflow that runs tests and live-model evaluations with configured secrets and a spending limit. Build and tag the image only after its checks pass. Deploy the exact tag to kind with the required MCP service and persistent store configuration. Configure application settings and credentials, verify readiness and service access, then update and roll back. Document the complete setup and release commands.

**Check.** Block a candidate that fails evaluation, deploy the passing commit, smoke-test a review, and restore a healthy version after a bad rollout. Submit the image tag, evaluation report, sample trace, deployment evidence, and README.

**Guided scope.** Complete the specified function or configuration in the supplied starter, then run the provided check. Infrastructure and routine integration are preconfigured.
