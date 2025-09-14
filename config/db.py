import os
import logging
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models.product_models import Base

logging.basicConfig(level=logging.INFO)

# Usar SQLite local siempre
SQLITE_URI = 'sqlite:///product_local.db'
SCHEMA_SQL_PATH = os.path.join(os.path.dirname(__file__), '..', 'database.sql')

def get_engine():
    """Crea la conexión con SQLite local."""
    engine = create_engine(SQLITE_URI, echo=True)
    
    # Ejecutar database.sql si la base no existe aún
    if not os.path.exists('product_local.db'):
        logging.info("Creando base de datos local y tablas desde database.sql...")
        with engine.connect() as conn:
            with open(SCHEMA_SQL_PATH, 'r', encoding='utf-8') as f:
                sql_script = f.read()
                conn.execute(text(sql_script))
                conn.commit()
    return engine

# Crear engine y sesión
engine = get_engine()
Session = sessionmaker(bind=engine)

# Crear las tablas de SQLAlchemy si no existen
Base.metadata.create_all(engine)

def get_db_session():
    """Devuelve una sesión de base de datos."""
    return Session()

