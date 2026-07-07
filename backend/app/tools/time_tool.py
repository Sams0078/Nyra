from datetime import datetime

from app.tools.base import BaseTool


class TimeTool(BaseTool):

    name = "time"
    description = "Returns current system time."

    async def execute(
        self,
        query: str,
    ) -> str:

        return datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )