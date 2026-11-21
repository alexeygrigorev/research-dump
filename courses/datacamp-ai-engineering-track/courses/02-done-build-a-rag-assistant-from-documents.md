# 2. Build a RAG Assistant from Documents - DONE

Part of the [DataCamp AI Engineering track plan](../README.md). Stage: 1. Foundations. 6 lessons, 2-3 hours. Each lesson is designed for approximately 20-25 minutes.

## Summary

Learners build a retrieval-augmented generation pipeline over a collection of documents. They load and chunk text, retrieve relevant passages, and generate answers grounded in those passages. They learn to preserve citations and recognize questions the available evidence cannot answer.

## Learning objectives

- Load and chunk documents while retaining source metadata
- Build a keyword-search index and inspect its results
- Construct prompts grounded in retrieved context
- Return cited answers or identify insufficient evidence

## Why here

Builds on API calls by adding document retrieval, creating a baseline for semantic search.

## Transformation

From "I can ask a model about one passage" to "I can build a pipeline that finds and cites relevant documents."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Markdown frontmatter, section splitting, chunk size and overlap, source IDs, JSONL, MinSearch keyword indexing, and grounded prompt templates.

### How it's used in the exercises

Learners start with the fictional conference speaker handbook introduced in course 1. They load and chunk the Markdown, build an index, and connect retrieval to a prompt that generates cited answers.

### Model / release

Python 3.13. `openai==3.57.0`, `pydantic==2.14.4`, `minsearch==0.2.0`. Use DataCamp-funded model API calls. Select the lowest-cost available model that meets the exercise criteria; no fixed model release is required.

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): RAG 40.1% overall (56.0% AI-First, rising 32.8% → 38.2%), Finding Information in Company Data 32.5% of jobs (3,899 mentions; 28.3% → 31.7% Feb to Nov), RAG app builder archetype 26.6%
- **FG learning paths / portfolio** (`learning-paths/README.md`, `portfolio/`, commit `1556dcb2`): "RAG and Search" block; "RAG patterns" are "must have". The FG practice projects (FAQ assistant, document Q&A) match the running example.
- **LZ**: LLM Zoomcamp (`github.com/DataTalksClub/llm-zoomcamp`) Module 1 Agentic RAG, lessons 03-10
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 1: Foundation: LLMs, RAG and Search; Week 2: FAQ Assistant, Reusable RAG class

### Notes

MinSearch runs in memory. Bundle Markdown pages covering slide submission, rehearsal scheduling, and speaker check-in. Give each section a stable source ID that can be cited after re-chunking. Reuse these IDs in course 3.

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 2.1 | Introduction to RAG | LZ `01-agentic-rag/03-rag.md`; BC `v2/01-foundation/03-rag/04-rag.md` |
| 2.2 | Document Loading and Chunking | BC `v2/01-foundation/03-rag/05-getting-documentation-data.md`, `07-chunking-documents.md` |
| 2.3 | Chunk Size and Overlap | BC `v2/01-foundation/03-rag/07-chunking-documents.md`; LZ `07-project-example/07-chunking.md` |
| 2.4 | Keyword Search Indexing | LZ `01-agentic-rag/05-search.md`; BC `v2/01-foundation/03-rag/06-indexing-with-minsearch.md` |
| 2.5 | Grounded Answers and Citations | LZ `01-agentic-rag/06-building-prompt.md`, `07-llm.md` |
| 2.6 | Building a RAG Pipeline | LZ `01-agentic-rag/08-rag-helper.md`; BC `v2/02-rag-usecases-tech/01-overview/02-rag-class.md` |

## Detailed lesson outline

### 2.1 Introduction to RAG

Give learners the “Draft Slides,” “Final Slides,” and “Speaker Check-in” sections. A speaker asks where to upload the final deck. Select the passage that should go into the request from course 1. Inspect a worked RAG call and locate where search made that selection.

**Check.** Match the retrieved section, the text included in the prompt, and the sentence that supports the upload destination. Explain what would go wrong if search returned only “Draft Slides.”

### 2.2 Document Loading and Chunking

Read the fictional conference’s Markdown handbook and its frontmatter. Split it by headings and preserve the document ID, section ID, and heading path for sections such as “Draft Slides,” “Final Slides,” and “Speaker Check-in.”

**Check.** Trace a split section to its original heading and confirm that its ID survives export and reload.

### 2.3 Chunk Size and Overlap

Chunk a longer submission section with a fixed window. Its deadline and upload instructions fall on opposite sides of a boundary. Try a larger window, then restore the original size and add overlap. Give each chunk its own ID and keep the parent section ID for citations.

**Check.** Select a configuration that returns both facts in one chunk within a supplied length limit. Show the evidence and how much repeated text the overlap introduced.

### 2.4 Keyword Search Indexing

Build a MinSearch index on chunk titles and text. Query where to upload final slides and inspect the ranked source IDs.

**Check.** Verify that “Final Slides” ranks above “Draft Slides” on the supplied query.

### 2.5 Grounded Answers and Citations

Write an answer function that takes a question and retrieved chunks as inputs. Format each passage with its section ID. Ask the model to cite the supporting section and to say when the passages give insufficient information. Try the function with final-slide instructions, then with irrelevant passages for a travel reimbursement question.

**Check.** Inspect the formatted prompt and two recorded answers. Accept a deadline answer only if the cited passage supports the date. For reimbursement, identify the answer that leaves the question open.

### 2.6 Building a RAG Pipeline

Implement `ask_handbook(question)` by passing the question to the index from lesson 2.4 and its results to the answer function from 2.5. A second speaker asks about check-in. The function should now find the check-in instructions without anyone selecting a passage for it.

**Check.** Run slide submission, check-in, and reimbursement questions against the bundled index and a recorded model. Inspect the chunks passed to generation on each call. Verify that the first two answers cite their respective sections and the third reports insufficient information.
