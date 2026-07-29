from app.extensions import db


class Convenio(db.Model):
    __tablename__ = "convenios"

    id = db.Column(db.Integer, primary_key=True)

    titulo = db.Column(db.String(200), nullable=False)

    descripcion = db.Column(db.Text)

    fecha_firma = db.Column(db.Date)

    estado = db.Column(
        db.String(50),
        default="En negociación"
    )

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id"),
        nullable=False
    )

    pais_id = db.Column(
        db.Integer,
        db.ForeignKey("paises.id"),
        nullable=False
    )

    actor_id = db.Column(
        db.Integer,
        db.ForeignKey("actores.id"),
        nullable=False
    )

    tipo_convenio_id = db.Column(
        db.Integer,
        db.ForeignKey("tipos_convenio.id"),
        nullable=False
    )