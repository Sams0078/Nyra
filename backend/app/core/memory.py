from collections import deque


class ConversationMemory:

    def __init__(self, max_messages: int = 10):
        self.messages = deque(maxlen=max_messages)

    def add_user_message(self, message: str):
        self.messages.append(f"User: {message}")

    def add_ai_message(self, message: str):
        self.messages.append(f"Assistant: {message}")

    def history(self) -> list[str]:
        return list(self.messages)


conversation_memory = ConversationMemory()