from fastapi import FastAPI
from .schemas.product_schema import Product

app = FastAPI(title="FastAPI Project")


products = [
    Product(id=1, name="Laptop", price=999.99, quantity=10, description="A high-performance laptop"),
    Product(id=2, name="Smartphone", price=499.99, quantity=25, description="A latest model smartphone"),
    Product(id=3, name="Headphones", price=199.99, quantity=15, description="Noise-cancelling headphones"),
]

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/product/all")
async def get_all_products():
    return products

@app.get("/product/{product_id}")
async def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"error": "Product not found"}

@app.post("/product/add")
async def add_product(product:Product):
    products.append(product)
    return product

@app.post("/product/put/{id}")
async def put_product(id:int, product:Product):
    for i in range(len(products)):
         if products[i].id == id:
              products[i] = product
              return product
    return {"error": "Product not found"}


@app.post("/product/delete/{id}")
async def put_product(id:int, product:Product):
    for i in range(len(products)):
         if products[i].id == id:
              del products[i]
              return product
    return {"error": "Product not found"}

    
@app.get("/search/")
def search_items(name: str = None, limit: int = 10):
    return {"name": name, "limit": limit}