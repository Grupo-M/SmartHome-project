"""Módulo con automatizaciones del sistema SmartHome."""

from datos import dispositivos


def modo_ahorro():
    """
    Activa el modo de ahorro de energía:
    Apaga todos los dispositivos que no sean esenciales.
    """
    for d in dispositivos:
        if not d["esencial"]:
            d["estado"] = "apagado"
    print("Modo Ahorro de Energía activado. Dispositivos no esenciales apagados.")

