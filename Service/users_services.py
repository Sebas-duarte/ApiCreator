from models.models_user import User
from sqlalchemy.orm import Session

class UsersService:
    def __init__(self, db: Session):
        self.db = db
        self.model = User  # ✅ define el modelo que usará el servicio

    # 🧩 Crear usuario
    def create_user(self, username, password):
        existing_user = self.db.query(Users).filter_by(username=username).first()
        if existing_user:
            raise ValueError("El nombre de usuario ya existe")

        new_user = Users(username=username, password=password)
        self.db.add(new_user)
        self.db.commit()
        return new_user


    # 🧩 Autenticar usuario
    def authenticate_user(self, username, password):
        user = self.db.query(self.model).filter_by(username=username, password=password).first()
        return user

    # 🧩 Obtener todos los usuarios
    def get_all_users(self):
        return self.db.query(self.model).all()

    # 🧩 Obtener un usuario por ID
    def get_user_by_id(self, user_id):
        return self.db.query(self.model).filter_by(id=user_id).first()

    # 🧩 Actualizar usuario
    def update_user(self, user_id, username=None, password=None):
        user = self.get_user_by_id(user_id)
        if not user:
            return None
        if username:
            user.username = username
        if password:
            user.password = password
        self.db.commit()
        self.db.refresh(user)
        return user

    # 🧩 Eliminar usuario
    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if not user:
            return None
        self.db.delete(user)
        self.db.commit()
        return True
