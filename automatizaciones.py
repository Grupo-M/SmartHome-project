"""Módulo con automatizaciones del sistema SmartHome."""

from datos import dispositivos

def modo_ahorro():
    """
    Activa el modo de ahorro de energía:
    Apaga todos los dispositivos que no sean esenciales.
    """
    #Corrección: se recorre la lista de dispositivos y se apagan solo los no esenciales.
    #Esto no altera claves foráneas ni rompe la integridad del modelo relacional.
    for d in dispositivos:
        if not d["esencial"]:
            d["estado"] = "apagado"
    print("Modo Ahorro de Energía activado. Dispositivos no esenciales apagados.")
