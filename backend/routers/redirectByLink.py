from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from backend.midlewares.getFullLink import getFullLinkByCode

router = APIRouter()

@router.get("/{code}")
def redirect(code: str):
    fullLink = getFullLinkByCode(code)
    if type(fullLink) != TypeError:
        cleanUrl = fullLink.strip().strip("'")
        return RedirectResponse(url=cleanUrl)
    else: 
        raise HTTPException(status_code=404)