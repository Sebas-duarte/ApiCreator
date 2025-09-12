from flask import Flask
from config.db import init_db
from controller.product_controller import product_bp

# Crear la app
app = Flask(__name__)

# Inicializar la base de datos
init_db(app)

# Registrar las rutas (Blueprint)
app.register_blueprint(product_bp, url_prefix="/products")

if __name__ == "__main__":
    app.run(debug=True)
