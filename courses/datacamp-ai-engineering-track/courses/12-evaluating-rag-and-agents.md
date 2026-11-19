# 12. Evaluating RAG and Agents

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 4. Application quality. 8 lessons, 2–3 hours.

## Summary

A proposed change helps the conference assistant find handbook sections for paraphrased questions. Does it also help a speaker get an accurate answer or a usable support-ticket draft? Learners compare two versions in two parts. First they score retrieval and the claims made from the retrieved passages. Then they run complete speaker requests and check what the agent actually accomplished. Both parts feed one release decision.

## Learning objectives

- Construct a small, human-checked evaluation set from traces and synthetic questions
- Measure retrieval hit rate and rank, answer correctness, grounding, and appropriate abstention
- Calibrate an answer judge against held-out human labels
- Score agent tasks from their answers, tool records, and final local state
- Compare assistant versions on the same cases and report the quality and cost trade-off

## Why here

Course 10 supplies the test suite and a first judge rubric. Course 11 supplies examples of real failure modes. Learners now ask how frequently each version succeeds across several kinds of speaker requests. The resulting metrics report becomes the input to the quality check in course 14.

## Transformation

Learners can defend a decision to ship or hold a change, identify the group of speakers affected, and point to individual cases that explain a metric.

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Labeled case records, ranked section IDs, hit rate@k and mean reciprocal rank@k, claim-level rubrics, judge agreement, local tool-state snapshots, paired version reports.

### How it's used in the exercises

Supply two assistant versions, a frozen handbook, a local ticket-draft tool, and recorded outputs for roughly two dozen cases. Include direct lookups, paraphrases, questions the handbook cannot answer, and requests to draft a ticket. Each case has a stable ID. Both versions receive the same starting state. Keep scenario families together when splitting development and held-out cases so paraphrases of one question cannot leak into both sets.

### Model / release

Python 3.13, pandas, the course 9 project, and an inexpensive model for demonstrating synthetic questions and judging. Provide recorded candidates, answers, tool events, judge outputs, token counts and timings so the graded comparison is reproducible.

### Source material

- LLM Zoomcamp Module 4 covers ground truth, search metrics, RAG answer quality and agent trajectories. [LLM Zoomcamp evaluation](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/04-evaluation)
- Buildcamp Week 6 covers running scenarios, human-labeled datasets, judge alignment and synthetic questions. [Buildcamp evaluation](https://github.com/alexeygrigorev/ai-bootcamp/tree/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/06-evaluation)
- The AI Engineering Field Guide identifies evaluation as a differentiating skill in AI-first roles. Its portfolio guide recommends a small case set that includes messy questions, missing evidence and citations.

## Exercise adapted from the Buildcamp

Adapt the recipe-assistant exercise to speaker questions and ticket drafts. Label claims using the handbook, inspect disagreements with a judge, and freeze the revised rubric. On fresh cases, compare which version retrieved evidence, answered correctly and completed the requested task. Keep the results keyed by case ID so an instructor can trace a score back to its evidence. [Buildcamp Week 6 homework](https://github.com/alexeygrigorev/ai-bootcamp/blob/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/06-evaluation/homework/01-homework.md)

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 12.1 | Building a Benchmark for Handbook Questions | LZ `04-evaluation/01-intro.md`, `02-ground-truth.md`. BC Week 6 `02-measure/04-gold-standard-dataset.md` |
| 12.2 | Generating and Reviewing Synthetic Questions | BC `03-synthetic-data/02-generating-questions.md` |
| 12.3 | Measuring Retrieval Quality | LZ `04-search-evaluation.md` and `05-search-metrics.md` |
| 12.4 | Scoring Grounded Answers and Calibrating the Judge | LZ `12-rag-answers.md` and `13-llm-as-judge.md`. BC `02-measure/05-judge-alignment.md` |
| 12.5 | Defining Success for Agent Tasks | LZ `14-agent-evaluation.md`. BC `02-measure/03-running-scenarios.md` |
| 12.6 | Replaying Agent Scenarios and Inspecting Tool State | BC `02-measure/03-running-scenarios.md` and `06-running-evals.md` |
| 12.7 | Measuring Task Success and Analyzing Failures | LZ `14-agent-evaluation.md`. BC `02-measure/06-running-evals.md` |
| 12.8 | Comparing Assistant Versions before Release | LZ `06-search-tuning.md`. BC `03-synthetic-data/04-judging-synthetic-data.md` |

## Detailed lesson outline

**Part 1. Evaluating handbook retrieval and answers**

### 12.1 Building a Benchmark for Handbook Questions

Start with a release report in which both versions pass the deadline regression test, but one retrieves the wrong section for several paraphrases. Trace one report row to its source. Turn the course 11 examples into labeled cases with a case ID, question, expected fact or abstention, and acceptable handbook section IDs. A speaker rating helps select a case. A human checks its label against the frozen handbook.

**Check.** Label the final-slides deadline and the unanswered travel-reimbursement question. Explain which one belongs in the retrieval hit-rate denominator and how to score the other answer.

### 12.2 Generating and Reviewing Synthetic Questions

Ask for paraphrases and harder questions from a handbook passage. Review the generated questions and reference answers for ambiguity, near-duplicates and invented facts. Group accepted variants by the underlying request before reserving families for a final comparison.

**Check.** Reject a candidate that assumes travel reimbursement and correct a reference answer that confuses draft and final deadlines. Verify that all variants of a single underlying request stay on one side of the split.

### 12.3 Measuring Retrieval Quality

Run both retrievers on the labeled lookup cases. Record the rank of the first acceptable section within the top three results. Calculate hit rate@3 and mean reciprocal rank@3, giving a miss zero credit.

**Check.** For three answerable cases whose first relevant sections rank first, third, and outside the top three, derive a hit rate of 2/3 and an MRR of 4/9. Inspect a case whose section moved up even though its hit indicator stayed the same.

### 12.4 Scoring Grounded Answers and Calibrating the Judge

Label answer correctness against the reference fact, and grounding against the passages actually supplied to the model. Score abstention separately on unanswered cases. Reuse the claim rubric from course 10. Inspect human–judge disagreements on a calibration sample, revise the rubric, and measure agreement on untouched labels.

**Check.** Score one answer that gives the correct final deadline after retrieving only draft instructions and one that invents a deadline extension. Show a false pass by the judge and report held-out agreement as a count and denominator.

**Part 2. Evaluating complete agent tasks**

### 12.5 Defining Success for Agent Tasks

For “When are slides due?”, success means a supported answer. For “Draft a support ticket asking for a later rehearsal,” it means a usable local draft reflecting the speaker's request. For an ambiguous ticket request, the expected outcome is a clarification with no draft created. Give each scenario its starting state, allowed actions and observable end condition.

**Check.** Compare two valid paths to the same draft, then score a third run whose reply says “I drafted it” but leaves the draft store empty. Identify which evidence settles each outcome.

### 12.6 Replaying Agent Scenarios and Inspecting Tool State

Reset the local tool store before each scenario. Run the baseline and candidate against the same scripted inputs and record the reply, tool events, and resulting draft state for each version. Use the frozen answer rubric for question-answering tasks and direct state checks for draft creation.

**Check.** Reverse execution order and rerun two cases with the same starting state. Their success labels must remain the same. Flag a duplicate draft even though the final reply reads correctly.

### 12.7 Measuring Task Success and Analyzing Failures

Compute success separately for lookups, unsupported questions, and draft or clarification requests. For failed cases, follow the tool records and retrieved passages to identify the first consequential mistake: a missed source, an unsupported claim, or an incorrect tool action.

**Check.** Report a numerator and denominator for each task group. Identify two failed requests that sound equally confident but require different fixes. Show the evidence behind each diagnosis.

### 12.8 Comparing Assistant Versions before Release

Compare the two versions on the held-out cases with the same handbook, starting tool state, and frozen rubric. Join outcomes by case ID. Report retrieval rank, answer quality, task success, cost and latency. Apply release criteria supplied before scoring, including a minimum draft-task success rate.

**Check.** Make a ship-or-hold decision on a fixture where better retrieval conceals a decline in correct drafts. Show the threshold calculation and a changed case that explains it. Save the per-version counts, denominators and threshold results in a machine-readable report for CI.
