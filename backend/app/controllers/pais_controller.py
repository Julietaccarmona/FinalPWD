from flask import request, jsonify

from app.services.pais_service import PaisService


def listar_paises():
    paises = PaisService.obtener_todos()

    return jsonify([
        {
            "id": pais.id,
            "nombre": pais.nombre,
            "codigo_iso": pais.codigo_iso,
            "continente": pais.continente
        }
        for pais in paises
    ])


def obtener_pais(pais_id):
    pais = PaisService.obtener_por_id(pais_id)

    if not pais:
        return jsonify({"mensaje": "País no encontrado"}), 404

    return jsonify({
        "id": pais.id,
        "nombre": pais.nombre,
        "codigo_iso": pais.codigo_iso,
        "continente": pais.continente
    })


def crear_pais():
    datos = request.get_json()

    pais = PaisService.crear(datos)

    return jsonify({
        "mensaje": "País creado correctamente",
        "id": pais.id
    }), 201


def actualizar_pais(pais_id):
    pais = PaisService.obtener_por_id(pais_id)

    if not pais:
        return jsonify({"mensaje": "País no encontrado"}), 404

    datos = request.get_json()

    PaisService.actualizar(pais, datos)

    return jsonify({
        "mensaje": "País actualizado correctamente"
    })


def eliminar_pais(pais_id):
    pais = PaisService.obtener_por_id(pais_id)

    if not pais:
        return jsonify({"mensaje": "País no encontrado"}), 404

    PaisService.eliminar(pais)

    return jsonify({
        "mensaje": "País eliminado correctamente"
    })