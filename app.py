from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "message":"hello from CI/CD",
        "environment": os.getenv("APP_ENV", "local")
    })

@app.get("/health")
def health():
    return jsonify({
        "status": "unhealthy"
    })

def create_app():
    return app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5123)