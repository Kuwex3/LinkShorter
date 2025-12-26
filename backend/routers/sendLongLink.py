from fastapi import APIRouter

router = APIRouter()

@router.post("/sendLongLink{longLink}")
def testHandler(longLink: str):
    return longLink