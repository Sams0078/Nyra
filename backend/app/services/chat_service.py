from app.llm.manager import llm_manager
from app.schemas.chat import ChatRequest, ChatResponse


class ChatService:

    async def generate_response(
        self,
        request: ChatRequest,
    ) -> ChatResponse:

        response = await llm_manager.generate(
            request.message
        )

        return ChatResponse(
            response=response
        )


chat_service = ChatService()