from datos_de_usuarios import usuarios

def registrar_usuario(nombre, email, contraseña):
    for u in usuarios:
        if u ['email'] == email:
            return False, 'el email ya está registrado'
    nuevo_usuario = {'nombre' : nombre, 'email' : email, 'contraseña' : contraseña, 'rol' : 'estandar'} #se le asigna rol estandar al registrador.
    usuarios.append(nuevo_usuario)
    return True, 'usuario registrado con exito'

def validar_usuario(email,contraseña):
    for u in usuarios:
        if u ['email'] == email and u['contraseña'] == contraseña:
            return True, u 
    return False, 'email o contraseña incorrectos'
        
def modificar_rol(email_usuario, nuevo_rol):
    roles_validos = ['administrador', 'estandar']
    if nuevo_rol not in roles_validos:
        return False, ' rol no valido'
    for u in usuarios:
        if u ['email'] == email_usuario:
            u ['rol'] == nuevo_rol
            return True, f'rol cambiado a {nuevo_rol} para {u['nombre']}'
        return False, 'usuario no encontrado'