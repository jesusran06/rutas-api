from pydantic import BaseModel

class RoutineBase(BaseModel):
    name: str

class RoutineCreate(RoutineBase):
    pass

class Routine(RoutineBase):
    id: int

    class Config:
        from_attributes = True
