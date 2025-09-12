from Repository.product_repository import ProductRepository
from sqlalchemy.orm import Session

class ProductService:
    def __init__(self, db: Session):
        self.repository = ProductRepository(db)

    # Categorías
    def listar_categorias(self):
        return self.repository.get_all_categories()

    def crear_categoria(self, nombreCategoria: str):
        return self.repository.create_category(nombreCategoria)

    # Productos
    def listar_productos(self):
        return self.repository.get_all_products()

    def obtener_producto(self, product_id: int):
        return self.repository.get_product_by_id(product_id)

    def crear_producto(self, nombre: str, inventario: int, categoria_id: int):
        return self.repository.create_product(nombre, inventario, categoria_id)

    def actualizar_producto(self, product_id: int, nombre: str = None, inventario: int = None, categoria_id: int = None):
        return self.repository.update_product(product_id, nombre, inventario, categoria_id)

    def eliminar_producto(self, product_id: int):
        return self.repository.delete_product(product_id)
