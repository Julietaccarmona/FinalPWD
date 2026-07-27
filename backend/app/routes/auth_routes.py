from flask import Blueprint
from app.controllers.auth_controller import AuthController
from flask_jwt_extended import jwt_required

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["POST"])
def registrar():
    return AuthController.registrar()

@auth_bp.route("/login", methods=["POST"])
def login():
    return AuthController.login()

@auth_bp.route("/perfil", methods=["GET"])
@jwt_required()
def perfil():
    return AuthController.perfil()