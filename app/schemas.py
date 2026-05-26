from datetime import datetime

from pydantic import BaseModel, ConfigDict


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

    # Allow Pydantic to read data from SQLAlchemy model objects
    model_config = ConfigDict(from_attributes=True)
