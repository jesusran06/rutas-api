from sqlalchemy import Column, Integer, Date, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship

class Suscription(Base):
    __tablename__ = 'Suscription'
    
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("Client.id"), nullable=False)
    plan_id = Column(Integer, ForeignKey("Plan.id"), nullable=False)
    suscription_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable = False)
    
    client = relationship("Client", back_populates="suscription")
    plan = relationship("Plan", back_populates="suscription")