from flask import request, jsonify
from app.services.auth_service import AuthService


class AuthController:

    @staticmethod
    def registrar():
        datos = request.get_json()

        nombre = datos.get("nombre")
        email = datos.get("email")
        password = datos.get("password")

        if not nombre or not email or not password:
            return jsonify({
                "mensaje": "Todos los campos son obligatorios."
            }), 400

        usuario, error = AuthService.registrar_usuario(
            nombre,
            email,
            password
        )

        if error:
            return jsonify({
                "mensaje": error
            }), 400

        return jsonify({
            "mensaje": "Usuario registrado correctamente.",
            "usuario": {
                "id": usuario.id,
                "nombre": usuario.nombre,
                "email": usuario.email,
                "rol": usuario.rol
            }
        }), 201