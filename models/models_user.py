import logging
from sqlalchemy import Column, Integer, String
from models.db import Base

# Configuración del logger para este modelo
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class User(Base):
    __tablename__ = "users"

    # Identificador único del usuario (clave primaria)
    id = Column(Integer, primary_key=True, index=True)

    # Nombre de usuario (único y obligatorio)
    username = Column(String(50), unique=True, index=True, nullable=False)

    # Contraseña del usuario (almacenada como hash)
    password = Column(String(255), nullable=False)

    def __repr__(self):
        return f"<User(username='{self.username}')>"


