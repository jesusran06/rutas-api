from pydantic import BaseModel

class ExerciseBase(BaseModel):
    name: str
    description: str = None
    difficulty: str
    equipment_id: int = None

class ExerciseCreate(ExerciseBase):
    pass

class Exercise(ExerciseBase):
    id: int

    class Config:
        from_attributes = True