from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.logging import logger

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Personal AI Companion"
)

app.include_router(api_router)


@app.on_event("startup")
async def startup():
    logger.info("NYRA Server Started Successfully")


@app.get("/")
def root():
    logger.info("Root endpoint accessed")

    return {
        "message": f"Welcome to {settings.APP_NAME} 🚀"
    }