# 14. Deploying AI Applications with Kubernetes

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 5. Production. 6 lessons, 2–3 hours.

## Summary

Learners deploy the same container to a local Kubernetes cluster. They write the deployment and service, manage API keys as secrets, scale the application, roll out a new version and roll it back.

## Learning objectives

- Explain pods, deployments and services and write their manifests
- Run a local cluster and deploy a containerized LLM application to it
- Manage API keys and configuration with secrets and config maps
- Scale the application and perform a rolling update and a rollback

## Why here

Reuses the image from courses 12–13 and is the last infrastructure step before the capstone.

## Transformation

From "I can deploy one container to a managed service" to "I can run and update my AI application on Kubernetes."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

kind cluster, kubectl apply/get/logs/port-forward, Deployment, Service, Secret, ConfigMap, readiness probes, replicas, rollout and rollback

### How it's used in the exercises

The learner creates a kind cluster, loads the image, writes the manifests one by one, port-forwards to the service and sends a question, then changes the image tag and watches the rollout.

### Model / release

kind and kubectl (versions TBC), Docker, Python 3.13 application image from course 13. Small model.

### Source material

- Alexey's instruction for this track (Kubernetes as a separate course)
- Machine Learning Zoomcamp Module 10 Kubernetes (github.com/DataTalksClub/machine-learning-zoomcamp, 10-kubernetes) — to be confirmed as source

### Notes

No-subscription constraint: fully local with kind (or minikube), no cloud account. Needs Docker inside the exercise environment — to confirm with DataCamp. Kubernetes is not covered in LLM Zoomcamp or the Buildcamp; the outline follows Alexey's ML Zoomcamp Kubernetes module adapted to an LLM service and needs his review.

## Lesson outline and source map

LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. 'new' = no lesson in either source.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 14.1 | Why Kubernetes for an AI application | new; ML Zoomcamp 10-kubernetes |
| 14.2 | A local cluster with kind | ML Zoomcamp 10-kubernetes |
| 14.3 | Deployments and pods | ML Zoomcamp 10-kubernetes |
| 14.4 | Services and reaching the application | ML Zoomcamp 10-kubernetes |
| 14.5 | Secrets and configuration for API keys | new |
| 14.6 | Scaling, rolling updates and rollbacks | new |
