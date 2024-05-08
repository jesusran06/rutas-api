from sqlalchemy import Column, String, Integer
from app.config.database import Base
from sqlalchemy.orm import relationship

class Day(Base):
    __tablename__ = 'Day'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    
    daysHours = relationship("DaysHours", back_populates="day")