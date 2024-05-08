from sqlalchemy import Column, Integer, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship

class RoutineExercise(Base):
    __tablename__ = 'RoutineExercise'
    
    id = Column(Integer, primary_key=True, index=True)
    routine_id = Column(Integer, ForeignKey("Routine.id"), nullable=False)
    exercise_id = Column(Integer, ForeignKey("Exercise.id"), nullable=False)
    
    exercise = relationship("Exercise", back_populates="routineExercise")
    routine = relationship("Routine", back_populates="routineExercise")