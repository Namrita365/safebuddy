class MemoryBank:
    """
    Simple memory to store chat history or previous alerts
    """
    def __init__(self):
        self.history = []

    def add_entry(self, entry: str):
        self.history.append(entry)

    def get_history(self):
        return self.history
