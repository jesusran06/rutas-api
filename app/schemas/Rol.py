from pydantic import BaseModel

class RolBase(BaseModel):
    name: str

class RolCreate(RolBase):
    pass

class Rol(RolBase):
    id: int

    class Config:
        from_attributes = True
