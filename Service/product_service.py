from Repository.product_repository import ProductRepository, CategoryRepository
from sqlalchemy.orm import Session
from models.product_models import Product


class ProductService:

    def __init__(self, db_session: Session):

        self.repository = ProductRepository(db_session)

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


class CategoryService:

    def __init__(self, db_session: Session):

        self.repository = CategoryRepository(db_session)

    def listar_categorias(self):

        return self.repository.get_all_categories()

    def crear_categoria(self, nombre_categoria: str):

        return self.repository.create_category(nombre_categoria)
