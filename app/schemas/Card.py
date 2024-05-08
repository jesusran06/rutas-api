from pydantic import BaseModel

class CardBase(BaseModel):
    number: str
    client_id: int

class CardCreate(CardBase):
    pass

class Card(CardBase):
    id: int

    class Config:
        from_attributes = True