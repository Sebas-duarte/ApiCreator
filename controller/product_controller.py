from flask import Blueprint, request, jsonify
from config.db import get_db_session
from Service import product_service

product_bp = Blueprint("product_bp", __name__)

@product_bp.route("/products", methods=["GET"])
def get_products():
    db = next(get_db_session())
    products = product_service.get_products(db)
    return jsonify([{
        "id": p.idProduct,
        "nombre": p.nombre,
        "inventario": p.inventario,
        "categoria_id": p.categoria_id
    } for p in products])

@product_bp.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    db = next(get_db_session())
    product = product_service.get_product(db, product_id)
    if not product:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify({
        "id": product.idProduct,
        "nombre": product.nombre,
        "inventario": product.inventario,
        "categoria_id": product.categoria_id
    })

@product_bp.route("/products", methods=["POST"])
def create_product():
    db = next(get_db_session())
    data = request.json
    product = product_service.create_product(
        db, nombre=data["nombre"], inventario=data.get("inventario", 0), categoria_id=data["categoria_id"]
    )
    return jsonify({
        "id": product.idProduct,
        "nombre": product.nombre,
        "inventario": product.inventario,
        "categoria_id": product.categoria_id
    }), 201

@product_bp.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    db = next(get_db_session())
    data = request.json
    product = product_service.update_product(db, product_id, data)
    if not product:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify({
        "id": product.idProduct,
        "nombre": product.nombre,
        "inventario": product.inventario,
        "categoria_id": product.categoria_id
    })

@product_bp.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    db = next(get_db_session())
    product = product_service.delete_product(db, product_id)
    if not product:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify({"message": "Producto eliminado"})
