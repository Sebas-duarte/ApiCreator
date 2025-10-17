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

---

## Tecnologías utilizadas
- **Python **
- **Flask** 
- **SQLite** 
- **SQLAlchemy** 
- **Werkzeug** 

---
