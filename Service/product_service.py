from models.product_models import Product
from repository import product_repository

def get_products(db):
    return product_repository.get_all_products(db)

def get_product(db, product_id: int):
    return product_repository.get_product_by_id(db, product_id)

def create_product(db, nombre: str, inventario: int, categoria_id: int):
    new_product = Product(nombre=nombre, inventario=inventario, categoria_id=categoria_id)
    return product_repository.create_product(db, new_product)

def update_product(db, product_id: int, data: dict):
    return product_repository.update_product(db, product_id, data)

def delete_product(db, product_id: int):
    return product_repository.delete_product(db, product_id)
