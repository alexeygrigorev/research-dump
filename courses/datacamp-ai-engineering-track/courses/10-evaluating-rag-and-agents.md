# 10. Evaluating RAG and Agents

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 4. Quality. 7 lessons, 2–3 hours.

## Summary

Tests say whether something broke; evaluation says how good the system is. **Evaluation is the #1 hiring differentiator** in the field guide: **61.8%** of AI-First roles require evaluation skills (climbing from 55.9% in Feb to **69.3%** in Nov), and LLM-native eval tooling rose from 26.7% to 34.5%. Learners build golden and synthetic datasets, measure retrieval and answer quality (including faithfulness/hallucinations), align an LLM judge with human labels, and compare system versions.

## Learning objectives

- Build an evaluation dataset from real and synthetic questions
- Measure retrieval quality and answer quality (including faithfulness/hallucinations) separately
- Create an LLM judge and check its agreement with human labels
- Run an evaluation over two versions of a system and decide which one ships

## Why here

Follows testing (judges are already familiar) and directly addresses the market's #1 differentiator before online monitoring, where the same judges run on live traffic.

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

- **FG** (AI Engineering Field Guide, 9,760 jobs): Evaluation #1 differentiator (61.8% AI-First → 69.3% Nov), LLM Evaluation 33.5% AI-First (20.3% → 26.6% overall), LLM-native eval tooling (LangSmith, Langfuse, LLM Evaluation) 26.7% → 34.5%
- **LZ**: LLM Zoomcamp (`github.com/DataTalksClub/llm-zoomcamp`) Module 4 Evaluation (all lessons)
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 6: Measure: Offline Evaluation for Agents, Synthetic Evaluation Data

### Notes

Dataset sizes must stay small (tens of questions) to keep API cost and run time inside a 20–30 minute lesson; a pre-computed larger result file can be provided for analysis. Also introduces how LLM-native eval workflows (e.g., Langfuse/LangSmith-style dataset & experiment tables) replace classic MLOps eval tools.

## Lesson outline and source map

FG = AI Engineering Field Guide, LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. `'new'` = no lesson in LZ or BC.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 10.1 | Why evaluate: offline, online and LLM-native evals | LZ `04-evaluation/01-intro.md`, `11-evaluation-intro.md`; FG Eval (69.3% Nov) |
| 10.2 | Ground truth and synthetic questions | LZ `02-ground-truth.md`, `03-ground-truth-batch.md`; BC `v2/06-evaluation/03-synthetic-data/02-generating-questions.md` |
| 10.3 | Evaluating retrieval | LZ `04-search-evaluation.md`, `05-search-metrics.md` |
| 10.4 | Evaluating answers and faithfulness | LZ `12-rag-answers.md`; BC `v2/06-evaluation/02-measure/04-gold-standard-dataset.md` |
| 10.5 | LLM as a judge and judge alignment | LZ `13-llm-as-judge.md`; BC `02-measure/05-judge-alignment.md` |
| 10.6 | Evaluating agents on scenarios | LZ `14-agent-evaluation.md`; BC `02-measure/03-running-scenarios.md`, `06-running-evals.md` |
| 10.7 | Using results to choose a version | LZ `06-search-tuning.md`; BC `03-synthetic-data/04-judging-synthetic-data.md` |
