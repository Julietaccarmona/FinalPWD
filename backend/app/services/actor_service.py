from app.extensions import db
from app.models.actor import Actor


class ActorService:

    @staticmethod
    def obtener_todos():
        return Actor.query.all()

    @staticmethod
    def obtener_por_id(actor_id):
        return Actor.query.get(actor_id)

    @staticmethod
    def crear(datos):
        actor = Actor(**datos)

        db.session.add(actor)
        db.session.commit()

        return actor

    @staticmethod
    def actualizar(actor, datos):
        for clave, valor in datos.items():
            setattr(actor, clave, valor)

        db.session.commit()

        return actor

    @staticmethod
    def eliminar(actor):
        db.session.delete(actor)
        db.session.commit()