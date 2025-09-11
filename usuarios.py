"""Módulo para gestionar los usuarios del sistema SmartHome."""

from datos_de_usuarios import usuarios


def registrar_usuario_desde_input():
    """Solicita datos al usuario y registra un nuevo usuario en la lista."""
    print("\n=== Registro de Usuario ===")
    nombre = input("Nombre completo: ").strip()
    email = input("Correo electrónico: ").strip().lower()
    contrasena = input("Contraseña: ").strip()

    nuevo_usuario = {
        "nombre_completo": nombre,
        "email": email,
        "contrasena": contrasena,
    }

    usuarios.append(nuevo_usuario)
    print("Usuario registrado con éxito.")


def listar_usuarios():
    """Lista todos los usuarios registrados en consola."""
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        for idx, u in enumerate(usuarios, 1):
            print(f"{idx}. {u['nombre_completo']} - {u['email']}")

