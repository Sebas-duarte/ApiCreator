# RPM API - Gestión de Productos y Categorías

## Descripción

El proyecto utiliza una **base de datos SQLite** para almacenar los datos y está diseñado para ser fácilmente escalable y adaptable a otros motores de base de datos si se requie.

Esta API permite registrar, autenticar y gestionar usuarios de manera segura utilizando Flask, SQLAlchemy y JSON Web Tokens (JWT).
Incluye endpoints protegidos por token y ejemplos listos para usar con cURL.
---

## Características principales
- Gestión de **productos**:
   Crear, consultar, actualizar y eliminar productos.
   Cada producto pertenece a una categoría.
- Gestión de **categorías**:
   Crear, consultar, actualizar y eliminar categorías.
- Datos iniciales cargados automáticamente desde `database.sql`.
- Estructura modular para facilitar mantenimiento y escalabilidad.


Funcionalidades implementadas

Registro de usuarios (/registry)
Se desarrolló un endpoint POST que permite registrar nuevos usuarios enviando su nombre de usuario y contraseña en formato JSON. El sistema valida que el usuario no exista previamente en la base de datos y, de ser válido, lo almacena de manera segura.

Autenticación de usuarios (/login)
A través de un endpoint POST, los usuarios pueden autenticarse enviando sus credenciales. Si son correctas, el sistema genera un token JWT con tiempo de expiración, el cual debe incluirse en el encabezado Authorization de las siguientes solicitudes para acceder a los recursos protegidos.

Gestión de usuarios protegida
Se implementaron varios endpoints con protección JWT:

GET /users: obtiene la lista completa de usuarios registrados.

GET /users/<id>: consulta los datos de un usuario específico.

PUT /users/<id>: permite actualizar información de un usuario existente.

DELETE /users/<id>: elimina un usuario del sistema.

Estas rutas verifican la validez del token JWT antes de ejecutar cualquier acción, garantizando la seguridad y autenticidad del usuario solicitante.
---

Para la verificación del funcionamiento de la API, se utilizaron comandos cURL desde la terminal, simulando las diferentes solicitudes HTTP.
Durante las pruebas, se validó el correcto flujo de registro, autenticación, emisión y verificación de tokens, así como la ejecución de las operaciones CRUD protegidas.

---

## Tecnologías utilizadas
- **Python **
- **Flask** 
- **SQLite** 
- **SQLAlchemy** 
- **Werkzeug** 

---
