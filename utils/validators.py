def validar_monto(valor):
    try:
        return float(valor) > 0
    except ValueError:
        return False
