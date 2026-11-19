# 2. Build a RAG Assistant from Documents

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 1. Foundations. 6 lessons, 2-3 hours.

## Summary

An LLM does not know your company's internal data. Learners build a retrieval-augmented assistant (RAG appears in 40.1% of all jobs and 56.0% of AI-First roles; finding information in company data is a use case in 32.5% of jobs, up from 28.3% to 31.7% between February and November) over an internal knowledge base: search first, put the results into the prompt, then ask the model.

## Learning objectives

- Explain why RAG is needed for proprietary data and describe its search, prompt and LLM steps
- Load Markdown, chunk it while preserving source metadata, and index it for keyword search
- Build a prompt that grounds the answer in retrieved context
- Assemble search, prompt and LLM into one reusable RAG pipeline

## Why here

RAG is the most common named pattern in AI engineering postings and the running example for retrieval, agents, evaluation and monitoring later in the track.

## Transformation

From "I can call an LLM" to "I can build an assistant that answers questions from proprietary documents."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Markdown frontmatter, section splitting, chunk size and overlap, source IDs, JSONL, MinSearch keyword indexing, and grounded prompt templates.

### How it's used in the exercises

Learners start with the fictional conference speaker handbook introduced in course 1. They load and chunk the Markdown, build an index, and connect retrieval to a prompt that generates cited answers.

### Model / release

Python 3.13; `minsearch>=0.1.0`, `openai>=2.38.0`, `requests>=2.28.1`. Any small chat model.

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): RAG 40.1% overall (56.0% AI-First, rising 32.8% → 38.2%), Finding Information in Company Data 32.5% of jobs (3,899 mentions; 28.3% → 31.7% Feb to Nov), RAG app builder archetype 26.6%
- **FG learning paths / portfolio** (`learning-paths/README.md`, `portfolio/`, commit `1556dcb2`): "RAG and Search" block; "RAG patterns" are "must have". The FG practice projects (FAQ assistant, document Q&A) match the running example.
- **LZ**: LLM Zoomcamp (`github.com/DataTalksClub/llm-zoomcamp`) Module 1 Agentic RAG, lessons 03-10
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 1: Foundation: LLMs, RAG and Search; Week 2: FAQ Assistant, Reusable RAG class

### Notes

`minsearch` is Alexey's small in-memory search library: no server, runs inside the exercise environment. Bundle Markdown pages covering slide submission, rehearsal scheduling, and speaker check-in. Use stable document and section IDs so learners can cite the same sources in later retrieval, agent and evaluation exercises. Include cases with insufficient evidence in the accompanying question set.

## Exercise adapted from the Buildcamp

Have learners split the speaker handbook into chunks, index them with MinSearch, and assemble a prompt from the retrieved chunks. Grade the retrieved entry IDs and prompt context with fixed fixtures. Include an unanswered question so learners can check how the assistant responds when its sources are insufficient.

[Buildcamp Week 1 source](https://github.com/alexeygrigorev/ai-bootcamp/blob/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/01-foundation/homework/01-homework.md)

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 2.1 | Answer a question using a handbook excerpt | LZ `01-agentic-rag/03-rag.md`; BC `v2/01-foundation/03-rag/04-rag.md` |
| 2.2 | Load and chunk the speaker handbook | BC `v2/01-foundation/03-rag/05-getting-documentation-data.md`, `07-chunking-documents.md` |
| 2.3 | Choose chunk size and overlap | BC `v2/01-foundation/03-rag/07-chunking-documents.md`; LZ `07-project-example/07-chunking.md` |
| 2.4 | Index handbook chunks with MinSearch | LZ `01-agentic-rag/05-search.md`; BC `v2/01-foundation/03-rag/06-indexing-with-minsearch.md` |
| 2.5 | Generate answers with citations | LZ `01-agentic-rag/06-building-prompt.md`, `07-llm.md`, `08-rag-helper.md` |
| 2.6 | Debug missed handbook sections | LZ `01-agentic-rag/10-rag-next-steps.md`; BC `v2/01-foundation/03-rag/07-chunking-documents.md` |

## Detailed lesson outline

### 2.1 Answer a question using a handbook excerpt

Ask when final slides are due, then repeat the request with the “Final Slides” excerpt from lesson 1.1. Walk through how retrieval will supply that excerpt automatically.

**Check.** Identify the exact sentence that supports the answer.

### 2.2 Load and chunk the speaker handbook

Read the fictional conference’s Markdown handbook and its frontmatter. Split it by headings and preserve the document ID, section ID, and heading path for sections such as “Draft Slides,” “Final Slides,” and “Speaker Check-in.”

**Check.** Trace a split section to its original heading and confirm that its ID survives export and reload.

### 2.3 Choose chunk size and overlap

Apply two chunk sizes and overlaps to a longer slide-submission section. Inspect where the due date and upload instructions land and keep source IDs alongside each chunk.

**Check.** Show which configuration keeps the full submission instruction together.

### 2.4 Index handbook chunks with MinSearch

Build a MinSearch index on chunk titles and text. Query where to upload final slides and inspect the ranked source IDs.

**Check.** Verify that “Final Slides” ranks above “Draft Slides” on the supplied query.

### 2.5 Generate answers with citations

Build a reusable function that retrieves chunks, formats them with their section IDs, and sends a grounded prompt through the OpenAI API. Ask one question about the slide deadline and one about travel reimbursement, which the handbook does not cover.

**Check.** Check that the deadline answer cites “Final Slides” and that the reimbursement answer reports insufficient evidence.

### 2.6 Debug missed handbook sections

Compare a lookup where chunking separates the due date from the upload instructions with a paraphrase that keyword search misses. Inspect the retrieved text before changing either step.

**Check.** Identify which failure calls for changing the chunking and which motivates the next course on vector search.

purpose for that?
