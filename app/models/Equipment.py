from sqlalchemy import Column, String, Integer
from app.config.database import Base
from sqlalchemy.orm import relationship

class Equipment(Base):
    __tablename__ = 'Equipment'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    location = Column(String, nullable=True)
    quantity = Column(Integer, nullable= False)
    
    equipmentExercise = relationship("EquipExercise", back_populates="equipment")