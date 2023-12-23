from fastapi import FastAPI, status

app = FastAPI()

@app.get("/home")
def home():
    return {"message":"Hello World!"}


@app.get("/about")
def about():
    return {"message":"This is an about page"}