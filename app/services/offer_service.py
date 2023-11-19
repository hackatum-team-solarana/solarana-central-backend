from typing import Optional

from fastapi import HTTPException
from starlette import status

from app.repositories.offer_repository import offer_repository
from app.schemas.bundesland_enum import Bundesland
from app.schemas.offer_schema import OfferGet, OfferPost


def get_offer_stored(max_age: Optional[int] = None,
                     max_price: Optional[int] = None,
                     min_power: Optional[float] = None,
                     region: Optional[Bundesland] = None
                     ) -> OfferGet:
    if (max_age is not None and max_age < 0) or (max_price is not None and max_price < 0) or (
            min_power is not None and min_power < 0):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Negative values are not allowed")
    return offer_repository.get_offer_by_filter_val(max_age, max_price, min_power, region)


def store_offer(offer: OfferPost) -> OfferGet:
    if offer.price < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Negative values are not allowed")
    if offer.age < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Negative values are not allowed")
    if offer.amount < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Negative values are not allowed")
    if offer.power < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Negative values are not allowed")
    if offer.size < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Negative values are not allowed")
    return offer_repository.create_new_offer(offer)
