"""Módulo principal que ejecuta el sistema SmartHome.

Contiene el flujo principal del programa, incluyendo:
- Registro e inicio de sesión de usuarios.
- Menús para usuarios estándar y administradores.
- Gestión de dispositivos.
- Activación de automatizaciones.
"""

from usuarios import registrar_usuario, validar_usuario, modificar_rol
from datos_de_usuarios import usuarios
from automatizaciones import modo_ahorro
from dispositivos import (
    listar_dispositivos,
    buscar_dispositivo,
    agregar_dispositivo,
    eliminar_dispositivo,
)

# ---------------- MENÚS DE USUARIO ---------------- #

def registrar_usuario_desde_input():
    """Solicita datos por consola y registra un nuevo usuario."""
    print("\n=== Registro de Usuario ===")
    nombre = input("Nombre completo: ").strip()
    email = input("Correo electrónico: ").strip().lower()
    contraseña = input("Contraseña: ").strip()

    # Corrección: ahora registrar_usuario() guarda id_rol (FK) en vez de rol como texto.
    exito, mensaje = registrar_usuario(nombre, email, contraseña)
    print(mensaje)


def iniciar_sesion():
    """Solicita credenciales y valida el inicio de sesión."""
    print("\n=== Inicio de Sesión ===")
    email = input("Correo electrónico: ").strip().lower()
    contraseña = input("Contraseña: ").strip()
    exito, resultado = validar_usuario(email, contraseña)
    if exito:
        # Corrección: validar_usuario() devuelve id_rol y añade 'rol' solo para mostrarlo en el menú.
        print(f"¡Bienvenido {resultado['nombre_completo']}!") # type: ignore
        return resultado
    print(resultado)
    return None


def menu_usuario_estandar(usuario):
    """Muestra el menú y opciones disponibles para un usuario estándar."""
    while True:
        print("\n=== MENÚ USUARIO ESTÁNDAR ===")
        print("1. Consultar datos personales")
        print("2. Activar Modo Ahorro de Energía")
        print("3. Consultar dispositivos")
        print("4. Cerrar sesión")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            # Corrección: se muestra el rol usando el campo temporal 'rol', pero internamente se usa id_rol.
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
    """Muestra el menú y opciones disponibles para un usuario administrador."""
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
            # Corrección: gestión de dispositivos adaptada para trabajar con id_ubicacion en lugar de texto.
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

# ---------------- MENÚ DE DISPOSITIVOS ---------------- #

def agregar_dispositivo_desde_input():
    """Solicita datos por consola y agrega un nuevo dispositivo."""
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

    # Corrección: la ubicación ingresada se convierte a id_ubicacion en agregar_dispositivo() para mantener consistencia con el modelo relacional.
    agregar_dispositivo(nombre, estado, esencial, ubicacion)


def menu_gestion_dispositivos():
    """Muestra el menú de gestión de dispositivos y ejecuta la opción seleccionada."""
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

# ---------------- MENÚ PRINCIPAL ---------------- #

def main():
    """Ejecuta el menú principal del sistema SmartHome."""
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
                # Corrección: la lógica de menú usa 'rol' solo para mostrar, pero el dato real se guarda como id_rol.
                if usuario['rol'] == 'administrador': # type: ignore
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
