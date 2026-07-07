from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=4000,
        description="User input message",
    )

    session_id: str = Field(
        default="default",
        min_length=1,
        max_length=100,
        description="Conversation session ID",
    )


class ChatResponse(BaseModel):
    response: str