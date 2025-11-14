from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    description: str

    class Config:
        orm_mode = True
