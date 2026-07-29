from flask import Blueprint
from flask_jwt_extended import jwt_required

from app.controllers.tipo_convenio_controller import (
    listar_tipos,
    obtener_tipo,
    crear_tipo,
    actualizar_tipo,
    eliminar_tipo
)

from app.utils.decorators import admin_required

tipo_convenio_bp = Blueprint(
    "tipo_convenio",
    __name__,
    url_prefix="/tipos-convenio"
)


@tipo_convenio_bp.route("/", methods=["GET"])
@jwt_required()
def listar():
    return listar_tipos()


@tipo_convenio_bp.route("/<int:tipo_id>", methods=["GET"])
@jwt_required()
def obtener(tipo_id):
    return obtener_tipo(tipo_id)


@tipo_convenio_bp.route("/", methods=["POST"])
@jwt_required()
@admin_required()
def crear():
    return crear_tipo()


@tipo_convenio_bp.route("/<int:tipo_id>", methods=["PUT"])
@jwt_required()
@admin_required()
def actualizar(tipo_id):
    return actualizar_tipo(tipo_id)


@tipo_convenio_bp.route("/<int:tipo_id>", methods=["DELETE"])
@jwt_required()
@admin_required()
def eliminar(tipo_id):
    return eliminar_tipo(tipo_id)