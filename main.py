if st.button("Procesar"):
    if not rutas_input.strip():
        st.error("Coloca la ruta o visita a procesar.")
    else:
        if exclusion and (creacion or inicio or checkout):
            st.error("No puedes excluir visitas y procesar rutas al mismo tiempo.")
        else:
            links = asignacion.links(cuenta)
            rutas = [] # Inicializamos la lista vacía

            # --- MODIFICACIÓN CLAVE ---
            # Ahora decidimos qué tipo de ID buscar
            if exclusion:
                # Si es una exclusión, buscamos secuencias de dígitos (\d+)
                patron_numerico = r'\d+'
                rutas = re.findall(patron_numerico, rutas_input)
            else:
                # Para los demás casos, buscamos el formato UUID
                patron_id = r'[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}'
                rutas = re.findall(patron_id, rutas_input)

            if not rutas:
                st.warning("No se encontraron IDs con el formato esperado en el texto.")
            else:
                # El resto de tu código ya funciona perfecto con esta lógica
                if exclusion:
                    for r in rutas:
                        # Tu código original ya convierte 'r' a entero, lo que es correcto
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
