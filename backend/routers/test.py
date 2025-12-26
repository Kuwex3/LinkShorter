from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def testHandler():
    return "TEST STR"