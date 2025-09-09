from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos simulados: lista de productos
products = [
    {"id": 1, "name": "Laptop", "price": 3000, "stock": 5},
    {"id": 2, "name": "Smartphone", "price": 1200, "stock": 10},
    {"id": 3, "name": "Auriculares", "price": 200, "stock": 25}
]

# Obtener todos los productos
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

# Obtener un producto por ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(product), 200

# Crear un nuevo producto
@app.route('/products', methods=['POST'])
def create_product():
    if not request.json or 'name' not in request.json or 'price' not in request.json or 'stock' not in request.json:
        return jsonify({'error': 'Bad request'}), 400
    
    new_id = max(p['id'] for p in products) + 1 if products else 1
    product = {
        'id': new_id,
        'name': request.json['name'],
        'price': request.json['price'],
        'stock': request.json['stock']
    }
    products.append(product)
    return jsonify(product), 201

# Actualizar un producto existente
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    if not request.json:
        return jsonify({'error': 'Bad request'}), 400
    
    product['name'] = request.json.get('name', product['name'])
    product['price'] = request.json.get('price', product['price'])
    product['stock'] = request.json.get('stock', product['stock'])
    return jsonify(product), 200

# Eliminar un producto
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    products.remove(product)
    return jsonify({'result': 'Product deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
