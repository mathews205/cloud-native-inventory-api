from sqlalchemy import Column, Integer, String, DateTime, Index
from sqlalchemy.sql import func
from app.database import Base


class Product(Base):
    """SQLAlchemy model for products table."""
    __tablename__ = "products"

    # Primary key column with auto-increment
    id = Column(Integer, primary_key=True, index=True)
    
    # Product name (required)
    name = Column(String, nullable=False)
    
    # SKU - unique identifier, indexed for fast lookups (required)
    sku = Column(String, unique=True, nullable=False, index=True)
    
    # Stock quantity with default value of 0
    quantity = Column(Integer, default=0, nullable=False)
    
    # Timestamp automatically set to current UTC time
    created_at = Column(DateTime, default=func.now(), nullable=False)

    def __repr__(self):
        return f"<Product(id={self.id}, sku='{self.sku}', name='{self.name}', quantity={self.quantity})>"
