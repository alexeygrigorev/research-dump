# 13. Deploying AI Applications to the Cloud

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 5. Production. 6 lessons, 2–3 hours.

## Summary

Learners package the assistant as a web service with a small UI, containerize it, and deploy it to one cloud provider. They handle configuration and secrets, check the deployed service, and estimate what it costs to run.

## Learning objectives

- Expose an agent through an API and a simple UI
- Containerize the application with its configuration and secrets kept outside the image
- Deploy the container to a cloud provider and verify it works
- Estimate running cost and choose between a serverless and an always-on option

## Why here

After CI/CD produces a tested image, this is the simplest way to put it in front of users; Kubernetes follows for those who need more control.

## Transformation

From "it runs on my machine" to "my AI application runs in the cloud behind a URL."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

FastAPI endpoints, Streamlit UI, streaming responses, Dockerfile, environment variables and secrets, cloud CLI deploy commands, health checks, logs

### How it's used in the exercises

The learner wraps the agent in an API, adds the UI, builds and runs the container locally, then follows the deploy steps for the chosen provider, calls the public endpoint and reads the logs.

### Model / release

Python 3.13; fastapi and uvicorn (versions TBC), streamlit>=1.58.0, Docker, provider CLI (AWS: awscli>=1.44.28, boto3>=1.42.37). Small model.

### Source material

- Alexey's instruction for this track (one cloud provider, separate from Kubernetes)
- AI Engineering Buildcamp (Maven course; repo ai-engineering-buildcamp, curriculum.md) Week 7: Deployment (Streamlit, Render, AWS); Week 4: Streamlit application; Week 7: complete example 10-deployment.md
- LLM Zoomcamp (github.com/DataTalksClub/llm-zoomcamp) 07-project-example/04-interface.md; 05-monitoring/13-docker-compose.md

### Notes

No-subscription constraint: a real cloud deploy needs an external account, which the brief asks to avoid. Proposal: build everything locally in the exercise environment and make the final cloud step on a provider free tier (the Buildcamp material covers AWS and Render), or simulate it with a local emulator if DataCamp cannot allow an external account. Provider choice is an open question.

## Lesson outline and source map

LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. 'new' = no lesson in either source.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 13.1 | From script to service: an API for the agent | BC v2/07-project-bonus/03-complete-example/05-creating-app.md |
| 13.2 | A simple UI with streaming | BC v2/04-testing/02-preparing-project/06-streamlit.md, 03-streaming.md; LZ 07-project-example/04-interface.md |
| 13.3 | Containerizing the application | LZ 05-monitoring/13-docker-compose.md; BC 03-complete-example/10-deployment.md |
| 13.4 | Configuration and secrets | BC 03-complete-example/02-setup.md |
| 13.5 | Deploying to a cloud provider | BC v2/07-project-bonus/06-deployment/02-render.md, 03-aws.md |
| 13.6 | Checking the deployment: logs, health, cost | BC 06-deployment/03-aws.md; new |
