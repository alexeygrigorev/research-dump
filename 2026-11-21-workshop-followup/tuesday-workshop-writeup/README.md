# Full-Stack Vibe Coding Workshop

In this workshop, we take a team lunch restaurant-picker app from a product specification to a containerized, tested, and deployed full-stack application.

You'll build a React frontend and extract an OpenAPI schema from it. Then you'll implement a FastAPI backend with SQLite and PostgreSQL support, add a Playwright end-to-end test, and configure CI/CD and agent roles.

Source code: [alexeygrigorev/workshop-berlin](https://github.com/alexeygrigorev/workshop-berlin).

## Steps

We work through four stages:

1. [Spec and Frontend](01-spec-and-frontend.md) - Run a ChatGPT discovery interview, write `specs.md`, generate the UI, strip Supabase, and fix layout friction.
2. [OpenAPI and Backend](02-openapi-and-backend.md) - Extract `api/openapi.yaml`, build the FastAPI backend with `uv`, and connect the frontend.
3. [Database and Docker](03-database-and-docker.md) - Switch from an in-memory store to SQLAlchemy, SQLite, PostgreSQL, and Docker Compose.
4. [E2E Tests, Deploy, and Agent Roles](04-e2e-deploy-and-agents.md) - Add Playwright tests, ship to a VPS with CI/CD, and set up PM, engineer, and QA agent roles.
