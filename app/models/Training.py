from sqlalchemy import Column, String, Integer, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship

class Training(Base):
    __tablename__ = 'Training'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    schedule_id = Column(Integer, ForeignKey("Schedule.id"), nullable=True)
    
    planTraining = relationship("PlanTraining", back_populates="training")
    schedule = relationship("Schedule", back_populates="training")