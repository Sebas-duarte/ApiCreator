from Repository.product_repository import ProductRepository
from sqlalchemy.orm import Session
from typing import Optional
from models.product_models import Product


class ProductService:
    def __init__(self, db: Session):
        self.repository = ProductRepository(db)

    # Categorías
    def listar_categorias(self):
        try:
            return self.repository.get_all_categories()
        except Exception as e:
            raise Exception(f"Error al listar categorías: {str(e)}")

    def crear_categoria(self, nombreCategoria: str):
        try:
            return self.repository.create_category(nombreCategoria)
        except ValueError as ve:
            raise ve
        except Exception as e:
            raise Exception(f"Error al crear categoría: {str(e)}")

    # Productos
    def listar_productos(self):
        try:
            return self.repository.get_all_products()
        except Exception as e:
            raise Exception(f"Error al listar productos: {str(e)}")

    def obtener_producto(self, product_id: int):
        try:
            return self.repository.get_product_by_id(product_id)
        except ValueError as ve:
            raise ve
        except Exception as e:
            raise Exception(f"Error al obtener producto: {str(e)}")

    def crear_producto(self, nombre: str, inventario: int, categoria_id: int):
        try:
            return self.repository.create_product(nombre, inventario, categoria_id)
        except ValueError as ve:
            raise ve
        except Exception as e:
            raise Exception(f"Error al crear producto: {str(e)}")

    def actualizar_producto(
        self,
        product_id: int,
        nombre: Optional[str] = None,
        inventario: Optional[int] = None,
        categoria_id: Optional[int] = None
    ) -> Optional[Product]:
        producto = self.repository.update_product(
            product_id=product_id,
            nombre=nombre,
            inventario=inventario,
            categoria_id=categoria_id
        )
        return producto

    def eliminar_producto(self, product_id: int):
        try:
            return self.repository.delete_product(product_id)
        except ValueError as ve:
            raise ve
        except Exception as e:
            raise Exception(f"Error al eliminar producto: {str(e)}")