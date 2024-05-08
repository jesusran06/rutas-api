from sqlalchemy import Column, String, Integer
from app.config.database import Base
from sqlalchemy.orm import relationship

class Rol(Base):
    __tablename__ = 'Rol'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    
    user = relationship("User", back_populates="rol")