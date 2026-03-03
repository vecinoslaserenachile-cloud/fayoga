import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_extras.stylable_container import stylable_container
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
import time
import folium
from streamlit_folium import st_folium

# ==========================================
# 1. CONFIGURACIÓN DE PANTALLA TOTAL (TV & MOBILE)
# ==========================================
st.set_page_config(
    page_title="Fayoga Premium | Fabiola Pastén",
    page_icon="🧘‍♀️",
    layout="wide", # Clave para ocupar todo el espacio en PCs y TVs
    initial_sidebar_state="collapsed"
)

# Cargador de activos visuales
def load_lottie(url: str):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except: return None

lottie_yoga_flow = load_lottie("https://lottie.host/9f5064e4-399a-426c-829d-64d898517228/qG4K3nE0H5.json")
lottie_zen_pulse = load_lottie("https://lottie.host/807f4340-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")

# ==========================================
# 2. SISTEMA DE DISEÑO "BIG & BOLD" (CSS PRO)
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Quicksand:wght@300;500;700&display=swap');
    
    /* Forzar fondo y visibilidad */
    .stApp { background: linear-gradient(135deg, #fdfaf6 0%, #e9edc9 100%); }
    
    /* ELIMINAR MÁRGENES PARA OCUPAR TODO EL ESPACIO */
    .block-container {
        padding-top: 6rem !important;
        max-width: 95% !important;
        margin: auto;
    }

    /* TEXTOS GIGANTES Y LEGIBLES (PC Y MÓVIL) */
    h1 { font-size: clamp(3rem, 8vw, 6rem) !important; color: #2D4030 !important; font-family: 'Playfair Display', serif !important; }
    h2 { font-size: clamp(2rem, 5vw, 3.5rem) !important; color: #2D4030 !important; }
    h3 { font-size: clamp(1.5rem, 4vw, 2.5rem) !important; color: #4A5D4E !important; }
    p, li, span, label { 
        font-size: clamp(1.1rem, 2vw, 1.5rem) !important; 
        color: #1A1A1A !important; 
        font-weight: 500 !important;
        line-height: 1.6;
    }

    /* Ticker / Huincha Americana News */
    .ticker-wrapper {
        width: 100%; overflow: hidden; background: #2D4030; color: #E9EDC9;
        padding: 15px 0; position: fixed; top: 0; left: 0; z-index: 9999;
    }
    .ticker {
        display: inline-block; white-space: nowrap; padding-left: 100%;
        animation: ticker 30s linear infinite; font-weight: 700; font-size: 1.3rem;
    }
    @keyframes ticker { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-100%, 0, 0); } }

    /* Glassmorphism Premium Card */
    .premium-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(20px);
        border-radius: 40px;
        padding: 50px;
        border: 2px solid #A3B18A;
        box-shadow: 0 20px 50px rgba(0,0,0,0.1);
        margin-bottom: 30px;
    }

    /* Botones Pro */
    .stButton>button {
        background: linear-gradient(45deg, #4A5D4E 0%, #6B8E23 100%);
        color: white !important; border-radius: 60px; border: none; 
        padding: 25px 60px; font-weight: 700; font-size: 1.5rem; width: 100%;
        box-shadow: 0 15px 30px rgba(107, 142, 35, 0.3);
    }
    </style>
    
    <div class="ticker-wrapper"><div class="ticker">
        🧘‍♀️ NUEVOS CUPOS: YOGA MATINAL ONLINE | 💃 TALLER DE BIODANZA EN LA SERENA: SÁBADO 15 DE MARZO | 🗞️ HEMEROTECA WELLNESS: CURADURÍA PERIODÍSTICA | 🤖 CONSULTA A FABI IA
    </div></div>
    """, unsafe_allow_html=True)

# ==========================================
# 3. HEADER MAJESTUOSO
# ==========================================
st.markdown("<br><br>", unsafe_allow_html=True)
c_h1, c_h2, c_h3 = st.columns([1, 4, 1])
with c_h2:
    if lottie_zen_pulse: st_lottie(lottie_zen_pulse, height=200, key="lotus_top")
    st.markdown("<h1 style='text-align: center;'>FAYOGA</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; margin-top: -20px;'>Fabiola Pastén</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; opacity: 0.8;'>Periodista & Wellness Expert de Clase Mundial</p>", unsafe_allow_html=True)

st.divider()

# ==========================================
# 4. EXPERIENCIA DE USUARIO (TABS)
# ==========================================
tabs = st.tabs(["💎Dashboard", "🧘‍♀️ Mi Práctica", "🤖 FABI IA", "📅 Agenda Pro", "📰 Hemeroteca"])

with tabs[0]: # Dashboard Full Visual
    st.markdown("### El Universo Wellness Boutique")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='premium-card'><h3>Yoga</h3><p>Alineación y paz mental con el rigor comunicacional de Fabiola.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='premium-card'><h3>Biodanza</h3><p>Integración grupal a través del movimiento orgánico.</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='premium-card'><h3>IA Fabi</h3><p>Tu asistente personalizada para hábitos de vida consciente.</p></div>", unsafe_allow_html=True)

with tabs[1]: # MI PRÁCTICA (GUIADA CON ANIMACIÓN CONTEXTUAL)
    st.markdown("### Pausa Activa Guíada")
    col_p1, col_p2 = st.columns([1, 1])
    with col_p1:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.write("Sigue la animación de la derecha. **Inhala cuando se expande, exhala cuando se contrae.**")
        if st.button("🚀 Iniciar Guía de Respiración"):
            bar = st.progress(0)
            status = st.empty()
            for i in range(101):
                msg = "**Inhala profundamente...** 😤" if i < 50 else "**Exhala suavemente...** 😮‍💨"
                status.markdown(f"### {msg}")
                bar.progress(i)
                time.sleep(0.08)
            st.success("Ciclo completado. Namasté.")
        st.markdown("</div>", unsafe_allow_html=True)
    with col_p2:
        if lottie_yoga_flow: st_lottie(lottie_yoga_flow, height=450, key="yoga_sim")

with tabs[2]: # FABI IA ASESORA
    st.markdown("### FABI: Inteligencia en Bienestar")
    col_ia1, col_ia2 = st.columns([1, 2])
    with col_ia1:
        st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=600", caption="Consultoría Premium.")
    with col_ia2:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        pregunta = st.text_input("¿Qué área de tu bienestar quieres explorar hoy?")
        if st.button("Consultar a FABI Expert"):
            with st.spinner("Conectando con la esencia de Fayoga..."):
                time.sleep(1)
                st.markdown(f"**FABI IA Responde:** Como comunicadora y experta, te sugiero que para '{pregunta}' apliques la técnica de la pausa consciente de 3 minutos. La Biodanza nos enseña que el ritmo es la base de la salud.")
        st.markdown("</div>", unsafe_allow_html=True)

with tabs[3]: # Agendamiento Boutique
    st.markdown("### Agenda Tu Sesión Premium")
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        with st.form("agenda"):
            st.text_input("Nombre")
            st.selectbox("Servicio", ["Yoga Privado", "Taller Biodanza", "Coaching Wellness"])
            st.date_input("Fecha", min_value=date.today())
            st.form_submit_button("Confirmar Reserva Pro")
        st.markdown("</div>", unsafe_allow_html=True)
    with col_a2:
        st.markdown("#### Ubicación Fayoga Studio")
        m = folium.Map(location=[-29.9045, -71.2519], zoom_start=15)
        folium.Marker([-29.9045, -71.2519], popup="Fayoga La Serena").add_to(m)
        st_folium(m, height=400, width=700)

# FOOTER PRO
st.markdown("<br><hr><p style='text-align: center; opacity: 0.6;'>FAYOGA 2026 | Wellness SaaS Premium por Fabiola Pastén</p>", unsafe_allow_html=True)
