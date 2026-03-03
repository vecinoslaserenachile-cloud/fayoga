import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pandas as pd
import numpy as np
from datetime import date
import time

# ==========================================
# 1. CONFIGURACIÓN DE PANTALLA Y NÚCLEO
# ==========================================
st.set_page_config(
    page_title="Fayoga Academy | Fabiola Pastén",
    page_icon="🧘‍♀️",
    layout="wide", # Clave para ocupar todo el espacio en TVs y PCs
    initial_sidebar_state="collapsed"
)

def load_lottie(url: str):
    try:
        r = requests.get(url, timeout=5)
        return r.json() if r.status_code == 200 else None
    except: return None

# Animaciones Pro
lottie_yoga = load_lottie("https://lottie.host/9f5064e4-399a-426c-829d-64d898517228/qG4K3nE0H5.json")
lottie_zen = load_lottie("https://lottie.host/807f4340-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")

# ==========================================
# 2. SISTEMA DE DISEÑO "BIG & BOLD" (CSS)
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@900&family=Quicksand:wght@300;500;700&display=swap');
    
    .stApp { background: linear-gradient(135deg, #fdfaf6 0%, #e9edc9 100%); }
    .main .block-container { padding-top: 6rem !important; max-width: 95% !important; margin: auto; }

    /* FAYOGA: 10 VECES MÁS CUERPO */
    .brand-title {
        font-family: 'Playfair Display', serif;
        font-size: clamp(5rem, 15vw, 10rem) !important;
        color: #2D4030 !important;
        text-align: center; line-height: 0.9; font-weight: 900;
        margin-bottom: 0px; text-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    .brand-subtitle {
        font-family: 'Quicksand', sans-serif;
        font-size: clamp(1.5rem, 3vw, 2.8rem) !important;
        text-align: center; color: #4A5D4E; font-weight: 300;
        letter-spacing: 15px; text-transform: uppercase; margin-top: -10px;
    }

    /* TEXTOS GIGANTES PARA PC/TV */
    h1, h2, h3 { color: #2D4030 !important; font-family: 'Playfair Display', serif !important; }
    p, li, span, label { 
        font-size: clamp(1.2rem, 2vw, 1.6rem) !important; 
        color: #1A1A1A !important; font-weight: 500 !important;
    }

    /* Glassmorphism Academy Cards */
    .academy-card {
        background: rgba(255, 255, 255, 0.88);
        backdrop-filter: blur(20px); border-radius: 40px;
        padding: 50px; border: 2px solid #A3B18A;
        box-shadow: 0 25px 50px rgba(0,0,0,0.1); margin-bottom: 30px;
    }

    /* Botones Pro */
    .stButton>button {
        background: linear-gradient(45deg, #4A5D4E 0%, #6B8E23 100%);
        color: white !important; border-radius: 100px; border: none; 
        padding: 25px 60px; font-weight: 700; font-size: 1.6rem; width: 100%;
        box-shadow: 0 15px 35px rgba(107, 142, 35, 0.3);
    }
    
    .ticker-wrapper {
        width: 100%; overflow: hidden; background: #2D4030; color: #E9EDC9;
        padding: 15px 0; position: fixed; top: 0; left: 0; z-index: 9999;
    }
    .ticker {
        display: inline-block; white-space: nowrap; padding-left: 100%;
        animation: ticker 35s linear infinite; font-weight: 700; font-size: 1.4rem;
    }
    @keyframes ticker { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-100%, 0, 0); } }
    </style>
    
    <div class="ticker-wrapper"><div class="ticker">
        🧘 PRÓXIMO LIVE: YOGA DE INVIERNO - VIERNES 19:00 | 🎓 YOGADOC: NUEVO MÓDULO DE RESPIRACIÓN NIVEL 5 DISPONIBLE | 🤖 CONSULTA A FABI IA
    </div></div>
    """, unsafe_allow_html=True)

# ==========================================
# 3. HEADER MAJESTUOSO
# ==========================================
st.markdown("<br><br>", unsafe_allow_html=True)
c_logo_1, c_logo_2, c_logo_3 = st.columns([1, 1, 1])
with c_logo_2:
    st.markdown("""<img src="https://lookaside.fbsbx.com/lookaside/crawler/instagram/fayoga.bienestar/profile_pic.jpg" 
                style="border-radius: 50%; border: 6px solid #A3B18A; width: 100%; box-shadow: 0 20px 40px rgba(0,0,0,0.2);">""", unsafe_allow_html=True)

st.markdown("<h1 class='brand-title'>FAYOGA</h1>", unsafe_allow_html=True)
st.markdown("<p class='brand-subtitle'>Fabiola Pastén</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.8;'>Periodista & Wellness Master</p>", unsafe_allow_html=True)

st.divider()

# ==========================================
# 4. SISTEMA DE APRENDIZAJE (TABS)
# ==========================================
tabs = st.tabs(["💎 Dashboard", "🧘‍♂️ YogaDoc: Academia", "🤖 FABI IA", "📅 Niveles de Acceso", "👥 Alumnos"])

with tabs[0]: # Dashboard inmersivo
    st.markdown("## El Universo de Fabiola")
    col_d1, col_d2 = st.columns([1, 1])
    with col_d1:
        st.markdown("<div class='academy-card'><h3>Bienvenida a la Evolución</h3><p>Fayoga trasciende la clase de yoga tradicional para convertirse en un sistema de aprendizaje integral de bienestar y comunicación consciente.</p></div>", unsafe_allow_html=True)
    with col_d2:
        if lottie_yoga: st_lottie(lottie_yoga, height=400, key="main_yoga")

with tabs[1]: # YOGADOC: ACADEMIA PROGRESIVA
    st.markdown("## YogaDoc: Sistema de Aprendizaje Progresivo")
    st.write("Avanza a través de los niveles de conciencia y técnica física.")
    
    nivel_yoga = st.select_slider("Selecciona tu Nivel de Aprendizaje", options=[f"Nivel {i}" for i in range(1, 11)])
    
    col_y1, col_y2 = st.columns(2)
    with col_y1:
        st.markdown(f"<div class='academy-card'><h4>{nivel_yoga}</h4><p>Contenido curado por Fabiola para profundizar en la biomecánica y el silencio mental. Incluye simulaciones de asanas y guías de respiración específica.</p></div>", unsafe_allow_html=True)
        st.button(f"Iniciar Módulo {nivel_yoga}")
    with col_y2:
        # Aquí integramos el módulo de respiración con 10 niveles
        st.markdown("### Guía de Respiración Consciente")
        lvl_resp = st.slider("Nivel de Intensidad Respiratoria", 1, 10, 1)
        if st.button(f"🚀 Iniciar Respiración Nivel {lvl_resp}"):
            bar = st.progress(0)
            t = st.empty()
            duracion = 5 + lvl_resp # Escala con el nivel
            for i in range(101):
                msg = "**Inhala profundo...**" if i < 50 else "**Exhala suave...**"
                t.markdown(f"### {msg}")
                bar.progress(i)
                time.sleep(duracion / 100)
            st.success(f"Sesión Nivel {lvl_resp} Completada.")

with tabs[2]: # FABI IA
    st.markdown("## FABI IA: Asesora de Bienestar")
    st.info("FABI utiliza el expertise periodístico y wellness de Fabiola.")
    pregunta = st.text_input("¿Qué área de tu bienestar quieres explorar hoy?")
    if st.button("Consultar a FABI Expert"):
        st.markdown(f"<div class='academy-card'><b>FABI Responde:</b><br>Basada en la metodología Fayoga, para '{pregunta}' te recomiendo iniciar con el nivel 3 de YogaDoc, enfocándonos en la alineación matinal.</div>", unsafe_allow_html=True)

with tabs[3]: # NIVELES DE ACCESO (SIMULACIÓN DE SUSCRIPCIÓN)
    st.markdown("## Membresías Boutique")
    c_m1, c_m2, c_m3 = st.columns(3)
    with c_m1:
        st.markdown("<div class='academy-card' style='border-color: #A3B18A;'><h4>Gratuito</h4><p>Acceso a YogaDoc Nivel 1 y 2.<br>Tips semanales de bienestar.</p></div>", unsafe_allow_html=True)
        st.button("Unirse Gratis")
    with c_m2:
        st.markdown("<div class='academy-card' style='border-color: #6B8E23;'><h4>Live</h4><p>Clases en vivo con Fabiola.<br>Acceso a YogaDoc hasta Nivel 5.</p></div>", unsafe_allow_html=True)
        st.button("Suscribirse a Live")
    with c_m3:
        st.markdown("<div class='academy-card' style='border-color: #2D4030;'><h4>Premium</h4><p>Acceso TOTAL a YogaDoc.<br>Consultas personalizadas con Fabiola.</p></div>", unsafe_allow_html=True)
        st.button("Acceso Premium VIP")

with tabs[4]: # ALUMNOS
    st.markdown("## Comunidad de Alumnos")
    # Simulación de listado de alumnos y progreso
    df_alumnos = pd.DataFrame({
        "Alumno": ["Rodrigo Godoy", "Fabiola Pastén", "Alumno 03", "Alumno 04"],
        "Nivel YogaDoc": [8, 10, 3, 5],
        "Membresía": ["Premium", "Staff", "Gratuito", "Live"],
        "Última Clase": ["Hoy", "Ayer", "Hace 3 días", "Hoy"]
    })
    st.table(df_alumnos)

# FOOTER
st.markdown("<br><hr><p style='text-align: center; opacity: 0.6;'>FAYOGA 2026 | Wellness SaaS Premium por Fabiola Pastén</p>", unsafe_allow_html=True)
