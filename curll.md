 Crear usuario
 curl -X POST http://127.0.0.1:5000/registry \
-H "Content-Type: application/json" \
-d '{
  "username": "camilo2025",
  "password": "ClaveSegura123"
}'

Iniciar sesión (login)
curl -X POST http://127.0.0.1:5000/login \
-H "Content-Type: application/json" \
-d '{
  "username": "camilo2025",
  "password": "ClaveSegura123"
}'
Obtener todos los usuarios
curl -X GET http://127.0.0.1:5000/users \
-H "Authorization: Bearer TOKEN"

Obtener un usuario por ID (ejemplo: ID = 4)
curl -X GET http://127.0.0.1:5000/users/4 \
-H "Authorization: Bearer TOKEN"

Actualizar un usuario (ejemplo: ID = 4)
curl -X PUT http://127.0.0.1:5000/users/4 \
-H "Authorization: Bearer TOKEN" \
-H "Content-Type: application/json" \
-d '{
  "username": "camilo_actualizado",
  "password": "NuevaClave2025"
}'

Eliminar un usuario (ejemplo: ID = 4)

curl -X DELETE http://127.0.0.1:5000/users/4 \
-H "Authorization: Bearer TOKEN"
