from app.extensions import db


class Actor(db.Model):
    __tablename__ = "actores"

    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(
        db.String(150),
        nullable=False
    )

    tipo = db.Column(
        db.String(100),
        nullable=False
    )