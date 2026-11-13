# 3. Preparing Data for RAG

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 2. Retrieval. 7 lessons, 2–3 hours.

## Summary

Real enterprise knowledge bases are documentation sites, transcripts and PDFs, not clean FAQ files (document processing rose from 13.3% to 16.0% of jobs; data and pipelines responsibilities jumped +10.0 pp to 29.7%). Learners ingest these sources, split them into chunks, use an LLM to clean and structure the content, and store it in a persistent index.

## Learning objectives

- Load documentation, transcripts and PDF text into a common document format
- Chunk long documents and judge how chunk size and overlap affect retrieval
- Use structured output to extract clean, typed records from messy content
- Process many documents in parallel and persist the index between runs

## Why here

Course 2 used a ready-made dataset; before improving search, learners need the data-ingestion and document-processing pipeline that real jobs require.

## Transformation

From "my assistant works on a prepared dataset" to "I can turn raw enterprise documents into a searchable knowledge base."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Markdown/frontmatter parsing, sliding-window chunking, section-based chunking, PyMuPDF text extraction, structured output for page/transcript records, `concurrent.futures` thread pools, `sqlitesearch` persistent index

### How it's used in the exercises

The learner parses a folder of markdown docs, compares search results before and after chunking, extracts text from a PDF chapter and structures it with an LLM, runs the processing over all pages in parallel, and saves the result to a SQLite-backed index.

### Model / release

Python 3.13; `python-frontmatter>=1.1.0`, `pymupdf>=1.26.7`, `sqlitesearch>=0.0.5`, `minsearch>=0.1.0`, `openai>=2.38.0`, `tqdm>=4.67.3`. Cheapest model with structured output.

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): Document Processing 13.3% → 16.0%, Data and Pipelines responsibilities 19.7% → 29.7% (+10.0 pp), SQL 14.6% (rising 11.1% → 14.9%)
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 1: Getting data from GitHub, Chunking documents; Week 2: YouTube Transcripts, Books
- **LZ**: LLM Zoomcamp (`github.com/DataTalksClub/llm-zoomcamp`) `01-agentic-rag/09-data-ingestion.md`; `07-project-example/07-chunking.md`; workshop `cohorts/2026/workshops/dlt.md`

### Notes

Source lessons download from GitHub and YouTube; here the raw files (docs, one transcript, one PDF) must be bundled with the course. The `dlt` workshop is listed as optional source only.

## Lesson outline and source map

FG = AI Engineering Field Guide, LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. `'new'` = no lesson in LZ or BC.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 3.1 | From raw files to documents | BC `v2/01-foundation/03-rag/05-getting-documentation-data.md`; LZ `01-agentic-rag/09-data-ingestion.md` |
| 3.2 | Chunking documents | BC `03-rag/07-chunking-documents.md`; LZ `07-project-example/07-chunking.md` |
| 3.3 | Transcripts: long unstructured text | BC `v2/02-rag-usecases-tech/03-youtube/02–05` |
| 3.4 | PDFs: extracting text | BC `v2/02-rag-usecases-tech/04-books/02-extracting-text-from-pdfs.md`; FG Document Processing (16.0%) |
| 3.5 | Structuring content with an LLM | BC `04-books/03-structured-output.md`; `03-youtube/04-structured-output.md` |
| 3.6 | Processing everything in parallel | BC `04-books/06-processing-all-pages.md`, `07-parallel-processing.md` |
| 3.7 | Persistent indexes | BC `04-books/09-external-databases.md`, `10-persistent-rag.md` |
