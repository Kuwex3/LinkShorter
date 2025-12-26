from fastapi import APIRouter

from backend.midlewares.reduceLink import reduceLink

router = APIRouter()

@router.post("/sendLongLink/")
def testHandler(longLink: str):
    code = reduceLink(longLink)
    return f"127.0.0.1/{code}"