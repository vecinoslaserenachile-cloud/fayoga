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
# 1. NÚCLEO Y PANTALLA TOTAL (TV & 4K)
# ==========================================
st.set_page_config(
    page_title="Fayoga Premium | Fabiola Pastén",
    page_icon="🧘‍♀️",
    layout="wide", # Ocupación total de espacio
    initial_sidebar_state="collapsed"
)

# Cargadores de activos visuales
def load_lottie(url: str):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except: return None

# Animaciones de alta gama (Contextualizadas)
lottie_yoga_flow = load_lottie("https://lottie.host/9f5064e4-399a-426c-829d-64d898517228/qG4K3nE0H5.json")
lottie_respira = load_lottie("https://lottie.host/807f4340-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")
lottie_ia_brain = load_lottie("https://lottie.host/07as9pva-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")

# ==========================================
# 2. INYECCIÓN DE DISEÑO "LIQUID ZEN" (CSS)
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Quicksand:wght@300;500;700&display=swap');
    
    /* Configuración de Contenedor Expandido al 95% */
    .stApp { background: linear-gradient(135deg, #fdfaf6 0%, #e9edc9 100%); }
    .block-container {
        padding-top: 6rem !important;
        max-width: 95% !important; /* Ocupa casi toda la TV/PC */
        margin: auto;
    }

    /* Títulos y Textos Escalables (Responsivos) */
    h1 { 
        font-size: clamp(4rem, 10vw, 7rem) !important; 
        color: #2D4030 !important; 
        font-family: 'Playfair Display', serif !important;
        line-height: 1.1; margin-bottom: 0;
    }
    h2 { font-size: clamp(2.5rem, 5vw, 4rem) !important; color: #2D4030 !important; }
    p, li, span, label { 
        font-size: clamp(1.2rem, 1.8vw, 1.6rem) !important; 
        color: #1A1A1A !important; 
        font-weight: 500 !important;
    }

    /* Huincha Americana (News Ticker) Estilo TV */
    .ticker-wrapper {
        width: 100%; overflow: hidden; background: #2D4030; color: #E9EDC9;
        padding: 15px 0; position: fixed; top: 0; left: 0; z-index: 9999;
    }
    .ticker {
        display: inline-block; white-space: nowrap; padding-left: 100%;
        animation: ticker 35s linear infinite; font-weight: 700; font-size: 1.4rem;
    }
    @keyframes ticker { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-100%, 0, 0); } }

    /* Glassmorphism Premium Cards */
    .premium-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(20px);
        border-radius: 50px;
        padding: 60px;
        border: 2px solid #A3B18A;
        box-shadow: 0 30px 60px rgba(0,0,0,0.1);
        margin-bottom: 40px;
    }

    /* Botones de Acción Estilo Boutique */
    .stButton>button {
        background: linear-gradient(45deg, #4A5D4E 0%, #6B8E23 100%);
        color: white !important; border-radius: 100px; border: none; 
        padding: 30px 80px; font-weight: 700; font-size: 1.8rem; width: 100%;
        box-shadow: 0 20px 40px rgba(107, 142, 35, 0.4);
        transition: 0.3s ease;
    }
    .stButton>button:hover { transform: scale(1.02); }
    </style>
    
    <div class="ticker-wrapper"><div class="ticker">
        🌟 NOVEDAD: Taller Boutique de Biodanza - Sábado 15 de Marzo en La Serena | 🧘‍♀️ Nuevos Cupos Yoga Matinal Online | 🗞️ Hemeroteca Wellness Curada por Fabiola Pastén | 🤖 FABI IA Asesora
    </div></div>
    """, unsafe_allow_html=True)

# ==========================================
# 3. HEADER MAJESTUOSO
# ==========================================
add_vertical_space(2)
c_h1, c_h2, c_h3 = st.columns([1, 4, 1])
with c_h2:
    if lottie_respira: st_lottie(lottie_respira, height=250, key="hero_anim")
    st.markdown("<h1 style='text-align: center;'>FAYOGA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 2.5rem !important; color: #4A5D4E; font-weight: 700;'>Fabiola Pastén</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-style: italic; opacity: 0.7;'>Periodista & Wellness Expert de Clase Mundial</p>", unsafe_allow_html=True)

st.divider()

# ==========================================
# 4. EXPERIENCIA DE USUARIO (TABS LÍQUIDAS)
# ==========================================
tabs = st.tabs(["💎Dashboard", "🧘‍♀️ Mi Práctica", "🤖 FABI IA", "📅 Agenda Pro", "📊 Métricas"])

with tabs[0]: # Dashboard Full Visual
    st.markdown("## El Universo Wellness Boutique")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='premium-card'><h3>Yoga Integral</h3><p>Sesiones de Hatha y Vinyasa terapéutico con enfoque comunicacional.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='premium-card'><h3>Biodanza</h3><p>Renovación vital a través del movimiento orgánico y rítmico.</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='premium-card'><h3>IA Fabi</h3><p>Tu asistente personalizada para hábitos y vida consciente.</p></div>", unsafe_allow_html=True)
    
    # Ilustración Premium
    st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=1600", caption="Fayoga: El arte de la integración mente-cuerpo.")

with tabs[1]: # MI PRÁCTICA (INMERSIVA)
    st.markdown("## Sesión de Respiración Guiada")
    col_p1, col_p2 = st.columns([1, 1])
    with col_p1:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.write("Sigue la animación de la derecha. **Inhala cuando se expande, exhala cuando se contrae.**")
        if st.button("🚀 INICIAR GUÍA DE RESPIRACIÓN"):
            bar = st.progress(0)
            status = st.empty()
            for i in range(101):
                msg = "**Inhala profundo...** 😤" if i < 50 else "**Exhala suave...** 😮‍💨"
                status.markdown(f"### {msg}")
                bar.progress(i)
                time.sleep(0.08)
            st.success("Ciclo completado. Siente la paz en tu sistema nervioso.")
        st.markdown("</div>", unsafe_allow_html=True)
    with col_p2:
        if lottie_yoga_flow: st_lottie(lottie_yoga_flow, height=500, key="practice_anim")

with tabs[2]: # FABI IA EXPERT
    st.markdown("## FABI IA: Asesora de Bienestar")
    col_ia1, col_ia2 = st.columns([1, 2])
    with col_ia1:
        if lottie_ia_brain: st_lottie(lottie_ia_brain, height=400, key="ia_anim")
    with col_ia2:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        pregunta = st.text_input("¿Qué área de tu bienestar quieres explorar hoy?", placeholder="Escribe tu consulta aquí...")
        if st.button("Consultar a FABI Expert"):
            with st.spinner("Conectando con la esencia de Fayoga..."):
                time.sleep(1.5)
                st.markdown(f"**Respuesta de FABI IA:** Como comunicadora y experta, te sugiero que para mejorar '{pregunta}', integres una pausa consciente de 3 minutos. La Biodanza nos enseña que el ritmo es la base de la salud.")
        st.markdown("</div>", unsafe_allow_html=True)

with tabs[3]: # Agendamiento con Mapa Pro
    st.markdown("## Reserva tu Sesión Boutique")
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        with st.form("agenda_form"):
            st.text_input("Nombre Completo")
            st.selectbox("Servicio", ["Yoga Privado 1:1", "Taller Biodanza Serena", "Wellness Corporativo"])
            st.date_input("Fecha preferida", min_value=date.today())
            st.form_submit_button("Confirmar Reserva Pro")
        st.markdown("</div>", unsafe_allow_html=True)
    with col_a2:
        st.markdown("#### Ubicación Fayoga Studio (La Serena)")
        m = folium.Map(location=[-29.9045, -71.2519], zoom_start=15)
        folium.Marker([-29.9045, -71.2519], popup="Fayoga La Serena").add_to(m)
        st_folium(m, height=450, width=750)

# FOOTER PRO
st.markdown("<br><hr><p style='text-align: center; opacity: 0.6;'>FAYOGA 2026 | Wellness SaaS Premium por Fabiola Pastén</p>", unsafe_allow_html=True)
