# 14. Deploying AI Applications with Kubernetes

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 5. Production. 6 lessons, 2–3 hours.

## Summary

**Kubernetes** appears in **23.6%** of all postings (2,307 jobs; rising 18.6% → 23.8% in AI-First, 28.3% in AI-Support, and 43% in platform/infra roles). Learners deploy the containerized FastAPI/agent service from course 13 to a local Kubernetes cluster (`kind`), manage API keys as Secrets, scale replicas, roll out a new version and roll it back.

## Learning objectives

- Explain pods, deployments and services and write their manifests
- Run a local cluster and deploy a containerized LLM application to it
- Manage API keys and configuration with Secrets and ConfigMaps
- Scale the application and perform a rolling update and a rollback

## Why here

Reuses the Docker image from courses 12–13 and covers the container orchestration skill demanded in nearly a quarter of all AI engineering jobs.

## Transformation

From "I can deploy one container to a managed service" to "I can run, scale and update my AI application on Kubernetes."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

`kind` cluster, `kubectl apply/get/logs/port-forward`, Deployment, Service, Secret, ConfigMap, readiness probes, replicas, rollout and rollback

### How it's used in the exercises

The learner creates a `kind` cluster, loads the image, writes the manifests one by one, port-forwards to the service and sends a question, then changes the image tag and watches the rollout and rollback.

### Model / release

`kind` and `kubectl` (versions TBC), Docker, Python 3.13 application image from course 13. Small model.

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): Kubernetes 23.6% (2,307 jobs; rising 18.6% → 23.8% in AI-First; 28.3% in AI-Support), Docker 24.2%, GenAI + Ops 71.0% AI-First
- Alexey's instruction for this track (Kubernetes as a separate course)
- Machine Learning Zoomcamp Module 10 Kubernetes (`github.com/DataTalksClub/machine-learning-zoomcamp`, `10-kubernetes`) — to be confirmed as source

### Notes

No-subscription constraint: fully local with `kind` (or `minikube`), no cloud account. Needs Docker inside the exercise environment — to confirm with DataCamp. Kubernetes is not covered in LLM Zoomcamp or the Buildcamp; the outline follows Alexey's ML Zoomcamp Kubernetes module adapted to an LLM service and needs his review.

## Lesson outline and source map

FG = AI Engineering Field Guide, LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. `'new'` = no lesson in LZ or BC.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 14.1 | Why Kubernetes for an AI application | new; ML Zoomcamp `10-kubernetes`; FG Kubernetes (23.6%) |
| 14.2 | A local cluster with kind | ML Zoomcamp `10-kubernetes` |
| 14.3 | Deployments and pods | ML Zoomcamp `10-kubernetes` |
| 14.4 | Services and reaching the application | ML Zoomcamp `10-kubernetes` |
| 14.5 | Secrets and configuration for API keys | new |
| 14.6 | Scaling, rolling updates and rollbacks | new |
