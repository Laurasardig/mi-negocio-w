"""Operaciones del simulador: independientes de la interfaz gráfica."""


def calcular_resultado(ventas, costos, otros_gastos):
    """Recibe tres enteros no negativos y devuelve el resumen mensual."""
    if any(type(valor) is not int for valor in (ventas, costos, otros_gastos)):
        raise ValueError("Use pesos enteros sin puntos ni comas.")
    if ventas < 0 or costos < 0 or otros_gastos < 0:
        raise ValueError("Ningún monto puede ser negativo.")
    total_egresos = costos + otros_gastos
    resultado = ventas - total_egresos
    if resultado > 0:
        estado = "GANANCIA"
    elif resultado < 0:
        estado = "PÉRDIDA"
    else:
        estado = "EQUILIBRIO"
    return total_egresos, resultado, estado


def pesos(valor):
    """Muestra un entero con signo monetario y puntos de miles."""
    signo = "-" if valor < 0 else ""
    return signo + "$" + format(abs(valor), ",d").replace(",", ".")
