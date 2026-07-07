from app.tools.base import BaseTool


class CalculatorTool(BaseTool):

    name = "calculator"
    description = "Performs basic mathematical calculations."

    async def execute(
        self,
        query: str,
    ) -> str:

        try:
            result = eval(
                query,
                {"__builtins__": {}},
                {},
            )

            return str(result)

        except Exception:
            return "Invalid mathematical expression."