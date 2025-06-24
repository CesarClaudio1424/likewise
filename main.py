import streamlit as st
import asignacion
import envio

st.set_page_config(page_title="Checkouts Likewise", layout="centered")
st.title("🧠 Webhooks Likewise")

# Opciones de cuenta
cuenta = st.radio("Selecciona una cuenta:", ["Telefonica", "Entel", "Omnicanalidad", "Biobio"])

# Acciones
st.write("Selecciona qué quieres procesar:")
creacion = st.checkbox("Creación")
inicio = st.checkbox("Inicio")
checkout = st.checkbox("Checkout")
exclusion = st.checkbox("Exclusiones")

rutas_input = st.text_area("Introduce las rutas o visitas (una por línea):")

if st.button("Procesar"):
    if not rutas_input.strip():
        st.error("Coloca la ruta o visita a procesar.")
    else:
        if exclusion and (creacion or inicio or checkout):
            st.error("No puedes excluir visitas y procesar rutas al mismo tiempo.")
        else:
            links = asignacion.links(cuenta)
            rutas = rutas_input.strip().split("\n")

            if exclusion:
                for r in rutas:
                    response = envio.ejecucionurlvisitas([int(r)], links[3])
                    st.markdown(f"**Exclusión:** {response[0]}", unsafe_allow_html=True)
            else:
                if creacion:
                    for r in rutas:
                        response = envio.ejecucionurl([r], links[0])
                        st.markdown(f"**Creación:** {response[0]}", unsafe_allow_html=True)
                if inicio:
                    for r in rutas:
                        response = envio.ejecucionurl([r], links[1])
                        st.markdown(f"**Inicio:** {response[0]}", unsafe_allow_html=True)
                if checkout:
                    for r in rutas:
                        response = envio.ejecucionurl([r], links[2])
                        st.markdown(f"**Checkout:** {response[0]}", unsafe_allow_html=True)

            st.success("✅ Proceso finalizado.")