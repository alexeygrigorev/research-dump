# 16. Deploying AI Applications with Kubernetes

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 5. Production. 6 lessons, 2-3 hours.

## Summary

**Kubernetes** appears in **23.6%** of all postings (2,307 jobs; rising 18.6% → 23.8% in AI-First, 28.3% in AI-Support, and 43% in platform/infra roles). Learners deploy the containerized FastAPI/agent service from the cloud deployment course to a local Kubernetes cluster (`kind`), manage API keys as Secrets, scale replicas, roll out a new version and roll it back.

## Learning objectives

- Explain pods, deployments and services and write their manifests
- Run a local cluster and deploy a containerized LLM application to it
- Manage API keys and configuration with Secrets and ConfigMaps
- Scale the application and perform a rolling update and a rollback

## Why here

Reuses the Docker image from the CI/CD and cloud deployment courses and covers the container orchestration skill demanded in nearly a quarter of all AI engineering jobs.

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

`kind` and `kubectl` (versions TBC), Docker, Python 3.13 application image from the cloud deployment course. Small model.

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): Kubernetes 23.6% (2,307 jobs; rising 18.6% → 23.8% in AI-First; 28.3% in AI-Support), Docker 24.2%, GenAI + Ops 71.0% AI-First
- **FG learning paths / portfolio** (`learning-paths/README.md`, `portfolio/`, commit `1556dcb2`): "Docker and Kubernetes - containerization and orchestration"; Kubernetes is "high value".
- Alexey's instruction for this track (Kubernetes as a separate course)
- Machine Learning Zoomcamp `10-kubernetes/05-kubernetes-intro.md` and `10-kubernetes/06-kubernetes-simple-service.md` (kind, local image loading, Deployment and Service)

- **AI Dev Tools Zoomcamp**: `cohorts/2026/homework/03-deployment/homework.md`, Questions 5–6 (kind deployment, versioned images, and rollout verification).

### Notes

Use a local `kind` cluster in a Docker-capable exercise environment or a preprovisioned cluster with a supplied application image. For environments without cluster access, grade manifest changes and have learners interpret saved `kubectl` output for a successful rollout, a failed rollout, and a rollback.

## Lesson outline and source map

FG = AI Engineering Field Guide, LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. `'new'` = no lesson in LZ or BC.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 16.1 | Why Kubernetes for an AI application | new; ML Zoomcamp `10-kubernetes`; FG Kubernetes (23.6%) |
| 16.2 | A local cluster with kind | ML Zoomcamp `10-kubernetes` |
| 16.3 | Deployments and pods | ML Zoomcamp `10-kubernetes` |
| 16.4 | Services and reaching the application | ML Zoomcamp `10-kubernetes` |
| 16.5 | Secrets and configuration for API keys | new |
| 16.6 | Scaling, rolling updates and rollbacks | new |

## Detailed lesson outline

### 16.1 Why Kubernetes for an AI application

Map the existing container service to Pods, a Deployment, and a Service.

**Check.** Identify which object owns replicas and which provides a stable endpoint.

### 16.2 A local cluster with kind

Create a kind cluster and load the application image, or inspect supplied cluster output.

**Check.** Verify node readiness and the image reference used by the workload.

### 16.3 Deployments and pods

Apply the Deployment and inspect a failing Pod using status and logs.

**Check.** Identify the mismatch in a supplied failure and verify the corrected manifest.

### 16.4 Services and reaching the application

Create a Service and forward its port to the local machine.

**Check.** Call the health endpoint and verify the Service points to the expected Pods.

### 16.5 Secrets and configuration for API keys

Wire non-secret settings through a ConfigMap and a placeholder key through a Secret.

**Check.** Verify both environment variable references in the Deployment manifest.

### 16.6 Scaling, rolling updates and rollbacks

Scale the Deployment, update its image tag, and roll back after a failing readiness check.

**Check.** Verify the restored version and replica readiness from rollout output.
