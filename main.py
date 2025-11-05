from flask import Flask, send_from_directory
from config.jwt import *
from controller.product_controller import product_bp
from controller.controller_user import user_bp, register_jwt_error_handlers
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config.db import Base, engine
from models.models_user import User
import os

Base.metadata.create_all(bind=engine)
app = Flask(__name__)
    
"""configuracion de jwt"""
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['JWT_TOKEN_LOCATION'] = JWT_TOKEN_LOCATION
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES
app.config['JWT_HEADER_NAME'] = JWT_HEADER_NAME
app.config['JWT_HEADER_TYPE'] = JWT_HEADER_TYPE

jwt = JWTManager(app)
# Permitir CORS para desarrollo local (frontend estático en :8000)
CORS(app)


app.register_blueprint(product_bp)
app.register_blueprint(user_bp)

""" Registrar manejadores personalizados de errores JWT"""
register_jwt_error_handlers(app)


@app.route("/")
def index():
    return send_from_directory('frontend', 'index.html')

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory('frontend', path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=3000)
