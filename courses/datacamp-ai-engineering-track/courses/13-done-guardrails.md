# 13. Guardrails for AI Agents - DONE

Part of the [DataCamp AI Engineering track plan](../README.md). Stage: 4. Application quality. 6 lessons, 2-3 hours. Each lesson is designed for approximately 20-25 minutes.

## Summary

Learners add runtime controls to an agent whose quality they can already measure. They check inputs and outputs, restrict tool actions, and require human approval before selected writes. They evaluate whether the controls block disallowed behavior while still allowing valid requests.

## Learning objectives

- Place checks at input, output, and tool boundaries
- Enforce tool permissions with trusted application data
- Require approval for the exact action being submitted
- Prevent repeated submission of the same approved action
- Measure blocked violations and incorrectly blocked valid requests

## Why here

Builds on the evaluation baseline so safeguards can be assessed for both protection and usability.

## Transformation

From "my agent can use tools" to "I can enforce when it may act and what it may return."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Typed validation, policy functions, tool preconditions, human approval, structured refusals, output schemas, and citation checks.

### How it's used in the exercises

Give learners the speaker handbook and a simulated speaker ticket store. Drafts stay in the current workflow. Only approved submissions write to the ticket store. They validate requests before routing, check permission and approval before changing the store, and verify citation IDs against the evidence returned by the search tools. Bundle allowed and denied requests, an approval and a rejection, and a knowledge document containing an instruction to submit a ticket. Grade the returned decision and inspect the fixture store to verify which requests caused a write.

### Model / release

Python 3.13. `langchain==1.5.2`, `langchain-openai==1.8.5`, `langgraph==1.2.24`, `pydantic==2.14.4`. Use DataCamp-funded model API calls. Select the lowest-cost available model that meets the exercise criteria; no fixed model release is required.

### Source material

- Alexey’s May workshop, `2026/05/2026-05-26-agent-with-guardrails` in `ai-shipping-labs-workshops-raw`, uses a Zoomcamp FAQ agent to introduce input and output checks. Reuse the progression with speaker support.
- Alexey’s January workshop, `2026/01/2026-01-06-guardrails-for-ai-agents` in the same repository, covers tool-based guardrails. Keep approvals and permissions in application code.
- **BC** Week 7 Guardrails, `v2/07-project-bonus/04-guardrails-sdk/02-guardrails-sdk.md` and `v2/07-project-bonus/05-guardrails-pydantic/02-guardrails-tool-calls.md`. Adapt the policy and tool-call patterns to the existing assistant.
- **BC** Week 4 Multi-Agent Systems, human-in-the-loop exercises.
- **FG** Guardrails appear in 19.8% of AI-First roles and rose from 10.2% to 17.5% of all roles during the sampled period.

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 13.1 | Introduction to Guardrails | May 2026 guardrails workshop `01-overview.md` |
| 13.2 | Input Guardrails | May 2026 guardrails workshop `05-input-guardrails.md` |
| 13.3 | Tool Permissions | January 2026 guardrails workshop `09-tool-based-guardrails.md` |
| 13.4 | Human Approval | Buildcamp Week 4 human-in-the-loop exercises |
| 13.5 | Preventing Duplicate Actions | Buildcamp Week 4 human-in-the-loop exercises; new retry exercise |
| 13.6 | Output Guardrails | May 2026 guardrails workshop `07-output-guardrails.md`, `08-multiple-guardrails.md` |

## Detailed lesson outline

### 13.1 Introduction to Guardrails

Compare three runs of the existing assistant: a valid rehearsal question, an unrelated request, and a response that promises an extension the handbook does not authorize. Identify where each decision belongs in the request, tool, and reply flow.

**Check.** Assign each case an expected outcome and the boundary responsible for enforcing it.

### 13.2 Input Guardrails

Add a typed topic and intent decision before the agent runs. Use scripted verdicts to exercise the route, then inspect a borderline speaker question.

**Check.** Confirm an unrelated request does not reach retrieval and a relevant one still reaches the assistant.

### 13.3 Tool Permissions

Allow the assistant to prepare a local draft. Bind a draft to its authenticated speaker. Route a request about that speaker’s own rehearsal to approval and deny a request to file a ticket for another speaker. Test a handbook passage that tries to instruct the assistant to submit a ticket.

**Check.** Verify that the authorized request reaches approval, the cross-speaker request is denied, and neither request writes a ticket at this step.

### 13.4 Human Approval

Show the reviewer the proposed ticket, record approval for that draft version, and resume the workflow. Run fixtures for approval, rejection, and a changed draft.

**Check.** Verify that rejected drafts and drafts changed after approval cannot be submitted.

### 13.5 Preventing Duplicate Actions

Retry an approved submission after a simulated lost response. Associate the operation with a stable identifier and reuse the recorded result when the same submission is retried.

**Check.** Verify that repeated submission of the approved draft creates one ticket, while a rejected or changed draft creates none.

### 13.6 Output Guardrails

Check the completed answer before returning it. Check both a citation outside the retrieved evidence and an extension promise that cites a real retrieved section without support for that promise. Use the held-out cases from evaluation to compare the guarded and baseline assistants.

**Check.** Verify that unsafe replies are withheld and report any valid answers the new checks reject.
