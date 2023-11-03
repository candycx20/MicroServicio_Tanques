from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"
    
    id = Column(Integer, primary_key=True, index=True)
    dpi = Column(String(50), default=None)
    nombre = Column(String(50), default=None)
    puntos = Column(Float(50), default=None)
    createdAt = Column(Date, nullable=False)
    updatedAt = Column(Date)