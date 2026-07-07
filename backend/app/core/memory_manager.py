from app.core.memory import ConversationMemory


class MemoryManager:

    def __init__(self):
        self.sessions: dict[str, ConversationMemory] = {}

    def get_memory(
        self,
        session_id: str,
    ) -> ConversationMemory:

        if session_id not in self.sessions:
            self.sessions[session_id] = ConversationMemory()

        return self.sessions[session_id]


memory_manager = MemoryManager()