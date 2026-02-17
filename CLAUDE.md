# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
make install        # Install dependencies (uv sync)
make run            # Dev server with hot reload on :8000
make test           # pytest with coverage
make lint           # ruff check + mypy strict
make format         # ruff format + ruff check --fix
make docker-build   # Build Docker image
make docker-run     # Run container on :8000
```

Run a single test file: `uv run pytest tests/api/test_health.py`
Run a single test: `uv run pytest tests/api/test_health.py::test_health_endpoint -v`

## Architecture

FastAPI microservice using a layered architecture with `src/` as the root package.

**Layers:**
- `src/api/endpoints/` — Thin async route handlers. One router per file, registered in `src/api/router.py`.
- `src/schemas/` — Pydantic request/response models.
- `src/services/` — Business logic. Must not import FastAPI; injected into endpoints via `src/dependencies.py` using `Depends()`.
- `src/core/` — Middleware (request ID, logging, CORS) and exception handling (`AppError`).

**Key patterns:**
- App factory: `create_app()` in `src/main.py` wires middleware, exception handlers, routers, and Prometheus.
- Configuration: `src/config.py` uses Pydantic Settings, loaded from env vars / `.env` file. Singleton `settings` instance.
- Logging: `structlog` with JSON output in prod, console in dev (controlled by `DEBUG` env var). Use `structlog.get_logger()` and log with key-value pairs.
- Errors: Raise `AppError(status_code, detail)` from `src/core/exceptions.py` — never catch broad `Exception`.
- Request ID: Auto-generated UUID per request, bound to structlog context vars, returned in `x-request-id` header.

## Adding a New Endpoint

1. Create `src/api/endpoints/<domain>.py` with `router = APIRouter()`
2. Create request/response schemas in `src/schemas/<domain>.py`
3. Register router in `src/api/router.py` via `router.include_router()`
4. Add tests in `tests/api/test_<domain>.py` (mirror the endpoint file structure)

## Code Style

- Python 3.12+, all functions require type annotations (params and return)
- Line length: 120
- Use `async def` for I/O-bound functions
- mypy strict mode with pydantic plugin
- Import order enforced by ruff: stdlib → third-party → local
- Use `collections.abc` for abstract types, built-in generics (`list[str]` not `List[str]`)

## Testing

- All tests are `async def` — pytest-asyncio in auto mode
- Use the `client` fixture from `tests/conftest.py` (httpx `AsyncClient` with `ASGITransport`)
- Test file structure mirrors `src/api/endpoints/`
