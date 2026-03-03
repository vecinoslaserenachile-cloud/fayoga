import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pandas as pd
import numpy as np
import time

# ==========================================
# 1. NÚCLEO Y PANTALLA TOTAL (TV & 4K)
# ==========================================
st.set_page_config(
    page_title="Fayoga | Academia Premium",
    page_icon="🧘‍♀️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Cargador de activos visuales
def load_lottie(url: str):
    try:
        r = requests.get(url, timeout=5)
        return r.json() if r.status_code == 200 else None
    except: return None

lottie_zen = load_lottie("https://lottie.host/807f4340-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")

# ==========================================
# 2. INYECCIÓN DE DISEÑO "ENTERPRISE BOUTIQUE"
# ==========================================
# Aquí forzamos a Streamlit a ocupar TODO el espacio y escalamos el logo masivamente
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@900&family=Quicksand:wght@300;400;700&display=swap');
    
    /* Configuración de Pantalla Total */
    .stApp {
        background: linear-gradient(135deg, #fdfaf6 0%, #e9edc9 100%);
        background-attachment: fixed;
    }
    
    /* ELIMINAR MÁRGENES NATIVOS - OCUPAR TODA LA TV */
    .main .block-container {
        padding-top: 5rem !important;
        max-width: 98% !important;
        padding-left: 2% !important;
        padding-right: 2% !important;
    }

    /* FAYOGA: ESCALADO MONUMENTAL (10x CUERPO) */
    .brand-title {
        font-family: 'Playfair Display', serif;
        font-size: clamp(8rem, 25vw, 15rem) !important;
        color: #2D4030;
        text-align: center;
        line-height: 0.8;
        font-weight: 900;
        letter-spacing: -5px;
        margin-bottom: 0px;
        background: linear-gradient(to bottom, #2D4030, #6B8E23);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(5px 5px 15px rgba(0,0,0,0.1));
    }

    .brand-subtitle {
        font-family: 'Quicksand', sans-serif;
        font-size: clamp(1.5rem, 4vw, 3.5rem);
        text-align: center;
        color: #4A5D4E;
        font-weight: 300;
        letter-spacing: 20px;
        text-transform: uppercase;
        margin-top: -20px;
    }

    /* TARJETAS PREMIUM CON ILUSTRACIÓN DE FONDO */
    .premium-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(25px);
        border-radius: 50px;
        padding: 60px;
        border: 2px solid #A3B18A;
        box-shadow: 0 40px 80px rgba(0,0,0,0.1);
        margin-bottom: 40px;
        color: #1A1A1A !important;
    }

    /* BOTONERÍA ESTILO SPA */
    .stButton>button {
        background: linear-gradient(45deg, #4A5D4E 0%, #6B8E23 100%);
        color: white !important;
        border-radius: 100px;
        border: none;
        padding: 30px 80px;
        font-weight: 700;
        font-size: 1.8rem;
        width: 100%;
        box-shadow: 0 20px 40px rgba(107, 142, 35, 0.3);
        transition: all 0.4s ease;
    }
    .stButton>button:hover { transform: translateY(-5px) scale(1.02); }

    /* TICKER / HUINCHA AMERICANA */
    .ticker-wrapper {
        width: 100%; overflow: hidden; background: #2D4030; color: #E9EDC9;
        padding: 15px 0; position: fixed; top: 0; left: 0; z-index: 9999;
    }
    .ticker {
        display: inline-block; white-space: nowrap; padding-left: 100%;
        animation: ticker 40s linear infinite; font-weight: 700; font-size: 1.5rem;
    }
    @keyframes ticker { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-100%, 0, 0); } }

    /* ILUSTRACIONES DE RELLENO (ESCRITORIO) */
    @media (min-width: 1200px) {
        .stApp::before {
            content: "";
            position: fixed; top: 0; left: 0; width: 150px; height: 100%;
            background-image: url('https://www.transparenttextures.com/patterns/leaves.png');
            opacity: 0.1; pointer-events: none;
        }
    }
    </style>
    
    <div class="ticker-wrapper"><div class="ticker">
        🌿 BIENVENIDOS A LA ACADEMIA FAYOGA | ✨ NUEVOS NIVELES DE BIODANZA DISPONIBLES | 🎓 YOGADOC: TU RUTA HACIA EL MODO PREMIUM | 🤖 FABI IA ASESORA ACTIVA
    </div></div>
    """, unsafe_allow_html=True)

# ==========================================
# 3. HEADER MAJESTUOSO (LOGO Y NOMBRE)
# ==========================================
st.markdown("<br><br><br>", unsafe_allow_html=True)
c_logo_1, c_logo_2, c_logo_3 = st.columns([1, 1, 1])
with c_logo_2:
    st.markdown("""<img src="https://lookaside.fbsbx.com/lookaside/crawler/instagram/fayoga.bienestar/profile_pic.jpg" 
                style="border-radius: 50%; border: 8px solid #A3B18A; width: 80%; margin: auto; display: block; box-shadow: 0 30px 60px rgba(0,0,0,0.2);">""", unsafe_allow_html=True)

st.markdown("<h1 class='brand-title'>FAYOGA</h1>", unsafe_allow_html=True)
st.markdown("<p class='brand-subtitle'>Fabiola Pastén</p>", unsafe_allow_html=True)

# ==========================================
# 4. SISTEMA DE APRENDIZAJE 10 NIVELES
# ==========================================
tabs = st.tabs(["💎 Dashboard", "🎓 YogaDoc Learning", "💃 Biodanza Flow", "👥 Alumnos", "🤖 FABI IA"])

with tabs[1]: # YogaDoc: El corazón del Learning
    st.markdown("## YogaDoc: Progresión de Conciencia")
    
    # Lógica de Niveles (Cambian ejercicios, no dificultad)
    nivel = st.select_slider("Tu Progreso Actual", options=[i for i in range(1, 12)], 
                            format_func=lambda x: f"Nivel {x}" if x <= 10 else "💎 MODO PREMIUM")
    
    if nivel <= 10:
        ejercicios = {
            1: ("Respiración Primordial", "Iniciación al silencio mental.", "https://images.unsplash.com/photo-1506126613408-eca07ce68773"),
            2: ("Alineación Ósea", "Conexión con la estructura física.", "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b"),
            3: ("Fluidez Vinyasa", "El arte de transitar entre estados.", "https://images.unsplash.com/photo-1599447421416-3414500d18a5"),
            4: ("Resonancia Vocal", "Uso del sonido para equilibrar chakras.", "https://images.unsplash.com/photo-1512438248247-f0f2a5a8b7f0"),
            5: ("Equilibrio Estático", "Encontrar el centro en la quietud.", "https://images.unsplash.com/photo-1510894347713-fc3ed6fdf539"),
            6: ("Biodanza Matinal", "Movimiento rítmico de despertar.", "https://images.unsplash.com/photo-1518310383802-640c2de311b2"),
            7: ("Pranayama Avanzado", "Control total de la energía vital.", "https://images.unsplash.com/photo-1499209974431-9dac3adaf471"),
            8: ("Yoga de los Sentidos", "Exploración sensorial consciente.", "https://images.unsplash.com/photo-1524633212363-36dd03f0dd2e"),
            9: ("Meditación Periodística", "Análisis crítico del yo interior.", "https://images.unsplash.com/photo-1474418397713-7ded018049ce"),
            10: ("Integración Fayoga", "La maestría de todos los elementos.", "https://images.unsplash.com/photo-1447452001602-7090c7ab2db3")
        }
        
        titulo, desc, img = ejercicios[nivel]
        
        col_ex1, col_ex2 = st.columns([1, 1])
        with col_ex1:
            st.markdown(f"""<div class='premium-card'>
                <h2>Nivel {nivel}: {titulo}</h2>
                <p>{desc}</p>
                <hr>
                <small>Completa este nivel para desbloquear el siguiente paso hacia el Modo Premium.</small>
            </div>""", unsafe_allow_html=True)
            
            # Simulador de Respiración Contextualizado
            st.write("### Simulador de Práctica")
            if st.button(f"🚀 Iniciar Práctica de {titulo}"):
                bar = st.progress(0)
                status = st.empty()
                for i in range(101):
                    msg = "Inhala..." if i < 50 else "Exhala..."
                    status.markdown(f"### {msg}")
                    bar.progress(i)
                    time.sleep(0.06)
                st.success(f"¡Nivel {nivel} Completado!")
        
        with col_ex2:
            st.image(f"{img}?auto=format&fit=crop&w=1200", use_container_width=True)

    else:
        st.markdown("""<div class='premium-card' style='text-align: center; border-color: #6B8E23; background: #2D4030; color: white !important;'>
            <h1 style='color: white !important;'>💎 MODO PREMIUM BLOQUEADO</h1>
            <p style='color: white !important;'>Has completado la formación básica de 10 niveles. 
            El modo Premium incluye clases en vivo con Fabiola, Hemeroteca ilimitada y consultoría IA avanzada.</p>
            <br>
            <button style='padding: 20px 50px; border-radius: 50px; border: none; background: #E9EDC9; color: #2D4030; font-weight: bold; font-size: 1.5rem;'>
                SUSCRIBIRSE AHORA
            </button>
        </div>""", unsafe_allow_html=True)

with tabs[2]: # BIODANZA (NUEVO CONTENIDO)
    st.markdown("## Biodanza: La Danza de la Vida")
    st.write("Explora el sistema de integración afectiva de Fabiola Pastén.")
    col_b1, col_b2, col_b3 = st.columns(3)
    with col_b1:
        st.markdown("<div class='premium-card'><h4>Rimo y Vitalidad</h4><p>Ejercicios para despertar la energía física.</p></div>", unsafe_allow_html=True)
    with col_b2:
        st.markdown("<div class='premium-card'><h4>Afectividad</h4><p>Conexión profunda con el otro y el grupo.</p></div>", unsafe_allow_html=True)
    with col_b3:
        st.markdown("<div class='premium-card'><h4>Creatividad</h4><p>Expresión libre a través del movimiento orgánico.</p></div>", unsafe_allow_html=True)

# FOOTER PRO
st.markdown("<br><hr><p style='text-align: center; opacity: 0.6;'>FAYOGA 2026 | Wellness SaaS Premium por Fabiola Pastén</p>", unsafe_allow_html=True)
