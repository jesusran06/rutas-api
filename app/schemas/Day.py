from pydantic import BaseModel

class DayBase(BaseModel):
    name: str

class DayCreate(DayBase):
    pass

class Day(DayBase):
    id: int

    class Config:
        from_attributes = True