"""Interfaz web de Mi Negocio W, construida íntegramente en Python."""
from pathlib import Path
import streamlit as st
from calculos import calcular_resultado, pesos

st.set_page_config(page_title="Mi Negocio W", page_icon="💜", layout="centered")
BASE = Path(__file__).resolve().parent
CAMPOS = ("ventas", "costos", "otros_gastos")
EJEMPLOS = {
    "Ganancia": (3000000, 1500000, 800000),
    "Pérdida": (1000000, 700000, 500000),
    "Equilibrio": (1500000, 1000000, 500000),
}


def cargar_ejemplo():
    """Actualiza los campos antes de volver a mostrar el formulario."""
    valores = EJEMPLOS.get(st.session_state.ejemplo, ("", "", ""))
    for campo, valor in zip(CAMPOS, valores):
        st.session_state[campo] = str(valor)


st.caption("LAURA SARDI · MI PRIMER PROGRAMA EN PYTHON")
st.title("Mi Negocio W")
st.subheader("De las ventas al resultado real.")
st.write("Descubre si tu mes terminó con ganancia, pérdida o equilibrio.")
st.caption("Proyecto académico inspirado en Banco W. No es una herramienta oficial.")
st.selectbox("Prueba un ejemplo o ingresa tus datos", ["Ingresar datos"] + list(EJEMPLOS),
             key="ejemplo", on_change=cargar_ejemplo)

with st.form("datos_del_mes"):
    st.markdown("### Los números de tu mes")
    st.caption("Pesos colombianos enteros, sin puntos ni comas. Usa datos del mismo mes.")
    ventas_texto = st.text_input("Ventas del mes (COP)", key="ventas")
    costos_texto = st.text_input("Costo de productos o materiales vendidos (COP)",
                                key="costos")
    otros_texto = st.text_input("Otros gastos del negocio (COP)", key="otros_gastos",
                               help="No repitas los costos de lo vendido.")
    enviado = st.form_submit_button("Calcular resultado", type="primary")

if enviado:
    try:
        # ENTRADA: convertir el texto del formulario en pesos enteros.
        ventas = int(ventas_texto)
        costos = int(costos_texto)
        otros_gastos = int(otros_texto)
        # PROCESO: aplicar las mismas operaciones del programa de consola.
        total_egresos, resultado, estado = calcular_resultado(ventas, costos, otros_gastos)
    except ValueError:
        st.error("Revisa los tres campos: usa enteros no negativos, sin puntos ni comas.")
    else:
        # SALIDA: presentar los valores y la interpretación del resultado.
        st.markdown("### Así cerró tu negocio")
        st.metric("Resultado mensual", pesos(resultado))
        if estado == "GANANCIA":
            st.success("GANANCIA: tus ventas superaron los costos y otros gastos.")
        elif estado == "PÉRDIDA":
            st.error("PÉRDIDA: los costos y otros gastos superaron tus ventas.")
        else:
            st.info("EQUILIBRIO: tus ventas cubrieron exactamente los costos y gastos.")
        st.table({"Concepto": ["Ventas", "Costos", "Otros gastos", "Total de egresos"],
                  "Valor (COP)": [pesos(ventas), pesos(costos), pesos(otros_gastos),
                                  pesos(total_egresos)]})
        st.caption("Ventas − costos − otros gastos = resultado mensual.")

st.divider()
with st.expander("Ver el código Python de la entrega"):
    codigo = (BASE / "mi_negocio_w.py").read_text(encoding="utf-8")
    st.code(codigo, language="python")
    st.download_button("Descargar código de consola", codigo,
                       file_name="mi_negocio_w.py", mime="text/plain")
with st.expander("Ver código de la versión Streamlit"):
    st.code((BASE / "app.py").read_text(encoding="utf-8"), language="python")
    st.code((BASE / "calculos.py").read_text(encoding="utf-8"), language="python")
documento = BASE / "Laura_Sardi_PrimerProgramaPython.pdf"
if documento.exists():
    st.download_button("Descargar entrega en PDF", documento.read_bytes(),
                       file_name=documento.name, mime="application/pdf")
st.caption("Cálculo académico simplificado: sin impuestos, créditos ni intereses. "
           "No representa un estado financiero completo. "
           "Usa datos ficticios; los valores no se guardan en un historial.")
