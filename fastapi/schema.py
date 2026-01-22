from pydantic import BaseModel
from typing import Optional

# 1. Define the Data Model
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class UserProfile(BaseModel):
    username: str
    email: str
    birth_year: Optional[int] = None
    age: Optional[int] = None
    is_active: bool = True  
    bio: Optional[str] = None

class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: float
    quantity: int = 0
    