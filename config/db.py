import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from models.product_models import Base

logging.basicConfig(level=logging.INFO)

MYSQL_URI = "mysql+pymysql://usuario:password@localhost:3306/basedatos"
SQLITE_URI = "sqlite:///product_local.db"

def get_engine():
    if MYSQL_URI:
        try:
            engine = create_engine(MYSQL_URI, echo=True)
            conn = engine.connect()
            conn.close()
            logging.info("✅ Conexión a MySQL exitosa.")
            return engine
        except OperationalError:
            logging.warning("⚠️ No se pudo conectar a MySQL. Usando SQLite local.")
    engine = create_engine(SQLITE_URI, echo=True)
    logging.info("✅ Conexión a SQLite local establecida.")
    return engine

engine = get_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear tablas si no existen
Base.metadata.create_all(engine)

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
