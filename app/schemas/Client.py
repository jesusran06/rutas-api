from pydantic import BaseModel
from typing import Optional
from datetime import date

class ClientBase(BaseModel):
    ci: int
    ci_type: Optional[str] = None
    name: str
    last_name: str
    plan_id: int
    promotion_id: Optional[int] = None
    status: str
    due_date: date

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int

    class Config:
        from_attributes = True