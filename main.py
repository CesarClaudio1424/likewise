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
    # 1. Validar que el campo de texto no esté vacío
    if not rutas_input.strip():
        st.error("Coloca la ruta o visita a procesar.")
    else:
        # 2. Validar que no se seleccionen opciones incompatibles
        if exclusion and (creacion or inicio or checkout):
            st.error("No puedes excluir visitas y procesar rutas al mismo tiempo.")
        else:
            # 3. Lógica principal de procesamiento
            links = asignacion.links(cuenta)
            rutas = []  # Inicializamos la lista de rutas

            # Decidimos qué patrón de ID buscar según la selección del usuario
            if exclusion:
                # Si es una exclusión, buscamos solo IDs numéricos
                patron = r'\d+'
                rutas = re.findall(patron, rutas_input)
            else:
                # Para los demás casos, buscamos el formato UUID
                patron = r'[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}'
                rutas = re.findall(patron, rutas_input)

            # 4. Procesar los IDs encontrados
            if not rutas:
                st.warning("No se encontraron IDs con el formato esperado en el texto.")
            else:
                # Lógica para exclusiones
                if exclusion:
                    for r in rutas:
                        # La función de exclusión requiere un entero (int)
                        response = envio.ejecucionurlvisitas([int(r)], links[3])
                        st.markdown(f"**Exclusión:** {response[0]}", unsafe_allow_html=True)
                
                # Lógica para creación, inicio y checkout
                else:
                    if creacion:
                        for r in rutas:
                            response = envio.ejecucionurl([r], links[0])
                            st.markdown
