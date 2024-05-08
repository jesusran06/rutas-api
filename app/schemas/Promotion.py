from pydantic import BaseModel
from typing import Optional
from datetime import date

class PromotionBase(BaseModel):
    name: str
    description: Optional[str] = None
    discount_inscription: Optional[int] = None
    month_free: Optional[int] = None
    payment_discount: Optional[int] = None
    time_start: Optional[date] = None
    time_end: Optional[date] = None

class PromotionCreate(PromotionBase):
    pass

class Promotion(PromotionBase):
    id: int

    class Config:
        from_attributes = True
