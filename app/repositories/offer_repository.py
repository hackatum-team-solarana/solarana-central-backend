from typing import Optional

from fastapi import HTTPException

from app.schemas.bundesland_enum import Bundesland
from app.schemas.offer_schema import OfferGet, OfferPost
from app.utils.db import get_db
from app.models import offers
from starlette import status


class OfferRepository:
    def __init__(self):
        self.db = next(get_db())

    def get_offer_by_filter_val(self,
                                max_age: Optional[int] = None,
                                max_price: Optional[int] = None,
                                min_power: Optional[float] = None,
                                region: Optional[Bundesland] = None
                                ) -> list[OfferGet]:
        offer = self.db.query(offers.Offer)

        if max_age:
            offer = offer.filter(offers.Offer.age <= max_age)
        if max_price:
            offer = offer.filter(offers.Offer.price <= max_price)
        if min_power:
            offer = offer.filter(offers.Offer.power >= min_power)
        if region:
            offer = offer.filter(offers.Offer.region == region)
        offer_list = offer.all()

        if not offer_list:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Offer not found for your selection")

        return [OfferGet(**offer.to_dict()) for offer in offer_list]

    def create_new_offer(self, offer: OfferPost) -> OfferGet:
        new_offer = offers.Offer(**offer.model_dump())
        self.db.add(new_offer)
        self.db.commit()
        self.db.refresh(new_offer)
        return OfferGet(**new_offer.to_dict())


offer_repository = OfferRepository()
