from fastapi import APIRouter

from src.api.endpoints import health

router = APIRouter()
router.include_router(health.router, tags=["health"])
