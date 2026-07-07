from app.llm.gemini import GeminiLLM


class LLMManager:

    def __init__(self):
        self.provider = GeminiLLM()

    async def generate(self, prompt: str) -> str:
        return await self.provider.generate(prompt)


llm_manager = LLMManager()