from dispositivos import listar_dispositivos, buscar_dispositivo, agregar_dispositivo, eliminar_dispositivo
from automatizaciones import modo_ahorro
from usuarios import registrar_usuario_desde_input, validar_usuario, modificar_rol
from datos_de_usuarios import usuarios

def registrar_usuario_desde_input():
    print("\n=== Registro de Usuario ===")
    nombre = input("Nombre completo: ").strip()
    email = input("Correo electrónico: ").strip().lower()
    contraseña = input("Contraseña: ").strip()

    print(f"Usuarios actuales antes de registrar: {usuarios}")  # Depuración

    if not usuarios:  # Verifica que sea el primer usuario
        nuevo_usuario = {
            "nombre_completo": nombre,
            "email": email,
            "contraseña": contraseña,
            "rol": "administrador"
        }
        usuarios.append(nuevo_usuario)
        print("Primer usuario registrado como administrador.")
    else:
        nuevo_usuario = {
            "nombre_completo": nombre,
            "email": email,
            "contraseña": contraseña,
            "rol": "estandar"
        }
        usuarios.append(nuevo_usuario)
        print("Usuario registrado con éxito.")



def iniciar_sesion():
    print("\n=== Inicio de Sesión ===")
    email = input("Correo electrónico: ").strip().lower()
    contraseña = input("Contraseña: ").strip()
    exito, resultado = validar_usuario(email, contraseña)
    if exito:
        print(f"¡Bienvenido {resultado['nombre_completo']}!")
        return resultado
    else:
        print(resultado)
        return None
    
def menu_usuario_estandar(usuario):
    while True:
        print("\n=== MENÚ USUARIO ESTÁNDAR ===")
        print("1. Consultar datos personales")
        print("2. Activar Modo Ahorro de Energía")
        print("3. Consultar dispositivos")
        print("4. Cerrar sesión")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            print(f"\nNombre: {usuario['nombre_completo']}")
            print(f"Email: {usuario['email']}")
            print(f"Rol: {usuario['rol']}")
        elif opcion == "2":
            modo_ahorro()
        elif opcion == "3":
            listar_dispositivos()
        elif opcion == "4":
            print("Sesión cerrada.\n")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def menu_usuario_admin():
    while True:
        print("\n=== MENÚ ADMINISTRADOR ===")
        print("1. Consultar automatizaciones activas (Modo Ahorro)")
        print("2. Gestionar dispositivos")
        print("3. Modificar rol de usuario")
        print("4. Cerrar sesión")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            modo_ahorro()
        elif opcion == "2":
            menu_gestion_dispositivos()
        elif opcion == "3":
            email_usuario = input("Ingrese el email del usuario a modificar: ").strip().lower()
            nuevo_rol = input("Ingrese el nuevo rol (administrador/estandar): ").strip().lower()
            exito, mensaje = modificar_rol(email_usuario, nuevo_rol)
            print(mensaje)
        elif opcion == "4":
            print("Sesión cerrada.\n")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    
def menu_gestion_dispositivos():
    while True:
        print("\n--- Gestión de Dispositivos ---")
        print("1. Listar dispositivos")
        print("2. Buscar dispositivo")
        print("3. Agregar dispositivo")
        print("4. Eliminar dispositivo")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            listar_dispositivos()
        elif opcion == "2":
            buscar_dispositivo()
        elif opcion == "3":
            agregar_dispositivo_desde_input()
        elif opcion == "4":
            eliminar_dispositivo()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def agregar_dispositivo_desde_input():
    nombre = input("Nombre del nuevo dispositivo: ").strip()
    if not nombre:
        print("El nombre es obligatorio.")
        return

    estado = input("Estado (encendido/apagado) [por defecto apagado]: ").strip().lower()
    if estado not in ["encendido", "apagado", ""]:
        print("Estado no válido. Se usará 'apagado' por defecto.")
        estado = "apagado"
    if estado == "":
        estado = "apagado"

    esencial_input = input("¿Es esencial? (s/n) [por defecto n]: ").strip().lower()
    esencial = esencial_input == 's'

    ubicacion = input("Ubicación del dispositivo (ej: sala, dormitorio, cocina) [por defecto No especificada]: ").strip()
    if not ubicacion:
        ubicacion = "No especificada"

    agregar_dispositivo(nombre, estado, esencial, ubicacion)


def main():
    while True:
        print("\n=== SISTEMA DE AUTOMATIZACIÓN ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrar_usuario_desde_input()
        elif opcion == "2":
            usuario = iniciar_sesion()
            if usuario:
                if usuario['rol'] == 'administrador':
                    menu_usuario_admin()
                else:
                    menu_usuario_estandar(usuario)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()




