from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    idCategory = Column(Integer, primary_key=True, index=True)
    nombreCategoria = Column(String(255), nullable=False, unique=True)

    products = relationship("Product", back_populates="categoria", cascade="all, delete-orphan")


