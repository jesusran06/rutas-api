from pydantic import BaseModel
from typing import Union

class User(BaseModel):
    email:str
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None
    password:  str = ""
    rol: int = None
    active: bool = None
    last_latitude: Union[float, None] = None
    last_longitude: Union[float, None] = None
    
class UserInDb(User):
    hashed_password: str
    
class UserActUbi(BaseModel): 
    active: bool = False
    last_latitude: float = None
    last_longitude: float = None