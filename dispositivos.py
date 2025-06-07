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
    if not dispositivos:
        print("No hay dispositivos para buscar.")
        return

    nombre_busqueda = input("Ingrese el nombre del dispositivo a buscar: ").strip() 
    if not nombre_busqueda: 
        print("Formato incorrecto, por favor ingrese un nombre válido.")
        return

    coincidencias = []
    busqueda_lower = nombre_busqueda.lower()

    for d in dispositivos:
        if busqueda_lower in d.get("nombre", "").lower():
            coincidencias.append(d)

    if not coincidencias:
        print(f"No se encontró ningún dispositivo que coincida con '{nombre_busqueda}'.")
    else:
        print(f"\n--- Resultados de búsqueda para '{nombre_busqueda}' ---")
        if len(coincidencias) > 1:
            print(f"Se encontraron {len(coincidencias)} coincidencias:")
        
        for d in coincidencias:
            esencial_texto = "Esencial" if d.get("esencial", False) else "No esencial"
            ubicacion = d.get("ubicacion", "No especificada")
            print(f"ID: {d.get('id', 'N/A')} | {d.get('nombre', 'Nombre Desconocido')} - Estado: {d.get('estado', 'N/A')} | {esencial_texto} | Ubicación: {ubicacion}")
        print("---------------------------------------")

def agregar_dispositivo(nombre, estado="apagado", esencial=False, ubicacion="No especificada"):
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
    if not dispositivos:
        print("No hay dispositivos registrados para eliminar.")
        return

    nombre = input("Nombre del dispositivo a eliminar: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return

    for d in dispositivos:
        if d["nombre"].lower() == nombre.lower():
            confirmacion = input(f"¿Está seguro de que desea eliminar el dispositivo '{d['nombre']}'? (s/n): ").lower()
            if confirmacion == 's':
                dispositivos.remove(d)
                print("Dispositivo eliminado correctamente.")
            else:
                print("Eliminación cancelada.")
            return

    print("No se encontró ningún dispositivo con ese nombre.")
