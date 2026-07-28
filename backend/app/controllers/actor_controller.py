from flask import request, jsonify

from app.services.actor_service import ActorService


def listar_actores():
    actores = ActorService.obtener_todos()

    return jsonify([
        {
            "id": actor.id,
            "nombre": actor.nombre,
            "tipo": actor.tipo
        }
        for actor in actores
    ])


def obtener_actor(actor_id):
    actor = ActorService.obtener_por_id(actor_id)

    if not actor:
        return jsonify({"mensaje": "Actor no encontrado"}), 404

    return jsonify({
        "id": actor.id,
        "nombre": actor.nombre,
        "tipo": actor.tipo
    })


def crear_actor():
    datos = request.get_json()

    actor = ActorService.crear(datos)

    return jsonify({
        "mensaje": "Actor creado correctamente",
        "id": actor.id
    }), 201


def actualizar_actor(actor_id):
    actor = ActorService.obtener_por_id(actor_id)

    if not actor:
        return jsonify({"mensaje": "Actor no encontrado"}), 404

    datos = request.get_json()

    ActorService.actualizar(actor, datos)

    return jsonify({
        "mensaje": "Actor actualizado correctamente"
    })


def eliminar_actor(actor_id):
    actor = ActorService.obtener_por_id(actor_id)

    if not actor:
        return jsonify({"mensaje": "Actor no encontrado"}), 404

    ActorService.eliminar(actor)

    return jsonify({
        "mensaje": "Actor eliminado correctamente"
    })