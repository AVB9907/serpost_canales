import streamlit as st
from datetime import datetime
from supabase import create_client

st.set_page_config(layout="wide")

# =========================
# ESTILOS PRO
# =========================

st.markdown("""
<style>
body {
    background-color: #f4f6f9;
}

.card {
    background-color: white;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    text-align: center;
    transition: 0.2s;
}

.card:hover {
    transform: scale(1.03);
}

.titulo {
    font-size: 36px;
    font-weight: bold;
    color: #1f4e79;
    text-align: center;
}

.sub {
    text-align: center;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SUPABASE
# =========================

SUPABASE_URL = "https://mloxdzoadanzfkbwbdlw.supabase.co"
SUPABASE_KEY = "sb_publishable_8oIML4DDkjw4MBFu8Mee2g_2Kw-VLgB"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# =========================
# SESSION STATE
# =========================

if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"

import streamlit as st
from datetime import datetime
from supabase import create_client

st.set_page_config(layout="wide")

# =========================
# ESTILOS
# =========================

st.markdown("""
<style>
body {
    background-color: #f4f6f9;
}

.card {
    background-color: white;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    text-align: center;
    transition: 0.2s;
}

.card:hover {
    transform: scale(1.03);
}

.titulo {
    font-size: 36px;
    font-weight: bold;
    color: #1f4e79;
    text-align: center;
}

.sub {
    text-align: center;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SUPABASE
# =========================

SUPABASE_URL = "https://mloxdzoadanzfkbwbdlw.supabase.co"
SUPABASE_KEY = "sb_publishable_8oIML4DDkjw4MBFu8Mee2g_2Kw-VLgB"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# =========================
# SESSION STATE
# =========================

if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"

elif st.session_state.pagina == "vehiculos":

    st.markdown("## Módulo Vehículos")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Registrar vehículo"):
            st.session_state.pagina = "registro"
            st.rerun()

    with col2:
        if st.button("Reportar incidencia"):
            st.session_state.pagina = "incidencia"
            st.rerun()

    if st.button("Volver"):
        st.session_state.pagina = "inicio"
        st.rerun()

# EJEMPLO SIMPLE

def login(usuario, password):
    res = supabase.table("usuarios").select("*").eq("usuario", usuario).eq("password", password).execute()
    return len(res.data) > 0

elif st.session_state.pagina == "apartados":
    st.subheader("Apartados postales")
    st.write("Módulo en construcción")

    if st.button("Volver"):
        st.session_state.pagina = "inicio"
        st.rerun()

elif st.session_state.pagina == "nodist":
    st.subheader("No distribuibles")
    st.write("Módulo en construcción")

    if st.button("Volver"):
        st.session_state.pagina = "inicio"
        st.rerun()
