from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Date, BigInteger
from app.config.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'User'
    
    id = Column(Integer, primary_key=True, index=True)
    ci = Column(Integer, unique=True, nullable=False)
    ci_type = Column(String, nullable=True)
    name = Column(String,  nullable=False)
    last_name = Column(String, nullable=False)
    phone = Column(BigInteger, nullable=True)
    hashed_password = Column(String, nullable=False)
    rol_id = Column(Integer, ForeignKey("Rol.id"), nullable=False)
    active = Column(Boolean, nullable=False)
    date = Column(Date, nullable=False)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=False)
    
    
    rol = relationship("Rol", back_populates="user")
    schedule = relationship("Schedule", back_populates="user")
    historyAsist = relationship("HistoryAsist", back_populates="user")
    historyAction = relationship("HistoryAction", back_populates="user")