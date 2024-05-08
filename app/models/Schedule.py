from sqlalchemy import Column, String, Integer, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship

class Schedule(Base):
    __tablename__ = 'Schedule'
    
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=True)
    type = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=True)
    
    user = relationship("User", back_populates="schedule")
    training = relationship("Training", back_populates="schedule")
    daysHours = relationship("DaysHours", back_populates="schedule")
    configuration = relationship("Configuration", back_populates="schedule")