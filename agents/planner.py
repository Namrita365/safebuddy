class PlannerAgent:
    """
    Planner Agent:
    - Takes user input
    - Plans the next steps for SafeBuddy workflow
    """

    def __init__(self):
        pass

    def create_plan(self, user_input: str) -> str:
        """
        Generate a simple plan based on user input.
        For now, it just returns a text describing the plan.
        """
        plan = f"Plan generated for input: '{user_input}'"
        return plan
