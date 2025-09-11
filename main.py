"""Módulo principal que ejecuta el sistema SmartHome."""

from dispositivos import (
    listar_dispositivos,
    buscar_dispositivo,
    agregar_dispositivo,
    eliminar_dispositivo,
)
from automatizaciones import modo_ahorro

def agregar_dispositivo_desde_input():
    """Solicita datos por consola y agrega un dispositivo nuevo."""
    nombre = input("Nombre del nuevo dispositivo: ").strip()
    if not nombre:
        print("El nombre es obligatorio.")
        return

    estado = input(
        "Estado (encendido/apagado) [por defecto apagado]: "
    ).strip().lower()
    if estado not in ["encendido", "apagado", ""]:
        print("Estado no válido. Se usará 'apagado' por defecto.")
        estado = "apagado"
    if estado == "":
        estado = "apagado"

    esencial_input = input(
        "¿Es esencial? (s/n) [por defecto n]: "
    ).strip().lower()
    esencial = esencial_input == "s"

    ubicacion = input(
        "Ubicación del dispositivo "
        "(ej: sala, dormitorio, cocina) [por defecto No especificada]: "
    ).strip()
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
    """Ejecuta el bucle principal del sistema."""
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
