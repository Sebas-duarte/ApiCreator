from flask import Flask
from config.jwt import *
from controller.product_controller import product_bp
from controller.controller_user import user_bp, register_jwt_error_handlers
from flask_jwt_extended import JWTManager
from config.db import Base, engine
from models.models_user import User
import os

Base.metadata.create_all(bind=engine)
app = Flask(__name__)

# Configurar JWT
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['JWT_TOKEN_LOCATION'] = JWT_TOKEN_LOCATION
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES
app.config['JWT_HEADER_NAME'] = JWT_HEADER_NAME
app.config['JWT_HEADER_TYPE'] = JWT_HEADER_TYPE

jwt = JWTManager(app)

# Registrar Blueprints (rutas)
app.register_blueprint(product_bp)
app.register_blueprint(user_bp)

# Registrar manejadores personalizados de errores JWT
register_jwt_error_handlers(app)

# Ruta de prueba del servidor
@app.route("/")
def index():
    return "✅ API funcionando correctamente", 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
