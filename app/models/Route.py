from sqlalchemy import Column, String, Integer, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship

class Route(Base):
    __tablename__ = 'Route'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey("User.id"))
    
    user = relationship("User", back_populates="route")
    coordenate = relationship("Coordenate", back_populates="route")