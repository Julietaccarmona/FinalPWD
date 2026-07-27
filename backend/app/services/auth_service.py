from app.extensions import db
from app.models.usuario import Usuario


class AuthService:

    @staticmethod
    def registrar_usuario(nombre, email, password):
        # Verificar si el email ya existe
        usuario_existente = Usuario.query.filter_by(email=email).first()

        if usuario_existente:
            return None, "El correo electrónico ya está registrado."

        # Crear el usuario
        usuario = Usuario(
            nombre=nombre,
            email=email
        )

        usuario.set_password(password)

        db.session.add(usuario)
        db.session.commit()

        return usuario, None