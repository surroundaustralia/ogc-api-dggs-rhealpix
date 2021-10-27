from fastapi import APIRouter
from rheal import *
from rhealsf import *

router = APIRouter(prefix="/dggs/rHEALPix/zone", tags=["zoneQueryQuery"])


@router.get("/{ZonalID}/relativePosition")
async def relativePosition(ZonalID, otherZonalID):
    return "Not yet implemented"


@router.get("/{ZonalID}/contains")
async def contains(ZonalID, otherZonalID):
    """Test if the current ZoneId contains another ZonalID"""
    return sfContains(ZonalID, otherZonalID)


@router.get("/{ZonalID}/crosses")
async def crosses(ZonalID, otherZonalID):
    return "Not yet implemented"


@router.get("/{ZonalID}/disjoint")
async def disjoint(ZonalID, otherZonalID):
    """Test if the current ZoneId is disjoint another ZonalID"""
    return sfDisjoint(ZonalID, otherZonalID)


@router.get("/{ZonalID}/equals")
async def equals(ZonalID, otherZonalID):
    """Test if the current ZoneId equals another ZonalID"""
    return sfEquals(ZonalID, otherZonalID)


@router.get("/{ZonalID}/intersects")
async def intersects(ZonalID, otherZonalID):
    """Test if the current ZoneId intersects another ZonalID"""
    return sfIntersects(ZonalID, otherZonalID)


@router.get("/{ZonalID}/overlaps")
async def overlaps(ZonalID, otherZonalID):
    """Test if the current ZoneId overlaps another ZonalID"""
    return sfOverlaps(ZonalID, otherZonalID)


@router.get("/{ZonalID}/touches")
async def intersects(ZonalID, otherZonalID):
    """Test if the current ZoneId touches another ZonalID"""
    return sfTouches(ZonalID, otherZonalID)


@router.get("/{ZonalID}/within")
async def within(ZonalID, otherZonalID):
    """Test if the current ZoneId within another ZonalID"""
    return sfIntersects(ZonalID, otherZonalID)


@router.get("/{ZonalID}/withinDistance")
async def withinDistance(ZonalID, otherZonalID):
    """Test if the current ZoneId withinDistance another ZonalID"""
    return "Not yet implemented"


@router.get("/{ZonalID}/childOf")
async def childOf(ZonalID, otherZonalID, direct=True):
    """Test if the current ZoneId childOf another ZonalID"""
    if direct:
        return ZonalID in Cell(otherZonalID).children()
    else:
        return sfWithin(ZonalID, Cell(otherZonalID).children())


@router.get("/{ZonalID}/parentOf")
async def parentOf(ZonalID, otherZonalID):
    """Test if the current ZoneId parentOf another ZonalID"""
    return "Not yet implemented"


@router.get("/{ZonalID}/siblingOf")
async def siblingOf(ZonalID, otherZonalID):
    """Test if the current ZoneId siblingOf another ZonalID"""
    return "Not yet implemented"
