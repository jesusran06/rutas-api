from sqlalchemy import Column, String, Integer, ForeignKey, Date
from app.config.database import Base
from sqlalchemy.orm import relationship

class Client(Base):
    __tablename__ = 'Client'
    
    id = Column(Integer, primary_key=True, index=True)
    ci = Column(Integer, nullable=False, unique=True)
    ci_type = Column(String, nullable=True)
    name = Column(String,  nullable=False)
    last_name = Column(String, nullable=False)
    status = Column(String, nullable = False)
    
    card = relationship("Card", uselist=False, back_populates="client")
    suscription = relationship("Suscription", back_populates= "client")
    payment = relationship("Payment", back_populates="client")