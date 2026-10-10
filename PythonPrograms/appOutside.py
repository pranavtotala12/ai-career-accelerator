#Explorer = create file
#Editor = write code
#Terminal = run server

from fastapi import FastAPI

app = FastAPI()

@app.get("/Outsidehome")
def home():
    return {
        "message": "Week2 AI service is running Outside home"
    }   

@app.get("/Outsideawayhome")
def awayhome():
    return {
        "message": "Week2 AI service is running Outside awayhome"
    }