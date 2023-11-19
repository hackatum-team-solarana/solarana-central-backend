from app.schemas.bundesland_enum import Bundesland
from app.utils.db import Base
from sqlalchemy import Column, Integer, Double, String, TIMESTAMP, text as fun_text, ForeignKey, Enum


class MyBase(Base):
    __abstract__ = True

    def to_dict(self):
        return {field.name: getattr(self, field.name) for field in self.__table__.c}


class Offer(MyBase):
    __tablename__ = "offers"

    offer_id = Column(Integer, primary_key=True, nullable=False, index=True)
    owner_pk = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    region = Column(Enum(Bundesland), nullable=False)
    size = Column(Double, nullable=False)
    power = Column(Double, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=fun_text('now()'))

