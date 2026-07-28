from app.extensions import db
from app.models.convenio import Convenio


class ConvenioService:

    @staticmethod
    def obtener_todos():
        return Convenio.query.all()

    @staticmethod
    def obtener_por_id(convenio_id):
        return Convenio.query.get(convenio_id)

    @staticmethod
    def crear(datos):
        convenio = Convenio(**datos)

        db.session.add(convenio)
        db.session.commit()

        return convenio

    @staticmethod
    def actualizar(convenio, datos):
        for clave, valor in datos.items():
            setattr(convenio, clave, valor)

        db.session.commit()

        return convenio

    @staticmethod
    def eliminar(convenio):
        db.session.delete(convenio)
        db.session.commit()