from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.middleware import logging_middleware
from app.core.exceptions import (
    NYRAException,
    nyra_exception_handler,
)
from app.core.logging import logger
from app.schemas.response import APIResponse

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Personal AI Companion"
)

app.add_exception_handler(
    NYRAException,
    nyra_exception_handler,
)

app.middleware("http")(logging_middleware)

app.include_router(api_router)


@app.on_event("startup")
async def startup():
    logger.info("NYRA Server Started Successfully")


@app.get("/", response_model=APIResponse)
def root():
    logger.info("Root endpoint accessed")

    return APIResponse(
        success=True,
        message=f"Welcome to {settings.APP_NAME} 🚀",
        data=None,
    )

@app.get("/error")
def error():
    raise NYRAException(
        "This is a test exception.",
        status_code=500,
    )