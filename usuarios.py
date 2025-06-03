from datos_de_usuarios import usuarios

def registrar_usuario(nombre_completo, email, contraseña):
    for u in usuarios:
        if u ['email'] == email:
            return False, 'el email ya está registrado'
    nuevo_usuario = {'nombre_completo' : nombre_completo, 'email' : email, 'contraseña' : contraseña, 'rol' : 'estandar'} #se le asigna rol estandar al registrador.
    usuarios.append(nuevo_usuario)
    return True, 'usuario registrado con exito'

def validar_usuario(email,contraseña):
    for u in usuarios:
        if u ['email'] == email and u['contraseña'] == contraseña:
            return True, u 
    return False, 'email o contraseña incorrectos'
        
    
def modificar_rol(email_usuario, nuevo_rol):
    roles_validos = ['administrador', 'estandar']
    email_usuario = email_usuario.lower().strip()
    nuevo_rol = nuevo_rol.lower().strip()
    if nuevo_rol not in roles_validos:
        return False, f'rol no válido. Los roles permitidos son: {', '.join(roles_validos)}'
    for u in usuarios:
        if u['email'].lower().strip() == email_usuario:
         if u['rol'] == nuevo_rol:
            return False, f"El usuario ya tiene asignado el rol '{nuevo_rol}'."
         u['rol'] = nuevo_rol
        return True, f"rol cambiado a {nuevo_rol} para {u['nombre_completo']}"
    
    return False, 'usuario no encontrado'
