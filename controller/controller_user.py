import logging
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError
from config.db import get_db_session
from Service.users_services import UsersService 


# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicializar Blueprint y servicio
user_bp = Blueprint('user_bp', __name__)
service = UsersService(get_db_session())

def register_jwt_error_handlers(app):
    @app.errorhandler(NoAuthorizationError)
    def handle_no_auth_error(e):
        logger.warning("Intento de acceso sin autenticación JWT")
        return jsonify({
            'error': 'No autenticado. Debe enviar un token JWT válido en el header Authorization.'
        }), 401

@user_bp.route('/login', methods=['POST'])
def login():
    """
    POST /login
    Autentica a un usuario y devuelve un token JWT si las credenciales son válidas.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        logger.warning("Login fallido: usuario o contraseña no proporcionados")
        return jsonify({'error': 'El nombre de usuario y la contraseña son obligatorios'}), 400

    user = service.authenticate_user(username, password)
    if not user:
        logger.warning(f"Login fallido para usuario: {username}")
        return jsonify({'error': 'Credenciales inválidas'}), 401

    access_token = create_access_token(identity={'id': user.id, 'username': user.username})
    logger.info(f"Usuario autenticado: {username}")
    return jsonify({'access_token': access_token}), 200


@user_bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    """Obtiene todos los usuarios registrados."""
    users = service.get_all_users()
    logger.info("Consulta de todos los usuarios")
    return jsonify([{'id': u.id, 'username': u.username} for u in users]), 200


@user_bp.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    """Obtiene un usuario por su ID."""
    user = service.get_user_by_id(user_id)
    if not user:
        logger.warning(f"Usuario no encontrado: {user_id}")
        return jsonify({'error': 'Usuario no encontrado'}), 404

    logger.info(f"Consulta de usuario por ID: {user_id}")
    return jsonify({'id': user.id, 'username': user.username}), 200


@user_bp.route('/registry', methods=['POST'])
def create_user():
    """Registra un nuevo usuario."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        logger.warning("Registro fallido: usuario o contraseña no proporcionados")
        return jsonify({'error': 'El nombre de usuario y la contraseña son obligatorios'}), 400

    user = service.create_user(username, password)
    logger.info(f"Usuario creado: {username}")
    return jsonify({'id': user.id, 'username': user.username}), 201


@user_bp.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    """Actualiza los datos de un usuario existente."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = service.update_user(user_id, username, password)
    if not user:
        logger.warning(f"Usuario no encontrado para actualizar: {user_id}")
        return jsonify({'error': 'Usuario no encontrado'}), 404

    logger.info(f"Usuario actualizado: {user_id}")
    return jsonify({'id': user.id, 'username': user.username}), 200


@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    """Elimina un usuario del sistema."""
    user = service.delete_user(user_id)
    if not user:
        logger.warning(f"Usuario no encontrado para eliminar: {user_id}")
        return jsonify({'error': 'Usuario no encontrado'}), 404

    logger.info(f"Usuario eliminado: {user_id}")
    return jsonify({'message': 'Usuario eliminado correctamente'}), 200
