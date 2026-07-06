from app.llm.base import BaseLLM


class GeminiLLM(BaseLLM):

    async def generate(self, prompt: str) -> str:
        return "Gemini integration coming soon..."