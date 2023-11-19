from datetime import datetime
from pydantic import BaseModel

from app.schemas.bundesland_enum import Bundesland


class OfferPost(BaseModel):
    owner_pk: str
    age: int
    amount: int
    price: int
    region: Bundesland
    size: float
    power: float


class OfferGet(OfferPost):
    offer_id: int
    owner_pk: str
    age: int
    amount: int
    price: int
    region: Bundesland
    size: float
    power: float
    created_at: datetime
