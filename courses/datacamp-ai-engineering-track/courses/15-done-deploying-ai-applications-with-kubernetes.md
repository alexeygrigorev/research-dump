# 15. Deploying AI Applications with Kubernetes - DONE

Part of the [DataCamp AI Engineering track plan](../README.md). Stage: 5. Production. 6 lessons, 2-3 hours. Each lesson is designed for approximately 20-25 minutes.

## Summary

Learners deploy a tested AI service to a local Kubernetes cluster. They define workloads and services, configure application settings and credentials, and verify readiness. They then update the service and recover a working version after a failed rollout.

## Learning objectives

- Write deployment and service manifests
- Configure application settings and credentials
- Verify readiness and send requests to the deployed service
- Update a workload and roll back a failed release

## Why here

Uses the versioned image from CI/CD and introduces the operating tasks needed after a release.

## Transformation

From "I can build a tested image" to "I can deploy, update, and recover a running service."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

`kind` cluster, `kubectl apply/get/logs/port-forward`, Deployment, Service, Secret, ConfigMap, readiness probes, rollout and rollback

### How it's used in the exercises

Deploy the read-only speaker handbook endpoint from CI. Use readiness, a Service, and a smoke request to verify the rollout. Ticket submission stays in the local simulated workflow because the deployment exercise has no shared durable store.

### Model / release

Python 3.13. No additional Python packages; uses the container from the preceding course.. Docker and local runtime tools are supplied by the exercise workspace; see [Runtime requirements](../runtime.md).

### Source material

- [Kubernetes rollout and rollback](https://kubernetes.io/docs/tasks/run-application/update-deployment-rolling/) and [port-forward reference](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_port-forward/)
- **FG** (AI Engineering Field Guide, 9,760 jobs): Kubernetes 23.6% (2,307 jobs; rising 18.6% → 23.8% in AI-First; 28.3% in AI-Support), Docker 24.2%, GenAI + Ops 71.0% AI-First
- **FG learning paths / portfolio** (`learning-paths/README.md`, `portfolio/`, commit `1556dcb2`): "Docker and Kubernetes - containerization and orchestration"; Kubernetes is "high value".
- Alexey's instruction for this track (Kubernetes as a separate course)
- Machine Learning Zoomcamp `10-kubernetes/05-kubernetes-intro.md` and `10-kubernetes/06-kubernetes-simple-service.md` (kind, local image loading, Deployment and Service)

- **AI Dev Tools Zoomcamp**: `cohorts/2026/homework/03-deployment/homework.md`, Questions 5–6 (kind deployment, versioned images, and rollout verification).

### Notes

Supply a local kind cluster or a preprovisioned isolated cluster in the exercise workspace. Learners apply manifests and inspect actual runtime output without creating a cloud account.

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 15.1 | Introduction to Kubernetes | ML Zoomcamp `10-kubernetes/06-kubernetes-simple-service.md` |
| 15.2 | Local Kubernetes with kind | ML Zoomcamp `10-kubernetes/06-kubernetes-simple-service.md` |
| 15.3 | Kubernetes Deployments and Readiness | ML Zoomcamp `10-kubernetes/06-kubernetes-simple-service.md` |
| 15.4 | Kubernetes Services | ML Zoomcamp `10-kubernetes/06-kubernetes-simple-service.md` |
| 15.5 | Application Configuration | AI Dev Tools Zoomcamp 2026 deployment homework, Question 6 |
| 15.6 | Updates and Rollbacks | AI Dev Tools Zoomcamp 2026 deployment homework, Question 6 |

## Detailed lesson outline

### 15.1 Introduction to Kubernetes

Inspect a running Deployment, its Pods, and a Service. See how the Service selects Pods, then follow one HTTP request through a local port-forward to a selected Pod.

**Check.** Identify which object keeps a replica running and which gives clients a stable target.

### 15.2 Local Kubernetes with kind

Create a local Kubernetes cluster with kind or use the preprovisioned environment. Load the exact image tag produced by the CI lesson.

**Check.** Check node readiness and verify the image referenced by the Deployment is available.

### 15.3 Kubernetes Deployments and Readiness

Write or complete the Deployment with matching labels, a container port, and a readiness probe. Use a supplied bad image or probe configuration to practice diagnosis.

**Check.** Explain the failed state using recorded events or logs, then verify the corrected Pod is ready.

### 15.4 Kubernetes Services

Add a Service selector and port mapping. Forward the Service port to the learner’s machine and submit a speaker handbook question.

**Check.** Verify that the Service has a ready backend and that the response cites the expected section.

### 15.5 Application Configuration

Pass the assistant’s non-secret settings through a ConfigMap and a placeholder credential through a Secret reference. Keep the exercised endpoint read-only and its fixtures local to the service.

**Check.** Change a harmless runtime setting and verify its effect after restarting the workload. With a dummy credential, confirm the application sees the Secret reference without showing its value in normal output.

### 15.6 Updates and Rollbacks

Update to a new image tag, wait on readiness, then diagnose a supplied bad update and roll back. Use the same request as a smoke check after rollback.

**Check.** Verify the restored image tag, ready replicas, and successful response after rollback.
