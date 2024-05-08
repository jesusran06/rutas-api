from sqlalchemy import Column, String, Integer, Float
from app.config.database import Base
from sqlalchemy.orm import relationship

class Plan(Base):
    __tablename__ = 'Plan'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price= Column(Float, nullable=False)
    
    suscription = relationship("Suscription", back_populates="plan")
    planTraining = relationship("PlanTraining", back_populates="plan")