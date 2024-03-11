from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.config.database import Base

class Coordenate(Base):
    __tablename__ = 'Coordenate'
    
    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    order = Column(Integer)
    route_id = Column(Integer, ForeignKey("Route.id"))
    route = relationship("Route", back_populates="coordenate")