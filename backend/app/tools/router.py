class ToolRouter:

    @staticmethod
    def detect(
        message: str,
    ) -> str | None:

        message = message.lower()

        if any(
            word in message
            for word in [
                "time",
                "date",
                "clock",
            ]
        ):
            return "time"

        if any(
            op in message
            for op in [
                "+",
                "-",
                "*",
                "/",
            ]
        ):
            return "calculator"

        return None


tool_router = ToolRouter()