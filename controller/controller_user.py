import logging
from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import create_access_token, jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError
from config.db import get_db_session
from Service.users_services import UsersService  # <- corregido

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

service = UsersService(get_db_session())
user_bp = Blueprint('users', __name__)


def register_jwt_error_handlers(app):
    @app.errorhandler(NoAuthorizationError)
    def handle_no_auth_error(e):
        logger.warning("Intento de acceso sin autenticación JWT")
        return jsonify({'error': 'No autenticado. Debe enviar un token JWT válido en el header Authorization.'}), 401


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'El nombre de usuario y la contraseña son obligatorios'}), 400
    user = service.authenticate_user(username, password)
    if user:
        access_token = create_access_token(identity={'id': user.id, 'username': user.username})
        return jsonify({'access_token': access_token}), 200
    return jsonify({'error': 'Credenciales inválidas'}), 401

@user_bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    """
    GET /users
    Recupera y retorna todos los usuarios registrados en el sistema.
    Utiliza la capa de servicios para obtener la lista completa de usuarios.
    No recibe parámetros.
    Respuesta: JSON con la lista de usuarios.
    """
    users = service.get_all_users()
    logger.info("Consulta de todos los usuarios")
    return jsonify([{'id': u.id, 'username': u.username} for u in users]), 200, {'Content-Type': 'application/json; charset=utf-8'}

@user_bp.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    """
    GET /users/<user_id>
    Recupera la información de un usuario específico por su ID.
    Parámetros:
        user_id (int): ID del usuario a consultar (en la URL).
    Respuesta: JSON con los datos del usuario o 404 si no existe.
    """
    user = service.get_user_by_id(user_id)
    if user:
        logger.info(f"Consulta de usuario por ID: {user_id}")
        return jsonify({'id': user.id, 'username': user.username}), 200, {'Content-Type': 'application/json; charset=utf-8'}
    logger.warning(f"Usuario no encontrado: {user_id}")
    return jsonify({'error': 'Usuario no encontrado'}), 404, {'Content-Type': 'application/json; charset=utf-8'}

@user_bp.route('/registry', methods=['POST'])
def create_user():
    """
    POST /registry
    Crea un nuevo usuario.
    Parámetros esperados (JSON):
        username (str): Nombre de usuario.
        password (str): Contraseña del usuario.
    Respuesta: JSON con los datos del usuario creado.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        logger.warning("Registro fallido: usuario o contraseña no proporcionados")
        return jsonify({'error': 'El nombre de usuario y la contraseña son obligatorios'}), 400, {'Content-Type': 'application/json; charset=utf-8'}
    user = service.create_user(username, password)
    logger.info(f"Usuario creado: {username}")
    return jsonify({'id': user.id, 'username': user.username}), 201, {'Content-Type': 'application/json; charset=utf-8'}

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    """
    PUT /users/<user_id>
    Actualiza la información de un usuario existente.
    Parámetros:
        user_id (int): ID del usuario a actualizar (en la URL).
    Parámetros esperados (JSON):
        username (str, opcional): Nuevo nombre de usuario.
        password (str, opcional): Nueva contraseña del usuario.
    Respuesta: JSON con los datos del usuario actualizado o 404 si no existe.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = service.update_user(user_id, username, password)
    if user:
        logger.info(f"Usuario actualizado: {user_id}")
        return jsonify({'id': user.id, 'username': user.username}), 200, {'Content-Type': 'application/json; charset=utf-8'}
    logger.warning(f"Usuario no encontrado para actualizar: {user_id}")
    return jsonify({'error': 'Usuario no encontrado'}), 404, {'Content-Type': 'application/json; charset=utf-8'}

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    """
    DELETE /users/<user_id>
    Elimina un usuario del sistema.
    Parámetros:
        user_id (int): ID del usuario a eliminar (en la URL).
    Respuesta: JSON confirmando la eliminación o 404 si no existe.
    """
    user = service.delete_user(user_id)
    if user:
        logger.info(f"Usuario eliminado: {user_id}")
        return jsonify({'message': 'Usuario eliminado correctamente'}), 200, {'Content-Type': 'application/json; charset=utf-8'}
    logger.warning(f"Usuario no encontrado para eliminar: {user_id}")
    return jsonify({'error': 'Usuario no encontrado'}), 404, {'Content-Type': 'application/json; charset=utf-8'}