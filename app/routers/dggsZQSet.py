from fastapi import APIRouter
from rheal import *
from rhealsf import *

router = APIRouter(prefix="/dggs/rHEALPix/zone", tags=["zoneQuerySet"])


@router.get("/{ZonalID}/buffer")
async def buffer(ZonalID: str):
    """Get the list of zonalId that are within a buffer of dist from the given zoneId"""
    return {"result": "Not yet implemented"}


@router.get("/{ZonalID}/difference")
async def difference(ZonalID: str, otherZonalID: str):
    """Get the list of zonalID that are the result of zoneId.difference(another)"""
    return {"result": (Cell(ZonalID) - Cell(otherZonalID)).wkt}


@router.get("/{ZonalID}/intersection")
async def intersection(ZonalID: str, otherZonalID: str):
    """Get the list of zonalID that are the result of zoneId.intersection(another)"""
    # as we're dealing with single zones, can use contains/within
    if sfContains(ZonalID, otherZonalID):
        return [{"result": otherZonalID.wkt}]
    elif sfWithin(ZonalID, otherZonalID):
        return [{"result": ZonalID.wkt}]
    elif sfEquals(ZonalID, otherZonalID):
        return [{"result": ZonalID.wkt}]


@router.get("/{ZonalID}/symDifference")
async def symDifference(ZonalID: str, otherZonalID: str):
    """Get the list of zonalID that are the result of zoneId.symDifference(another)"""
    return {"result": (Cell(ZonalID) - Cell(otherZonalID)).wkt}


@router.get("/{ZonalID}/union")
async def union(ZonalID: str, otherZonalID: str):
    """Get the list of zonalID that are the result of zoneId.union(another)"""
    return {"ZonalIDs": (Cell(ZonalID) + Cell(otherZonalID)).wkt}


@router.get("/{ZonalID}/children")
async def children(ZonalID: str):
    """Get the list of zones children of a given zone"""
    return {"result": Cell(ZonalID).children().wkt}


@router.get("/{ZonalID}/parent")
async def parent(ZonalID: str):
    """Get the list of zones parents of a given zone"""
    return {"result": "Not yet implemented"}


@router.get("/{ZonalID}/sibling")
async def sibling(ZonalID: str):
    """Get the list of zones siblings of a given zone"""
    return {"result": Cell(ZonalID).neighbours().wkt}
