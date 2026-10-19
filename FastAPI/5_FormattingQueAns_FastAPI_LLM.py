import os
from pathlib import Path
import json
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

# 3. Define request body
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

# 3. Define answer body
class AnswerData(BaseModel):
    answer: str
    topic: str
    confidence: float = Field(ge=0, le=1)

# 4. Create API endpoint
@app.post("/ask")
def ask(request: AskRequest):

    cleaned_question = request.question.strip()

    # Validate question after removing spaces
    if len(cleaned_question) < 5:
        raise HTTPException(
            status_code=400,
            detail="Question must have at least 5 characters"
        )

    structured_prompt = f"""
    Answer the question.
    Return JSON only with:
    - answer: string
    - topic: string
    - confidence: number from 0 to 1
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
        raw = response.text

    except Exception as e:
        print("Gemini error:", str(e))

        raise HTTPException(
            status_code=502,
            detail="Gemini request failed. Please try again."
        ) from e

    # 6. Check for empty response
    if not raw:
        raise HTTPException(
            status_code=502,
            detail="Gemini returned an empty answer"
        )

    # 7. Parse JSON and validate its fields
    try:
        parsed = json.loads(raw)

        # The model must return a JSON object
        if not isinstance(parsed, dict):
            raise ValueError("Expected a JSON object")

        result = AnswerData(**parsed)

    except (ValueError, ValidationError) as e:
        print("Output validation error:", str(e))
        raise HTTPException(
            status_code=502,
            detail="Invalid model output"
        ) from e
    
    # 8. Return response
    return {
        "question": cleaned_question,
        "result": result.model_dump(),
        "model": model,
        "max_output_tokens": request.max_output_tokens
    }
