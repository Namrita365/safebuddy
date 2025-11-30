import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Configure your Google Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class GPTClient:
    def __init__(self):
        self.model = genai.GenerativeModel("models/gemini-2.5-flash")  # choose a working model

    def ask(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"
