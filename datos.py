"""Módulo con los datos iniciales de ubicaciones y dispositivos."""


# Lista de ubicaciones (modelo relacional)
ubicaciones = [
    {"id_ubicacion": 1, "nombre_ubicacion": "salón", "id_casa": 1},
    {"id_ubicacion": 2, "nombre_ubicacion": "dormitorio", "id_casa": 1},
    {"id_ubicacion": 3, "nombre_ubicacion": "cocina", "id_casa": 1},
    {"id_ubicacion": 4, "nombre_ubicacion": "No especificada", "id_casa": 1},
]

# Lista de dispositivos usando id_ubicacion
dispositivos = [
    {"id": 1, "nombre": "Luz del salón", "estado": "encendido", "esencial": True, "ubicacion": "salón"},
    {"id": 2, "nombre": "Televisor", "estado": "encendido", "esencial": False},
    {"id": 3, "nombre": "Router WiFi", "estado": "encendido", "esencial": True},
    {"id": 4, "nombre": "Ventilador", "estado": "encendido", "esencial": False, "ubicacion": "dormitorio"},
]
