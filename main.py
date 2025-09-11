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
    """Muestra el menú principal de opciones en consola."""
    ok_blue = "\033[94m"
    ok_green = "\033[92m"
    endc = "\033[0m"
    bold = "\033[1m"

    print(f"\n{bold}{ok_green}==================== MENÚ ===================={endc}")
    print(f"{ok_blue}1.{endc} Listar dispositivos")
    print(f"{ok_blue}2.{endc} Buscar dispositivo")
    print(f"{ok_blue}3.{endc} Agregar dispositivo")
    print(f"{ok_blue}4.{endc} Eliminar dispositivo")
    print(f"{ok_blue}5.{endc} Activar Modo Ahorro de Energía")
    print(f"{ok_blue}6.{endc} Salir")
    print(f"{bold}{ok_green}=============================================={endc}")


def main():
    """Ejecuta el bucle principal del sistema."""
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

