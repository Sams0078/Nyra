from app.tools.calculator import CalculatorTool
from app.tools.time_tool import TimeTool


class ToolManager:

    def __init__(self):

        self.tools = {
            "calculator": CalculatorTool(),
            "time": TimeTool(),
        }

    def get_tool(
        self,
        tool_name: str,
    ):

        return self.tools.get(tool_name)


tool_manager = ToolManager()