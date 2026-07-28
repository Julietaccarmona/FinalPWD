from flask import Blueprint
from flask_jwt_extended import jwt_required

from app.controllers.convenio_controller import ConvenioController

convenio_bp = Blueprint("convenios", __name__, url_prefix="/convenios")


@convenio_bp.route("/", methods=["GET"])
@jwt_required()
def listar():
    return ConvenioController.listar()


@convenio_bp.route("/<int:convenio_id>", methods=["GET"])
@jwt_required()
def obtener(convenio_id):
    return ConvenioController.obtener(convenio_id)


@convenio_bp.route("/", methods=["POST"])
@jwt_required()
def crear():
    return ConvenioController.crear()


@convenio_bp.route("/<int:convenio_id>", methods=["PUT"])
@jwt_required()
def actualizar(convenio_id):
    return ConvenioController.actualizar(convenio_id)


@convenio_bp.route("/<int:convenio_id>", methods=["DELETE"])
@jwt_required()
def eliminar(convenio_id):
    return ConvenioController.eliminar(convenio_id)