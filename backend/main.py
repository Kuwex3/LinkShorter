from fastapi import FastAPI
from backend.routers.sendLongLink import router as sendLongRouter

app = FastAPI()

app.include_router(sendLongRouter)