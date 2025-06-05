from automatizaciones import modo_ahorro
from dispositivos import agregar_dispositivo, listar_dispositivos, buscar_dispositivo, eliminar_dispositivo
from usuarios import modificar_rol


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
