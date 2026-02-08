from fastapi import FastAPI
from routers.sendLongLink import router as sendLongRouter
from routers.redirectByLink import router as redirectRouter

app = FastAPI()

app.include_router(sendLongRouter)
app.include_router(redirectRouter)

@app.get("/")
def mainPage():
    return "Hello, world!"