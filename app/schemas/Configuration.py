from pydantic import BaseModel

class ConfigurationBase(BaseModel):
    exchange_rate: float


class ConfigurationCreate(ConfigurationBase):
    days: list
    
class ConfigurationUpdate(ConfigurationCreate):
    id: int
    schedule_id:int
    
class ConfigurationSave(ConfigurationBase):
    schedule_id: int
    
class Configuration(ConfigurationBase):
    id: int
    
        

    class Config:
        from_attributes = True