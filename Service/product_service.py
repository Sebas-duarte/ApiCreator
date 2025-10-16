from models.product_models import Product, Category
from Repository import product_repository

class ProductService:
    def __init__(self, session):
        self.session = session

    def listar_productos(self):
        return self.session.query(Product).all()

    def obtener_producto(self, product_id):
        return self.session.query(Product).filter_by(idProduct=product_id).first()

    def crear_producto(self, nombre, inventario, categoria_id):
        producto = Product(nombre=nombre, inventario=inventario, categoria_id=categoria_id)
        self.session.add(producto)
        self.session.commit()
        return producto

    def actualizar_producto(self, product_id, nombre=None, inventario=None, categoria_id=None):
        producto = self.obtener_producto(product_id)
        if not producto:
            return None
        if nombre:
            producto.nombre = nombre
        if inventario is not None:
            producto.inventario = inventario
        if categoria_id:
            producto.categoria_id = categoria_id
        self.session.commit()
        return producto

    def eliminar_producto(self, product_id):
        producto = self.obtener_producto(product_id)
        if not producto:
            return False
        self.session.delete(producto)
        self.session.commit()
        return True


class CategoryService:
    def __init__(self, session):
        self.session = session

    def listar_categorias(self):
        return self.session.query(Category).all()

    def crear_categoria(self, nombreCategoria):
        categoria = Category(nombreCategoria=nombreCategoria)
        self.session.add(categoria)
        self.session.commit()
        return categoria
