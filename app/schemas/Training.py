from pydantic import BaseModel
from typing import Optional

class TrainingBase(BaseModel):
    name: str
    client_id: Optional[int] = None
    user_id: int
    schedule_id: Optional[int] = None

class TrainingCreate(TrainingBase):
    pass

class Training(TrainingBase):
    id: int

    class Config:
        from_attributes = True
