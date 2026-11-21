# Step 2: OpenAPI and Backend

We want web API parity from the start. Every action the frontend can take should also work through a clean HTTP API for a CLI or an AI agent.

## Extract the OpenAPI schema

Look at the mock client in `frontend/` and generate `api/openapi.yaml` at the repository root. Using subagents keeps the main context window clean while reading frontend routes and drafting schemas.

```text
Analyze the frontend in frontend/ and extract every backend call it makes.

Create api/openapi.yaml at the repository root defining every endpoint, method, path, request body, response body, and which endpoints require authentication.
```

## Build the FastAPI backend

While the frontend uses React defaults, I pick Python and FastAPI for the backend because I know the ecosystem well. Use `uv` for dependency management and start with an in-memory store seeded with demo users (such as `anna@example.com` / `password123`) so you can test right away.

```text
Build a FastAPI backend in backend/ using uv that implements api/openapi.yaml.

Use an in-memory store for now (no database yet) and seed it with a few fake users and sample records so the frontend has something to show.

Add authentication with hashed passwords and bearer tokens for the endpoints that need it.

Split the code into modules: routers, models, store, auth. Write tests.
```

## Connect frontend and backend with a Makefile

Switch the frontend from the single-file mock to the real FastAPI client, and add a `Makefile` so every dev command is one line:

```bash
cd backend && uv sync
WSWE_FIXED_NOW=2026-11-18T09:00:00Z uv run uvicorn app.main:create_app --factory --port 8000
```

In a second terminal, run `make frontend` (which starts Vite on port 8080). `WSWE_FIXED_NOW` freezes the server clock so the daily lunch poll stays open during testing.

Run `make backend-test` and `make frontend-test` to confirm both test suites pass before adding a database.
