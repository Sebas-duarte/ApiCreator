from models.product_models import Product
from sqlalchemy.orm import Session

def get_all_products(db: Session):
    return db.query(Product).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.idProduct == product_id).first()

def create_product(db: Session, product: Product):
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def update_product(db: Session, product_id: int, data: dict):
    product = get_product_by_id(db, product_id)
    if not product:
        return None
    for key, value in data.items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

def delete_product(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)
    if not product:
        return None
    db.delete(product)
    db.commit()
    return product
