from pydantic import BaseModel
from typing import Optional
from datetime import date

class UserBase(BaseModel):
    ci: int
    ci_type: Optional[str] = None
    name: str
    last_name: str
    phone: Optional[int] = None
    password:  str
    rol_id: int
    active: bool
    dateBird: date
    created_at: date
    updated_at: date

class UserCreate(UserBase):
    pass

class UserInDb(UserBase):
    hashed_password: str
    
class User(UserBase):
    id: int

    class Config:
        from_attributes = True










# from pydantic import BaseModel
# from typing import Union

# class User(BaseModel):
#     email:str
#     full_name: Union[str, None] = None
#     disabled: Union[bool, None] = None
#     password:  str = ""
#     rol: int = None
#     active: bool = None
#     last_latitude: Union[float, None] = None
#     last_longitude: Union[float, None] = None
    
# class UserInDb(User):
#     hashed_password: str
    
# class UserActUbi(BaseModel): 
#     active: bool = False
#     last_latitude: float = None
#     last_longitude: float = None