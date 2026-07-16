"""
Router principal da API.
"""

from backend.app.api.endpoints.militar import router as militar_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(
    militar_router,
    prefix="/militares",
    tags=["Militares"],
)
