from abc import ABC, abstractmethod


class BaseLLM(ABC):
    """
    Base interface for every LLM provider.
    """

    @abstractmethod
    async def generate(self, prompt: str) -> str:
        """
        Generate response from the LLM.
        """
        pass