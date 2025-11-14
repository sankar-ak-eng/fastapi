from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.sessions import engine,get_db
from app.db.base import Base
from app.models.product import Product
from app.schemas.product_schema import Product as ProductSchema


products = [
    ProductSchema(id=1, name="Laptop", price=999.99, quantity=10, description="A high-performance laptop"),
    ProductSchema(id=2, name="Smartphone", price=499.99, quantity=25, description="A latest model smartphone"),
    ProductSchema(id=3, name="Headphones", price=199.99, quantity=15, description="Noise-cancelling headphones"),
]

def init_db():
    print("🔧 Creating tables if not exist...")
    db: Session = next(get_db())

    count = db.query(Product).count()
    if count == 0:
        for pro in products:
           db.add(Product(**pro.dict()))

        db.commit()
        
    Base.metadata.create_all(bind=engine)
