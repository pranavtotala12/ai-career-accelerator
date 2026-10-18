
import os
import json
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, ValidationError
from google import genai
from google.genai import types

# 1. Load configuration
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path, override=True)

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing")

if not model:
    raise RuntimeError("GEMINI_MODEL is missing")

# 2. Initialize Gemini and FastAPI
client = genai.Client(api_key=api_key)
app = FastAPI()


# 3. Define request and response models
class AskRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=5,
        max_length=4000
    )

    max_output_tokens: int = Field(
        default=250,
        ge=1,
        le=2000
    )


class AnswerData(BaseModel):
    answer: str
    topic: str
    confidence: float = Field(ge=0, le=1)


# 4. Create API endpoint
@app.post("/ask")
def ask(request: AskRequest):

    cleaned_question = request.question.strip()

    if len(cleaned_question) < 5:
        raise HTTPException(
            status_code=400,
            detail="Question must have at least 5 characters"
        )

    structured_prompt = f"""
    Answer the question accurately.

    Return these fields:
    - answer: a string containing the answer
    - topic: a short topic label
    - confidence: a number between 0 and 1

    Question: {cleaned_question}
    """

    # 5. Call Gemini
    try:
        response = client.models.generate_content(
            model=model,
            contents=structured_prompt,
            config=types.GenerateContentConfig(
                max_output_tokens=request.max_output_tokens,
                response_mime_type="application/json",
                response_schema=AnswerData
            )
        )

    except Exception as e:
        print("Gemini error:", str(e))
        raise HTTPException(
            status_code=502,
            detail="Gemini request failed. Please try again."
        ) from e

    # 6. Check for empty response
    raw = response.text

    if not raw or not raw.strip():
        raise HTTPException(
            status_code=502,
            detail="Gemini returned an empty response"
        )

    # 7. Parse and validate JSON
    try:
        parsed = json.loads(raw)
        result = AnswerData.model_validate(parsed)

    except (json.JSONDecodeError, ValidationError, TypeError):
        raise HTTPException(
            status_code=502,
            detail="Invalid model output"
        )

    # 8. Return response
    return {
        "question": cleaned_question,
        "result": result.model_dump(),
        "model": model,
        "max_output_tokens": request.max_output_tokens
    }
