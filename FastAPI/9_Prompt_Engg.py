import os
from pathlib import Path
import json
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, ValidationError
from google import genai
from google.genai import types

from Structured_Prompt_8 import build_triage_prompt

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
class TriageRequest(BaseModel):
    ticket: str = Field(min_length=5, max_length=4000)


# 3. Define answer body
class TriageResult(BaseModel):
    category: str
    reason: str

# 4. Create API endpoint
@app.post("/triage")
def triage(request: TriageRequest):
    cleaned_ticket = request.ticket.strip()
    prompt = build_triage_prompt(cleaned_ticket)

    response = client.models.generate_content(
        model=model,
        contents=prompt
    )
    ans = response.text
    

    try:
        parsed = json.loads(ans)
        result = TriageResult(**parsed)
    except (json.JSONDecodeError, ValidationError):
        raise HTTPException(
            status_code=502,
            detail="Invalid model output"
        )

    allowed = {"payment", "delivery", "account", "other"}
    if result.category not in allowed:
        raise HTTPException(status_code=502, detail="Unexpected category")

    return result.model_dump()
    
    