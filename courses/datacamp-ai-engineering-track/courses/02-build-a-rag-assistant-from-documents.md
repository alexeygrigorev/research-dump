# 2. Build a RAG Assistant from Documents

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 1. Foundations. 6 lessons, 2-3 hours.

## Summary

In course 1, someone had to find the handbook excerpt before the model could answer. Here learners build a retrieval-augmented generation (RAG) assistant that finds the relevant sections itself, cites them in its answer, and tells the speaker when the handbook leaves a question open.

## Learning objectives

- Trace an answer to the passage retrieved for a speaker’s question
- Load Markdown, chunk it while preserving source metadata, and index it for keyword search
- Build a prompt that grounds the answer in retrieved context
- Assemble search, prompt and LLM into one reusable RAG pipeline

## Why here

Learners already know how to ask a model a question about one passage. Searching the full handbook gives them a working keyword baseline for the vector search course.

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

MinSearch runs in memory. Bundle Markdown pages covering slide submission, rehearsal scheduling, and speaker check-in. Give each section a stable source ID that can be cited after re-chunking. Reuse these IDs in course 3.

## Exercise adapted from the Buildcamp

Have learners split the speaker handbook into chunks, index them with MinSearch, and assemble a prompt from the retrieved chunks. Grade the retrieved entry IDs and prompt context with fixed fixtures. Include an unanswered question so learners can check how the assistant responds when its sources are insufficient.

[Buildcamp Week 1 source](https://github.com/alexeygrigorev/ai-bootcamp/blob/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/01-foundation/homework/01-homework.md)

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 2.1 | Answering a Question from the Handbook | LZ `01-agentic-rag/03-rag.md`; BC `v2/01-foundation/03-rag/04-rag.md` |
| 2.2 | Loading and Chunking the Speaker Handbook | BC `v2/01-foundation/03-rag/05-getting-documentation-data.md`, `07-chunking-documents.md` |
| 2.3 | Choosing Chunk Size and Overlap | BC `v2/01-foundation/03-rag/07-chunking-documents.md`; LZ `07-project-example/07-chunking.md` |
| 2.4 | Indexing Handbook Chunks | LZ `01-agentic-rag/05-search.md`; BC `v2/01-foundation/03-rag/06-indexing-with-minsearch.md` |
| 2.5 | Generating Answers with Citations | LZ `01-agentic-rag/06-building-prompt.md`, `07-llm.md` |
| 2.6 | Putting the RAG Pipeline Together | LZ `01-agentic-rag/08-rag-helper.md`; BC `v2/02-rag-usecases-tech/01-overview/02-rag-class.md` |

## Detailed lesson outline

### 2.1 Answering a Question from the Handbook

Give learners the “Draft Slides,” “Final Slides,” and “Speaker Check-in” sections. A speaker asks where to upload the final deck. Select the passage that should go into the request from course 1. Inspect a worked RAG call and locate where search made that selection.

**Check.** Match the retrieved section, the text included in the prompt, and the sentence that supports the upload destination. Explain what would go wrong if search returned only “Draft Slides.”

### 2.2 Loading and Chunking the Speaker Handbook

Read the fictional conference’s Markdown handbook and its frontmatter. Split it by headings and preserve the document ID, section ID, and heading path for sections such as “Draft Slides,” “Final Slides,” and “Speaker Check-in.”

**Check.** Trace a split section to its original heading and confirm that its ID survives export and reload.

### 2.3 Choosing Chunk Size and Overlap

Chunk a longer submission section with a fixed window. Its deadline and upload instructions fall on opposite sides of a boundary. Try a larger window, then restore the original size and add overlap. Give each chunk its own ID and keep the parent section ID for citations.

**Check.** Select a configuration that returns both facts in one chunk within a supplied length limit. Show the evidence and how much repeated text the overlap introduced.

### 2.4 Indexing Handbook Chunks

Build a MinSearch index on chunk titles and text. Query where to upload final slides and inspect the ranked source IDs.

**Check.** Verify that “Final Slides” ranks above “Draft Slides” on the supplied query.

### 2.5 Generating Answers with Citations

Write an answer function that takes a question and retrieved chunks as inputs. Format each passage with its section ID. Ask the model to cite the supporting section and to say when the passages give insufficient information. Try the function with final-slide instructions, then with irrelevant passages for a travel reimbursement question.

**Check.** Inspect the formatted prompt and two recorded answers. Accept a deadline answer only if the cited passage supports the date. For reimbursement, identify the answer that leaves the question open.

### 2.6 Putting the RAG Pipeline Together

Implement `ask_handbook(question)` by passing the question to the index from lesson 2.4 and its results to the answer function from 2.5. A second speaker asks about check-in. The function should now find the check-in instructions without anyone selecting a passage for it.

**Check.** Run slide submission, check-in, and reimbursement questions against the bundled index and a recorded model. Inspect the chunks passed to generation on each call. Verify that the first two answers cite their respective sections and the third reports insufficient information.
