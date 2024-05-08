from sqlalchemy import Column, String, Integer, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship

class PlanTraining(Base):
    __tablename__ = 'PlanTraining'
    
    id = Column(Integer, primary_key=True, index=True)
    plan_id = Column(Integer, ForeignKey('Plan.id'), nullable=False)
    training_id = Column(Integer, ForeignKey('Training.id'), nullable=False)
    
    plan = relationship("Plan", back_populates="planTraining")
    training = relationship("Training", back_populates="planTraining")