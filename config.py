import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file
load_dotenv()

# Choose correct model
GEMINI_MODEL = "models/gemini-2.5-pro"

# Configure Gemini with your API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
