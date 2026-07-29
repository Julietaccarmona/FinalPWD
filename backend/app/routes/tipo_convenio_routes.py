from flask import Blueprint

from app.controllers.tipo_convenio_controller import (
    listar_tipos,
    obtener_tipo,
    crear_tipo,
    actualizar_tipo,
    eliminar_tipo
)

tipo_convenio_bp = Blueprint(
    "tipos_convenio",
    __name__,
    url_prefix="/tipos-convenio"
)

tipo_convenio_bp.route("/", methods=["GET"])(listar_tipos)
tipo_convenio_bp.route("/<int:tipo_id>", methods=["GET"])(obtener_tipo)
tipo_convenio_bp.route("/", methods=["POST"])(crear_tipo)
tipo_convenio_bp.route("/<int:tipo_id>", methods=["PUT"])(actualizar_tipo)
tipo_convenio_bp.route("/<int:tipo_id>", methods=["DELETE"])(eliminar_tipo)