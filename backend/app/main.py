from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from backend.app.api.router import router

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="Promoções COMAER",
    version="1.0.0",
)

# Servir arquivos estáticos
app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static",
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "status": "online",
        "sistema": "Promoções COMAER",
    }


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(BASE_DIR / "static" / "img" / "favicon.ico")
