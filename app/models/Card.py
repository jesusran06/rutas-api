from sqlalchemy import Column, String, Integer, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship

class Card(Base):
    __tablename__ = "Card"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(String)
    client_id = Column(Integer, ForeignKey("Client.id"), unique=True)
    
    client = relationship("Client", back_populates="card")