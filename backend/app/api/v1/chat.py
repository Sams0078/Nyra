from fastapi import APIRouter

from app.schemas import APIResponse, ChatRequest
from app.services.chat_service import chat_service

router = APIRouter()


@router.post("/chat", response_model=APIResponse)
async def chat(request: ChatRequest):

    response = await chat_service.generate_response(request)

    return APIResponse(
        success=True,
        message="Response generated successfully",
        data=response,
    )