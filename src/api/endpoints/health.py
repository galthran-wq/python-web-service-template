from fastapi import APIRouter

from src.schemas.health import HealthResponse

router = APIRouter()


@router.get("/health")
async def health_check() -> HealthResponse:
    return HealthResponse(status="ok")
