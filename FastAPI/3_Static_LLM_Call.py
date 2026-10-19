import os
from dotenv import load_dotenv
from google import genai

load_dotenv()                                       # Load environment variables from .env
api_key = os.getenv("GEMINI_API_KEY")               # Get the Gemini API key
model = os.getenv("GEMINI_MODEL", "gemini-3.8-flash") # Get the Gemini model name

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing. Add your Gemini API key to the .env file.")

client = genai.Client(api_key=api_key)              # Create a Gemini client using the API key
                                                    #client is used to make concversations with the Gemini API

response = client.models.generate_content(          #call the Gemini API to generate content
    model=model,
    contents="Reply exactly with: Hello LLM"
)

print(response.text)