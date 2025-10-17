from models.models_user import User
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash
import logging

logger = logging.getLogger(__name__)

class UsersService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_users(self):
        """Obtiene todos los usuarios."""
        return self.db.query(User).all()

    def get_user_by_username(self, username: str):
        """Obtiene un usuario por su nombre de usuario."""
        return self.db.query(User).filter(User.username == username).first()

    def create_user(self, username: str, password: str):
        """Crea un nuevo usuario con contraseña cifrada."""
        hashed_password = generate_password_hash(password)
        user = User(username=username, password=hashed_password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        logger.info(f"Usuario creado: {username}")
        return user

    def authenticate_user(self, username: str, password: str):
        """Autentica un usuario verificando la contraseña."""
        user = self.get_user_by_username(username)
        if user and check_password_hash(user.password, password):
            logger.info(f"Usuario autenticado: {username}")
            return user
        logger.warning(f"Intento fallido de autenticación: {username}")
        return None

    def delete_user(self, user_id: int):
        """Elimina un usuario por ID."""
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        self.db.delete(user)
        self.db.commit()
        logger.info(f"Usuario eliminado: {user.username}")
        return user
