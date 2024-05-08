from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Float
from app.config.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'User'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    full_name = Column(String,  nullable=False)
    hashed_password = Column(String, nullable=False)
    disabled= Column(Boolean, nullable=False, default=False)
    rol_id = Column(Integer, ForeignKey("Rol.id"))
    active = Column(Boolean, nullable=False)
    last_latitude = Column(Float)
    last_longitude = Column(Float)
    
    route = relationship("Route", back_populates="user")
    rol = relationship("Rol", back_populates="user")