from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return send_from_directory('frontend', 'index.html')

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory('frontend', path)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)