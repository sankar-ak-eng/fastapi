from sqlalchemy import Column, Integer, String, Float, Text
from app.db.base_class import Base

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Integer)
    description = Column(Text)