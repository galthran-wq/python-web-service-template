# Python Service Template

Minimal production-ready Python microservice template.

## Stack

- **FastAPI** — async web framework
- **uv** — package manager
- **Pydantic v2** — validation and settings
- **structlog** — structured logging
- **pytest + httpx** — testing
- **ruff** — linting and formatting
- **mypy** — type checking
- **Docker** — containerization

## Quick Start

```bash
make install
make run
```

## Commands

| Command | Description |
|---|---|
| `make install` | Install dependencies |
| `make run` | Run dev server with hot reload |
| `make test` | Run tests |
| `make lint` | Run ruff + mypy |
| `make format` | Auto-format code |
| `make pre-commit` | Install pre-commit hooks |
| `make docker-build` | Build Docker image |
| `make docker-run` | Run Docker container |

## Project Structure

```
src/
├── main.py           — app factory + structlog config
├── config.py         — pydantic-settings based configuration
├── dependencies.py   — FastAPI dependency injection providers
├── api/
│   ├── router.py     — aggregated API router
│   └── endpoints/    — route handlers
├── schemas/          — Pydantic request/response models
├── services/         — business logic layer
└── core/
    ├── exceptions.py — custom exceptions + handlers
    └── middleware.py  — CORS, request logging
```
