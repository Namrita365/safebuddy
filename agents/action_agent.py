class ActionAgent:
    """
    Action Agent:
    - Performs the planned actions from PlannerAgent
    """

    def __init__(self):
        pass

    def perform_action(self, plan: str) -> str:
        """
        For now, simply returns a simulated action response.
        """
        response = f"Action taken based on plan: '{plan}'"
        return response
