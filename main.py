import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pandas as pd
import numpy as np
import time

# ==========================================
# 1. NÚCLEO Y PANTALLA TOTAL
# ==========================================
st.set_page_config(
    page_title="Fayoga | Academia Premium",
    page_icon="🧘‍♀️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_lottie(url: str):
    try:
        r = requests.get(url, timeout=5)
        return r.json() if r.status_code == 200 else None
    except: return None

# Animaciones de alta gama
lottie_yoga_header = load_lottie("https://lottie.host/9f5064e4-399a-426c-829d-64d898517228/qG4K3nE0H5.json") # Icono Yoga para el header
lottie_zen = load_lottie("https://lottie.host/807f4340-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")

# ==========================================
# 2. SISTEMA DE DISEÑO (CSS EQUILIBRADO)
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@900&family=Quicksand:wght@300;500;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #fdfaf6 0%, #e9edc9 100%);
        background-attachment: fixed;
    }
    
    /* ELIMINAR MÁRGENES NATIVOS */
    .main .block-container {
        padding-top: 4rem !important;
        max-width: 95% !important;
    }

    /* FAYOGA: ESCALADO MONUMENTAL */
    .brand-title {
        font-family: 'Playfair Display', serif;
        font-size: clamp(6rem, 20vw, 12rem) !important;
        color: #4A5D4E;
        text-align: center;
        line-height: 0.8;
        font-weight: 900;
        margin-bottom: 0px;
        margin-top: -20px;
        text-shadow: 2px 5px 15px rgba(0,0,0,0.1);
    }

    .brand-subtitle {
        font-family: 'Quicksand', sans-serif;
        font-size: clamp(1.2rem, 3vw, 2.5rem) !important;
        text-align: center;
        color: #6B8E23;
        font-weight: 500;
        letter-spacing: 15px;
        text-transform: uppercase;
        margin-top: 10px;
        margin-bottom: 40px;
    }

    /* RESTAURAR PESTAÑAS (TABS) GIGANTES Y LEGIBLES */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 1.5rem !important;
        font-family: 'Quicksand', sans-serif !important;
        font-weight: 700 !important;
        color: #4A5D4E !important;
        padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] {
        border-bottom-color: #6B8E23 !important;
        color: #2D4030 !important;
    }

    /* TARJETAS PREMIUM */
    .premium-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(25px);
        border-radius: 40px;
        padding: 40px;
        border: 2px solid #A3B18A;
        box-shadow: 0 20px 40px rgba(0,0,0,0.08);
        margin-bottom: 30px;
        color: #1A1A1A !important;
    }
    
    .premium-card h2, .premium-card h3, .premium-card h4 {
        color: #2D4030 !important;
        font-family: 'Playfair Display', serif !important;
    }

    /* RESTAURAR BOTONERÍA MAJESTUOSA */
    .stButton>button {
        background: linear-gradient(45deg, #4A5D4E 0%, #6B8E23 100%);
        color: white !important;
        border-radius: 50px !important;
        border: none !important;
        padding: 20px 40px !important;
        font-weight: 700 !important;
        font-size: 1.5rem !important;
        width: 100% !important;
        box-shadow: 0 10px 20px rgba(107, 142, 35, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover { transform: translateY(-3px) !important; box-shadow: 0 15px 25px rgba(107, 142, 35, 0.5) !important; }

    /* TEXTOS GENERALES */
    p, li, label { 
        font-size: 1.2rem !important; 
        color: #1A1A1A !important; 
        font-family: 'Quicksand', sans-serif !important; 
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. HEADER MAJESTUOSO (CON ICONO YOGA)
# ==========================================
c_logo_1, c_logo_2, c_logo_3 = st.columns([1, 2, 1])
with c_logo_2:
    # Icono de Yoga animado sobre el título
    if lottie_yoga_header: 
        st_lottie(lottie_yoga_header, height=180, key="header_icon")
    st.markdown("<h1 class='brand-title'>FAYOGA</h1>", unsafe_allow_html=True)
    st.markdown("<p class='brand-subtitle'>Fabiola Pastén</p>", unsafe_allow_html=True)

# ==========================================
# 4. SISTEMA DE APRENDIZAJE 10 NIVELES
# ==========================================
tabs = st.tabs(["💎 Dashboard", "🎓 YogaDoc Learning", "💃 Biodanza Flow", "👥 Alumnos", "🤖 FABI IA"])

with tabs[0]: # Dashboard
    st.markdown("## Bienvenida al Universo Fayoga")
    col_d1, col_d2 = st.columns([1, 1])
    with col_d1:
        st.markdown("""<div class='premium-card'>
            <h3>La Evolución del Bienestar</h3>
            <p>Fayoga trasciende la clase de yoga tradicional para convertirse en un sistema de aprendizaje integral. Navega por nuestros módulos interactivos y descubre una nueva forma de conectar cuerpo y mente.</p>
        </div>""", unsafe_allow_html=True)
    with col_d2:
        st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=1200", use_container_width=True)

with tabs[1]: # YogaDoc: 10 Niveles + Premium
    st.markdown("## YogaDoc: Progresión de Conciencia")
    
    nivel = st.select_slider("Selecciona tu Nivel", options=[i for i in range(1, 12)], 
                            format_func=lambda x: f"Nivel {x}" if x <= 10 else "💎 MODO PREMIUM")
    
    if nivel <= 10:
        ejercicios = {
            1: ("Respiración Primordial", "Iniciación al silencio mental.", "https://images.unsplash.com/photo-1506126613408-eca07ce68773"),
            2: ("Alineación Ósea", "Conexión con la estructura física.", "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b"),
            3: ("Fluidez Vinyasa", "El arte de transitar.", "https://images.unsplash.com/photo-1599447421416-3414500d18a5"),
            4: ("Resonancia Vocal", "Uso del sonido.", "https://images.unsplash.com/photo-1512438248247-f0f2a5a8b7f0"),
            5: ("Equilibrio Estático", "Centro en la quietud.", "https://images.unsplash.com/photo-1510894347713-fc3ed6fdf539"),
            6: ("Biodanza Matinal", "Movimiento de despertar.", "https://images.unsplash.com/photo-1518310383802-640c2de311b2"),
            7: ("Pranayama Avanzado", "Control de energía vital.", "https://images.unsplash.com/photo-1499209974431-9dac3adaf471"),
            8: ("Yoga de los Sentidos", "Exploración consciente.", "https://images.unsplash.com/photo-1524633212363-36dd03f0dd2e"),
            9: ("Meditación Periodística", "Análisis crítico interior.", "https://images.unsplash.com/photo-1474418397713-7ded018049ce"),
            10: ("Integración Fayoga", "La maestría de todos los elementos.", "https://images.unsplash.com/photo-1447452001602-7090c7ab2db3")
        }
        
        titulo, desc, img = ejercicios[nivel]
        
        col_ex1, col_ex2 = st.columns([1, 1])
        with col_ex1:
            st.markdown(f"""<div class='premium-card'>
                <h2>Nivel {nivel}: {titulo}</h2>
                <p>{desc}</p>
                <hr>
                <p>Completa este nivel para avanzar en tu ruta.</p>
            </div>""", unsafe_allow_html=True)
            
            if st.button(f"🚀 Iniciar Práctica de {titulo}"):
                bar = st.progress(0)
                status = st.empty()
                for i in range(101):
                    msg = "Inhala..." if i < 50 else "Exhala..."
                    status.markdown(f"**{msg}**")
                    bar.progress(i)
                    time.sleep(0.04)
                st.success(f"¡Nivel {nivel} Completado!")
        with col_ex2:
            st.image(f"{img}?auto=format&fit=crop&w=800", use_container_width=True)

    else:
        # Modo Premium Bloqueado
        st.markdown("""<div class='premium-card' style='text-align: center; border-color: #6B8E23; background: #2D4030;'>
            <h1 style='color: white !important;'>💎 MODO PREMIUM</h1>
            <p style='color: #E9EDC9 !important; font-size: 1.5rem !important;'>Has completado la formación de 10 niveles. 
            El modo Premium incluye clases en vivo con Fabiola y consultoría IA avanzada.</p>
        </div>""", unsafe_allow_html=True)
        st.button("SUSCRIBIRSE AL MODO PREMIUM")

with tabs[2]: # BIODANZA
    st.markdown("## Biodanza: La Danza de la Vida")
    c_b1, c_b2 = st.columns(2)
    with c_b1:
        st.markdown("<div class='premium-card'><h4>Afectividad y Movimiento</h4><p>El sistema de integración grupal de Fabiola Pastén. Recupera la alegría de vivir a través del ritmo y la conexión humana.</p></div>", unsafe_allow_html=True)
    with c_b2:
        if lottie_zen: st_lottie(lottie_zen, height=250)

with tabs[3]: # ALUMNOS
    st.markdown("## Comunidad Fayoga")
    df_alumnos = pd.DataFrame({
        "Alumno": ["Rodrigo Godoy", "Fabiola Pastén", "María José", "Carlos R."],
        "Nivel Actual": [8, 10, 3, 5],
        "Membresía": ["Premium", "Staff", "Gratuito", "Live"]
    })
    st.dataframe(df_alumnos, use_container_width=True)

with tabs[4]: # FABI IA
    st.markdown("## FABI IA Asesora")
    st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
    pregunta = st.text_input("¿Qué área de tu bienestar quieres explorar hoy?")
    if st.button("Consultar a FABI Expert"):
        st.success(f"**FABI:** Para tu consulta sobre '{pregunta}', te recomiendo revisar el Nivel 3 de YogaDoc.")
    st.markdown("</div>", unsafe_allow_html=True)

# FOOTER PRO
st.markdown("<br><hr><p style='text-align: center; opacity: 0.6;'>FAYOGA 2026 | Wellness SaaS Premium por Fabiola Pastén</p>", unsafe_allow_html=True)
