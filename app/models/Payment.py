from sqlalchemy import Column, String, Integer, Float, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship

class Payment(Base):
    __tablename__ = 'Payment'
    
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=True)
    mount = Column(Float, nullable=False)
    exchange_rate = Column(Float, nullable=False)
    type_id = Column(Integer, ForeignKey("PaymentType.id"), nullable=False)
    client_id = Column(Integer, ForeignKey("Client.id"), nullable=False)
    
    client = relationship("Client", back_populates="payment")
    paymentType = relationship("PaymentType", back_populates="payment")