import streamlit as st
from datetime import datetime
from supabase import create_client

st.set_page_config(layout="wide")

st.markdown("""
<style>

/* FONDO */
[data-testid="stAppViewContainer"] {
    background-image: url("https://webservice.serpost.com.pe/prj_online/Imagen/Seguimiento_Linea.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* TÍTULO */
.titulo {
    font-size: 40px !important;
    font-weight: 800 !important;
    color: #f0f0f0 !important;
    text-align: center !important;
    margin-bottom: 30px !important;
}

/* SUBTÍTULO */
.sub {
    text-align: center;
    color: #f0f0f0 !important;
    font-size: 20px !important;
}

/* BOTONES GRANDES */
div.stButton > button {
    height: 140px !important;
    font-size: 20px !important;
    font-weight: 600 !important;
    border-radius: 16px !important;
    background-color: white !important;
    border: 1px solid #e0e0e0 !important;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08) !important;
    transition: all 0.2s ease;
}

/* HOVER */
div.stButton > button:hover {
    background-color: #eef3f8 !important;
    transform: translateY(-3px);
}

/* COLORES POR MÓDULO */
div.stButton:nth-of-type(1) > button {
    border-left: 6px solid #1f77b4 !important;
}

div.stButton:nth-of-type(2) > button {
    border-left: 6px solid #dc3545 !important;
}

div.stButton:nth-of-type(3) > button {
    border-left: 6px solid #ffc107 !important;
}

div.stButton:nth-of-type(4) > button {
    border-left: 6px solid #6c757d !important;
}

</style>
""", unsafe_allow_html=True)

# SUPABASE

SUPABASE_URL = "https://mloxdzoadanzfkbwbdlw.supabase.co"
SUPABASE_KEY = "sb_publishable_8oIML4DDkjw4MBFu8Mee2g_2Kw-VLgB"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# USUARIOS

def login(usuario, password):
    res = supabase.table("usuarios").select("*").eq("usuario", usuario).eq("password", password).execute()
    return len(res.data) > 0

# ===== SESSION STATE ===== #

if "pagina" not in st.session_state:
    st.session_state["pagina"] = "inicio"
    
# ===== MAIN NAVIGATION ===== #

if st.session_state["pagina"] == "inicio":

    st.markdown('<p class="titulo">ADMINISTRACIÓN DE CANALES</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub">Seleccione un módulo</p>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    # VEHICULOS
    with col1:
        if st.button("🚚\n\nGestión de vehículos\nRegistro y control de la flota", 
                 key="vehiculos_btn", 
                 use_container_width=True):
            st.session_state["pagina"] = "vehiculos"
            st.rerun()
                     
    # DEMORAS
    with col2:
        if st.button("⏱️\n\nDemoras operativas\nIncidencias externas",
                key="demoras_btn",
                use_container_width=True):
            st.session_state["pagina"] = "demoras"
            st.rerun()

    # APARTADOS
    with col3:
        if st.button("📦\n\nApartados\nGestión de apartados",
                key="apartados_btn",
                use_container_width=True):
            st.session_state["pagina"] = "apartados"
            st.rerun()
        
    # NO DISTRIBUIBLES
    with col4:
        if st.button("⚠️\n\nNo distribuibles\nEnvíos no entregados",
                key="nodist_btn",
                use_container_width=True):
            st.session_state["pagina"] = "nodist"
            st.rerun()

# ===== MODULO VEHICULOS =====
elif st.session_state.pagina == "vehiculos":

    # subestado interno
    if "subvehiculos" not in st.session_state:
        st.session_state.subvehiculos = "menu"
        st.rerun()

    st.markdown("## 🚚 Módulo Vehículos")

    # MENU
    if st.session_state.subvehiculos == "menu":

        st.markdown("Seleccione una opción:")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Registrar vehículo", use_container_width=True):
                st.session_state.subvehiculos = "registro"
                st.rerun()

        with col2:
            if st.button("Reportar incidencia", use_container_width=True):
                st.session_state.subvehiculos = "incidencia"
                st.rerun()

    # REGISTRO
    elif st.session_state.subvehiculos == "registro":

        st.markdown("### 📝 Registro de vehículo")

        placa = st.text_input("Placa")
        tipo = st.selectbox("Tipo", ["Camión", "Van", "Auto"])
        capacidad = st.number_input("Capacidad (kg)", min_value=0)

        if st.button("Guardar"):
            st.success("Vehículo registrado")
            st.rerun()
            
        col1, col2 = st.columns([1,10])

        with col1:
            if st.button("← Volver al inicio"):
                st.session_state["pagina"] = "inicio"
                st.rerun()
    
    # INCIDENCIA
    elif st.session_state.subvehiculos == "incidencia":

        st.markdown("### ⚠️ Reporte de incidencia")

        placa = st.text_input("Placa")
        descripcion = st.text_area("Descripción")
        fecha = st.date_input("Fecha")

        if st.button("Enviar"):
            st.success("Incidencia registrada")
            st.rerun()

        col1, col2 = st.columns([1,10])

        with col1:
            if st.button("← Volver al inicio"):
                st.session_state["pagina"] = "inicio"
                st.reru

# ===== MODULO DEMORAS =====
elif st.session_state.pagina == "demoras":

    st.markdown("## ⏱️ Demoras operativas")

    st.markdown("Reporta problemas por clima, huaicos u otros eventos")

    st.link_button(
        "Ir al formulario",
        "https://docs.google.com/forms/d/e/1FAIpQLSdANPp9EjjhS51Jkg0AP0WHihKGK48OqoV0sfNKKm4U_B8APw/viewform"
    )

    col1, col2 = st.columns([1,10])

    with col1:
        if st.button("← Volver al inicio"):
            st.session_state["pagina"] = "inicio"
            st.reru

# ===== MODULO APARTADOS =====
elif st.session_state.pagina == "apartados":

    st.markdown("## 📦 Apartados postales")
    st.write("Módulo en construcción")

    col1, col2 = st.columns([1,10])

    with col1:
        if st.button("← Volver al inicio"):
            st.session_state["pagina"] = "inicio"
            st.reru

# ===== MODULO NO DISTRIBUIBLES =====
elif st.session_state.pagina == "nodist":

    st.markdown("## ⚠️ No distribuibles")
    st.write("Módulo en construcción")

    col1, col2 = st.columns([1,10])

    with col1:
        if st.button("← Volver al inicio"):
            st.session_state["pagina"] = "inicio"
            st.reru
