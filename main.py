from dispositivos import listar_dispositivos, buscar_dispositivo, agregar_dispositivo, eliminar_dispositivo
from automatizaciones import modo_ahorro

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
            agregar_dispositivo()
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
