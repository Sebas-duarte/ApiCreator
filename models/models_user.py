import logging
from sqlalchemy import Column, Integer, String
from config.db import Base


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)


    username = Column(String(50), unique=True, index=True, nullable=False)


    password = Column(String(255), nullable=False)

    def __repr__(self):
        return f"<User(username='{self.username}')>"


