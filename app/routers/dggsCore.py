from fastapi import APIRouter
from rheal import *

router = APIRouter(prefix="/dggs", tags=["dggsCore"])


@router.get("/")
async def dggs():
    """Currently this API only implements rHEALPix, and uses default parameters for this."""


@router.get("/{dggsRSID}")
async def dggsRSID():
    """Currently this API only implements rHEALPix, and uses default parameters for this."""


@router.get("/{dggsRSID}/zones/")
async def zones():
    """Zones have suids starting with one of {N,O,P,Q,R,S}, and have 0-15 digits following, each in the range (0,8),
    for example N, N1, or N123456789123456
    """


@router.get("/rHEALPix/zone/{ZonalID}")
async def zone(ZonalID):
    return {"Cell": Cell(ZonalID)}
