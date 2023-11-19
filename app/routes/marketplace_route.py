from typing import Optional

from fastapi import APIRouter, Query
from starlette import status

from app.schemas.bundesland_enum import Bundesland
from app.schemas.offer_schema import OfferGet, OfferPost
from app.services import offer_service

router = APIRouter(
    prefix="/marketplace",
    tags=['Message']
)


@router.get("/order", response_model=list[OfferGet])
async def get_offer(
        max_age: Optional[int] = Query(None),
        max_price: Optional[int] = Query(None),
        min_power: Optional[float] = Query(None),
        region: Optional[Bundesland] = Query(None)
):
    return offer_service.get_offer_stored(max_age, max_price, min_power, region)


@router.post("/order", status_code=status.HTTP_201_CREATED, response_model=OfferGet)
async def post_offer(offer: OfferPost):
    return offer_service.store_offer(offer)
