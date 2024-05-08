from sqlalchemy import Column, String, Integer, Date
from app.config.database import Base
from sqlalchemy.orm import relationship

class Promotion(Base):
    __tablename__ = 'Promotion'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    discount_inscription = Column(Integer, nullable=True)
    month_free = Column(Integer, nullable=True)
    payment_discount = Column(Integer, nullable=True)
    time_start = Column(Date, nullable=True)
    time_end = Column(Date, nullable=True)