# Frontend - Guía de Uso

## 📱 Descripción General

El frontend es una aplicación web moderna y responsiva desarrollada con HTML, CSS y JavaScript Vanilla. Proporciona una interfaz completa para interactuar con la API RPM.

## 🎨 Características del Diseño

- **Diseño Moderno**: Gradientes de colores atractivos (púrpura y azul)
- **Animaciones Suaves**: Transiciones y animaciones fluidas
- **Responsivo**: Compatible con dispositivos móviles, tablets y desktop
- **Sin Dependencias Externas**: Solo HTML, CSS y JavaScript vanilla
- **Almacenamiento Seguro**: JWT tokens guardados en localStorage

## 📄 Páginas Principales

### 1. Página de Autenticación (`/index.html`)

**Funcionalidades:**
- ✅ Formulario de Login
- ✅ Formulario de Registro
- ✅ Validación de datos en cliente
- ✅ Transición suave entre formularios
- ✅ Manejo de errores
- ✅ Almacenamiento automático de tokens

**Campos:**
- **Login**: Usuario y contraseña
- **Registro**: Usuario, contraseña y confirmación de contraseña

**Validaciones:**
- Usuario requerido
- Contraseña mínimo 6 caracteres
- Las contraseñas deben coincidir en registro
- Mensajes de error claros

### 2. Página de CRUD (`/crud.html`)

**Funcionalidades:**

#### Panel de Productos
- Visualización de todos los productos en tarjetas
- Información: nombre, categoría, inventario, ID
- Botones de edición y eliminación
- Diseño responsivo (grid automático)

#### Agregar Producto
- Formulario para crear nuevos productos
- Campos: nombre, inventario, categoría
- Validación de campos requeridos
- Confirmación de éxito

#### Gestión de Categorías
- Crear nuevas categorías
- Visualización de todas las categorías
- Selector de categorías en formularios
- Actualización automática

#### Editar Producto
- Modal de edición moderna
- Todos los campos editables
- Confirmación de cambios
- Cierre automático al guardar

#### Eliminar Producto
- Confirmación de eliminación
- Eliminación inmediata
- Actualización de lista

## 🔐 Autenticación

### Flujo de Seguridad

1. **Login**: Usuario y contraseña se envían al backend
2. **Token JWT**: Se recibe y almacena en localStorage
3. **CRUD**: Todo acceso requiere el token en header `Authorization: Bearer <token>`
4. **Logout**: Se elimina el token y se redirige a login
5. **Protección**: Si no hay token, se redirige automáticamente a login

## 🚀 Cómo Usar

### Instalación y Ejecución

```bash
# 1. Navega al directorio del proyecto
cd /workspaces/ApiCreator

# 2. Instala las dependencias Python
pip install -r requirements.txt

# 3. Ejecuta el servidor
python main.py

# 4. Abre en el navegador
# Login/Registro: http://localhost:5000/
# CRUD: http://localhost:5000/crud (después de autenticarse)
```

### Ejemplo de Uso Paso a Paso

1. **Abre `http://localhost:5000/`**
   - Verás el formulario de login

2. **Crea una cuenta**
   - Haz clic en "Crear cuenta"
   - Ingresa usuario y contraseña
   - Haz clic en "Crear Cuenta"

3. **Inicia sesión**
   - Usa las credenciales que acabas de crear
   - Se te redirigirá automáticamente a `/crud`

4. **Gestiona Productos**
   - **Agregar**: Completa el formulario y haz clic en "Agregar Producto"
   - **Ver**: Los productos aparecen como tarjetas
   - **Editar**: Haz clic en "✏️ Editar" para abrir el modal
   - **Eliminar**: Haz clic en "🗑️ Eliminar" (requiere confirmación)

5. **Gestiona Categorías**
   - Ingresa el nombre en el campo
   - Haz clic en "Agregar" para crear nueva categoría
   - Las categorías aparecen como etiquetas

## 📝 Estructura de Archivos

```
frontend/
├── index.html           # Página de autenticación
├── crud.html            # Página de gestión de productos
└── static/
    ├── style.css        # Estilos globales
    └── app.js           # Funciones compartidas
```

## 🎯 Endpoints API Utilizados

### Autenticación
- `POST /login` - Iniciar sesión
- `POST /registry` - Registrar usuario

### Productos (requieren autenticación)
- `GET /products` - Obtener todos los productos
- `POST /products` - Crear producto
- `PUT /products/<id>` - Actualizar producto
- `DELETE /products/<id>` - Eliminar producto

### Categorías (requieren autenticación)
- `GET /categories` - Obtener todas las categorías
- `POST /categories` - Crear categoría

## 🎨 Paleta de Colores

| Elemento | Color | Código |
|----------|-------|--------|
| Gradiente Principal | Púrpura-Azul | #667eea → #764ba2 |
| Fondo | Blanco | #ffffff |
| Texto Principal | Gris Oscuro | #333333 |
| Borde | Gris Claro | #e0e0e0 |
| Éxito | Verde | #28a745 |
| Error | Rojo | #dc3545 |
| Info | Azul | #17a2b8 |

## 💡 Características Técnicas

### JavaScript
- Fetch API para comunicación con backend
- Async/await para operaciones asincrónicas
- Event listeners para interactividad
- LocalStorage para persistencia

### CSS
- CSS Grid para responsive design
- Flexbox para alineación
- Animaciones CSS (@keyframes)
- Media queries para mobile

### Validaciones
- Client-side: Campos requeridos, longitud mínima
- Server-side: JWT, credenciales, datos válidos

## 🔧 Personalización

### Cambiar Colores
En `static/style.css`, busca la sección de variables y modifica:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Agregar Nuevos Campos a Productos
En `crud.html`, agrega campos en el formulario y actualiza la llamada API

### Cambiar URL de API
En `static/app.js`:
```javascript
const API_URL = 'http://localhost:5000';  // Cambia aquí
```

## 🐛 Troubleshooting

### No puedo acceder a `/crud`
- Verifica que hayas iniciado sesión en `/`
- Revisa que el token esté en localStorage (abre DevTools → Application → Storage)

### Los productos no aparecen
- Verifica que la API esté corriendo en puerto 5000
- Revisa la consola del navegador (F12) para errores
- Asegúrate de tener categorías creadas

### Errores de CORS
- El backend debe tener CORS habilitado (`CORS(app)` en main.py)
- Verifica que `http://localhost:5000` sea la URL correcta

## 📚 Recursos

- [MDN Web Docs - Fetch API](https://developer.mozilla.org/es/docs/Web/API/Fetch_API)
- [CSS Grid Guide](https://developer.mozilla.org/es/docs/Web/CSS/CSS_Grid_Layout)
- [JWT en LocalStorage](https://stackoverflow.com/questions/27067251/where-to-store-jwt-tokens-safely)
