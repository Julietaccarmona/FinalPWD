from flask import Blueprint
from flask_jwt_extended import jwt_required

from app.controllers.actor_controller import (
    listar_actores,
    obtener_actor,
    crear_actor,
    actualizar_actor,
    eliminar_actor
)

from app.utils.decorators import admin_required

actor_bp = Blueprint("actor", __name__, url_prefix="/actores")


@actor_bp.route("/", methods=["GET"])
@jwt_required()
def listar():
    return listar_actores()


@actor_bp.route("/<int:actor_id>", methods=["GET"])
@jwt_required()
def obtener(actor_id):
    return obtener_actor(actor_id)


@actor_bp.route("/", methods=["POST"])
@jwt_required()
@admin_required()
def crear():
    return crear_actor()


@actor_bp.route("/<int:actor_id>", methods=["PUT"])
@jwt_required()
@admin_required()
def actualizar(actor_id):
    return actualizar_actor(actor_id)


@actor_bp.route("/<int:actor_id>", methods=["DELETE"])
@jwt_required()
@admin_required()
def eliminar(actor_id):
    return eliminar_actor(actor_id)