from pydantic import BaseModel

class PlanBase(BaseModel):
    name: str
    description: str = None
    price: float

class PlanCreate(PlanBase):
    pass

class Plan(PlanBase):
    id: int

    class Config:
        from_attributes = True