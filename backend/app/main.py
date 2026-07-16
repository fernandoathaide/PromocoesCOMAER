from fastapi import FastAPI

from backend.app.api.router import router

app = FastAPI(
    title="Promoções COMAER",
    version="1.0.0",
)

app.include_router(router)


@app.get("/")
def root():

    return {
        "status": "online",
        "sistema": "Promoções COMAER",
    }
