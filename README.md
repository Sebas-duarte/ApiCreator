# RPM API - Gestión de Productos y Categorías

## Descripción
 Descripción
Este proyecto implementa una API RESTful para la gestión de productos y categorías, con autenticación segura de usuarios. Utiliza una base de datos SQLite, pero está diseñada para ser fácilmente escalable y adaptable a otros motores de base de datos como PostgreSQL o MySQL.
La API está desarrollada con Flask, SQLAlchemy y JSON Web Tokens (JWT) para garantizar una arquitectura modular, segura y mantenible.

Además, incluye un **frontend moderno y atractivo** con dos páginas principales:
- **Página de Autenticación**: Login y registro de usuarios con validación integrada
- **Página de CRUD**: Gestión completa de productos y categorías

---

## Características principales
- Gestión de productos: Crear, consultar, actualizar y eliminar productos. Cada producto está asociado a una categoría.
- Gestión de categorías: Crear, consultar, actualizar y eliminar categorías.
- Gestión de usuarios: Registro, autenticación y administración de usuarios con protección JWT.
- Autenticación segura: Uso de tokens JWT con expiración para proteger rutas sensibles.
- Datos iniciales: Carga automática desde database.sql.
- Estructura modular: Código organizado para facilitar mantenimiento y escalabilidad.
- **Frontend moderno**: Interfaz atractiva con diseño responsivo y animaciones fluidas.


## Autenticación y Seguridad
La autenticación se implementa mediante JSON Web Tokens (JWT). Los tokens se generan al iniciar sesión y deben incluirse en el encabezado Authorization de las solicitudes protegidas.


Flujo de autenticación:
- Registro de usuarios (POST /registry):
- Recibe username y password en formato JSON.
- Verifica que el usuario no exista.
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
  - Flask-CORS
- Frontend:
  - HTML5
  - CSS3 (Diseño moderno con gradientes y animaciones)
  - JavaScript (Vanilla, sin dependencias externas)

---

## Estructura del Proyecto

```
ApiCreator/
├── main.py                  # Archivo principal de la aplicación Flask
├── config/                  # Configuración
│   ├── db.py               # Configuración de base de datos
│   └── jwt.py              # Configuración de JWT
├── controller/             # Controladores/Rutas
│   ├── controller_user.py  # Rutas de usuario (login, registro)
│   └── product_controller.py # Rutas de productos y categorías
├── models/                 # Modelos de datos
│   ├── models_user.py      # Modelo de Usuario
│   └── product_models.py   # Modelos de Producto y Categoría
├── Service/                # Lógica de negocio
│   ├── users_services.py   # Servicios de usuario
│   └── product_service.py  # Servicios de productos
├── Repository/             # Acceso a datos
│   ├── user_repository.py  # Repositorio de usuario
│   └── product_repository.py # Repositorio de productos
├── frontend/               # Frontend Web
│   ├── index.html          # Página de login/registro
│   ├── crud.html           # Página de gestión de productos
│   └── static/
│       ├── style.css       # Estilos CSS
│       └── app.js          # Lógica JavaScript compartida
└── database.sql            # Datos iniciales
```

---

## Acceso a la Aplicación

### Desarrollo Local

1. **Inicia el servidor**:
   ```bash
   python main.py
   ```
   El servidor estará disponible en `http://localhost:5000`

2. **Accede al frontend**:
   - **Login/Registro**: `http://localhost:5000/` 
   - **Gestión de Productos**: `http://localhost:5000/crud` (requiere autenticación)

### Página de Autenticación (`/`)
- Interfaz moderna para login y registro de usuarios
- Formularios interactivos con validación en cliente
- Transición suave entre formularios de login y registro
- Almacenamiento seguro de tokens JWT

### Página de CRUD (`/crud`)
- **Panel de Productos**: Visualización de todos los productos en tarjetas
- **Agregar Producto**: Formulario para crear nuevos productos
- **Gestión de Categorías**: Crear categorías y visualizar todas las existentes
- **Editar Producto**: Modal para editar productos existentes
- **Eliminar Producto**: Eliminación con confirmación
- **Navegación**: Barra de navegación con opción de cerrar sesión

---

## Pruebas
Se realizaron pruebas con:
- cURL: Para simular solicitudes HTTP y validar el flujo completo de autenticación y operaciones CRUD.
- Frontend: Interfaz web integrada para verificar la integración con la API
