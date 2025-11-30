class EvaluatorAgent:
    """
    Evaluator Agent:
    - Evaluates the result from ActionAgent
    - Returns the final response to display to the user
    """

    def __init__(self):
        pass

    def evaluate(self, action_response: str) -> str:
        """
        For now, simply appends a confirmation message
        """
        evaluation = f"{action_response} ✅ (SafeBuddy confirms)"
        return evaluation
