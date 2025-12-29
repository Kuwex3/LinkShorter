from fastapi import FastAPI
from backend.routers.sendLongLink import router as sendLongRouter
from backend.routers.redirectByLink import router as redirectRouter

app = FastAPI()

app.include_router(sendLongRouter)
app.include_router(redirectRouter)

@app.get("/")
def mainPage():
    return "Hello, world!"