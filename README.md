# Mi Negocio W · Python y Streamlit

Proyecto académico de **Laura Sardi** para la actividad **Mi primer programa en Python**.

La calculadora recibe las ventas, el costo de productos o materiales vendidos y los otros gastos del mismo mes, en pesos colombianos enteros. Calcula el total de egresos y el resultado, e identifica ganancia, pérdida o equilibrio.

```text
Total de egresos = costos + otros gastos
Resultado = ventas - total de egresos
```

## Ejecutar en consola

Requiere Python 3. Esta versión no usa paquetes externos.

```bash
python mi_negocio_w.py
```

## Ejecutar con Streamlit

Usar Python 3.12 y, preferiblemente, un entorno virtual.

```bash
pip install -r requirements.txt
streamlit run app.py
```

La versión web utiliza `calculos.py` para validar los montos y calcular el resumen. Aplica la misma fórmula y las mismas tres categorías que el programa original de consola. El formulario reemplaza las llamadas a `input()` y los componentes de Streamlit presentan las salidas.

## Desplegar en Streamlit Community Cloud

1. Conectar la cuenta de GitHub en [Streamlit Community Cloud](https://share.streamlit.io/).
2. Elegir **Create app** y seleccionar este repositorio, la rama `main` y el archivo `app.py`.
3. En las opciones avanzadas, elegir Python 3.12 y pulsar **Deploy**.
4. Compartir la dirección pública de la aplicación.

## Ejemplos

| Ventas | Costos | Otros gastos | Resultado |
| ---: | ---: | ---: | --- |
| 3000000 | 1500000 | 800000 | Ganancia de 700000 COP |
| 1000000 | 700000 | 500000 | Pérdida de 200000 COP |
| 1500000 | 1000000 | 500000 | Equilibrio |

Los montos pueden ser cero y no pueden ser negativos. No se aceptan letras, decimales ni separadores de miles. Se deben separar los costos de los otros gastos para no contar dos veces un mismo valor.

## Archivos

- `mi_negocio_w.py`: programa original de consola incluido en la entrega.
- `app.py`: aplicación web en Python y Streamlit.
- `calculos.py`: lógica de cálculo de la versión web.
- `requirements.txt`: dependencia necesaria para Streamlit.
- `.streamlit/config.toml`: tema y configuración de la aplicación.

Proyecto inspirado en el contexto de Banco W, sin afiliación oficial. Usa datos ficticios y un cálculo simplificado, sin impuestos, créditos ni intereses. No representa un estado financiero completo.
