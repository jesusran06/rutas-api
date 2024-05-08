from pydantic import BaseModel

class PaymentTypeBase(BaseModel):
    name: str
    ref: str

class PaymentTypeCreate(PaymentTypeBase):
    pass

class PaymentType(PaymentTypeBase):
    id: int

    class Config:
        from_attributes = True