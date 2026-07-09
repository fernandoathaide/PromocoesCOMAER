from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.app.core.logging import configure_logging
from backend.app.core.settings import settings
from backend.app.infrastructure.migration.migration_runner import (
    MigrationRunner,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    MigrationRunner().run()
    yield


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Sistema de Apoio à Decisão para Promoções do COMAER",
    lifespan=lifespan,
)


@app.get("/")
def root():
    return {
        "system": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
