from google import genai

from app.core.config import settings
from app.llm.base import BaseLLM
from app.prompts.system_prompt import SYSTEM_PROMPT


class GeminiLLM(BaseLLM):

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    async def generate(self, prompt: str) -> str:

        final_prompt = f"""
{SYSTEM_PROMPT}

User:
{prompt}
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=final_prompt,
        )

        return response.text