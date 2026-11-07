"""Mi Negocio W: cálculo académico simplificado del resultado mensual."""


def pesos(valor):
    # Da formato al entero; los cálculos conservan los pesos originales.
    return "$" + format(valor, ",d").replace(",", ".")


print("MI NEGOCIO W - RESULTADO MENSUAL")
print("Ejercicio académico no oficial, inspirado en Banco W.")
print("Use COP enteros sin puntos ni comas y datos del mismo mes.")

try:
    # ENTRADA: input lee texto e int lo convierte a un número entero.
    ventas = int(input("Ventas del mes: "))
    costos = int(input("Costo de productos o materiales vendidos: "))
    otros_gastos = int(input("Otros gastos del negocio: "))

    # Los tres montos pueden ser cero, pero no pueden ser negativos.
    if ventas < 0 or costos < 0 or otros_gastos < 0:
        print("Datos inválidos: ningún monto puede ser negativo.")
    else:
        # PROCESO: sumar las salidas y restarlas de las ventas.
        total_egresos = costos + otros_gastos
        resultado = ventas - total_egresos

        # Clasificar el resultado sin confundir ventas con ganancia.
        if resultado > 0:
            estado = "GANANCIA"
        elif resultado < 0:
            estado = "PÉRDIDA"
        else:
            estado = "EQUILIBRIO"

        # SALIDA: presentar los datos, el cálculo y su interpretación.
        print("\nRESUMEN DEL MES (COP)")
        print("Ventas:", pesos(ventas))
        print("Costos:", pesos(costos))
        print("Otros gastos:", pesos(otros_gastos))
        print("Total de egresos:", pesos(total_egresos))
        print("Resultado:", pesos(resultado))
        print("Situación del negocio:", estado)
except ValueError:
    # Letras, vacíos o montos con punto/coma no se convierten a entero.
    print("Entrada inválida. Reinicie y use pesos enteros sin separadores.")
except (EOFError, KeyboardInterrupt):
    print("\nPrograma finalizado: entrada cerrada o cancelada.")
