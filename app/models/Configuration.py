from sqlalchemy import Column, Float, Integer, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship

class Configuration(Base):
    __tablename__ = 'Configuration'
    
    id = Column(Integer, primary_key=True, index=True)
    exchange_rate = Column(Float, nullable=False)
    schedule_id = Column(Integer, ForeignKey('Schedule.id'), nullable=False)
    
    schedule = relationship("Schedule", back_populates="configuration")