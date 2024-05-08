from pydantic import BaseModel
from app.schemas.Coordenate import Coordenate
from typing import List
class Route(BaseModel):
    name:str
    user_id: int
    
class RouteFront(Route):
    coordenates: List[Coordenate]