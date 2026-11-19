# 16. Deploying AI Applications to the Cloud

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 5. Production. 6 lessons, 2-3 hours.

## Summary

59.2% of AI-First roles require web skills (**APIs**: 2,515 jobs; **REST APIs**: 1,630; **FastAPI**: 928, the top Python web framework), and **AWS** is the #1 cloud provider (**39.3%** overall, **41.8%** in AI-First, ahead of Azure 29.7% and GCP 29.1%). Learners package the assistant as a FastAPI service with a streaming UI, containerize it with Docker, and learn how to deploy it on Amazon ECS with AWS Fargate.

## Learning objectives

- Expose an agent through a FastAPI REST API and a simple streaming UI
- Containerize the application with Docker, keeping configuration and secrets outside the image
- Prepare an ECS task definition for an ECR image and promote a tested image from development to production
- Verify deployment health using service events, logs, and application traces, and identify what drives running cost

## Why here

After CI/CD produces a tested image, this puts it behind a FastAPI endpoint and cloud URL using the #1 Python web framework and #1 cloud provider in the field guide.

## Transformation

From "it runs on my machine" to "my AI application runs behind a FastAPI service and cloud URL."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

FastAPI endpoints, Streamlit UI, streaming responses, `Dockerfile`, runtime configuration and secrets, ECR, ECS task definitions and services on Fargate, load balancer health checks, CloudWatch logs and OpenTelemetry traces

### How it's used in the exercises

The learner wraps the agent in a FastAPI service, adds the UI, and builds and checks the container locally. Using supplied deployment files, the learner prepares environment-specific task definitions that reference the same tested ECR image. In the worked deployment, the development service rolls out first, the production service receives the tested image after verification, and the learner follows a request ID from the service logs to a trace.

### Model / release

Python 3.13; `fastapi` and `uvicorn` (versions TBC), `streamlit>=1.58.0`, Docker, `awscli>=1.44.28`, `boto3>=1.42.37`. Small model.

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): AWS 39.3% (#1 cloud, 41.8% AI-First) > Azure 29.7% > GCP 29.1%; GenAI + Web 59.2%; Backend 61.0%; APIs 2,515, REST APIs 1,630, FastAPI 928; Docker 24.2%
- **FG learning paths / portfolio** (`learning-paths/README.md`, `portfolio/`, commit `1556dcb2`): FastAPI is "the most common Python web framework for AI" (high value); one cloud platform and Docker are "must have"; "Deployment - like Streamlit for prototypes" (Production block).
- Alexey's instruction for this track (one cloud provider, separate from Kubernetes)
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 4: Streamlit application; Week 7: complete example `10-deployment.md` and AWS container deployment basics in `v2/07-project-bonus/06-deployment/03-aws.md`
- **LZ**: LLM Zoomcamp (`github.com/DataTalksClub/llm-zoomcamp`) `07-project-example/04-interface.md`; `05-monitoring/13-docker-compose.md`

- **DataTalks.Club Course Management Platform** (historical commit `5a3a95b`): `.github/workflows/deploy-dev.yaml`, `deploy/deploy_dev.sh`, `deploy/deploy_prod.sh`, and `deploy/update_task_def.py` demonstrate tagging a release, registering a task definition revision, and updating the appropriate ECS service.
- **AI Dev Tools Zoomcamp**: `articles/04-devops.md` (development and production environments, container registry, OpenTelemetry, and alerting).

### Notes

Grade the task definition, version promotion decision, and diagnosis of saved service and monitoring outputs using supplied fixtures. Demonstrate the live ECS rollout in a provisioned sandbox or a recording. Learners can run and check the container locally.

## Lesson outline and source map

FG = AI Engineering Field Guide, LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. `'new'` = no lesson in LZ or BC.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 16.1 | From script to service: a FastAPI endpoint | BC `v2/07-project-bonus/03-complete-example/05-creating-app.md`; FG FastAPI (928 jobs) |
| 16.2 | A simple UI with streaming | BC `v2/04-testing/02-preparing-project/06-streamlit.md`, `03-streaming.md`; LZ `07-project-example/04-interface.md` |
| 16.3 | Containerizing the application | LZ `05-monitoring/13-docker-compose.md`; BC `03-complete-example/10-deployment.md` |
| 16.4 | Configuration and secrets | BC `03-complete-example/02-setup.md` |
| 16.5 | Deploy an image to ECS and promote it to production | Course Management Platform `5a3a95b` deployment scripts; AI Dev Tools Zoomcamp `articles/04-devops.md` |
| 16.6 | Verify service health with deployment events, logs, and traces | AI Dev Tools Zoomcamp `articles/04-devops.md`; reuses the track’s OpenTelemetry instrumentation |
