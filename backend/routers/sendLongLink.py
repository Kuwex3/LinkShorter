from fastapi import APIRouter

from backend.midlewares.reduceLink import reduceLink

router = APIRouter()

@router.post("/sendLongLink/")
def testHandler(longLink: str):
    reduceLink(longLink)
    return longLink