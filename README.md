# Python Service Template

[![CI](https://github.com/galthran-wq/python-web-service-template/actions/workflows/ci.yml/badge.svg)](https://github.com/galthran-wq/python-web-service-template/actions/workflows/ci.yml)
[![Coverage Status](https://coveralls.io/repos/github/galthran-wq/python-web-service-template/badge.svg?branch=master)](https://coveralls.io/github/galthran-wq/python-web-service-template?branch=master)
![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![mypy](https://img.shields.io/badge/type_checker-mypy-blue)](https://mypy-lang.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Minimal production-ready Python microservice template.

## Stack

- **FastAPI** — async web framework
- **uv** — package manager
- **Pydantic v2** — validation and settings
- **structlog** — structured logging
- **Prometheus** — metrics via prometheus-fastapi-instrumentator
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
| `make test` | Run tests with coverage |
| `make lint` | Run ruff + mypy |
| `make format` | Auto-format code |
| `make pre-commit` | Install pre-commit hooks |
| `make docker-build` | Build Docker image |
| `make docker-run` | Run Docker container |

## Project Structure

```
src/
├── main.py           — app factory, structlog config, Prometheus setup
├── config.py         — pydantic-settings based configuration
├── dependencies.py   — FastAPI dependency injection providers
├── api/
│   ├── router.py     — aggregated API router
│   └── endpoints/    — route handlers
├── schemas/          — Pydantic request/response models
├── services/         — business logic layer
└── core/
    ├── exceptions.py — custom exceptions + handlers
    └── middleware.py  — CORS, request logging, request ID
```
