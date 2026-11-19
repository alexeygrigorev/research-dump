# 13. Evaluating RAG and Agents

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 4. Application quality. 7 lessons, 2-3 hours.

## Summary

Tests say whether something broke; evaluation says how good the system is. **Evaluation is the #1 hiring differentiator** in the field guide: **61.8%** of AI-First roles require evaluation skills (climbing from 55.9% in Feb to **69.3%** in Nov), and LLM-native eval tooling rose from 26.7% to 34.5%. Learners build golden and synthetic datasets, measure retrieval and answer quality (including faithfulness/hallucinations), align an LLM judge with human labels, and compare system versions.

## Learning objectives

- Build an evaluation dataset from real and synthetic questions
- Measure retrieval quality and answer quality (including faithfulness/hallucinations) separately
- Create an LLM judge and check its agreement with human labels
- Run an evaluation over two versions of a system and decide which one ships

## Why here

Uses the tests and traces from the preceding courses. Learners turn representative trace examples into offline scenarios, then measure changes before they reach deployment.

## Transformation

From "the answers look fine to me" to "I can measure how good my application is and prove that a change improved it."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Ground-truth generation with an LLM, batch runs over a dataset, hit rate/MRR, LLM-as-a-judge with structured output (faithfulness, relevance, correctness), judge-vs-human agreement, comparing prompts and models in a results table

### How it's used in the exercises

The learner generates synthetic questions for documents, runs two prompt/model variants over them, hand-labels a small sample, writes a judge, checks where the judge disagrees with their labels and fixes the judge prompt, then picks the winning version from the evaluation table.

### Model / release

Python 3.13; `pandas>=3.0.3`, `openai>=2.38.0`, `langgraph` / `pydantic-ai>=1.55.0`, `tqdm>=4.67.3`, `minsearch>=0.1.0`. Cheap model for generation; the judge model is a lesson topic.

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): Evaluation #1 differentiator (61.8% AI-First → 69.3% Nov), LLM Evaluation 33.5% AI-First (20.3% → 26.6% overall), LLM-native eval tooling (LangSmith, Langfuse, Guardrails, LLM Evaluation) 26.7% → 34.5%, Evaluation and quality in 71.3% of jobs' responsibilities (12,132 mentions)
- **FG learning paths / portfolio** (`learning-paths/README.md`, `portfolio/`, commit `1556dcb2`): "Evaluation" block (offline evaluation, retrieval evaluation, synthetic data, prompt optimization from eval results). `portfolio/04-polishing.md`: start with 20-50 cases covering easy, messy, out-of-scope, refusal and citation cases, and save dated results in the repo.
- **LZ**: LLM Zoomcamp (`github.com/DataTalksClub/llm-zoomcamp`) Module 4 Evaluation (all lessons)
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 6: Measure: Offline Evaluation for Agents, Synthetic Evaluation Data

### Notes

Dataset sizes must stay small (tens of questions) to keep API cost and run time inside a 20-30 minute lesson; a pre-computed larger result file can be provided for analysis. Also introduces how LLM-native eval workflows (e.g., Langfuse/LangSmith-style dataset & experiment tables) replace classic MLOps eval tools.

## Exercise adapted from the Buildcamp

Adapt the recipe assistant homework to a batch of internal knowledge requests. Learners label a small set of fixed answers, compare their labels with a judge’s verdicts, and revise the rubric after inspecting disagreements. Provide a separate labeled set to check whether agreement improves. Use the checked rubric to compare two assistant versions on the same scenarios.

[Buildcamp Week 6 source](https://github.com/alexeygrigorev/ai-bootcamp/blob/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/06-evaluation/homework/01-homework.md)

## Lesson outline and source map

FG = AI Engineering Field Guide, LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. `'new'` = no lesson in LZ or BC.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 13.1 | Why evaluate: offline, online and LLM-native evals | LZ `04-evaluation/01-intro.md`, `11-evaluation-intro.md`; FG Eval (69.3% Nov) | too long
| 13.2 | Ground truth and synthetic questions | LZ `02-ground-truth.md`, `03-ground-truth-batch.md`; BC `v2/06-evaluation/03-synthetic-data/02-generating-questions.md` | split into GT and synthetic data see AI BC 
| 13.3 | Evaluating retrieval | LZ `04-search-evaluation.md`, `05-search-metrics.md` | 
| 13.4 | Evaluating answers | LZ `12-rag-answers.md`; BC `v2/06-evaluation/02-measure/04-gold-standard-dataset.md` | more concrete
| 13.5 | LLM as a judge and judge alignment | LZ `13-llm-as-judge.md`; BC `02-measure/05-judge-alignment.md` | split or rename
| 13.6 | Evaluating agents on scenarios | LZ `14-agent-evaluation.md`; BC `02-measure/03-running-scenarios.md`, `06-running-evals.md` | i thikn it's more like testing? 
| 13.7 | Using results to choose a version | LZ `06-search-tuning.md`; BC `03-synthetic-data/04-judging-synthetic-data.md` | better title

## Detailed lesson outline

### 13.1 Why evaluate: offline, online and LLM-native evals

Review a fixed benchmark, user feedback, and a production trace. Decide which evidence answers an offline or online quality question.

**Check.** Match each evidence source to the decision it can support.

### 13.2 Ground truth and synthetic questions

Add human-labeled and synthetic queries to a small dataset with expected answers and source IDs.

**Check.** Spot-check a generated query against its assigned source before admitting it.

### 13.3 Evaluating retrieval

Run retrieval against the dataset and calculate hit rate and mean reciprocal rank.

**Check.** Verify metrics against a fixture with known ranks and inspect a missed source.

### 13.4 Evaluating answers and faithfulness

Score answers for correctness and support from retrieved text.

**Check.** Identify a fluent answer that makes a claim outside its cited passage.

### 13.5 LLM as a judge and judge alignment

Compare an LLM judge with human labels and revise its rubric after examining disagreements.

**Check.** Check agreement on a held-out set after the revision.

### 13.6 Evaluating agents on scenarios

Replay multi-step agent requests with expected tool calls and approval behavior.

**Check.** Check both final outputs and intermediate steps for a saved run.

### 13.7 Using results to choose a version

Compare two versions on a common dataset with quality, cost, and latency results.

**Check.** Choose a version using stated criteria and point to specific cases that influenced the decision.
