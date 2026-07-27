from app.extensions import db
from app.models.usuario import Usuario
from flask_jwt_extended import create_access_token


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

    @staticmethod
    def login(email, password):
        usuario = Usuario.query.filter_by(email=email).first()

        if not usuario:
            return None, "Credenciales incorrectas."

        if not usuario.check_password(password):
            return None, "Credenciales incorrectas."

        access_token = create_access_token(
            identity=str(usuario.id),
            additional_claims={
                "rol": usuario.rol
            }
        )

        return {
            "access_token": access_token,
            "usuario": {
                "id": usuario.id,
                "nombre": usuario.nombre,
                "email": usuario.email,
                "rol": usuario.rol
            }
        }, None