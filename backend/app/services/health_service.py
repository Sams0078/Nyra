from app.schemas.response import APIResponse


def get_health_status() -> APIResponse:
    return APIResponse(
        success=True,
        message="NYRA is healthy",
        data={
            "status": "healthy",
            "version": "0.1.0",
        },
    )