from pydantic import BaseModel
from typing import Union

class Coordenate(BaseModel):
    latitude: float
    longitude:  float
    order: int