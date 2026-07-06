import time

from fastapi import Request

from app.core.logging import logger


async def logging_middleware(request: Request, call_next):
    start_time = time.perf_counter()

    response = await call_next(request)

    process_time = time.perf_counter() - start_time

    logger.info(
        f"{request.method} {request.url.path} | "
        f"{response.status_code} | "
        f"{process_time:.4f} sec"
    )

    response.headers["X-Process-Time"] = f"{process_time:.4f}"

    return response