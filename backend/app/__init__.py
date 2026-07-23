from flask import Flask

from app.config import Config
from app.extensions import db, jwt, migrate, cors


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    @app.route("/")
    def home():
        return {"mensaje": "API Observatorio de Cooperación Internacional"}

    return app