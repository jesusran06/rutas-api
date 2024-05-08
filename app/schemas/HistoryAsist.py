from pydantic import BaseModel
from datetime import datetime

class HistoryAsistBase(BaseModel):
    dateTimeEntry: datetime
    dateTimeExit: datetime = None
    user_id: int

class HistoryAsistCreate(HistoryAsistBase):
    pass

class HistoryAsist(HistoryAsistBase):
    id: int

    class Config:
        from_attributes = True