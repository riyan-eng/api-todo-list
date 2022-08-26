from flask import Flask
from flask_jwt_extended import JWTManager
from datetime import timedelta
import os
from flask_cors import CORS

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
jwt = JWTManager(app)
CORS(app, resources={r"/*": {"origins": "*"}})

from app import routes

if __name__ == "__main__":
    app.run()