from fastapi import APIRouter
from rheal import *
from rhealsf import *

router = APIRouter(prefix="/dggs/rHEALPix/zone", tags=["zoneQueryQuery"])

# TODO limit input to single ZonalID


@router.get("/{ZonalID}/relativePosition")
async def relativePosition(ZonalID, otherZonalID: str):
    return {"result": "Not yet implemented"}


@router.get("/{ZonalID}/contains")
async def contains(ZonalID: str, otherZonalID: str):
    """Test if the current ZoneId contains another ZonalID"""
    return {"result": sfContains(ZonalID, otherZonalID)}


@router.get("/{ZonalID}/crosses")
async def crosses(ZonalID: str, otherZonalID: str):
    return {"result": "Not yet implemented"}


@router.get("/{ZonalID}/disjoint")
async def disjoint(ZonalID: str, otherZonalID: str):
    """Test if the current ZoneId is disjoint another ZonalID"""
    return {"result": sfDisjoint(ZonalID, otherZonalID)}


@router.get("/{ZonalID}/equals")
async def equals(ZonalID: str, otherZonalID: str):
    """Test if the current ZoneId equals another ZonalID"""
    return {"result": sfEquals(ZonalID, otherZonalID)}


@router.get("/{ZonalID}/intersects")
async def intersects(ZonalID: str, otherZonalID: str):
    """Test if the current ZoneId intersects another ZonalID"""
    return {"result": sfIntersects(ZonalID, otherZonalID)}


@router.get("/{ZonalID}/overlaps")
async def overlaps(ZonalID: str, otherZonalID: str):
    """Test if the current ZoneId overlaps another ZonalID"""
    return {"result": sfOverlaps(ZonalID, otherZonalID)}


@router.get("/{ZonalID}/touches")
async def intersects(ZonalID: str, otherZonalID: str):
    """Test if the current ZoneId touches another ZonalID"""
    return {"result": sfTouches(ZonalID, otherZonalID)}


@router.get("/{ZonalID}/within")
async def within(ZonalID: str, otherZonalID: str):
    """Test if the current ZoneId within another ZonalID"""
    return {"result": sfIntersects(ZonalID, otherZonalID)}


@router.get("/{ZonalID}/withinDistance")
async def withinDistance(ZonalID: str, otherZonalID: str):
    """Test if the current ZoneId withinDistance another ZonalID"""
    return {"result": "Not yet implemented"}


@router.get("/{ZonalID}/childOf")
async def childOf(ZonalID, otherZonalID, direct=True):
    """Test if the current ZoneId childOf another ZonalID"""
    if direct:
        return {"result": ZonalID in Cell(otherZonalID).children()}
    else:
        return {"result": sfWithin(ZonalID, Cell(otherZonalID).children())}


@router.get("/{ZonalID}/parentOf")
async def parentOf(ZonalID: str, otherZonalID: str):
    """Test if the current ZoneId parentOf another ZonalID"""
    return {"result": "Not yet implemented"}


@router.get("/{ZonalID}/siblingOf")
async def siblingOf(ZonalID: str, otherZonalID: str):
    """Test if the current ZoneId siblingOf another ZonalID"""
    return {"result": "Not yet implemented"}
