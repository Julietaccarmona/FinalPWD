from flask import request, jsonify
from app.services.auth_service import AuthService
from flask_jwt_extended import get_jwt_identity


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
        
    @staticmethod
    def login():
        datos = request.get_json()

        email = datos.get("email")
        password = datos.get("password")

        if not email or not password:
            return jsonify({
                "mensaje": "Email y contraseña son obligatorios."
            }), 400

        respuesta, error = AuthService.login(email, password)

        if error:
            return jsonify({
                "mensaje": error
            }), 401

        return jsonify(respuesta), 200

    @staticmethod
    def perfil():
        usuario_id = get_jwt_identity()

        return jsonify({
            "mensaje": "Acceso autorizado.",
            "usuario_id": usuario_id
        }), 200