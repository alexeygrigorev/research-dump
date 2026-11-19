# 9. From Notebooks to Python Projects

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 4. Application quality. 5 lessons, 2–3 hours.

## Summary

A speaker asks “When are my final slides due?” The notebook can answer, but a conference website needs to send that question to a running service. Learners move the assistant into Python, open the handbook index saved in course 3, and turn the answer function into an HTTP endpoint. By the last lesson another program can send a question to the container and read its answer and sources.

## Learning objectives

- Move the assistant's tools and answer function into importable modules
- Load the prepared handbook index and its matching query embedder in a fresh process
- Accept a question and return a cited answer through FastAPI
- Reproduce the service with a uv lockfile and a Docker image

## Why here

Learners have built several ways to orchestrate tools. Use the LangChain assistant from course 6, including its handbook, rehearsal schedule, and local ticket-draft tools. The deadline lookup gives learners a single request to follow through every packaging step. The project becomes the application under test in course 10.

## Transformation

Learners can give a teammate a checkout and a request example that works even after the notebook kernel has stopped.

## Theory or application

Application

## Build details

### Syntax / functionality involved

Python packages and imports, a read-only SQLite handbook index, a local query embedder, FastAPI, Pydantic, HTTP requests, `pyproject.toml`, `uv.lock`, Docker.

### How it's used in the exercises

Supply a working notebook, a prebuilt handbook index, its matching local embedding model, and a recorded model client for sample speaker questions. Reuse the small schedule and draft store from course 6. Learners keep the real search and fetch tools in the request path. Only the model's choices and final wording are replayed. The index and embedder ship with the example so a clean run can retrieve evidence without downloading a model.

### Model / release

Python 3.13, uv, FastAPI, Uvicorn, Pydantic, sqlitesearch, and the assistant's existing model client. A provided Python environment supports the first three lessons while learners develop the service.

### Source material

The ML Zoomcamp workshop takes a churn prediction from a notebook to a Python script, an HTTP service, a locked environment, and a container. Here the saved file is the searchable handbook, and the request is a speaker question. The Buildcamp supplies the assistant-to-package example. [ML Zoomcamp Module 5 workshop](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/main/05-deployment/workshop) · [Buildcamp project preparation](https://github.com/alexeygrigorev/ai-bootcamp/tree/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/04-testing/02-preparing-project)

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 9.1 | Moving the Assistant from a Notebook to a Python Script | ML Zoomcamp Module 5 workshop, starter notebook and script conversion. BC Week 4, converting to a project |
| 9.2 | Loading the Handbook Index at Startup | ML Zoomcamp 5.2, saving and loading. Course 3.7, persistent SQLite search |
| 9.3 | Serving Answers with FastAPI | ML Zoomcamp workshop, `predict.py` and `test.py`. BC Week 4, structured output |
| 9.4 | Locking Python Dependencies with uv | ML Zoomcamp workshop, `pyproject.toml` and `uv.lock` |
| 9.5 | Running the Assistant in Docker | ML Zoomcamp workshop, Dockerfile and client request |

## Detailed lesson outline

### 9.1 Moving the Assistant from a Notebook to a Python Script

Run the final-slides example in the supplied notebook. Read a sample HTTP request and response for the same question to see what the conference website will need. Move the existing tool functions and the LangChain answer function into a Python package. Take the model client and search dependency as arguments so a script can use the small starter fixtures.

**Check.** From another Python process, import the answer function and call it twice with different questions. The import makes zero model calls. Each call uses its own question and returns the associated answer and source IDs.

### 9.2 Loading the Handbook Index at Startup

The notebook prepared its search data in earlier cells. Configure the script to open the SQLite index from course 3, embed the question with the matching local model, and fetch the text of the highest-ranked section by ID.

**Check.** Start from a directory outside the package and ask “Where do I send my deck?” Resolve the returned ID against the stored section and show the upload instructions. Point the script at a missing index and check that startup identifies the missing file.

### 9.3 Serving Answers with FastAPI

Load the search and model dependencies at startup. Define a Pydantic request with a required question and the course 6 response with answer text, source IDs and an optional draft ID. Call the same answer function from `POST /answer` and expose `GET /health` for a startup check.

**Check.** Send the deadline question from a separate client. Its response contains October 15, 2027 and a citation to “Final Slides.” A recorded draft request also returns the ID in the local store. Send a request missing the question and verify that validation rejects it before the model is called.

### 9.4 Locking Python Dependencies with uv

Declare the libraries the service imports in `pyproject.toml`, generate `uv.lock`, and recreate the environment with `uv sync --locked` in a clean checkout. Document how to select the recorded client and locate the two search assets.

**Check.** Start the API from that checkout and rerun the client request. Inspect a checkout with a dependency declaration changed after locking and identify why the locked install stops.

### 9.5 Running the Assistant in Docker

Write a Dockerfile that installs the locked dependencies, copies the package and search assets, and starts Uvicorn. Build the image from a clean checkout, publish the service port and call it from the host.

**Check.** Run the container without mounting the checkout. Check its health, then send the same deadline request and follow its citation back to the handbook. A second image missing the index must fail the startup check before accepting questions.
