# 3. Preparing Data for RAG

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 2. Retrieval and document processing. 5 lessons, 2-3 hours.

## Summary

Learners turn the fictional IT help desk's Markdown documentation into the searchable records used by the RAG assistant. They normalize content, preserve source references and test how chunk boundaries affect retrieval.

## Learning objectives

- Load Markdown documents and frontmatter into a common record format
- Split documentation by section or with a sliding window
- Preserve stable document and chunk IDs along with headings and source references
- Export valid chunk records and compare retrieval on two chunking configurations

## Why here

Learners start with pre-chunked FAQ entries in the previous course. Here they build the data preparation step needed when new documentation arrives.

## Transformation

From loading prepared FAQ entries to producing searchable, citable records from raw documentation.

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Markdown and frontmatter parsing, document metadata, section-aware chunking, sliding windows with overlap, JSONL export, and retrieval with an in-memory MinSearch index.

### How it's used in the exercises

Learners load a bundled folder of help desk policy and troubleshooting pages, split a long section with a sliding window, and attach stable IDs and source headings. They export the records and inspect which chunks are retrieved for a small fixed query set.

### Model / release

Python 3.13, `python-frontmatter>=1.1.0` and `minsearch>=0.1.0`. The exercise compares search results using the existing keyword index.

### Source material

- **FG**: Document processing rose from 13.3% to 16.0% of postings between February and November. The RAG and Search learning path covers preparing and chunking source documents.
- **BC**: Week 1, getting documentation data and chunking documents.
- **LZ**: `01-agentic-rag/09-data-ingestion.md` and `07-project-example/07-chunking.md`.

### Notes

Bundle the raw Markdown pages, expected JSONL record schema, and a fixed query set with expected source sections.

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 3.1 | Load Markdown documentation and frontmatter | BC `v2/01-foundation/03-rag/05-getting-documentation-data.md`; LZ `01-agentic-rag/09-data-ingestion.md` |
| 3.2 | Split documents by heading | BC `v2/01-foundation/03-rag/07-chunking-documents.md`; LZ `07-project-example/07-chunking.md` |
| 3.3 | Set chunk size and overlap | BC `v2/01-foundation/03-rag/07-chunking-documents.md` |
| 3.4 | Export chunks with source metadata | BC `v2/01-foundation/03-rag/07-chunking-documents.md`; LZ `01-agentic-rag/09-data-ingestion.md` |
| 3.5 | Check which chunks retrieval returns | BC `v2/01-foundation/03-rag/06-indexing-with-minsearch.md`; LZ `07-project-example/07-chunking.md` |
