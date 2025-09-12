from flask import Flask
from config.db import init_db
from controller.product_controller import product_bp


app = Flask(__name__)

init_db(app)

app.register_blueprint(product_bp, url_prefix="/products")

if __name__ == "__main__":
    app.run(debug=True)
