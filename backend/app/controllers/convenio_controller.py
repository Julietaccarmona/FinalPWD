from flask import request, jsonify

from app.services.convenio_service import ConvenioService


class ConvenioController:

    @staticmethod
    def listar():
        convenios = ConvenioService.obtener_todos()

        return jsonify([
            {
                "id": c.id,
                "titulo": c.titulo,
                "descripcion": c.descripcion,
                "fecha_firma": c.fecha_firma.isoformat() if c.fecha_firma else None,
                "estado": c.estado,
                "usuario_id": c.usuario_id
            }
            for c in convenios
        ])

    @staticmethod
    def obtener(convenio_id):
        convenio = ConvenioService.obtener_por_id(convenio_id)

        if not convenio:
            return {"mensaje": "Convenio no encontrado"}, 404

        return jsonify({
            "id": convenio.id,
            "titulo": convenio.titulo,
            "descripcion": convenio.descripcion,
            "fecha_firma": convenio.fecha_firma.isoformat() if convenio.fecha_firma else None,
            "estado": convenio.estado,
            "usuario_id": convenio.usuario_id
        })

    @staticmethod
    def crear():
        datos = request.get_json()

        convenio = ConvenioService.crear(datos)

        return {
            "mensaje": "Convenio creado correctamente",
            "id": convenio.id
        }, 201

    @staticmethod
    def actualizar(convenio_id):
        convenio = ConvenioService.obtener_por_id(convenio_id)

        if not convenio:
            return {"mensaje": "Convenio no encontrado"}, 404

        datos = request.get_json()

        ConvenioService.actualizar(convenio, datos)

        return {"mensaje": "Convenio actualizado correctamente"}

    @staticmethod
    def eliminar(convenio_id):
        convenio = ConvenioService.obtener_por_id(convenio_id)

        if not convenio:
            return {"mensaje": "Convenio no encontrado"}, 404

        ConvenioService.eliminar(convenio)

        return {"mensaje": "Convenio eliminado correctamente"}