import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pandas as pd
import time

# ==========================================
# 1. NÚCLEO Y SESIÓN (SIN MURO DE ENTRADA)
# ==========================================
st.set_page_config(page_title="Fayoga Academy", page_icon="🧘‍♀️", layout="wide", initial_sidebar_state="collapsed")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = "Invitado"
if 'nivel_actual' not in st.session_state:
    st.session_state.nivel_actual = 1

# Cargador de Animaciones (Lottie)
def load_lottie(url: str):
    try:
        r = requests.get(url, timeout=5)
        return r.json() if r.status_code == 200 else None
    except: return None

# Galería de Animaciones Restauradas
lottie_logo = load_lottie("https://lottie.host/807f4340-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json") # Loto
lottie_yoga_flow = load_lottie("https://lottie.host/9f5064e4-399a-426c-829d-64d898517228/qG4K3nE0H5.json") # Práctica
lottie_dance = load_lottie("https://lottie.host/0a9f5d34-d9ae-44d5-83e8-8a033b0067b5/7L6A0G0U0V.json") # Monitos bailando
lottie_ia = load_lottie("https://lottie.host/07as9pva-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")

# ==========================================
# 2. DISEÑO RESTAURADO (TEXTO BLANCO SOBRE VERDE Y BOTONES GIGANTES)
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@900&family=Quicksand:wght@400;600;700&display=swap');
    
    .stApp { background: linear-gradient(135deg, #fdfaf6 0%, #e9edc9 100%); }
    .main .block-container { padding-top: 3rem !important; max-width: 95% !important; }

    /* FAYOGA: EL LOGO GIGANTE RESTAURADO */
    .brand-title {
        font-family: 'Playfair Display', serif; 
        font-size: clamp(5rem, 15vw, 10rem) !important;
        color: #2D4030 !important; 
        text-align: center; 
        line-height: 0.8; 
        font-weight: 900; 
        margin-bottom: 0px;
        text-shadow: 2px 5px 15px rgba(0,0,0,0.1);
    }
    .brand-subtitle {
        font-family: 'Quicksand', sans-serif; 
        font-size: clamp(1.2rem, 3vw, 2.2rem) !important;
        text-align: center; 
        color: #6B8E23 !important; 
        font-weight: 700; 
        letter-spacing: 12px; 
        margin-top: 15px; 
        text-transform: uppercase;
    }

    /* TARJETAS VERDE OSCURO CON TEXTO BLANCO INMACULADO */
    .premium-card {
        background: #2D4030;
        border-radius: 35px;
        padding: 40px;
        border: 2px solid #A3B18A;
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        margin-bottom: 30px;
    }
    .premium-card h2, .premium-card h3, .premium-card h4 { color: #FFFFFF !important; font-family: 'Playfair Display', serif !important; }
    .premium-card p, .premium-card li { color: #FDF9F3 !important; font-family: 'Quicksand', sans-serif !important; font-size: 1.25rem !important; line-height: 1.6; }

    /* BOTONES SECUNDARIOS PROPORCIONADOS Y HERMOSOS */
    .stButton>button {
        background: linear-gradient(45deg, #6B8E23 0%, #A3B18A 100%);
        color: white !important; 
        border-radius: 50px !important; 
        border: none !important;
        padding: 18px 40px !important; 
        font-weight: 700 !important; 
        font-size: 1.3rem !important; 
        width: 100% !important;
        box-shadow: 0 10px 20px rgba(107, 142, 35, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover { transform: translateY(-3px) !important; box-shadow: 0 15px 25px rgba(107, 142, 35, 0.5) !important; }

    /* PESTAÑAS (TABS) GRANDES Y VISIBLES */
    .stTabs [data-baseweb="tab-list"] { gap: 15px; justify-content: center; flex-wrap: wrap; }
    .stTabs [data-baseweb="tab"] { font-size: 1.4rem !important; font-family: 'Quicksand', sans-serif !important; font-weight: 700 !important; color: #4A5D4E !important; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. HEADER (SIN MURO DE LOGIN)
# ==========================================
c_logo_1, c_logo_2, c_logo_3 = st.columns([1, 2, 1])
with c_logo_2:
    if lottie_logo: st_lottie(lottie_logo, height=150, key="header_anim")
    st.markdown("<h1 class='brand-title'>FAYOGA</h1>", unsafe_allow_html=True)
    st.markdown("<p class='brand-subtitle'>Fabiola Pastén</p>", unsafe_allow_html=True)

st.divider()

# Radio Fayoga Integrada y siempre visible
with st.expander("📻 Radio Fayoga: Sintoniza tu Frecuencia antes de iniciar"):
    pistas_radio = {
        "🌿 Despertar Zen": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        "💧 Flujo de Vinyasa": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
    }
    tema_elegido = st.selectbox("🎵 Selecciona la vibra:", list(pistas_radio.keys()))
    st.audio(pistas_radio[tema_elegido], format="audio/mp3")

# ==========================================
# 4. NAVEGACIÓN ABIERTA (CONTENIDO PROFUNDO)
# ==========================================
tabs = st.tabs(["💎 Dashboard", "🎓 YogaDoc Learning", "💃 Biodanza Flow", "🤖 FABI IA", "🔐 Mi Cuenta (VIP)"])

with tabs[0]: # DASHBOARD
    st.markdown("## Bienvenido, Explora el Universo Fayoga")
    col_d1, col_d2 = st.columns([1.2, 1])
    with col_d1:
        st.markdown("""<div class='premium-card'>
            <h3>La Evolución del Bienestar</h3>
            <p>Fayoga no es solo una clase, es una academia de vida. Hemos estructurado el conocimiento de Fabiola Pastén en módulos progresivos para que conectes tu mente, cuerpo y comunicación.</p>
            <p><b>Explora los primeros niveles de forma gratuita.</b></p>
        </div>""", unsafe_allow_html=True)
    with col_d2:
        st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=1200", use_container_width=True)

with tabs[1]: # YOGADOC (PROFUNDIZANDO EN NIVELES 1, 2 Y 3)
    st.markdown("## YogaDoc: Ruta de Aprendizaje")
    
    col_y1, col_y2 = st.columns([1.5, 1])
    with col_y1:
        st.markdown("""<div class='premium-card'>
            <h3>🌱 Nivel 1: Respiración Primordial</h3>
            <p>El primer paso es el control del diafragma. Aprenderás a expandir tu capacidad pulmonar para reducir el cortisol de forma inmediata.</p>
        </div>""", unsafe_allow_html=True)
        if st.button("▶️ Iniciar Práctica Nivel 1"):
            bar = st.progress(0)
            status = st.empty()
            for i in range(101):
                status.markdown(f"**{'Inhala...' if i < 50 else 'Exhala...'}**")
                bar.progress(i)
                time.sleep(0.03)
            st.success("¡Nivel 1 Superado! Has desbloqueado el Nivel 2.")

        st.markdown("""<div class='premium-card'>
            <h3>🌿 Nivel 2: Alineación Ósea</h3>
            <p>Antes del movimiento, está la estructura. Profundizamos en la postura de la montaña (Tadasana) para enraizar los pies y alinear la columna vertebral, previniendo lesiones corporativas.</p>
        </div>""", unsafe_allow_html=True)
        st.button("🔒 Iniciar Nivel 2 (Requiere completar Nivel 1)")

        st.markdown("""<div class='premium-card'>
            <h3>🌳 Nivel 3: Fluidez Vinyasa</h3>
            <p>El arte de transitar. Aquí sincronizamos la respiración del Nivel 1 con la postura del Nivel 2, creando un flujo dinámico (Flow) que oxigena el cerebro.</p>
        </div>""", unsafe_allow_html=True)
        st.button("🔒 Iniciar Nivel 3 (Requiere cuenta Live/Premium)")

    with col_y2:
        if lottie_yoga_flow: st_lottie(lottie_yoga_flow, height=500)

with tabs[2]: # BIODANZA FLOW CON "MONITOS"
    st.markdown("## Biodanza Flow")
    c_b1, c_b2 = st.columns([1.5, 1])
    with c_b1:
        st.markdown("""<div class='premium-card'>
            <h3>Afectividad y Movimiento</h3>
            <p>Recupera la alegría de vivir. La Biodanza es el sistema de integración grupal de Fabiola. Aquí no hay coreografías perfectas, hay expresión auténtica y conexión humana a través del ritmo.</p>
        </div>""", unsafe_allow_html=True)
    with c_b2:
        # Aquí están las animaciones rítmicas / monitos bailando
        if lottie_dance: st_lottie(lottie_dance, height=250)
        st.caption("Sigue el flujo orgánico...")

with tabs[3]: # FABI IA
    st.markdown("## FABI IA Asesora")
    col_ia1, col_ia2 = st.columns([1, 2])
    with col_ia1:
        if lottie_ia: st_lottie(lottie_ia, height=300)
    with col_ia2:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.markdown("<h3>Consulta a tu mentora virtual</h3>", unsafe_allow_html=True)
        pregunta = st.text_input("¿En qué área de tu bienestar necesitas orientación hoy?", placeholder="Ej: Reducir ansiedad antes de dormir")
        if st.button("Consultar a FABI Expert"):
            st.success("**FABI:** Para esa inquietud, te recomiendo realizar el Nivel 1 de YogaDoc con la música 'Relajación Nocturna' de nuestra Radio Fayoga.")
        st.markdown("</div>", unsafe_allow_html=True)

with tabs[4]: # LOGIN OPCIONAL
    st.markdown("## Zona de Alumnos (VIP)")
    col_log1, col_log2, col_log3 = st.columns([1, 2, 1])
    with col_log2:
        if not st.session_state.logged_in:
            st.markdown("""<div class='premium-card'>
                <h3>Accede a tu cuenta</h3>
                <p>Inicia sesión para desbloquear desde el Nivel 3, acceder a tus estadísticas y a la comunidad de alumnos.</p>
            </div>""", unsafe_allow_html=True)
            usuario = st.text_input("Email o Usuario")
            clave = st.text_input("Contraseña", type="password")
            if st.button("Ingresar a mi portal"):
                if usuario:
                    st.session_state.logged_in = True
                    st.session_state.username = usuario
                    st.rerun()
                else:
                    st.warning("Ingresa un usuario válido.")
        else:
            st.markdown(f"""<div class='premium-card'>
                <h3>Bienvenido de vuelta, {st.session_state.username}</h3>
                <p>Tu pase Premium está activo. Tienes acceso total a la Hemeroteca y a los 10 niveles de YogaDoc.</p>
            </div>""", unsafe_allow_html=True)
            if st.button("Cerrar Sesión"):
                st.session_state.logged_in = False
                st.rerun()

# FOOTER
st.markdown("<br><hr><p style='text-align: center; opacity: 0.6;'>FAYOGA 2026 | Wellness SaaS Premium por Fabiola Pastén</p>", unsafe_allow_html=True)
