from pydantic import BaseModel
from datetime import date

class SubscriptionBase(BaseModel):
    client_id: int
    plan_id: int
    subscription_date: date

class SubscriptionCreate(SubscriptionBase):
    pass

class Subscription(SubscriptionBase):
    id: int

    class Config:
        from_attributes = True
