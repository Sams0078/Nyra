from fastapi import Request
from fastapi.responses import JSONResponse


class NYRAException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code


async def nyra_exception_handler(
    request: Request,
    exc: NYRAException,
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.message,
        },
    )