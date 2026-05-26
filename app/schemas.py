from pydantic import BaseModel
from datetime import datetime


class ProductCreate(BaseModel):
    """Schema for creating a new product."""
    name: str
    sku: str
    quantity: int = 0


class StockUpdate(BaseModel):
    """Schema for updating product stock quantity."""
    quantity: int


class ProductResponse(BaseModel):
    """Schema for product responses from API."""
    id: int
    name: str
    sku: str
    quantity: int
    created_at: datetime

    class Config:
        # Enable ORM mode to work with SQLAlchemy objects
        from_attributes = True
