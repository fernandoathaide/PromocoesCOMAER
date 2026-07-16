"""
Router principal da API.
"""

from fastapi import APIRouter

from backend.app.api.endpoints.militar import router as militar_router
from backend.app.api.endpoints.simulacao import (
    router as simulacao_router,
)

router = APIRouter()

router.include_router(
    militar_router,
    prefix="/militares",
    tags=["Militares"],
)

router.include_router(
    simulacao_router,
    prefix="/simulacao",
    tags=["Simulação"],
)
