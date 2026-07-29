from flask import Blueprint
from flask_jwt_extended import jwt_required

from app.controllers.pais_controller import (
    listar_paises,
    obtener_pais,
    crear_pais,
    actualizar_pais,
    eliminar_pais
)

from app.utils.decorators import admin_required


pais_bp = Blueprint("pais", __name__, url_prefix="/paises")


@pais_bp.route("/", methods=["GET"])
@jwt_required()
def listar():
    return listar_paises()


@pais_bp.route("/<int:pais_id>", methods=["GET"])
@jwt_required()
def obtener(pais_id):
    return obtener_pais(pais_id)


@pais_bp.route("/", methods=["POST"])
@jwt_required()
@admin_required()
def crear():
    return crear_pais()


@pais_bp.route("/<int:pais_id>", methods=["PUT"])
@jwt_required()
@admin_required()
def actualizar(pais_id):
    return actualizar_pais(pais_id)


@pais_bp.route("/<int:pais_id>", methods=["DELETE"])
@jwt_required()
@admin_required()
def eliminar(pais_id):
    return eliminar_pais(pais_id)