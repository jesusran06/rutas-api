from pydantic import BaseModel
from typing import Optional

class PaymentBase(BaseModel):
    description: Optional[str] = None
    mount: float
    exchange_rate: float
    type_id: int
    client_id: int

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int

    class Config:
        from_attributes = True