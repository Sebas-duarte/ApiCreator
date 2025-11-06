# RPM API - Gestión de Productos y Categorías

## Descripción
 Descripción
Este proyecto implementa una API RESTful para la gestión de productos y categorías, con autenticación segura de usuarios. Utiliza una base de datos SQLite, pero está diseñada para ser fácilmente escalable y adaptable a otros motores de base de datos como PostgreSQL o MySQL.
La API está desarrollada con Flask, SQLAlchemy y JSON Web Tokens (JWT) para garantizar una arquitectura modular, segura y mantenible. Además, se incluye una interfaz frontend básica en HTML y CSS para facilitar el registro e inicio de sesión de usuarios.

---

## Características principales
- Gestión de productos: Crear, consultar, actualizar y eliminar productos. Cada producto está asociado a una categoría.
- Gestión de categorías: Crear, consultar, actualizar y eliminar categorías.
- Gestión de usuarios: Registro, autenticación y administración de usuarios con protección JWT.
- Autenticación segura: Uso de tokens JWT con expiración para proteger rutas sensibles.
- Datos iniciales: Carga automática desde database.sql.
- Frontend básico: Interfaz web para registro e inicio de sesión de usuarios.
- Estructura modular: Código organizado para facilitar mantenimiento y escalabilidad.


## Autenticación y Seguridad
La autenticación se implementa mediante JSON Web Tokens (JWT). Los tokens se generan al iniciar sesión y deben incluirse en el encabezado Authorization de las solicitudes protegidas.


Flujo de autenticación:
- Registro de usuarios (POST /registry):
- Recibe username y password en formato JSON.
- Verifica que el usuario no exista.
- Almacena la contraseña de forma segura usando hashing con Werkzeug.
- Inicio de sesión (POST /login):
- Recibe credenciales en JSON.
- Si son válidas, genera un token JWT con expiración.
- El token debe enviarse en el encabezado Authorization: Bearer <token> para acceder a rutas protegidas.
- Protección de rutas:
- Endpoints como /users, /products, /categories están protegidos.
- Se valida el token antes de ejecutar cualquier acción.


## Tecnologías utilizadas
- Backend:
- Python
- Flask
- SQLite
- SQLAlchemy
- Werkzeug
- PyJWT
- Frontend:
- HTML5
- CSS3
- JavaScript (básico para llamadas fetch a la API)


---
## Pruebas
Se realizaron pruebas con:
- cURL: Para simular solicitudes HTTP y validar el flujo completo de autenticación y operaciones CRUD.
- Frontend: Para verificar la integración entre la interfaz web y la API
