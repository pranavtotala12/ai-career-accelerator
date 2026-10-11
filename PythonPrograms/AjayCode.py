import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing. Add your Gemini API key to the .env file.")

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model=model,
    contents="Reply exactly with: Hello LLM"
)
print(response.text)