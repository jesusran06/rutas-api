from sqlalchemy import Column, Integer, ForeignKey, Time, Date, Boolean
from app.config.database import Base
from sqlalchemy.orm import relationship

class DaysHours(Base):
    __tablename__ = 'DaysHours'
    
    id = Column(Integer, primary_key=True, index=True)
    day_id = Column(Integer, ForeignKey("Day.id"), nullable=False)
    schedule_id = Column(Integer, ForeignKey("Schedule.id"), nullable=False)
    time_init = Column(Time, nullable=True)
    time_end = Column(Time, nullable=True)
    date = Column(Date, nullable=True)
    routine_id = Column(Integer, ForeignKey("Routine.id"), nullable=True)
    state = Column(Boolean)
    
    day = relationship("Day", back_populates="daysHours")
    schedule = relationship("Schedule", back_populates="daysHours")
    routine = relationship("Routine", back_populates="daysHours")