from pydantic import BaseModel
from typing import Optional, List
from datetime import time

class Day(BaseModel):
    day_id: int
    start_time: time
    end_time: time
    
class ScheduleBase(BaseModel):
    description: Optional[str] = None
    type: Optional[str] = None
    user_id: Optional[int] = None
    
class ScheduleDays(ScheduleBase):
    days: Optional[List[Day]] = None


class ScheduleCreate(ScheduleBase):
    pass

class Schedule(ScheduleBase):
    id: int

class viewConfigSchedule(BaseModel):
    schedule_id: int
    schedule_description: str
    # schedule_type: str
    day_id: int
    day_name: str
    day_time_init: Optional[time]
    day_time_end: Optional[time]
    state: bool

    class Config:
        from_attributes = True
