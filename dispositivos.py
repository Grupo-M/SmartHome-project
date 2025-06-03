from datos import dispositivos

def listar_dispositivos():
    if not dispositivos:
        print("No hay dispositivos registrados.")
    else:
        for d in dispositivos:
            esencial_texto = "Esencial" if d["esencial"] else "No esencial"
            ubicacion = d.get("ubicacion", "No especificada")
            print(f"ID: {d['id']} | {d['nombre']} - Estado: {d['estado']} - {esencial_texto} - Ubicación: {ubicacion}")
            
def buscar_dispositivo():
    nombre = input("Ingrese el nombre del dispositivo a buscar: ")
    for d in dispositivos:
        if nombre.lower() in d["nombre"].lower():
            esencial_texto = "Esencial" if d["esencial"] else "No esencial"
            ubicacion = d.get("ubicacion", "No especificada")
            print(f"ID: {d['id']} - {d['nombre']} | Estado: {d['estado']} | {esencial_texto} | Ubicación: {ubicacion}")
            return
    print("Dispositivo no encontrado.")

def agregar_dispositivo(nombre, estado ="apagado", esencial= False, ubicacion ="No especificada"):
    if not nombre.strip():
        print("Error: El nombre no puede estar vacío.")
        return

    if estado not in ["encendido", "apagado"]:
        print("Error: El estado debe ser 'encendido' o 'apagado'.")
        return
    if dispositivos:
        max_id = max(d.get("id", 0) for d in dispositivos)
        nuevo_id = max_id + 1
    else:
        nuevo_id = 1

    dispositivos.append({
        "id": nuevo_id,
        "nombre": nombre,
        "estado": estado,
        "esencial": esencial,
        "ubicacion": ubicacion
    })
    print("Dispositivo agregado correctamente.")

def eliminar_dispositivo():
    nombre = input("Nombre del dispositivo a eliminar: ")
    for d in dispositivos:
        if d["nombre"].lower() == nombre.lower():
            dispositivos.remove(d)
            print("Dispositivo eliminado.")
            return
    print("No se encontró el dispositivo.")
