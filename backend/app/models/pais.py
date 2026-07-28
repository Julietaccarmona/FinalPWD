from app.extensions import db


class Pais(db.Model):
    __tablename__ = "paises"

    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )

    codigo_iso = db.Column(
        db.String(3),
        nullable=False,
        unique=True
    )

    continente = db.Column(
        db.String(50),
        nullable=False
    )