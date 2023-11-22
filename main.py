from fastapi import FastAPI, status

app = FastAPI()

@app.get("/home")
def home():
    return {"message":"Hello MCC!!!"}