from flask import Blueprint

from app.controllers.pais_controller import (
    listar_paises,
    obtener_pais,
    crear_pais,
    actualizar_pais,
    eliminar_pais
)

pais_bp = Blueprint("pais", __name__, url_prefix="/paises")

pais_bp.route("/", methods=["GET"])(listar_paises)
pais_bp.route("/<int:pais_id>", methods=["GET"])(obtener_pais)
pais_bp.route("/", methods=["POST"])(crear_pais)
pais_bp.route("/<int:pais_id>", methods=["PUT"])(actualizar_pais)
pais_bp.route("/<int:pais_id>", methods=["DELETE"])(eliminar_pais)