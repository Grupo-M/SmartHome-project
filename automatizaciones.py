from datos import dispositivos

def modo_ahorro():
    contador = 0
    for d in dispositivos:
        if not d.get("esencial", False) and d["estado"] != "apagado":
            d["estado"] = "apagado"
            contador += 1
    print(f"Modo Ahorro activado. {contador} dispositivos no esenciales fueron apagados.")
