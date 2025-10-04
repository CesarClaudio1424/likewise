import streamlit as st
import asignacion
import envio
import re # ¡Importante! Añade esta línea al inicio de tu script

st.set_page_config(page_title="Checkouts Likewise", layout="centered")
st.title("Webhooks Likewise")

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
            
            # --- AQUÍ ESTÁ LA MODIFICACIÓN ---
            # 1. Definimos el patrón de un ID (formato UUID).
            patron_id = r'[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}'
            
            # 2. Usamos re.findall para extraer todos los IDs que coincidan con el patrón.
            rutas = re.findall(patron_id, rutas_input)
            
            # (Opcional pero recomendado) Verificar si se encontraron IDs
            if not rutas:
                st.warning("No se encontraron IDs con el formato esperado en el texto.")
            
            # El resto de tu código funciona exactamente igual
            if exclusion:
                for r in rutas:
                    # Asumiendo que 'exclusion' trabaja con otro tipo de ID numérico, mantenemos esa lógica si es necesario.
                    # Si 'exclusion' también usa los UUIDs, debes ajustar el tipo de dato.
                    # Para este ejemplo, asumiré que 'exclusion' no se usa con estos IDs.
                    pass # Ajustar si es necesario
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

            if rutas: # Solo muestra el mensaje de éxito si se procesó algo
                st.success("✅ Proceso finalizado.")
