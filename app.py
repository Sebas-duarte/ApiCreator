from flask import Flask
from controller.product_controller import product_bp

def create_app():
    app = Flask(__name__)

    # Registrar blueprints
    app.register_blueprint(product_bp, url_prefix="/productos")

    # Configuraciones adicionales si las necesitas
    app.config["JSON_SORT_KEYS"] = False  # Para mantener el orden de los campos

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)