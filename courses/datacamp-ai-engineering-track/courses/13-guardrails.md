# 13. Guardrails for AI Agents


Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 4. Application quality. 5 lessons, 2-3 hours.

## Summary

Learners add policy checks to the conference speaker support assistant. They validate requests, enforce tool permissions before execution, route ticket submission to explicit approval for the reviewed draft, and check the assistant's output before returning it.

## Learning objectives

- Translate an application policy into checks at the input, tool, and output boundaries
- Validate tool arguments and enforce permissions using trusted application data
- Pause for a human decision before a workflow action writes to a ticket store
- Validate output fields and check cited document IDs against retrieved evidence
- Verify behavior on allowed, rejected, and approval-required requests

## Why here

The evaluation course establishes a baseline. Learners add controls, rerun representative cases, and check whether safeguards block disallowed actions while still serving legitimate speakers. The invoice capstone reuses the approval boundary.

## Transformation

From building an assistant that can use tools to enforcing when it may use them and what it may return.

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Typed validation, policy functions, tool preconditions, human approval, structured refusals, output schemas, and citation checks.

### How it's used in the exercises

Give learners the speaker handbook and a simulated speaker ticket store. Drafts stay in the current workflow. Only approved submissions write to the ticket store. They validate requests before routing, check permission and approval before changing the store, and verify citation IDs against the evidence returned by the search tools. Bundle allowed and denied requests, an approval and a rejection, and a knowledge document containing an instruction to submit a ticket. Grade the returned decision and inspect the fixture store to verify which requests caused a write.

### Model / release

Python 3.13, LangChain or LangGraph for the existing assistant, and Pydantic for structured validation. Use deterministic cases to grade policy enforcement.

### Source material

- Alexey’s May workshop, `2026/05/2026-05-26-agent-with-guardrails` in `ai-shipping-labs-workshops-raw`, uses a Zoomcamp FAQ agent to introduce input and output checks. Reuse the progression with speaker support.
- Alexey’s January workshop, `2026/01/2026-01-06-guardrails-for-ai-agents` in the same repository, covers tool-based guardrails. Keep approvals and permissions in application code.
- **BC** Week 7 Guardrails, `v2/07-project-bonus/04-guardrails-sdk/02-guardrails-sdk.md` and `v2/07-project-bonus/05-guardrails-pydantic/02-guardrails-tool-calls.md`. Adapt the policy and tool-call patterns to the existing assistant.
- **BC** Week 4 Multi-Agent Systems, human-in-the-loop exercises.
- **FG** Guardrails appear in 19.8% of AI-First roles and rose from 10.2% to 17.5% of all roles during the sampled period.

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 13.1 | Setting Limits for the Speaker Support Assistant | May 2026 guardrails workshop `01-overview.md` |
| 13.2 | Blocking Off-Topic Requests | May 2026 guardrails workshop `05-input-guardrails.md` |
| 13.3 | Checking Permissions before Ticket Submission | January 2026 guardrails workshop `09-tool-based-guardrails.md` |
| 13.4 | Getting Approval for a Ticket Draft | Buildcamp Week 4 human-in-the-loop exercises |
| 13.5 | Checking Replies for Unsupported Promises | May 2026 guardrails workshop `07-output-guardrails.md`, `08-multiple-guardrails.md` |

## Detailed lesson outline

### 13.1 Setting Limits for the Speaker Support Assistant

Compare three runs of the existing assistant: a valid rehearsal question, an unrelated request, and a response that promises an extension the handbook does not authorize. Identify where each decision belongs in the request, tool, and reply flow.

**Check.** Assign each case an expected outcome and the boundary responsible for enforcing it.

### 13.2 Blocking Off-Topic Requests

Add a typed topic and intent decision before the agent runs. Use scripted verdicts to exercise the route, then inspect a borderline speaker question.

**Check.** Confirm an unrelated request does not reach retrieval and a relevant one still reaches the assistant.

### 13.3 Checking Permissions before Ticket Submission

Allow the assistant to prepare a local draft. Bind a draft to its authenticated speaker. Route a request about that speaker’s own rehearsal to approval and deny a request to file a ticket for another speaker. Test a handbook passage that tries to instruct the assistant to submit a ticket.

**Check.** Verify that the authorized request reaches approval, the cross-speaker request is denied, and neither request writes a ticket at this step.

### 13.4 Getting Approval for a Ticket Draft

Show the reviewer the proposed ticket, record approval for that draft version, and resume the workflow. Run fixtures for rejection, a changed draft, and a retry of an approved submission.

**Check.** Verify one write for the approved version and zero writes when rejected or changed after approval.

### 13.5 Checking Replies for Unsupported Promises

Check the completed answer before returning it. Check both a citation outside the retrieved evidence and an extension promise that cites a real retrieved section without support for that promise. Use the held-out cases from evaluation to compare the guarded and baseline assistants.

**Check.** Verify that unsafe replies are withheld and report any valid answers the new checks reject.
