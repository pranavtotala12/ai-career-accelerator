from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class AskRequest(BaseModel):
    question: str = Field(min_length=1, max_length=4000)

@app.post("/ask")
def ask(request: AskRequest):
    cleaned_question = request.question.strip()

    return {
        "question": cleaned_question,
        "answer": "LLM will be connected next"
    }

@app.get("/home")
def home():
    return {
        "message": "Week2 AI service is running in home"
    }   

@app.get("/awayhome")
def awayhome():
    return {
        "message": "Week2 AI service is running in awayhome"
    }