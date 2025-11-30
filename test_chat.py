from config import GEMINI_MODEL
import google.generativeai as genai

# Load the model
model = genai.GenerativeModel(GEMINI_MODEL)

# Test message
response = model.generate_content("Hello! Is Gemini connected?")

print(response.text)
