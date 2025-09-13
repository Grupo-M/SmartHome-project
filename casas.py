"""Módulo para gestionar las casas del sistema SmartHome."""

from datos_de_casas import casas
from datos_de_usuarios import usuarios

def listar_casas():
    """Muestra todas las casas registradas."""
    if not casas:
        print("No hay casas registradas.")
    else:
        for c in casas:
            propietario = next((u["nombre_completo"] for u in usuarios if u["id_usuario"] == c["id_usuario"]), "Desconocido")
            print(f"ID: {c['id_casa']} | {c['nombre_casa']} - Dirección: {c['direccion']} - Propietario: {propietario}")

def agregar_casa(nombre_casa, direccion, id_usuario):
    """Agrega una nueva casa al sistema."""
    nuevo_id = max((c["id_casa"] for c in casas), default=0) + 1
    casas.append({
        "id_casa": nuevo_id,
        "nombre_casa": nombre_casa.strip(),
        "direccion": direccion.strip(),
        "id_usuario": id_usuario
    })
    print("Casa agregada correctamente.")

def buscar_casa_por_id(id_casa):
    """Devuelve la casa con el id especificado o None si no existe."""
    return next((c for c in casas if c["id_casa"] == id_casa), None)
