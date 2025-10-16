from flask import Flask
from config.jwt import *
from controller.product_controller import product_bp
from controller.controller_user import user_bp, register_jwt_error_handlers

app = Flask(__name__)

# Configurar JWT
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['JWT_TOKEN_LOCATION'] = JWT_TOKEN_LOCATION
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES
app.config['JWT_HEADER_NAME'] = JWT_HEADER_NAME
app.config['JWT_HEADER_TYPE'] = JWT_HEADER_TYPE

# Registrar blueprints
app.register_blueprint(product_bp)
app.register_blueprint(user_bp)

# Manejadores JWT
register_jwt_error_handlers(app)

if __name__ == "__main__":
    app.run(debug=True)
