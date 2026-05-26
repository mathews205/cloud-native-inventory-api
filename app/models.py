from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, DateTime
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
    
    # Timestamp automatically set to the current UTC time
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
