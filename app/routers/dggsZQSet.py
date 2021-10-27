from fastapi import APIRouter

router = APIRouter(prefix="/dggs/rHEALPix/zone", tags=["zoneQuerySet"])


@router.get("/{ZonalID}/buffer")
async def buffer(ZonalID):
    """Get the list of zonalId that are within a buffer of dist from the given zoneId"""
    return [{"ZonalID": ZonalID}]


@router.get("/{ZonalID}/difference")
async def difference(ZonalID):
    """Get the list of zonalID that are the result of zoneId.difference(another)"""
    return {"ZonalID": ZonalID}
