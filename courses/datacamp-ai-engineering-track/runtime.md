# Exercise runtime

## Models

Use the Claude, OpenAI, and DeepSeek models made available through DataCamp-funded API access. Choose the most efficient available model that passes each task's checks. Examples may use the OpenAI SDK interface; the skill being assessed is request construction, output validation, tool calling, or evaluation rather than a provider-specific feature. Provider adapters and model identifiers are supplied by DataCamp.

## Python packages

Python 3.13. Exact proposed direct pins are listed below and in requirements.in. They were checked against the Python package registry and resolved together for Python 3.13. This validates dependency resolution, not the exercises or service deployment. The full resolved set is in requirements.txt; DataCamp must validate the implementation against its own runtime before release.

- `openai==3.57.0`
- `pydantic==2.14.4`
- `python-dotenv==1.2.4`
- `minsearch==0.2.0`
- `sentence-transformers==6.3.0`
- `numpy==2.5.5`
- `sqlitesearch==0.3.0`
- `mcp==1.30.0`
- `langchain==1.5.2`
- `langchain-openai==1.8.5`
- `langgraph==1.2.24`
- `langchain-mcp-adapters==0.3.2`
- `fastapi==0.165.0`
- `uvicorn==0.54.0`
- `pytest==9.2.0`
- `httpx==0.28.1`
- `langfuse==5.2.0`
- `pandas==3.1.1`
- `uv==0.13.9`
- `PyYAML==6.0.4`
- `PyMuPDF==2.1`

- `pydantic-ai-slim==2.71.0`

## Local services and system tools

- Local SQLite/vector storage and supplied embedding-model assets; a supplied PostgreSQL sandbox is used only for the database comparison. No hosted database account is required.
- Local MCP server processes over stdio.
- A preconfigured local Langfuse service and bundled trace exports. No learner registration or external Langfuse subscription is required.
- Docker, a local workflow runner, kind, and kubectl are provided by the workspace. CI uses local workflow execution, not GitHub-hosted Actions or the GitHub CLI.
- The Kubernetes environment is local or an isolated cluster provisioned by DataCamp. No cloud account is required.
- Application, tracing, and deployment secrets are injected into the exercise environment, never included in learner source code.

The container-engine, cluster, tracing-service, and workflow-runner releases must be pinned by DataCamp when the workspace image is selected. This infrastructure dependency remains an implementation review item; the plan does not assume arbitrary Docker privileges in the tutor's Python process. If the standard tutor cannot host these components, supply an isolated sandbox for the corresponding courses.

## Exercise behavior

Model-based evaluation uses real model and judge calls within a supplied budget. Recorded traces and run logs support diagnosis and comparison exercises. Deterministic unit tests cover pure application logic; no mocked model responses are required by the CI course. The capstone starts from a supplied integration scaffold and assesses selected functions and decisions within seven lessons.
