# import os
# from dotenv import load_dotenv
# # from openai import OpenAI
# from google import genai

# load_dotenv()

# client = genai.Client(
#     api_key=os.getenv("GEMINI_API_KEY")
# )

# model = os.getenv("GEMINI_MODEL")

# response = client.models.generate_content(
#     model=model,
#     contents="Reply exactly with: Hello LLM"
# )

# print(response.text)

import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing")

client = genai.Client(api_key=api_key)

app = FastAPI()