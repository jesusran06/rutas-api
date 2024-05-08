from sqlalchemy import Column, Integer, DateTime, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship

class HistoryAsist(Base):
    __tablename__ = 'HistoryAsist'
    
    id = Column(Integer, primary_key=True, index=True)
    dateTimeEntry = Column(DateTime, nullable=False)
    dateTimeExit = Column(DateTime, nullable=True)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    
    user = relationship("User", back_populates="historyAsist")