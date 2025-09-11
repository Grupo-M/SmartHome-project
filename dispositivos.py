"""Módulo para gestionar los dispositivos del sistema SmartHome."""

from datos import dispositivos, ubicaciones


def obtener_id_ubicacion(nombre_ubicacion, id_casa=1):
    """
    Busca el id_ubicacion según el nombre y la casa.
    Si no existe, crea una nueva ubicación y devuelve su id.
    """
    nombre_ubicacion = nombre_ubicacion.strip().lower()
    for u in ubicaciones:
        if (
            u["nombre_ubicacion"].lower() == nombre_ubicacion
            and u["id_casa"] == id_casa
        ):
            return u["id_ubicacion"]

    # Crear nueva ubicación
    nuevo_id = max((u["id_ubicacion"] for u in ubicaciones), default=0) + 1
    ubicaciones.append(
        {
            "id_ubicacion": nuevo_id,
            "nombre_ubicacion": nombre_ubicacion,
            "id_casa": id_casa,
        }
    )
    return nuevo_id


def nombre_ubicacion_por_id(id_ubicacion):
    """
    Devuelve el nombre de la ubicación dado su id.
    Si no se encuentra, devuelve "No especificada".
    """
    for u in ubicaciones:
        if u["id_ubicacion"] == id_ubicacion:
            return u["nombre_ubicacion"]
    return "No especificada"


def listar_dispositivos():
    """Lista todos los dispositivos registrados en consola."""
    if not dispositivos:
        print("No hay dispositivos registrados.")
    else:
        for d in dispositivos:
            esencial_texto = "Esencial" if d["esencial"] else "No esencial"
            ubicacion_nombre = nombre_ubicacion_por_id(d.get("id_ubicacion"))
            print(
                f"ID: {d['id']} | {d['nombre']} - Estado: {d['estado']} - "
                f"{esencial_texto} - Ubicación: {ubicacion_nombre}"
            )


def buscar_dispositivo():
    """Busca un dispositivo por nombre e imprime su información."""
    nombre = input("Ingrese el nombre del dispositivo a buscar: ").strip()
    for d in dispositivos:
        if nombre.lower() in d["nombre"].lower():
            esencial_texto = "Esencial" if d["esencial"] else "No esencial"
            ubicacion_nombre = nombre_ubicacion_por_id(d.get("id_ubicacion"))
            print(
                f"ID: {d['id']} - {d['nombre']} | Estado: {d['estado']} | "
                f"{esencial_texto} | Ubicación: {ubicacion_nombre}"
            )
            return
    print("Dispositivo no encontrado.")


def agregar_dispositivo(
    nombre,
    estado="apagado",
    esencial=False,
    nombre_ubicacion="No especificada",
    id_casa=1,
):
    """
    Agrega un nuevo dispositivo a la lista.
    Valida el nombre, estado y ubicación antes de registrarlo.
    """
    if not nombre.strip():
        print("Error: El nombre no puede estar vacío.")
        return

    if estado not in ["encendido", "apagado"]:
        print("Error: El estado debe ser 'encendido' o 'apagado'.")
        return

    nuevo_id = max((d.get("id", 0) for d in dispositivos), default=0) + 1
    id_ubicacion = obtener_id_ubicacion(nombre_ubicacion, id_casa)

    dispositivos.append(
        {
            "id": nuevo_id,
            "nombre": nombre.strip(),
            "estado": estado,
            "esencial": bool(esencial),
            "id_ubicacion": id_ubicacion,
        }
    )
    print("Dispositivo agregado correctamente.")


def eliminar_dispositivo():
    """Elimina un dispositivo de la lista por su nombre."""
    nombre = input("Nombre del dispositivo a eliminar: ").strip()
    for d in list(dispositivos):
        if d["nombre"].lower() == nombre.lower():
            dispositivos.remove(d)
            print("Dispositivo eliminado.")
            return
    print("No se encontró el dispositivo.")

