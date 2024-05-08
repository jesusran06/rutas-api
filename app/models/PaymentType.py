from sqlalchemy import Column, String, Integer
from app.config.database import Base
from sqlalchemy.orm import relationship

class PaymentType(Base):
    __tablename__ = 'PaymentType'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    ref = Column(String, nullable=False)
    
    payment = relationship("Payment", back_populates="paymentType")