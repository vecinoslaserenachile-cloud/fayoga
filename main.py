import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.add_vertical_space import add_vertical_space
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
import time
import folium
from streamlit_folium import st_folium

# ==========================================
# 1. NÚCLEO ESTRATÉGICO Y PANTALLA TOTAL
# ==========================================
st.set_page_config(
    page_title="Fayoga Premium | Fabiola Pastén",
    page_icon="🧘‍♀️",
    layout="wide", # Ocupación total de pantalla en PCs y TVs
    initial_sidebar_state="collapsed"
)

# Cargador de activos visuales vectoriales
def load_lottie(url: str):
    try:
        r = requests.get(url, timeout=5)
        return r.json() if r.status_code == 200 else None
    except: return None

# Galería de Animaciones Premium
lottie_yoga_zen = load_lottie("https://lottie.host/9f5064e4-399a-426c-829d-64d898517228/qG4K3nE0H5.json")
lottie_pulse = load_lottie("https://lottie.host/807f4340-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")
lottie_brain_ia = load_lottie("https://lottie.host/07as9pva-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")

# ==========================================
# 2. SISTEMA DE DISEÑO "LIQUID ZEN" (CSS PRO)
# ==========================================
# Forzamos contraste profundo y tipografía de gran formato para escritorio
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Quicksand:wght@300;400;500;700&display=swap');
    
    /* Configuración de Contenedor Expandido al 95% para TVs */
    .stApp {
        background: linear-gradient(135deg, #fdfaf6 0%, #e9edc9 100%);
        color: #1A1A1A;
    }
    .main .block-container {
        padding-top: 5rem !important;
        max-width: 95% !important;
        margin: auto;
    }

    /* TEXTOS MAJESTUOSOS Y LEGIBLES */
    h1 { 
        font-size: clamp(4rem, 10vw, 7.5rem) !important; 
        color: #2D4030 !important; 
        font-family: 'Playfair Display', serif !important;
        line-height: 1.1; margin-bottom: 0.5rem; text-align: center;
    }
    h2 { font-size: clamp(2.5rem, 6vw, 4rem) !important; color: #2D4030 !important; font-family: 'Playfair Display', serif !important; }
    h3 { font-size: clamp(1.8rem, 4vw, 3rem) !important; color: #4A5D4E !important; font-family: 'Quicksand', sans-serif !important; }
    
    p, li, span, label { 
        font-size: clamp(1.2rem, 1.8vw, 1.7rem) !important; 
        color: #1A1A1A !important; 
        font-weight: 500 !important;
        line-height: 1.8;
    }

    /* Huincha Americana News Ticker (Estilo TV 2026) */
    .ticker-wrapper {
        width: 100%; overflow: hidden; background: #2D4030; color: #E9EDC9;
        padding: 15px 0; position: fixed; top: 0; left: 0; z-index: 9999;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }
    .ticker {
        display: inline-block; white-space: nowrap; padding-left: 100%;
        animation: ticker 35s linear infinite; font-weight: 700; font-size: 1.4rem;
    }
    @keyframes ticker { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-100%, 0, 0); } }

    /* Glassmorphism Premium Cards - Contraste Blindado */
    .premium-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(25px);
        border-radius: 50px;
        padding: 60px;
        border: 2px solid #A3B18A;
        box-shadow: 0 30px 70px rgba(0,0,0,0.12);
        margin-bottom: 40px;
        transition: transform 0.4s ease;
    }
    .premium-card:hover { transform: translateY(-10px); }

    /* Botones de Acción Estilo Boutique */
    .stButton>button {
        background: linear-gradient(45deg, #4A5D4E 0%, #6B8E23 100%);
        color: white !important; border-radius: 100px; border: none; 
        padding: 30px 80px; font-weight: 700; font-size: 1.8rem; width: 100%;
        box-shadow: 0 20px 40px rgba(107, 142, 35, 0.4);
        transition: 0.3s ease;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 25px 50px rgba(107, 142, 35, 0.6); }

    /* Estilo Tabs Premium */
    .stTabs [data-baseweb="tab-list"] { gap: 50px; justify-content: center; }
    .stTabs [data-baseweb="tab"] { font-size: 1.8rem !important; font-weight: 700; color: #4A5D4E; }
    
    /* Imagen del Logo Circular Pro */
    .logo-img {
        border-radius: 50%;
        border: 5px solid #A3B18A;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        display: block;
        margin: auto;
    }
    </style>
    
    <div class="ticker-wrapper"><div class="ticker">
        🌟 NOVEDAD: Taller Boutique de Biodanza - Sábado 15 de Marzo en La Serena | 🧘‍♀️ Nuevos Cupos Yoga Matinal Online | 🗞️ Hemeroteca Wellness Curada por Fabiola Pastén | 🤖 CONSULTA A FABI IA
    </div></div>
    """, unsafe_allow_html=True)

# ==========================================
# 3. HEADER MAJESTUOSO (LOGO REAL)
# ==========================================
add_vertical_space(2)
c_logo_1, c_logo_2, c_logo_3 = st.columns([1, 1, 1])
with c_logo_2:
    # Integración del Logo Real proporcionado
    st.markdown(f"""
        <img src="https://lookaside.fbsbx.com/lookaside/crawler/instagram/fayoga.bienestar/profile_pic.jpg" 
             class="logo-img" width="250">
    """, unsafe_allow_html=True)

st.markdown("<h1>FAYOGA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 2.8rem !important; color: #4A5D4E; font-weight: 700; margin-top: -15px;'>Fabiola Pastén</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; opacity: 0.8;'>Periodista, Comunicadora y Experta Wellness de Clase Mundial</p>", unsafe_allow_html=True)

st.divider()

# ==========================================
# 4. EXPERIENCIA DE USUARIO (TABS INMERSIVAS)
# ==========================================
tabs = st.tabs(["💎 Dashboard Experience", "🧘‍♀️ Práctica Guiada", "🤖 FABI IA Asesora", "📅 Agenda Boutique", "📊 Métricas"])

with tabs[0]: # Dashboard Full Visual
    st.markdown("## El Ecosistema de Bienestar Integrado")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='premium-card'><h3>Yoga Integral</h3><p>Alineación y paz mental con el rigor comunicacional de Fabiola. Sesiones terapéuticas 1:1 y grupales.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='premium-card'><h3>Biodanza</h3><p>Integración humana y renovación vital a través del movimiento orgánico y rítmico grupal.</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='premium-card'><h3>Wellness Pro</h3><p>Consultoría en bienestar corporativo y comunicación consciente para instituciones de alto impacto.</p></div>", unsafe_allow_html=True)
    
    # Ilustración Premium
    st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=1800", caption="Fayoga: El arte de la integración.")

with tabs[1]: # MI PRÁCTICA (GUIADA POR ANIMACIÓN CONTEXTUAL)
    st.markdown("## Pausa Activa Consciente")
    col_p1, col_p2 = st.columns([1, 1])
    with col_p1:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.write("Sigue el ritmo de la animación de la derecha. **Inhala cuando se expande, exhala cuando se contrae.**")
        st.info("**Técnica Fayoga:** Respiración profunda para el reseteo del sistema nervioso.")
        
        if st.button("🚀 INICIAR GUÍA DE RESPIRACIÓN"):
            status = st.empty()
            prog = st.progress(0)
            for i in range(101):
                msg = "**Inhala profundamente...** 😤" if i < 45 else "**Exhala suavemente...** 😮‍💨"
                status.markdown(f"### {msg}")
                prog.progress(i)
                time.sleep(0.08)
            st.success("Ciclo completado. Siente la paz interior.")
            st.balloons()
        st.markdown("</div>", unsafe_allow_html=True)
    with col_p2:
        if lottie_yoga_zen: st_lottie(lottie_yoga_zen, height=550, key="practice_anim")

with tabs[2]: # FABI IA ASESORA
    st.markdown("## FABI: Inteligencia en Bienestar")
    col_ia1, col_ia2 = st.columns([1, 2])
    with col_ia1:
        if lottie_brain_ia: st_lottie(lottie_brain_ia, height=450, key="ia_anim")
    with col_ia2:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        pregunta = st.text_input("¿Qué área de tu bienestar quieres explorar hoy con la guía de Fabiola?", placeholder="Ej: Hábitos para mejorar la concentración")
        if st.button("Consultar a FABI Expert"):
            if pregunta:
                with st.spinner("Conectando con la esencia wellness..."):
                    time.sleep(1.5)
                    st.markdown(f"""
                    **Respuesta de FABI IA:**
                    Basada en la metodología de Fabiola Pastén, para mejorar '{pregunta}' te recomiendo centrarte en la 'coherencia cardíaca' matinal. 
                    Como comunicadora, sé que el ritmo es la base de la salud mental y física.
                    """)
            else: st.warning("Por favor, ingresa tu consulta.")
        st.markdown("</div>", unsafe_allow_html=True)

with tabs[3]: # Agendamiento Boutique
    st.markdown("## Reserva tu Sesión Premium")
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        with st.form("agenda_premium"):
            st.text_input("Nombre Completo")
            st.text_input("Correo Electrónico")
            st.selectbox("Servicio", ["Yoga Privado", "Taller Biodanza", "Coaching Wellness"])
            st.date_input("Fecha Preferida", min_value=date.today())
            if st.form_submit_button("Confirmar Cita Pro"):
                st.balloons()
                st.success("Solicitud enviada. Fabiola te contactará para la confirmación.")
        st.markdown("</div>", unsafe_allow_html=True)
    with col_a2:
        st.markdown("#### Ubicación Fayoga Studio (La Serena)")
        m = folium.Map(location=[-29.9045, -71.2519], zoom_start=15)
        folium.Marker([-29.9045, -71.2519], popup="Fayoga Studio").add_to(m)
        st_folium(m, height=450, width=800)

# FOOTER PRO
st.markdown("<br><hr><p style='text-align: center; opacity: 0.7; font-size: 1.1rem !important;'>FAYOGA 2026 | Wellness SaaS Premium por Fabiola Pastén</p>", unsafe_allow_html=True)
