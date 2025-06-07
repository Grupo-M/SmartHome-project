from datos_de_usuarios import usuarios

def registrar_usuario_desde_input():
    print("\n=== Registro de Usuario ===")
    nombre = input("Nombre completo: ").strip()
    email = input("Correo electrónico: ").strip().lower()
    contraseña = input("Contraseña: ").strip()

    nuevo_usuario = {
        "nombre_completo": nombre,
        "email": email,
        "contraseña": contraseña,
        "rol": "estandar"  # Todos los nuevos usuarios serán estándar
    }

    usuarios.append(nuevo_usuario)
    print("Usuario registrado con éxito.")

def validar_usuario(email, contraseña):
    """Valida si el usuario existe y las credenciales son correctas."""
    email = email.strip().lower()
    contraseña = contraseña.strip()

    for usuario in usuarios:
        print(f"Comparando: {usuario['email'].strip().lower()} == {email}, {usuario['contraseña'].strip()} == {contraseña}")  # Depuración

        if usuario["email"].strip().lower() == email and usuario["contraseña"].strip() == contraseña:
            return True, usuario  # Usuario validado correctamente

    return False, "Email o contraseña incorrectos."  # Mensaje de error si no coincide



def modificar_rol(email_usuario, nuevo_rol):
    roles_validos = ['administrador', 'estandar']
    email_usuario = email_usuario.lower().strip()
    nuevo_rol = nuevo_rol.lower().strip()
    
    if nuevo_rol not in roles_validos:
        return False, f"Rol no válido. Los roles permitidos son: {', '.join(roles_validos)}"

    for u in usuarios:
        if u['email'].lower().strip() == email_usuario:
            if u['rol'] == nuevo_rol:
                return False, f"El usuario ya tiene asignado el rol '{nuevo_rol}'."
            u['rol'] = nuevo_rol
            return True, f"Rol cambiado a {nuevo_rol} para {u['nombre_completo']}"
    
    return False, "Usuario no encontrado"