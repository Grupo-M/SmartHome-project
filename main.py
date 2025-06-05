from dispositivos import listar_dispositivos, buscar_dispositivo, agregar_dispositivo, eliminar_dispositivo
from automatizaciones import modo_ahorro
from usuarios import registrar_usuario, validar_usuario
from datos_de_usuarios import usuarios

def registrar_usuario_desde_input():
    print("\n=== Registro de Usuario ===")
    nombre = input("Nombre completo: ").strip()
    email = input("Correo electrónico: ").strip().lower()
    contraseña = input("Contraseña: ").strip()
    
    # Si no hay usuarios registrados, asignar rol de administrador al primero
    if not usuarios:
        nuevo_usuario = {
            'nombre_completo': nombre,
            'email': email,
            'contraseña': contraseña,
            'rol': 'administrador'
        }
        usuarios.append(nuevo_usuario)
        print("Primer usuario registrado como administrador.")
    else:
        exito, mensaje = registrar_usuario(nombre, email, contraseña)
        print(mensaje)


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

def mostrar_menu():
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

    print(f"\n{BOLD}{OKGREEN}==================== MENÚ ===================={ENDC}")
    print(f"{OKBLUE}1.{ENDC} Listar dispositivos")
    print(f"{OKBLUE}2.{ENDC} Buscar dispositivo")
    print(f"{OKBLUE}3.{ENDC} Agregar dispositivo")
    print(f"{OKBLUE}4.{ENDC} Eliminar dispositivo")
    print(f"{OKBLUE}5.{ENDC} Activar Modo Ahorro de Energía")
    print(f"{OKBLUE}6.{ENDC} Salir")
    print(f"{BOLD}{OKGREEN}=============================================={ENDC}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            listar_dispositivos()
        elif opcion == "2":
            buscar_dispositivo()
        elif opcion == "3":
          agregar_dispositivo_desde_input()
        elif opcion == "4":
            eliminar_dispositivo()
        elif opcion == "5":
            modo_ahorro()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
