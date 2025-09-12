from flask import Blueprint, jsonify, request
from config.db import get_db_session
from Service.product_service import ProductService

# Crear el Blueprint
product_bp = Blueprint("products", __name__)

def get_service():
    session = get_db_session()
    return ProductService(session)


# Listar todos los productos
@product_bp.route("/", methods=["GET"])
def listar_productos():
    service = get_service()
    productos = service.listar_productos()
    return jsonify([
        {
            "id": p.idProduct,
            "nombre": p.nombre,
            "inventario": p.inventario,
            "categoria": {
                "id": p.categoria.idCategory,
                "nombreCategoria": p.categoria.nombreCategoria
            }
        }
        for p in productos
    ]), 200


# Obtener un producto por ID
@product_bp.route("/<int:product_id>", methods=["GET"])
def obtener_producto(product_id):
    service = get_service()
    producto = service.obtener_producto(product_id)
    if producto:
        return jsonify({
            "id": producto.idProduct,
            "nombre": producto.nombre,
            "inventario": producto.inventario,
            "categoria": {
                "id": producto.categoria.idCategory,
                "nombreCategoria": producto.categoria.nombreCategoria
            }
        }), 200
    return jsonify({"error": "Producto no encontrado"}), 404


# Crear un nuevo producto
@product_bp.route("/", methods=["POST"])
def crear_producto():
    service = get_service()
    data = request.get_json()

    nombre = data.get("nombre")
    inventario = data.get("inventario")
    categoria_id = data.get("categoria_id")

    if not nombre or inventario is None or not categoria_id:
        return jsonify({"error": "Faltan datos"}), 400

    producto = service.crear_producto(nombre, inventario, categoria_id)
    return jsonify({
        "id": producto.idProduct,
        "nombre": producto.nombre,
        "inventario": producto.inventario,
        "categoria_id": producto.categoria_id
    }), 201


# Actualizar un producto
@product_bp.route("/<int:product_id>", methods=["PUT"])
def actualizar_producto(product_id):
    service = get_service()
    data = request.get_json()

    nombre = data.get("nombre")
    inventario = data.get("inventario")
    categoria_id = data.get("categoria_id")

    producto = service.actualizar_producto(product_id, nombre, inventario, categoria_id)
    if producto:
        return jsonify({
            "id": producto.idProduct,
            "nombre": producto.nombre,
            "inventario": producto.inventario,
            "categoria_id": producto.categoria_id
        }), 200
    return jsonify({"error": "Producto no encontrado"}), 404


# Eliminar un producto
@product_bp.route("/<int:product_id>", methods=["DELETE"])
def eliminar_producto(product_id):
    service = get_service()
    producto = service.eliminar_producto(product_id)
    if producto:
        return jsonify({"message": "Producto eliminado"}), 200
    return jsonify({"error": "Producto no encontrado"}), 404
