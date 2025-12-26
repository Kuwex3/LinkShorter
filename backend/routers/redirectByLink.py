from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from backend.midlewares.getFullLink import getFullLinkByCode

router = APIRouter()

@router.get("/{code}")
def redirect(code: str):
    fullLink = getFullLinkByCode(code)
    cleanUrl = fullLink.strip().strip("'")
    return RedirectResponse(url=cleanUrl)