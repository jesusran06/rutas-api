from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship

class HistoryAction(Base):
    __tablename__ = 'HistoryAction'
    
    id = Column(Integer, primary_key=True, index=True)
    action = Column(String, nullable=False)
    dateAction = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    
    user = relationship("User", back_populates="historyAction")