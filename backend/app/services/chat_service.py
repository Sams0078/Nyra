from app.core.memory_manager import memory_manager
from app.core.prompt_builder import PromptBuilder
from app.llm.manager import llm_manager
from app.schemas.chat import ChatRequest, ChatResponse
from app.tools.manager import tool_manager
from app.tools.router import tool_router


class ChatService:

    async def generate_response(
        self,
        request: ChatRequest,
    ) -> ChatResponse:

        memory = memory_manager.get_memory(
            request.session_id
        )

        tool_name = tool_router.detect(
            request.message
        )

        if tool_name:

            tool = tool_manager.get_tool(
                tool_name
            )

            response = await tool.execute(
                request.message
            )

            memory.add_user_message(
                request.message
            )

            memory.add_ai_message(
                response
            )

            return ChatResponse(
                response=response,
            )

        memory.add_user_message(
            request.message
        )

        prompt = PromptBuilder.build(
            user_message=request.message,
            history=memory.history(),
        )

        response = await llm_manager.generate(
            prompt
        )

        memory.add_ai_message(
            response
        )

        return ChatResponse(
            response=response,
        )


chat_service = ChatService()