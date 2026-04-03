import streamlit as st
from datetime import datetime
from supabase import create_client

# SESSION USER

if "user" not in st.session_state:
    st.session_state.user = None

    st.set_page_config(layout="wide")

# CSS

st.markdown("""
<style>

/* BOTON VOLVER */

div[data-testid="stForm"] {
    border: none !important;
    background: transparent !important;
    padding: 0 !important;
}

/* FIJADO */
.volver-fixed {
    position: fixed;
    top: 80px;        
    left: 20px;       
    z-index: 9999;
}

.volver-fixed button {
    background-color: #0ea5e9 !important; 
    color: white !important;
    border: none !important;
    padding: 8px 14px !important;
    font-size: 14px !important;
    border-radius: 10px !important;
    cursor: pointer;
}

/* BOTONES DE FORM (LOGIN + VOLVER) */
div[data-testid="stForm"] button {
    background-color: #0ea5e9 !important;  /* azul fijo */
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 8px 16px !important;
    font-size: 14px !important;
}

/* HOVER */
div[data-testid="stForm"] button:hover {
    background-color: #0284c7 !important;
}

/* QUITAR EFECTOS DE TEMA */
div[data-testid="stForm"] button:focus,
div[data-testid="stForm"] button:active {
    outline: none !important;
    box-shadow: none !important;
}

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

/* TÍTULOS DENTRO DE LOS MÓDULOS */
h2 {
    color: #f0f0f0 !important;
}

/* TEXTOS EN GENERAL */
p {
    color: #f0f0f0 !important;
    font-size: 25px;
}

/* 🔥 TARJETAS (reemplazo visual de botones) */
div[data-testid="stHorizontalBlock"] > div:nth-child(1) div.stButton > button,
div[data-testid="stHorizontalBlock"] > div:nth-child(2) div.stButton > button,
div[data-testid="stHorizontalBlock"] > div:nth-child(3) div.stButton > button,
div[data-testid="stHorizontalBlock"] > div:nth-child(4) div.stButton > button {

    height: 180px !important;
    border-radius: 20px !important;

    display: flex !important;
    align-items: center;
    justify-content: center;

    font-size: 20px !important;
    font-weight: 600;

    color: white !important;

    background: linear-gradient(135deg, #0ea5e9, #2563eb) !important;

    border: none !important;

    box-shadow: 0 10px 30px rgba(0,0,0,0.25);

    transition: all 0.25s ease;
}

/* 🔥 HOVER PRO */
div[data-testid="stHorizontalBlock"] div.stButton > button:hover {
    transform: translateY(-6px) scale(1.02);
    box-shadow: 0 20px 40px rgba(0,0,0,0.35);
}

/* 🔥 COLORES DIFERENTES POR CARD */
div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {
    background: linear-gradient(135deg, #10b981, #065f46) !important;
}

div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
    background: linear-gradient(135deg, #f59e0b, #92400e) !important;
}

div[data-testid="stHorizontalBlock"] > div:nth-child(3) button {
    background: linear-gradient(135deg, #6366f1, #312e81) !important;
}

div[data-testid="stHorizontalBlock"] > div:nth-child(4) button {
    background: linear-gradient(135deg, #ef4444, #7f1d1d) !important;
}

/* CERRAR SESION */
div.stButton:nth-of-type(1) > button {
    background-color: #0ea5e9 !important;   
    box-shadow: inset 0 0 0 1px rgba(14,165,233,0.3);
}

""", unsafe_allow_html=True)

# SUPABASE

SUPABASE_URL = "https://mloxdzoadanzfkbwbdlw.supabase.co"
SUPABASE_KEY = "sb_publishable_8oIML4DDkjw4MBFu8Mee2g_2Kw-VLgB"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# INGRESAR

if st.session_state.user is None:

    st.markdown('<p class="titulo">INICIAR SESIÓN</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        with st.form("login_form"):
            usuario = st.text_input("Usuario")
            password = st.text_input("Contraseña", type="password")

            submitted = st.form_submit_button("Ingresar")

            if submitted:
                res = supabase.table("usuarios").select("*").eq("usuario", usuario).execute()

                if len(res.data) > 0:
                    user = res.data[0]

                    if user["password"] == password:
                        st.session_state.user = user
                        st.rerun()
                    else:
                        st.error("Contraseña incorrecta")
                else:
                    st.error("Usuario no existe")
# APP

else:

    st.sidebar.write(f"{st.session_state.user['usuario']}")
    
    if st.sidebar.button("Cerrar sesión"):
        st.session_state.user = None
        st.rerun()
    
    if "pagina" not in st.session_state:
        st.session_state.pagina = "inicio"
    
    if st.session_state.pagina == "inicio":
    
        st.markdown('<p class="titulo">ADMINISTRACIÓN DE CANALES</p>', unsafe_allow_html=True)
        st.markdown('<p class="sub">Seleccione un módulo</p>', unsafe_allow_html=True)
    
        col1, col2, col3, col4 = st.columns(4)
    
        with col1:
            if st.button("Gestión de vehículos", use_container_width=True):
                st.session_state.pagina = "vehiculos"
                st.rerun()
    
        with col2:
            if st.button("Reportar demoras", use_container_width=True):
                st.session_state.pagina = "demoras"
                st.rerun()
    
        with col3:
            if st.button("Apartados postales", use_container_width=True):
                st.session_state.pagina = "apartados"
                st.rerun()
    
        with col4:
            if st.button("No distribuibles", use_container_width=True):
                st.session_state.pagina = "nodist"
                st.rerun()

# MODULOS

    elif st.session_state.pagina == "vehiculos":
        
        st.markdown("## Módulo Vehículos")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Registrar vehículo", use_container_width=True):
                st.session_state.pagina = "registro"
                st.rerun()
        
        with col2:
            if st.button("Reportar incidencia", use_container_width=True):
                st.session_state.pagina = "incidencia"
                st.rerun()
        
        st.markdown('<div class="volver-fixed">', unsafe_allow_html=True)

        with st.form("volver_form", clear_on_submit=False):
            volver = st.form_submit_button("← Volver")
        
            if volver:
                st.session_state.pagina = "inicio"
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    elif st.session_state.pagina == "demoras":
        
        st.markdown("## Demoras Operativas")
        st.markdown("Reporta problemas por clima, huaicos u otros eventos")
        
        st.link_button(
            "Ir al formulario de demoras",
            "https://docs.google.com/forms/d/e/1FAIpQLSdANPp9EjjhS51Jkg0AP0WHihKGK48OqoV0sfNKKm4U_B8APw/viewform?usp=sharing"
        )
        
        st.markdown('<div class="volver-fixed">', unsafe_allow_html=True)

        with st.form("volver_form", clear_on_submit=False):
            volver = st.form_submit_button("← Volver")
        
            if volver:
                st.session_state.pagina = "inicio"
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    
    elif st.session_state.pagina == "apartados":
        
        st.markdown("## Apartados Postales")
        st.write("Módulo en construcción")
        
        st.markdown('<div class="volver-fixed">', unsafe_allow_html=True)

        with st.form("volver_form", clear_on_submit=False):
            volver = st.form_submit_button("← Volver")
        
            if volver:
                st.session_state.pagina = "inicio"
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    
    elif st.session_state.pagina == "nodist":
        
        st.markdown("## Envíos no distribuibles")
        st.write("Módulo en construcción")
        
        st.markdown('<div class="volver-fixed">', unsafe_allow_html=True)

        with st.form("volver_form", clear_on_submit=False):
            volver = st.form_submit_button("← Volver")
        
            if volver:
                st.session_state.pagina = "inicio"
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
