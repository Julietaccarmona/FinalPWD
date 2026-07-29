from flask import request, jsonify

from app.services.tipo_convenio_service import TipoConvenioService


def listar_tipos():
    tipos = TipoConvenioService.obtener_todos()

    return jsonify([
        {
            "id": tipo.id,
            "nombre": tipo.nombre,
            "descripcion": tipo.descripcion
        }
        for tipo in tipos
    ])


def obtener_tipo(tipo_id):
    tipo = TipoConvenioService.obtener_por_id(tipo_id)

    if not tipo:
        return jsonify({"mensaje": "Tipo de convenio no encontrado"}), 404

    return jsonify({
        "id": tipo.id,
        "nombre": tipo.nombre,
        "descripcion": tipo.descripcion
    })


def crear_tipo():
    datos = request.get_json()

    tipo = TipoConvenioService.crear(datos)

    return jsonify({
        "mensaje": "Tipo de convenio creado correctamente",
        "id": tipo.id
    }), 201


def actualizar_tipo(tipo_id):
    tipo = TipoConvenioService.obtener_por_id(tipo_id)

    if not tipo:
        return jsonify({"mensaje": "Tipo de convenio no encontrado"}), 404

    datos = request.get_json()

    TipoConvenioService.actualizar(tipo, datos)

    return jsonify({
        "mensaje": "Tipo de convenio actualizado correctamente"
    })


def eliminar_tipo(tipo_id):
    tipo = TipoConvenioService.obtener_por_id(tipo_id)

    if not tipo:
        return jsonify({"mensaje": "Tipo de convenio no encontrado"}), 404

    TipoConvenioService.eliminar(tipo)

    return jsonify({
        "mensaje": "Tipo de convenio eliminado correctamente"
    })