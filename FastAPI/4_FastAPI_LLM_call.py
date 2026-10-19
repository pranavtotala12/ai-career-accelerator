# import os
# from dotenv import load_dotenv
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, Field
# from google import genai

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# model = os.getenv("GEMINI_MODEL")

# if not api_key:
#     raise RuntimeError("GEMINI_API_KEY is missing")


# client = genai.Client   (api_key=api_key)
# app = FastAPI()

# # Define the request body BEFORE using it
# class AskRequest(BaseModel):
#     question: str = Field(..., min_length=1)


# @app.post("/ask")
# def ask(request: AskRequest):
#     cleaned_question = request.question.strip()

#     if not cleaned_question:
#         raise HTTPException(
#             status_code=400,
#             detail="Question cannot be blank"
#         )

#     try:
#         response = client.models.generate_content(
#             model=model,
#             contents=cleaned_question
#         )
#     except Exception:
#         raise HTTPException(
#             status_code=502,
#             detail="Gemini request failed. Please try again."
#         )

#     return {
#         "question": cleaned_question,
#         "answer": response.text,
#         "model": model
#     }

###################################################################################

import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from google import genai

# Load configuration
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path, override=True)

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing")

if not model:
    raise RuntimeError("GEMINI_MODEL is missing")

client = genai.Client(api_key=api_key)
app = FastAPI()

# Define the request body BEFORE using it
class AskRequest(BaseModel):
    question: str = Field(..., min_length=1)

@app.post("/ask")
def ask(request: AskRequest):
    cleaned_question = request.question.strip()

    if not cleaned_question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be blank"
        )

    try:
        response = client.models.generate_content(
            model=model,
            contents=cleaned_question
        )
    except Exception:
        raise HTTPException(
            status_code=502,
            detail="Gemini request failed. Please try again."
        )

    return {
        "question": cleaned_question,
        "answer": response.text,
        "model": model
    }