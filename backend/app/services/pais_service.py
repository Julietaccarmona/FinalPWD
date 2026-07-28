from app.extensions import db
from app.models.pais import Pais


class PaisService:

    @staticmethod
    def obtener_todos():
        return Pais.query.all()

    @staticmethod
    def obtener_por_id(pais_id):
        return Pais.query.get(pais_id)

    @staticmethod
    def crear(datos):
        pais = Pais(**datos)

        db.session.add(pais)
        db.session.commit()

        return pais

    @staticmethod
    def actualizar(pais, datos):
        for clave, valor in datos.items():
            setattr(pais, clave, valor)

        db.session.commit()

        return pais

    @staticmethod
    def eliminar(pais):
        db.session.delete(pais)
        db.session.commit()