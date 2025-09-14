# RPM API - Gestión de Productos y Categorías

## Descripción
RPM API es una API REST desarrollada en Python con Flask que permite gestionar productos y categorías. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre productos y categorías, y obtener la información en formato JSON.  

El proyecto utiliza una **base de datos SQLite** para almacenar los datos y está diseñado para ser fácilmente escalable y adaptable a otros motores de base de datos si se requiere.

---

## Características principales
- Gestión de **productos**:
  - Crear, consultar, actualizar y eliminar productos.
  - Cada producto pertenece a una categoría.
- Gestión de **categorías**:
  - Crear, consultar, actualizar y eliminar categorías.
- Endpoints organizados con **Blueprints** de Flask.
- Datos iniciales cargados automáticamente desde `database.sql`.
- Manejo de errores y validaciones básicas.
- Estructura modular para facilitar mantenimiento y escalabilidad.

---

## Tecnologías utilizadas
- **Python 3.12**
- **Flask** - Microframework para desarrollo de APIs REST.
- **SQLite** - Base de datos ligera integrada.
- **SQLAlchemy** - ORM para consultas y manipulación de la base de datos.
- **Werkzeug** - Servidor de desarrollo y utilidades de Flask.

---

## Instalación y ejecución

1. Clonar el repositorio:

```bash
git clone https://github.com/tu_usuario/rpm-api.git
cd rpm-api
