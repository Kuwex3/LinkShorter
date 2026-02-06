from fastapi import APIRouter

from pydantic import BaseModel

from backend.midlewares.reduceLink import reduceLink

router = APIRouter()

class Long_link_model(BaseModel):
    long_link: str

@router.post("/sendLongLink/")
def testHandler(longLink: Long_link_model):
    code = reduceLink(longLink.long_link)
    return code