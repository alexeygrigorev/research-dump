# 12. Evaluating RAG and Agents - DONE

Part of the [DataCamp AI Engineering track plan](../README.md). Stage: 4. Application quality. 6 lessons, 2-3 hours. Each lesson is designed for approximately 20-25 minutes.

## Summary

Learners use monitoring data to measure whether a change improves an agent. They define success criteria, align automated judgments with human labels, and establish a baseline. They compare versions fairly and use synthetic questions to fill coverage gaps found during evaluation.

## Learning objectives

- Prepare evaluation cases from reviewed monitoring data
- Define criteria for answer quality and completed actions
- Check an LLM judge against human labels
- Compare versions using quality, cost, and latency evidence
- Generate and review synthetic questions for missing coverage

## Why here

Uses the traces and reviewed dataset from monitoring to build a repeatable improvement loop.

## Transformation

From "I have examples of good and bad behavior" to "I can measure quality and justify a release decision."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Langfuse trace and dataset exports, human labels, structured judge verdicts, precision and recall, tool-state checks, paired comparison reports, and synthetic question generation.

### How it's used in the exercises

Use one dataset throughout the course. Start with course 11's reviewed monitoring export, including original questions, recorded answers, retrieved passages, human verdicts and corrections, tool events, costs, and source trace IDs. Supply the same snapshot to learners who skipped course 11. Include supported answers, missing-evidence questions, and requests to create or clarify a draft.

Separate development cases from held-out comparison cases before adjusting criteria, the judge, or the assistant. The first four lessons use the development cases to build and check the scoring pipeline and diagnose a baseline failure. The fifth runs supplied baseline and candidate versions on the reserved cases with the same handbook and resettable draft store. The final lesson expands coverage with reviewed synthetic questions, reported separately from the original benchmark. Recorded model responses support offline grading.

### Model / release

Python 3.13. `pandas==3.1.1`, `openai==3.57.0`, `pydantic==2.14.4`, `langfuse==5.2.0`. Use DataCamp-funded model API calls. Select the lowest-cost available model that meets the exercise criteria; no fixed model release is required.

### Source material

- **BC Week 6** supplies the main progression: run scenarios, use human labels, align the judge, measure quality, then generate synthetic questions. [Buildcamp evaluation](https://github.com/alexeygrigorev/ai-bootcamp/tree/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/06-evaluation).
- **Course 11** supplies the reviewed Langfuse traces and dataset, replacing a separate collection and labeling exercise here.
- **LZ Module 4** supplies supporting examples for answer quality and agent evaluation. [LLM Zoomcamp evaluation](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/04-evaluation).

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 12.1 | Loading Monitoring Data | Course 11 traces and dataset; BC `02-measure/04-gold-standard-dataset.md` |
| 12.2 | Defining Evaluation Criteria | BC `02-measure/04-gold-standard-dataset.md`; LZ `14-agent-evaluation.md` |
| 12.3 | Evaluating with LLM Judges | BC `02-measure/05-judge-alignment.md` |
| 12.4 | Measuring Agent Quality | BC `02-measure/06-running-evals.md` |
| 12.5 | Comparing Agent Versions | BC `02-measure/06-running-evals.md` |
| 12.6 | Generating Synthetic Questions | BC `03-synthetic-data/02-generating-questions.md`, `04-judging-synthetic-data.md` |

## Detailed lesson outline

### 12.1 Loading Monitoring Data

Start where course 11 ended: export the reviewed traces and dataset, or load the supplied snapshot. Join each question to its original answer, retrieved evidence, tool events, human verdict, and correction. Preserve case and trace IDs. Reserve separate development and held-out case families before making any changes.

**Check.** Load a correct answer and an incorrect answer with a human correction. Keep the original answer as the output to evaluate and the correction as reference data. Flag missing action evidence rather than assuming an action succeeded.

**Output.** A versioned evaluation dataset linked to the monitoring runs, with development and held-out splits.

### 12.2 Defining Evaluation Criteria

Use the development examples to make the existing human judgments explicit. A factual answer must be correct and supported by retrieved evidence. A question with missing evidence should receive an appropriate refusal or clarification. A request to create a draft requires evidence of the actual write. Define separate pass conditions for answers and actions, including how to report missing evidence.

**Check.** Apply the criteria to a grounded answer, an invented deadline extension, and a reply claiming to create a draft when the store is empty. Resolve unclear criteria against the reviewed evidence before automating them.

**Output.** A short scoring rubric and deterministic checks for completed actions.

### 12.3 Evaluating with LLM Judges

Adapt the judge from course 10 to the rubric from 12.2. Give it the question, retrieved evidence, and recorded answer; collect a structured verdict and reason. Compare verdicts with the human labels on development cases, inspect disagreements, and revise the judge on a calibration subset. Check it on untouched labeled development cases before freezing it. Keep tool-action checks in Python.

**Check.** Identify a false pass and a false alarm. Report precision and recall for failures on the untouched labels, with counts and denominators. Confirm that held-out comparison cases were not used for tuning.

**Output.** A frozen judge prompt and a report showing how well it matches human judgments.

### 12.4 Measuring Agent Quality

Apply the judge and action checks to the recorded development runs. Report answer pass rate and action success separately, along with failures, unverified actions, and agent and judge costs. Inspect failed cases through their source traces to locate the first consequential error. Choose one change to investigate and note a gap in dataset coverage.

**Check.** Produce baseline counts and denominators, flag a claimed draft that was never written, and explain whether one failed answer came from missing evidence or an unsupported claim. Keep unverified actions visible in the report.

**Output.** A baseline quality report, an evidence-backed diagnosis, and a proposed improvement.

### 12.5 Comparing Agent Versions

Test the proposed improvement using supplied baseline and candidate versions. Run both on the same reserved cases with the same handbook, starting tool state, and frozen scoring rules. Join outcomes by case ID and inspect improvements and regressions. Compare answer quality, action success, cost, and latency against release criteria supplied before scoring.

**Check.** Decide whether to ship a candidate whose answers improve but whose draft-task success declines. Show the counts, threshold result, and a changed case that explains the decision.

**Output.** A version-comparison report and release decision, saved in a format the CI course can consume.

### 12.6 Generating Synthetic Questions

Return to the coverage gap found in 12.4. Generate questions and proposed reference answers from handbook passages, then review them for unsupported assumptions, ambiguity, and near-duplicates. Score accepted cases with the existing pipeline and inspect disagreements. Report synthetic results separately from the reviewed-usage benchmark and keep related question families together in future splits.

**Check.** Reject an invented reimbursement policy and correct a reference that confuses draft and final deadlines. Add reviewed cases with source IDs and generation provenance without changing the benchmark used for the version comparison.

**Output.** A reviewed extension to the evaluation dataset for the next improvement cycle.
