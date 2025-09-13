from datos_de_usuarios import usuarios, roles

def _id_rol_por_nombre(nombre_rol):
    """
    Devuelve el id_rol correspondiente al nombre de rol.
    Si no existe, devuelve None.
    """
    #Nueva función: convierte nombre de rol a id_rol para mantener consistencia con el modelo relacional.
    nombre_rol = nombre_rol.strip().lower()
    for r in roles:
        if r["nombre"] == nombre_rol:
            return r["id_rol"]
    return None

def registrar_usuario(nombre_completo, email, contraseña):
    """
    Registra un nuevo usuario.
    El primer usuario registrado será administrador, los demás serán estándar.
    """
    email = email.strip().lower()
    for u in usuarios:
        if u['email'].lower() == email:
            return False, 'El email ya está registrado'

    nuevo_id = max((u.get("id_usuario", 0) for u in usuarios), default=0) + 1

    if not usuarios:
        
        id_rol = _id_rol_por_nombre("administrador") or 1
    else:
        id_rol = _id_rol_por_nombre("estandar") or 2

    #Corrección: ahora se guarda id_rol (FK) en vez de rol como texto, usando _id_rol_por_nombre() para mantener integridad con la tabla Rol.
    nuevo_usuario = {
        'id_usuario': nuevo_id,
        'nombre_completo': nombre_completo.strip(),
        'email': email,
        'contraseña': contraseña,
        'id_rol': id_rol
    }
    usuarios.append(nuevo_usuario)
    return True, 'Usuario registrado con éxito'

def validar_usuario(email, contraseña):
    """
    Valida las credenciales de un usuario.
    Devuelve (True, usuario) si es correcto, o (False, mensaje) si no lo es.
    """
    email = email.strip().lower()
    for u in usuarios:
        if u['email'].lower() == email and u['contraseña'] == contraseña:
            #Corrección: se obtiene el nombre del rol desde id_rol para mostrarlo, manteniendo el dato real como entero (FK).
            rol_nombre = next((r["nombre"] for r in roles if r["id_rol"] == u["id_rol"]), "desconocido")
            u["rol"] = rol_nombre
            return True, u
    return False, 'Email o contraseña incorrectos'

def modificar_rol(email_usuario, nuevo_rol_nombre):
    """
    Cambia el rol de un usuario existente.
    """
    email_usuario = email_usuario.strip().lower()
    id_rol_nuevo = _id_rol_por_nombre(nuevo_rol_nombre)
    if id_rol_nuevo is None:
        roles_permitidos = ", ".join(r["nombre"] for r in roles)
        return False, f"Rol no válido. Los roles permitidos son: {roles_permitidos}"

    for u in usuarios:
        if u['email'].lower() == email_usuario:
            if u['id_rol'] == id_rol_nuevo:
                return False, f"El usuario ya tiene asignado el rol '{nuevo_rol_nombre}'."
            #Corrección: se cambia id_rol en vez de texto y se valida contra la lista de roles para mantener consistencia con el modelo relacional.
            u['id_rol'] = id_rol_nuevo
            return True, f"Rol cambiado a '{nuevo_rol_nombre}' para {u['nombre_completo']}"

    return False, 'Usuario no encontrado'
