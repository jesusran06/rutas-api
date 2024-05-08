from pydantic import BaseModel

class EquipmentBase(BaseModel):
    name: str
    description: str = None
    location: str = None
    quantity: int

class EquipmentCreate(EquipmentBase):
    pass

class Equipment(EquipmentBase):
    id: int

    class Config:
        from_attributes = True