# 16. AI Engineering Capstone - DONE

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 6. Capstone. 8 lessons, 6-8 hours.

## Summary

Learners apply the skills from courses 1-15 to build and ship an invoice review assistant. They extract structured fields from PDFs, retrieve supplier terms, coordinate specialist agents, and query purchase orders through MCP. They serve the workflow through an API, add tests and guardrails, trace and evaluate real runs, and release the tested container to Kubernetes through CI/CD. The result is a reproducible application with evidence that each part works.

## Learning objectives

- Extract typed PDF data and build grounded retrieval with a persistent vector index
- Combine tool calling, specialist agents, MCP, and human approval in a workflow
- Package the application with an API, locked dependencies, and a container
- Test behavior, trace runs, and compare evaluated versions
- Run a CI pipeline that gates a versioned image on tests and evaluation
- Deploy, configure, update, and recover the application on Kubernetes

## Why here

This is the integration and transfer exercise for the whole track. Learners apply all fifteen preceding courses to a new document workflow and carry the same application from raw inputs to an evaluated release. Each stage produces an artifact used by the next, and the final submission includes evidence for every course's core skills.

## Transformation

From implementing individual AI engineering techniques to delivering an application that another engineer can run, evaluate, deploy, and maintain.

## Theory or application

Application

## Coverage of courses 1-15

| Course | Required capstone work | Evidence |
| :---- | :---- | :---- |
| 1. LLM APIs | Call the model with instructions, extract typed fields, and stream an answer. | Validated extraction, API request, and a completed response stream. |
| 2. RAG | Chunk agreements with source metadata and answer from retrieved passages. | Keyword baseline and answers with agreement/page citations. |
| 3. Embeddings and vector search | Embed agreement chunks, persist the vector index, and compare retrieval with the keyword baseline. | Saved index, retrieval comparison, and a successful restart. |
| 4. PDF processing | Recover invoice fields and table rows, handle continued text, and process independent documents in parallel. | Source-linked records and extraction checks. |
| 5. Agent basics | Inspect a model-selected tool call and its result through the agent loop. | A trace connecting the request, tool arguments, result, and answer. |
| 6. Agent frameworks | Register typed read/write tools and structured agent output with LangChain. | Validated tool schemas, review drafts, and updates by draft ID. |
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

Supply fictional invoice PDFs, supplier agreements, purchase orders, and a ledger of earlier reviews. An extraction specialist produces typed invoice fields with page evidence. An agreement specialist retrieves terms for the correct supplier and effective date. A coordinating graph combines their findings with purchase orders obtained over MCP. Python checks detect duplicate supplier/invoice pairs, missing orders, amount or currency mismatches, and inconsistent payment terms.

The application creates an editable review draft containing extracted fields, cited evidence, discrepancy reasons, and a status. Missing evidence is sent for review. A human approves the exact draft before a sandbox submission, and retries reuse the same operation ID. The MCP service and submission store use supplied adapters with persistent state suitable for the deployment exercise.

Use one repository throughout. Package and serve the workflow, test its behavior, then trace real development runs and review their failures. Evaluate a baseline and candidate on reserved cases. CI runs the checks and budgeted live evaluations, builds an image for the passing commit, and hands that image to the Kubernetes deployment. Finish by updating, rolling back, and reproducing a review from the documented commands.

### Model / release

Python 3.13 and the libraries already used in courses 1-15: OpenAI, Pydantic, PyMuPDF, minsearch, an embedding model and persistent vector backend, LangChain, LangGraph, MCP, FastAPI, pytest, Langfuse, pandas, uv, Docker, a local CI runner, kind, and kubectl. Lock dependencies against the exercise runtime. Model choice is justified by quality, cost, and latency measurements. Keep live agent and judge calls within the supplied evaluation budget.

### Source material

- Courses 1-15 provide the implementation patterns and required skills listed in the coverage map.
- **BC Week 7** supplies the integrated project pattern, tests, monitoring, and documentation. [Complete example](https://github.com/alexeygrigorev/ai-bootcamp/tree/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/07-project-bonus/03-complete-example).
- **LZ** supplies project and evaluation guidance. [Project requirements](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/project.md).
- **FG portfolio guidance**, commit `1556dcb2`, supplies the expectations for realistic inputs, reproducibility, tests, evaluation, logging, and documented trade-offs.

### Notes

This is a 6-8 hour guided capstone. Supply datasets, service adapters, a single-agent baseline, and starter CI/deployment templates. Learners complete the extraction, retrieval, agent wiring, validation, instrumentation, and release checks themselves. Use LangChain/LangGraph and one persistent vector backend for the assessed implementation.

Bundle 20-50 cases and reserve a subset before tuning. Grade extraction, citations, reconciliation, tool actions, and approval separately. Real model calls are used for the evaluated runs. Saved outputs can support diagnosis exercises when services are unavailable, but the final deployment evidence must come from a running application.

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 16.1 | Planning the Application | Courses 1-15 coverage map; FG portfolio; BC project guidelines |
| 16.2 | Processing Documents | Courses 1 and 4; BC structured extraction |
| 16.3 | Building Retrieval | Courses 2 and 3; LZ document retrieval |
| 16.4 | Connecting Agents and Tools | Courses 5-8; BC tools and agents |
| 16.5 | Serving the Application | Course 9; BC creating the app |
| 16.6 | Testing and Guardrails | Courses 10 and 13; BC tests and approval |
| 16.7 | Monitoring and Evaluation | Courses 11 and 12; BC monitoring and evaluations |
| 16.8 | CI/CD and Deployment | Courses 14 and 15; BC deployment and documentation |

## Detailed lesson outline

### 16.1 Planning the Application

Inspect a clean invoice, a mismatch, and a missing-evidence case. Define the review schema, specialist responsibilities, tool permissions, and approval boundary. Set quality and cost criteria before building. Reserve held-out case families and map the required skills to the project deliverables.

**Check.** Explain the expected outcome for each example and identify the artifact that will demonstrate each course's contribution.

### 16.2 Processing Documents

Extract text and table rows from PDFs, join continued sections across pages, and process independent invoices in parallel. Use the model to extract typed fields and retain source/page references. Save records for reuse and handle absent fields explicitly.

**Check.** Recover an invoice amount from a table, preserve a field continued on another page, and trace every assessed field to its source. Keep duplicate invoice numbers from different suppliers distinct.

### 16.3 Building Retrieval

Chunk supplier agreements with document, page, supplier, and effective-date metadata. Build a keyword baseline, then embed chunks and persist a vector index. Apply supplier and date filters and return cited payment terms from the relevant agreement.

**Check.** Compare retrieval on paraphrased queries, reload the index in a fresh process, and verify the cited clause belongs to the correct agreement version.

### 16.4 Connecting Agents and Tools

Register typed read/write tools with LangChain. Discover purchase-order lookup through MCP and connect the extraction and agreement specialists in a LangGraph workflow. Combine their outputs with deterministic reconciliation and create an editable review draft. Inspect a tool call through its full request/result loop and compare the specialist workflow with the supplied single-agent baseline.

**Check.** Follow evidence IDs into the final review, handle a missing purchase order, update a draft by ID, and compare supported decisions, calls, and cost across the two architectures.

### 16.5 Serving the Application

Organize the workflow into importable Python modules and load its index, embedding model, and tool clients at startup. Expose review and approval routes with FastAPI and stream a read-only explanation. Lock dependencies with uv and build the container with the required assets.

**Check.** Start from a clean checkout, send a request from another process, reconstruct a streamed answer, and run the container without mounting the source checkout.

### 16.6 Testing and Guardrails

Test deterministic reconciliation, tool arguments, citations, output quality, and follow-up draft edits. Add input and output checks and enforce permissions before tool execution. Require approval for the exact draft submitted. Test rejection, edits after approval, and retries with the same operation ID.

**Check.** Catch a seeded reconciliation regression. Show zero submissions for denied, rejected, or changed drafts and one submission for an approved retry. Verify that a malicious instruction in a document cannot authorize a write.

### 16.7 Monitoring and Evaluation

Trace extraction, retrieval, agent/tool calls, and approval with Langfuse. Inspect token usage and cost, attach feedback to the correct run, and record a human correction. Use reviewed traces to define evaluation criteria and check the judge against human labels. Compare baseline and candidate quality on the reserved cases, then generate and review a few questions for uncovered cases.

**Check.** Explain one failure from its trace and produce a versioned quality/cost report. Keep generated cases separate from the held-out comparison and preserve links to source traces.

### 16.8 CI/CD and Deployment

Complete the workflow that runs tests and live-model evaluations with configured secrets and a spending limit. Build and tag the image only after its checks pass. Deploy the exact tag to kind with the required MCP service and persistent store configuration. Configure application settings and credentials, verify readiness and service access, then update and roll back. Document the complete setup and release commands.

**Check.** Block a candidate that fails evaluation, deploy the passing commit, smoke-test a review, and restore a healthy version after a bad rollout. Submit the image tag, evaluation report, sample trace, deployment evidence, and README.
