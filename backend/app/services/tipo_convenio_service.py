from app.extensions import db
from app.models.tipo_convenio import TipoConvenio


class TipoConvenioService:

    @staticmethod
    def obtener_todos():
        return TipoConvenio.query.all()

    @staticmethod
    def obtener_por_id(tipo_id):
        return TipoConvenio.query.get(tipo_id)

    @staticmethod
    def crear(datos):
        tipo = TipoConvenio(**datos)

        db.session.add(tipo)
        db.session.commit()

        return tipo

    @staticmethod
    def actualizar(tipo, datos):
        for clave, valor in datos.items():
            setattr(tipo, clave, valor)

        db.session.commit()

        return tipo

    @staticmethod
    def eliminar(tipo):
        db.session.delete(tipo)
        db.session.commit()