from sqlalchemy import Column, Integer, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship

class EquipExercise(Base):
    __tablename__ = 'EquipExercise'
    
    id = Column(Integer, primary_key=True, index=True)
    exercise_id = Column(Integer, ForeignKey("Exercise.id"), nullable=False)
    equipment_id = Column(Integer, ForeignKey("Equipment.id"), nullable=False)
        
    exercise = relationship("Exercise", back_populates="equipmentExercise")
    equipment = relationship("Equipment", back_populates="equipmentExercise")