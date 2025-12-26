from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from backend.midlewares.getFullLink import getFullLinkByCode

router = APIRouter()

@router.get("/{code}")
def redirect(code: str):
    fullLink = getFullLinkByCode(code)
    return RedirectResponse(url=fullLink[0])