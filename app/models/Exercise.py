from sqlalchemy import Column, String, Integer
from app.config.database import Base
from sqlalchemy.orm import relationship

class Exercise(Base):
    __tablename__ = 'Exercise'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description= Column(String, nullable=True)
    difficulty= Column(String, nullable=False)
    equipment_id = Column(Integer, nullable=True)
    
    routineExercise = relationship("RoutineExercise", back_populates="exercise")
    equipmentExercise = relationship("EquipExercise", back_populates="exercise")