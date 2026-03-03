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
    layout="wide", # Clave para ocupar todo el espacio en PCs y TVs
    initial_sidebar_state="collapsed"
)

# Cargador de activos visuales vectoriales con manejo de errores robusto
def load_lottie(url: str):
    try:
        r = requests.get(url, timeout=5)
        return r.json() if r.status_code == 200 else None
    except: return None

# Galería de Animaciones Premium (Lotties contextuales)
lottie_yoga_main = load_lottie("https://lottie.host/9f5064e4-399a-426c-829d-64d898517228/qG4K3nE0H5.json")
lottie_lotus_zen = load_lottie("https://lottie.host/807f4340-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")
lottie_ia_brain = load_lottie("https://lottie.host/07as9pva-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")

# ==========================================
# 2. SISTEMA DE DISEÑO "LIQUID GLASS" (CSS PRO)
# ==========================================
# Forzamos contraste profundo y tamaños de texto majestuosos
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Quicksand:wght@300;400;500;700&display=swap');
    
    /* Configuración de Contenedor Expandido al 95% para TVs y PCs */
    .stApp {
        background: linear-gradient(135deg, #fdfaf6 0%, #e9edc9 100%);
        color: #1A1A1A;
    }
    .main .block-container {
        padding-top: 5rem !important;
        max-width: 95% !important;
        margin: auto;
    }

    /* TEXTOS GIGANTES Y LEGIBLES (PC Y MÓVIL) */
    h1 { 
        font-size: clamp(3.5rem, 9vw, 6.5rem) !important; 
        color: #2D4030 !important; 
        font-family: 'Playfair Display', serif !important;
        line-height: 1.1; margin-bottom: 0.5rem;
    }
    h2 { font-size: clamp(2.2rem, 5vw, 3.8rem) !important; color: #2D4030 !important; font-family: 'Playfair Display', serif !important; }
    h3 { font-size: clamp(1.6rem, 4vw, 2.8rem) !important; color: #4A5D4E !important; font-family: 'Quicksand', sans-serif !important; }
    
    p, li, span, label { 
        font-size: clamp(1.2rem, 1.8vw, 1.6rem) !important; 
        color: #1A1A1A !important; 
        font-weight: 500 !important;
        line-height: 1.7;
    }

    /* Huincha Americana News Ticker (Estilo TV 2026) */
    .ticker-wrapper {
        width: 100%; overflow: hidden; background: #2D4030; color: #E9EDC9;
        padding: 15px 0; position: fixed; top: 0; left: 0; z-index: 9999;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }
    .ticker {
        display: inline-block; white-space: nowrap; padding-left: 100%;
        animation: ticker 35s linear infinite; font-weight: 700; font-size: 1.3rem;
    }
    @keyframes ticker { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-100%, 0, 0); } }

    /* Glassmorphism Premium Cards - Contraste Blindado */
    .premium-card {
        background: rgba(255, 255, 255, 0.82);
        backdrop-filter: blur(25px);
        border-radius: 45px;
        padding: 60px;
        border: 2px solid #A3B18A;
        box-shadow: 0 25px 60px rgba(0,0,0,0.12);
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

    /* Estilo para las Tabs */
    .stTabs [data-baseweb="tab-list"] { gap: 40px; justify-content: center; }
    .stTabs [data-baseweb="tab"] { font-size: 1.6rem !important; font-weight: 700; color: #4A5D4E; }
    </style>
    
    <div class="ticker-wrapper"><div class="ticker">
        🌟 NOVEDAD: Taller Boutique de Biodanza - Sábado 15 de Marzo en La Serena | 🧘‍♀️ Nuevos Cupos Yoga Matinal Online | 🗞️ Hemeroteca Wellness Curada por Fabiola Pastén | 🤖 CONSULTA A FABI IA
    </div></div>
    """, unsafe_allow_html=True)

# ==========================================
# 3. CABECERA MAJESTUOSA (LOGO & ICONO)
# ==========================================
add_vertical_space(2)
c_header_1, c_header_2, c_header_3 = st.columns([1, 5, 1])
with c_header_2:
    if lottie_lotus_zen: st_lottie(lottie_lotus_zen, height=250, key="lotus_top")
    st.markdown("<h1 style='text-align: center;'>FAYOGA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 2.8rem !important; color: #4A5D4E; font-weight: 700; margin-top: -15px;'>Fabiola Pastén</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-style: italic; opacity: 0.8;'>Periodista, Comunicadora y Experta Wellness de Clase Mundial</p>", unsafe_allow_html=True)

st.divider()

# ==========================================
# 4. EXPERIENCIA DE USUARIO (TABS LÍQUIDAS)
# ==========================================
tabs = st.tabs(["💎 Dashboard Experience", "🧘‍♀️ Mi Práctica Zen", "🤖 FABI IA Asesora", "📅 Agenda Pro", "📊 Métricas"])

with tabs[0]: # Dashboard Full Visual
    st.markdown("## El Universo Wellness Boutique")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='premium-card'><h3>Yoga Integral</h3><p>Sesiones de Hatha y Vinyasa terapéutico con enfoque comunicacional para el equilibrio profundo.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='premium-card'><h3>Biodanza</h3><p>Renovación vital e integración afectiva a través del movimiento orgánico y rítmico grupal.</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='premium-card'><h3>Wellness Pro</h3><p>Consultoría en bienestar corporativo y liderazgo consciente basado en el rigor periodístico.</p></div>", unsafe_allow_html=True)
    
    # Imagen Pro que ocupa espacio
    st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=1800", caption="Fayoga: La integración perfecta entre cuerpo, mente y comunicación.")

with tabs[1]: # MI PRÁCTICA (INMERSIVA CON ANIMACIÓN)
    st.markdown("## Pausa Activa Consciente")
    col_p1, col_p2 = st.columns([1, 1])
    with col_p1:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.write("Utiliza este simulador para un ejercicio rápido de respiración guiada. **Sigue el ritmo de la animación.**")
        st.markdown("""
        **Guía Visual:**
        1.  Inhala profundamente por la nariz (4 segundos).
        2.  Exhala suavemente por la boca (6 segundos).
        """)
        if st.button("🚀 INICIAR GUÍA DE RESPIRACIÓN"):
            prog = st.progress(0)
            status = st.empty()
            for i in range(101):
                msg = "**Inhala profundamente...** 😤" if i < 41 else "**Exhala suavemente...** 😮‍💨"
                status.markdown(f"### {msg}")
                prog.progress(i)
                time.sleep(0.08)
            st.success("Ciclo completado. Tu sistema nervioso se ha reseteado. Namasté.")
            st.balloons()
        st.markdown("</div>", unsafe_allow_html=True)
    with col_p2:
        if lottie_yoga_main: st_lottie(lottie_yoga_main, height=550, key="yoga_sim")

with tabs[2]: # ASESORA IA: FABI Expert
    st.markdown("## FABI IA: Tu Asesora Premium")
    col_ia1, col_ia2 = st.columns([1, 2])
    with col_ia1:
        if lottie_ia_brain: st_lottie(lottie_ia_brain, height=450, key="ia_anim")
    with col_ia2:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        pregunta = st.text_input("¿Qué área de tu bienestar quieres explorar hoy con la guía de Fabiola?", placeholder="Ej: Ejercicio para la ansiedad laboral")
        if st.button("Consultar a FABI Expert"):
            if pregunta:
                with st.spinner("Conectando con la esencia wellness periodística..."):
                    time.sleep(1.5)
                    st.markdown(f"""
                    **Respuesta de FABI IA:**
                    Como comunicadora y experta, entiendo que para abordar '{pregunta}' debemos equilibrar el ritmo orgánico. 
                    Te sugiero integrar 5 minutos de 'coherencia cardíaca' antes de tus reuniones. 
                    La Biodanza nos enseña que el movimiento rítmico es la base de la salud mental.
                    """)
            else: st.warning("Por favor, ingresa tu consulta wellness.")
        st.markdown("</div>", unsafe_allow_html=True)

with tabs[3]: # Agendamiento con Mapa Pro
    st.markdown("## Reserva tu Sesión Boutique")
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        with st.form("agenda_premium"):
            st.text_input("Nombre Completo del Alumno")
            st.selectbox("Servicio Deseado", ["Yoga Privado 1:1", "Taller Biodanza Serena", "Wellness Corporativo Empresas"])
            st.date_input("Fecha Preferida", min_value=date.today())
            if st.form_submit_button("Confirmar Cita Boutique"):
                st.balloons()
                st.success("Solicitud Premium enviada. Fabiola te contactará pronto.")
        st.markdown("</div>", unsafe_allow_html=True)
    with col_a2:
        st.markdown("#### Ubicación Fayoga Studio (La Serena)")
        m = folium.Map(location=[-29.9045, -71.2519], zoom_start=15)
        folium.Marker([-29.9045, -71.2519], popup="Fayoga Studio", tooltip="Fabiola Pastén").add_to(m)
        st_folium(m, height=450, width=800)

# FOOTER PRO
st.markdown("<br><hr><p style='text-align: center; opacity: 0.7; font-size: 1.1rem !important;'>FAYOGA 2026 | Wellness SaaS Premium por Fabiola Pastén</p>", unsafe_allow_html=True)
