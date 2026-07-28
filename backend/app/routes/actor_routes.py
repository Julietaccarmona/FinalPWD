from flask import Blueprint

from app.controllers.actor_controller import (
    listar_actores,
    obtener_actor,
    crear_actor,
    actualizar_actor,
    eliminar_actor
)

actor_bp = Blueprint("actor", __name__, url_prefix="/actores")

actor_bp.route("/", methods=["GET"])(listar_actores)
actor_bp.route("/<int:actor_id>", methods=["GET"])(obtener_actor)
actor_bp.route("/", methods=["POST"])(crear_actor)
actor_bp.route("/<int:actor_id>", methods=["PUT"])(actualizar_actor)
actor_bp.route("/<int:actor_id>", methods=["DELETE"])(eliminar_actor)