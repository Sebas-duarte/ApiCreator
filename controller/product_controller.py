from flask import Blueprint, jsonify, request
from config.db import get_db_session
from Service.product_service import ProductService, CategoryService
from models.product_models import Product, Category

# Blueprint con prefijo /productos
product_bp = Blueprint("product_bp", __name__, url_prefix="/productos")

# Función para instanciar servicios
def get_services():
    session = get_db_session()
    return ProductService(session), CategoryService(session)

# ========================
# Categorías
# ========================

# Listar todas las categorías
@product_bp.route("/categorias", methods=["GET"])
def listar_categorias():
    _, category_service = get_services()
    categorias = category_service.listar_categorias()
    return jsonify([{"id": c.idCategory, "nombreCategoria": c.nombreCategoria} for c in categorias]), 200

# Crear una categoría
@product_bp.route("/categorias", methods=["POST"])
def crear_categoria():
    _, category_service = get_services()
    data = request.get_json()
    nombre = data.get("nombreCategoria")
    if not nombre:
        return jsonify({"error": "Falta el nombre de la categoría"}), 400
    categoria = category_service.crear_categoria(nombre)
    return jsonify({"id": categoria.idCategory, "nombreCategoria": categoria.nombreCategoria}), 201

# ========================
# Productos
# ========================

# Listar todos los productos
@product_bp.route("/", methods=["GET"])
def listar_productos():
    product_service, _ = get_services()
    productos = product_service.listar_productos()
    return jsonify([
        {
            "id": p.idProduct,
            "nombre": p.nombre,
            "inventario": p.inventario,
            "categoria": {
                "id": p.categoria.idCategory,
                "nombreCategoria": p.categoria.nombreCategoria
            }
        } for p in productos
    ]), 200

# Obtener un producto por ID
@product_bp.route("/<int:product_id>", methods=["GET"])
def obtener_producto(product_id):
    product_service, _ = get_services()
    producto = product_service.obtener_producto(product_id)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify({
        "id": producto.idProduct,
        "nombre": producto.nombre,
        "inventario": producto.inventario,
        "categoria": {
            "id": producto.categoria.idCategory,
            "nombreCategoria": producto.categoria.nombreCategoria
        }
    }), 200

# Crear un producto
@product_bp.route("/", methods=["POST"])
def crear_producto():
    product_service, _ = get_services()
    data = request.get_json()
    nombre = data.get("nombre")
    inventario = data.get("inventario")
    categoria_id = data.get("categoria_id")
    if not nombre or inventario is None or not categoria_id:
        return jsonify({"error": "Faltan datos obligatorios"}), 400
    producto = product_service.crear_producto(nombre, inventario, categoria_id)
    return jsonify({
        "id": producto.idProduct,
        "nombre": producto.nombre,
        "inventario": producto.inventario,
        "categoria_id": producto.categoria_id
    }), 201

# Actualizar un producto
@product_bp.route("/<int:product_id>", methods=["PUT"])
def actualizar_producto(product_id):
    product_service, _ = get_services()
    data = request.get_json()
    producto = product_service.actualizar_producto(
        product_id,
        data.get("nombre"),
        data.get("inventario"),
        data.get("categoria_id")
    )
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify({
        "id": producto.idProduct,
        "nombre": producto.nombre,
        "inventario": producto.inventario,
        "categoria_id": producto.categoria_id
    }), 200

# Eliminar un producto
@product_bp.route("/<int:product_id>", methods=["DELETE"])
def eliminar_producto(product_id):
    product_service, _ = get_services()
    eliminado = product_service.eliminar_producto(product_id)
    if not eliminado:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify({"message": "Producto eliminado"}), 200

