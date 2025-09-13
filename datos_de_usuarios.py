# Lista de roles (coherente con la tabla Rol del modelo relacional)
roles = [
    {"id_rol": 1, "nombre": "administrador", "descripcion": "Administrador con todos los permisos"},
    {"id_rol": 2, "nombre": "estandar", "descripcion": "Usuario con permisos limitados"}
]

# Lista de usuarios (coherente con la tabla Usuario del modelo relacional)
#Corrección: antes se guardaba el rol como texto, ahora se usa id_rol (FK) para
# mantener consistencia con el modelo relacional.

usuarios = [
    {
        "id_usuario": 1,
        "nombre_completo": "Administrador",
        "email": "administrador@gmail.com",
        "contraseña": "ad78",
        "id_rol": 1
    },
    {
        "id_usuario": 2,
        "nombre_completo": "Maria Gomez",
        "email": "maria@gmail.com",
        "contraseña": "maria41",
        "id_rol": 2
    }
]
