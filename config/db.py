import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from models.product_models import Base  # Importa tus modelos de productos/categorías
from dotenv import load_dotenv


# Configurar logging para mostrar info en consola
logging.basicConfig(level=logging.INFO)

# Cargar variables de entorno desde .env
load_dotenv()

# Intentar con MySQL si la variable existe
MYSQL_URI = os.getenv('MYSQL_URI')
# Fallback a SQLite si falla
SQLITE_URI = 'sqlite:///product_local.db'


def get_engine():
    """
    Intenta crear una conexión con MySQL. 
    Si falla, usa SQLite local.
    """
    if MYSQL_URI:
        try:
            engine = create_engine(MYSQL_URI, echo=True)
            # Probar conexión
            conn = engine.connect()
            conn.close()
            logging.info(' Conexión a MySQL exitosa.')
            return engine
        except OperationalError:
            logging.warning('No se pudo conectar a MySQL. Usando SQLite local.')

    # Fallback a SQLite
    engine = create_engine(SQLITE_URI, echo=True)
    logging.info('✅ Conectado a SQLite local.')
    return engine


# Crear motor
engine = get_engine()

# Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear tablas en la base de datos (si no existen)
Base.metadata.create_all(bind=engine)


def get_db_session():
    """
    Retorna una nueva sesión de base de datos 
    para ser utilizada en los servicios o controladores.
    """
    return SessionLocal()
