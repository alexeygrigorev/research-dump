# 4. Processing PDFs with LLMs

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 2. Retrieval and document processing. 6 lessons, 2-3 hours.

## Summary

The conference organizer needs a submission checklist from the PDF edition of the speaker handbook. Learners recover slide and bio instructions from prose and a deadline table, extract typed records across the handbook, and trace each item on the checklist to its source.

## Learning objectives

- Extract text from a PDF and check table rows against the rendered handbook
- Reassemble a submission instruction that crosses a page break
- Use structured output and supporting excerpts to verify deliverables, deadlines, and upload destinations
- Process independent sections concurrently and use the resulting records to build a deadline checklist

## Why here

The Markdown handbook supplied headings and source IDs. Its PDF edition puts some of the same facts in table cells or across page breaks. Learners need to recover those relationships before trusting a parsed date, a skill they will use again on invoices in the capstone.

## Transformation

From having a PDF to having validated records that can be traced back to the supporting excerpts.

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

PyMuPDF text and table extraction, Pydantic schemas, structured output, bounded thread pools, and JSONL.

### How it's used in the exercises

Learners extract sections from the conference speaker handbook PDF and check them against the rendered document. They adapt the deliverable schema from course 1, process sections in parallel, and use the saved records to show an organizer what is due and which dates still need confirmation.

### Model / release

Python 3.13, `pymupdf>=1.26.7`, `openai>=2.38.0` and Pydantic. Use a small OpenAI model with structured output for the demonstration and recorded responses for grading.

### Source material

- **BC**: Week 2 Books module, PDF extraction, structured output, processing all pages and parallel processing. Week 1 document processing homework supplies the exercise pattern.
- **FG**: Document processing rose from 13.3% to 16.0% of postings between February and November.

### Notes

Bundle a text-based PDF with a ruled deadline table, a submission instruction continued on the next page, and a blank page. Supply the matching handbook section IDs and recorded model calls for grading.

## Exercise adapted from the Buildcamp

The Buildcamp’s books chapter extracts one page into a schema, processes the book, then uses the stored results. For the speaker handbook, process one submission section at a time so a page break cannot separate a deadline from its destination. The organizer’s checklist is the test of whether the stored facts are usable.

[Buildcamp PDF extraction homework](https://github.com/alexeygrigorev/ai-bootcamp/blob/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/01-foundation/homework/01-homework.md) · [Buildcamp parallel processing lesson](https://github.com/alexeygrigorev/ai-bootcamp/blob/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/02-rag-usecases-tech/04-books/07-parallel-processing.md)

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 4.1 | PDF Extraction with PyMuPDF | `v2/02-rag-usecases-tech/04-books/02-extracting-text-from-pdfs.md` |
| 4.2 | Extracting PDF Tables | `v2/02-rag-usecases-tech/04-books/02-extracting-text-from-pdfs.md` (layout motivates extraction checks); new table exercise |
| 4.3 | Extraction with Source Evidence | `v2/02-rag-usecases-tech/04-books/03-structured-output.md` |
| 4.4 | Handling Page Breaks | `v2/02-rag-usecases-tech/04-books/06-processing-all-pages.md` (whole-document pass); new continuation exercise |
| 4.5 | Parallel Extraction | `v2/02-rag-usecases-tech/04-books/07-parallel-processing.md` |
| 4.6 | Storing Extracted Records | `v2/02-rag-usecases-tech/04-books/08-rag.md` (reuse stored records); new checklist exercise |

## Detailed lesson outline

### 4.1 PDF Extraction with PyMuPDF

Open the PDF edition with PyMuPDF, extract text from each page, and retain its order and document ID. Compare an ordinary paragraph, a blank page, and the submission table with the rendered PDF.

**Check.** Locate the final-slides heading and identify which extract needs its row order checked before the text can be used.

### 4.2 Extracting PDF Tables

The organizer spots a draft deadline next to the final-slides label in a flattened text extract. Read the ruled table as rows with PyMuPDF, remove its repeated header, and keep the deliverable beside its own deadline. Compare both rows with the rendered table.

**Check.** Recover both draft and final deadlines, including October 15, 2027 for final slides. A result that swaps two valid dates fails this check.

### 4.3 Extraction with Source Evidence

Apply the deliverable schema from course 1 to the recovered table rows and the bio instructions. Add the section ID in Python and ask for the supporting text alongside the extracted fields. Compare parsed records with the source to catch a validly formatted date assigned to the wrong deliverable.

**Check.** Identify the unsupported date in a pair of schema-valid records, match the correct one to its row, and leave the bio deadline empty where the handbook omits it.

### 4.4 Handling Page Breaks

The final-slides instructions start near the bottom of a page and the portal destination continues on the next. Walk the pages in order, drop the repeated running header, and append continuation text to the current section until the next section heading. Run the extractor on each complete section.

**Check.** Recover one final-slides deliverable with both its deadline and its destination. Confirm that the blank page produces no deliverable and the following section keeps its own ID.

### 4.5 Parallel Extraction

Run the model calls on the prepared sections with a small thread pool. Let one recorded request fail while the others finish. Attach the section ID to each result as it arrives and rerun the failed section.

**Check.** Use a recorded run to compare sequential and overlapping calls. Deliver results in a different order and verify that the records still match their sources and only the failed section is submitted twice.

### 4.6 Storing Extracted Records

The organizer asks which materials are due by October 16, 2027 and which still need a confirmed date. Save the extracted records as JSONL and reload them. Join the deadline-table rows to the submission instructions by deliverable, keeping the source excerpt for each field. Show one checklist item per deliverable and group the undated items separately.

**Check.** Find final slides once on the dated list and the speaker bio among the undated items. Follow the final-slides entry back to the PDF to verify both the deadline and the portal destination.
