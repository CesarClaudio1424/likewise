import streamlit as st
import re
import asignacion
import envio

# Configuración de la página de Streamlit
st.set_page_config(page_title="Checkouts Likewise", layout="centered")
st.title("Webhooks Likewise")

# --- Interfaz de Usuario ---

# Opciones de cuenta
cuenta = st.radio("Selecciona una cuenta:", ["Telefonica", "Entel", "Omnicanalidad", "Biobio"])

# Acciones a realizar
st.write("Selecciona qué quieres procesar:")
creacion = st.checkbox("Creación")
inicio = st.checkbox("Inicio")
checkout = st.checkbox("Checkout")
exclusion = st.checkbox("Exclusiones")

# Área para pegar los IDs
rutas_input = st.text_area("Introduce las rutas o visitas (una por línea):")

# --- Lógica de Procesamiento ---

if st.button("Procesar"):
    if not rutas_input.strip():
        st.error("Coloca la ruta o visita a procesar.")
    else:
        if exclusion and (creacion or inicio or checkout):
            st.error("No puedes excluir visitas y procesar rutas al mismo tiempo.")
        else:
            links = asignacion.links(cuenta)
            rutas = []

            if exclusion:
                patron = r'\d+'
                rutas = re.findall(patron, rutas_input)
            else:
                patron = r'[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}'
                rutas = re.findall(patron, rutas_input)

            if not rutas:
                st.warning("No se encontraron IDs con el formato esperado en el texto.")
            else:
                # --- ESTA ES LA SECCIÓN MODIFICADA ---
                if exclusion:
                    for r in rutas:
                        # 1. Recibimos ambos valores: mensaje y nombre del color
                        mensaje, color_name = envio.ejecucionurlvisitas([int(r)], links[3])
                        # 2. Simplificamos el nombre del color para Streamlit
                        color = "green" if "green" in color_name else "red"
                        # 3. Usamos la sintaxis de color de Streamlit: :color[texto]
                        st.markdown(f"**Exclusión:** :{color}[{mensaje}]")
                else:
                    if creacion:
                        for r in rutas:
                            mensaje, color_name = envio.ejecucionurl([r], links[0])
                            color = "green" if "green" in color_name else "red"
                            st.markdown(f"**Creación:** :{color}[{mensaje}]")
                    if inicio:
                        for r in rutas:
                            mensaje, color_name = envio.ejecucionurl([r], links[1])
                            color = "green" if "green" in color_name else "red"
                            st.markdown(f"**Inicio:** :{color}[{mensaje}]")
                    if checkout:
                        for r in rutas:
                            mensaje, color_name = envio.ejecucionurl([r], links[2])
                            color = "green" if "green" in color_name else "red"
                            st.markdown(f"**Checkout:** :{color}[{mensaje}]")
                
                st.success("✅ Proceso finalizado.")
