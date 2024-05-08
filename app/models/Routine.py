from sqlalchemy import Column, String, Integer
from app.config.database import Base
from sqlalchemy.orm import relationship

class Routine(Base):
    __tablename__ = 'Routine'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    
    routineExercise = relationship("RoutineExercise", back_populates="routine")
    daysHours = relationship("DaysHours", back_populates="routine")