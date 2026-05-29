from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Product
from app.schemas import ProductCreate, ProductResponse


router = APIRouter(prefix="/products", tags=["products"])


@router.post("", response_model=ProductResponse, status_code=201)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    existing_product = db.query(Product).filter(Product.sku == product.sku).first()

    if existing_product:
        raise HTTPException(status_code=400, detail="SKU already exists")

    db_product = Product(
        name=product.name,
        sku=product.sku,
        quantity=product.quantity,
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@router.get("", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
