from app.prompts.system_prompt import SYSTEM_PROMPT


class PromptBuilder:

    @staticmethod
    def build(
        user_message: str,
        history: list[str] | None = None,
    ) -> str:

        history = history or []

        conversation = "\n".join(history)

        return f"""
{SYSTEM_PROMPT}

Conversation History:

{conversation}

Current User Message:

{user_message}
"""