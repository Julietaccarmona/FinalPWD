from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, get_jwt

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
                "usuario_id": c.usuario_id,
                "usuario": c.usuario.nombre if c.usuario else None,
                "pais": c.pais.nombre if c.pais else None,
                "actor": c.actor.nombre if c.actor else None,
                "tipo_convenio": c.tipo_convenio.nombre if c.tipo_convenio else None,
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

            "usuario_id": convenio.usuario_id,

            "pais_id": convenio.pais_id,
            "actor_id": convenio.actor_id,
            "tipo_convenio_id": convenio.tipo_convenio_id,

            "pais": convenio.pais.nombre if convenio.pais else None,
            "actor": convenio.actor.nombre if convenio.actor else None,
            "tipo_convenio": convenio.tipo_convenio.nombre if convenio.tipo_convenio else None,
        })
        
    @staticmethod
    def crear():
        datos = request.get_json()

        datos["usuario_id"] = int(get_jwt_identity())

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

        usuario_actual = int(get_jwt_identity())
        claims = get_jwt()

        es_admin = claims.get("rol") == "admin"

        if convenio.usuario_id != usuario_actual and not es_admin:
            return {
                "mensaje": "No tiene permisos para editar este convenio"
            }, 403
    
    

        datos = request.get_json()

        ConvenioService.actualizar(convenio, datos)

        return {
            "mensaje": "Convenio actualizado correctamente"
        }


    @staticmethod
    def eliminar(convenio_id):
        convenio = ConvenioService.obtener_por_id(convenio_id)

        if not convenio:
            return {"mensaje": "Convenio no encontrado"}, 404

        ConvenioService.eliminar(convenio)

        return {"mensaje": "Convenio eliminado correctamente"}