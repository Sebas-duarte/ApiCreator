import os
import logging
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models.product_models import Base

logging.basicConfig(level=logging.INFO)

# Ruta de la base de datos SQLite
SQLITE_URI = 'sqlite:///product_local.db'
SCHEMA_SQL_PATH = os.path.join(os.path.dirname(__file__), '..', 'database.sql')

def get_engine():

    db_path = SQLITE_URI.replace('sqlite:///', '')
    db_exists = os.path.exists(db_path)

    engine = create_engine(SQLITE_URI, echo=True)

    if not db_exists:
        logging.info("Base de datos no encontrada. Creando nueva base")
        with engine.connect() as conn:
            with open(SCHEMA_SQL_PATH, 'r', encoding='utf-8') as f:
                schema_sql = f.read()
                conn.execute(text(schema_sql))
        logging.info("Esquema cargado desde database.sql.")

    return engine

# Crear motor y sesión
engine = get_engine()
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

def get_db_session():
    return Session()