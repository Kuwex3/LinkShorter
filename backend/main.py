from fastapi import FastAPI
from backend.routers.test import router as testRouter

app = FastAPI()

@app.get("/")
def mainPage():
    return "Hello, World!"

app.include_router(testRouter)