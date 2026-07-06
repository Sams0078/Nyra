from abc import ABC, abstractmethod


class BaseLLM(ABC):

    @abstractmethod
    async def generate(self, prompt: str) -> str:
        """Generate a response from the LLM."""
        pass