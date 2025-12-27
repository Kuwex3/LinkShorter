from fastapi import APIRouter
from fastapi import Form

from pydantic import BaseModel

from backend.midlewares.reduceLink import reduceLink

router = APIRouter()

class Body(BaseModel):
    longLink: str

@router.post("/sendLongLink/")
def testHandler(longLink: Body):
    code = reduceLink(longLink.longLink)
    return code