import logging
from sqlalchemy.orm import Session
from models.models_user import User

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserRepository:
    """
    Repositorio para la gestión de usuarios en la base de datos.
    Proporciona métodos para crear, consultar, actualizar y eliminar usuarios.
    """

    def __init__(self, db_session: Session):
        self.db = db_session


    def get_all_users(self):
        """
        Recupera todos los usuarios almacenados en la base de datos.
        Devuelve una lista con todas las instancias del modelo User.
        """
        logger.info("Obteniendo todos los usuarios desde el repositorio")
        return self.db.query(User).all()

    def get_user_by_id(self, user_id: int):
        """
        Busca y retorna un usuario específico por su ID.
        Devuelve la instancia del usuario si existe o None si no se encuentra.
        """
        logger.info(f"Buscando usuario por ID: {user_id}")
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_username(self, username: str):
        """
        Busca un usuario por su nombre de usuario.
        Devuelve la instancia si existe o None si no se encuentra.
        """
        logger.info(f"Buscando usuario por nombre de usuario: {username}")
        return self.db.query(User).filter(User.username == username).first()


    def create_user(self, username: str, password: str):
        """
        Crea y almacena un nuevo usuario en la base de datos.
        Retorna el nuevo usuario creado con su ID asignado.
        """
        if self.get_user_by_username(username):
            logger.warning(f"Intento de crear usuario duplicado: {username}")
            return None
        
        logger.info(f"Creando nuevo usuario: {username}")
        new_user = User(username=username, password=password)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def update_user(self, user_id: int, username: str = None, password: str = None):
        """
        Actualiza los datos de un usuario existente.
        Permite cambiar el nombre de usuario y/o contraseña.
        Retorna el usuario actualizado o None si no existe.
        """
        user = self.get_user_by_id(user_id)
        if not user:
            logger.warning(f"Usuario no encontrado para actualizar: {user_id}")
            return None
        
        if username:
            user.username = username
        if password:
            user.password = password
        
        self.db.commit()
        self.db.refresh(user)
        logger.info(f"Usuario actualizado correctamente: {user_id}")
        return user

    def delete_user(self, user_id: int):
        """
        Elimina un usuario de la base de datos según su ID.
        Retorna el usuario eliminado o None si no existe.
        """
        user = self.get_user_by_id(user_id)
        if not user:
            logger.warning(f"Usuario no encontrado para eliminar: {user_id}")
            return None
        
        logger.info(f"Eliminando usuario: {user_id}")
        self.db.delete(user)
        self.db.commit()
        return user
