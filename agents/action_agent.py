class ActionAgent:
    """
    ActionAgent: executes the plan. Here, it just returns GPT's output.
    """
    def perform_action(self, plan: str) -> str:
        # In more complex apps, this could do multiple steps.
        return f"{plan}"  # simply return GPT's response
