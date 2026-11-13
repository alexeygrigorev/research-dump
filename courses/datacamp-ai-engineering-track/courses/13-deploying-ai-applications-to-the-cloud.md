# 13. Deploying AI Applications to the Cloud

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 5. Production. 6 lessons, 2–3 hours.

## Summary

59.2% of AI-First roles require web skills (**APIs**: 2,515 jobs; **REST APIs**: 1,630; **FastAPI**: 928, the top Python web framework), and **AWS** is the #1 cloud provider (**39.3%** overall, **41.8%** in AI-First, ahead of Azure 29.7% and GCP 29.1%). Learners package the assistant as a FastAPI service with a streaming UI, containerize it with Docker, and deploy it to AWS (or a local container/emulator fallback).

## Learning objectives

- Expose an agent through a FastAPI REST API and a simple streaming UI
- Containerize the application with Docker, keeping configuration and secrets outside the image
- Deploy the container to AWS and verify health checks and logs
- Estimate running cost and choose between serverless and always-on options

## Why here

After CI/CD produces a tested image, this puts it behind a FastAPI endpoint and cloud URL using the #1 Python web framework and #1 cloud provider in the field guide.

## Transformation

From "it runs on my machine" to "my AI application runs behind a FastAPI service and cloud URL."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

FastAPI endpoints, Streamlit UI, streaming responses, `Dockerfile`, environment variables and secrets, AWS CLI deploy commands, health checks, logs

### How it's used in the exercises

The learner wraps the agent in a FastAPI service, adds the UI, builds and runs the container locally, then follows the AWS deploy steps (or local container/emulator simulation), calls the public endpoint and reads the logs.

### Model / release

Python 3.13; `fastapi` and `uvicorn` (versions TBC), `streamlit>=1.58.0`, Docker, `awscli>=1.44.28`, `boto3>=1.42.37`. Small model.

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): AWS 39.3% (#1 cloud, 41.8% AI-First) > Azure 29.7% > GCP 29.1%; GenAI + Web 59.2%; Backend 61.0%; APIs 2,515, REST APIs 1,630, FastAPI 928; Docker 24.2%
- Alexey's instruction for this track (one cloud provider, separate from Kubernetes)
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 7: Deployment (Streamlit, Render, AWS); Week 4: Streamlit application; Week 7: complete example `10-deployment.md`
- **LZ**: LLM Zoomcamp (`github.com/DataTalksClub/llm-zoomcamp`) `07-project-example/04-interface.md`; `05-monitoring/13-docker-compose.md`

### Notes

**Reworked from initial draft**: Field guide data resolves the cloud provider choice to **AWS** (#1 in postings at 39.3% / 41.8% AI-First). No-subscription constraint: if DataCamp cannot allow an external AWS free-tier account, build and test the container locally and simulate the final deploy step with a local emulator.

## Lesson outline and source map

FG = AI Engineering Field Guide, LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. `'new'` = no lesson in LZ or BC.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 13.1 | From script to service: a FastAPI endpoint | BC `v2/07-project-bonus/03-complete-example/05-creating-app.md`; FG FastAPI (928 jobs) |
| 13.2 | A simple UI with streaming | BC `v2/04-testing/02-preparing-project/06-streamlit.md`, `03-streaming.md`; LZ `07-project-example/04-interface.md` |
| 13.3 | Containerizing the application | LZ `05-monitoring/13-docker-compose.md`; BC `03-complete-example/10-deployment.md` |
| 13.4 | Configuration and secrets | BC `03-complete-example/02-setup.md` |
| 13.5 | Deploying to AWS | BC `v2/07-project-bonus/06-deployment/03-aws.md`; FG AWS (39.3%) |
| 13.6 | Checking the deployment: logs, health, cost | BC `06-deployment/03-aws.md`; new |
