import streamlit as st
import requests
from streamlit_lottie import st_lottie
import plotly.express as px
import pandas as pd
import datetime

# 1. CONFIGURACIÓN DE PANTALLA TOTAL
st.set_page_config(
    page_title="Fayoga | Fabiola Pastén",
    page_icon="🧘‍♀️",
    layout="wide", # Clave para ocupar todo el espacio en TVs
    initial_sidebar_state="collapsed"
)

# Cargador de Animaciones Pro
def load_lottie(url):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except: return None

lottie_yoga = load_lottie("https://lottie.host/9f5064e4-399a-426c-829d-64d898517228/qG4K3nE0H5.json")
lottie_brain = load_lottie("https://lottie.host/07as9pva-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")

# 2. SISTEMA DE DISEÑO PRO-CONTRASTE (Garantía de legibilidad)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Quicksand:wght@300;500;700&display=swap');
    
    /* Fondo Zen Líquido */
    .stApp { background: linear-gradient(135deg, #fdfaf6 0%, #e9edc9 100%); }

    /* Huincha Americana News Ticker */
    .ticker-wrapper {
        width: 100%; overflow: hidden; background: #2D4030; color: #E9EDC9;
        padding: 10px 0; position: fixed; top: 0; left: 0; z-index: 1001;
    }
    .ticker {
        display: inline-block; white-space: nowrap; padding-left: 100%;
        animation: ticker 30s linear infinite; font-weight: 700;
    }
    @keyframes ticker { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-100%, 0, 0); } }

    /* Premium Glass Cards - Texto Forzado en Oscuro */
    .glass-card {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(15px);
        border-radius: 35px;
        padding: 40px;
        border: 1px solid rgba(255, 255, 255, 0.5);
        box-shadow: 0 15px 35px rgba(0,0,0,0.05);
        margin-bottom: 25px;
        color: #1a1a1a !important; /* Inaceptable el blanco sobre blanco */
    }
    .glass-card h1, .glass-card h2, .glass-card h3 { color: #2D4030 !important; font-family: 'Playfair Display', serif; }
    .glass-card p, .glass-card b, .glass-card span { color: #1a1a1a !important; font-family: 'Quicksand', sans-serif; }

    /* Botón Premium */
    .stButton>button {
        background: #4A5D4E; color: #E9EDC9 !important; border-radius: 50px;
        border: none; padding: 18px 40px; font-weight: 700; width: 100%;
        transition: 0.3s ease;
    }
    .stButton>button:hover { background: #6B8E23; transform: scale(1.02); }
    </style>
    
    <div class="ticker-wrapper"><div class="ticker">
        🔥 NOVEDAD: Taller Boutique de Biodanza - Inscripciones Abiertas | 🧘 Clases de Yoga Matinal Online | 🗞️ Hemeroteca Wellness Curada por Fabiola Pastén | 🤖 FABI IA: Tu Asesora 24/7
    </div></div><br><br><br>
    """, unsafe_allow_html=True)

# 3. LAYOUT DE ALTA GAMA (Header Pro)
with st.container():
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.markdown("<h1 style='text-align: center; font-size: 4rem; margin-bottom: 0;'>FAYOGA</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 1.5rem; color: #4A5D4E;'><b>Fabiola Pastén</b></p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-style: italic; opacity: 0.8;'>Periodista & Wellness Expert</p>", unsafe_allow_html=True)

st.divider()

# 4. EXPERIENCIA DE USUARIO (TABS LÍQUIDAS)
tabs = st.tabs(["💎 Dashboard", "📅 Agendar", "🤖 FABI IA", "📊 Métricas Wellness"])

with tabs[0]: # Dashboard Full Visual
    st.markdown("### El Universo de Fabiola")
    col_v1, col_v2, col_v3 = st.columns(3)
    with col_v1:
        st.markdown("<div class='glass-card'><h3>Yoga</h3><p>Alineación integral y movimiento consciente para equilibrar tu sistema nervioso.</p></div>", unsafe_allow_html=True)
    with col_v2:
        st.markdown("<div class='glass-card'><h3>Biodanza</h3><p>La danza de la vida: integración afectiva y renovación orgánica a través del grupo.</p></div>", unsafe_allow_html=True)
    with col_v3:
        st.markdown("<div class='glass-card'><h3>Wellness</h3><p>Comunicación y bienestar bajo el rigor periodístico de una experta comunicadora.</p></div>", unsafe_allow_html=True)
    
    # Ilustración y Gráfica
    c_img1, c_img2 = st.columns(2)
    with c_img1:
        st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=1200", caption="Yoga: La ciencia del Ser.")
    with c_img2:
        if lottie_yoga: st_lottie(lottie_yoga, height=400)

with tabs[1]: # Agendamiento Premium
    st.markdown("### Reserva tu Transformación")
    col_a1, col_a2 = st.columns([2, 1])
    with col_a1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        nombre = st.text_input("Nombre Completo")
        servicio = st.selectbox("Elegir Experiencia", ["Yoga Matinal", "Taller Biodanza", "Coaching Wellness"])
        fecha = st.date_input("Fecha", min_value=datetime.date.today())
        if st.button("Confirmar Cita Boutique"):
            st.balloons()
            st.success(f"Solicitud enviada, {nombre}. Fabiola te contactará pronto.")
        st.markdown("</div>", unsafe_allow_html=True)
    with col_a2:
        st.markdown("<div class='glass-card'><h4>Ubicación</h4><p>📍 La Serena, Chile / Online Global</p></div>", unsafe_allow_html=True)
        # Mapa Pro de la Serena
        df_map = pd.DataFrame({'lat': [-29.9045], 'lon': [-71.2519]})
        st.map(df_map)

with tabs[2]: # FABI IA: ASESORA PREMIUM
    st.markdown("### FABI: Inteligencia en Bienestar")
    col_ia1, col_ia2 = st.columns([2, 1])
    with col_ia1:
        st.info("FABI utiliza el expertise periodístico de Fabiola para guiarte.")
        pregunta = st.text_input("¿Qué área de tu bienestar quieres explorar hoy?")
        if st.button("Consultar a FABI"):
            st.markdown(f"<div class='glass-card'><b>FABI Responde:</b><br>Basada en la metodología Fayoga, para '{pregunta}' te recomiendo centrarte en la respiración abdominal profunda y conectar con tu ritmo orgánico.</div>", unsafe_allow_html=True)
    with col_ia2:
        if lottie_brain: st_lottie(lottie_brain, height=250)

with tabs[3]: # Métricas y Gráficos (La Gran Ampliación)
    st.markdown("### Visualización del Bienestar")
    st.write("Datos que muestran el impacto real del yoga y la biodanza en tu vida.")
    
    # Gráfico Pro con Plotly
    df_data = pd.DataFrame({
        "Mes": ["Ene", "Feb", "Mar", "Abr"],
        "Bienestar": [70, 85, 92, 98]
    })
    fig = px.line(df_data, x="Mes", y="Bienestar", title="Progreso de Integración Wellness", 
                 color_discrete_sequence=['#6B8E23'], template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

# FOOTER PRO
st.markdown("<br><hr><p style='text-align: center; opacity: 0.6;'>FAYOGA 2026 | Wellness de Clase Mundial por Fabiola Pastén</p>", unsafe_allow_html=True)
