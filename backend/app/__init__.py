from flask import Flask

from app.config import Config
from app.extensions import db, jwt, migrate, cors
from app.models import Usuario

from app.routes.auth_routes import auth_bp

from app.routes.convenio_routes import convenio_bp

from app.routes.pais_routes import pais_bp

from app.routes.actor_routes import actor_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(convenio_bp)
    app.register_blueprint(pais_bp)
    app.register_blueprint(actor_bp)

    @app.route("/")
    def home():
        return {"mensaje": "API Observatorio de Cooperación Internacional"}
    
    return app