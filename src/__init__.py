import azure.functions as func

import fastapi

app = fastapi.FastAPI()

@app.get("/home")
async def index():
    return {
        "info": "This is a home page",
    }


@app.get("/hello/{name}")
async def get_name(name: str):
    return {
        "name": name,
    }