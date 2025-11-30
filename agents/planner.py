from utils.gpt_client import GPTClient

class PlannerAgent:
    """
    PlannerAgent: decides how to respond based on user input.
    For simplicity, it passes the text to GPT.
    """
    def __init__(self):
        self.gpt_client = GPTClient()

    def plan(self, user_input: str) -> str:
        """
        Creates a 'plan' — here it’s just sending the input to GPT for a response.
        """
        prompt = f"Respond to the user in a friendly, helpful way: {user_input}"
        return self.gpt_client.ask(prompt)
