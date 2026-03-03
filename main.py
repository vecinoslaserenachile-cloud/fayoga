import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
import time
import folium
from streamlit_folium import st_folium

# ==========================================
# 1. CONFIGURACIÓN DE NÚCLEO Y PANTALLA
# ==========================================
st.set_page_config(
    page_title="Fayoga Premium | Fabiola Pastén",
    page_icon="🧘‍♀️",
    layout="wide", # Maximiza espacio en TVs y monitores 4K
    initial_sidebar_state="collapsed"
)

# Cargador de activos visuales vectoriales
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except: return None

# Galería de Animaciones Lottie (Premium)
lottie_zen = load_lottieurl("https://lottie.host/807f4340-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")
lottie_yoga_pro = load_lottieurl("https://lottie.host/9f5064e4-399a-426c-829d-64d898517228/qG4K3nE0H5.json")
lottie_ia_brain = load_lottieurl("https://lottie.host/07as9pva-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")

# ==========================================
# 2. SISTEMA DE DISEÑO PRO (CSS AVANZADO)
# ==========================================
# Forzamos contrastes profundos: No más blanco sobre blanco.
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Quicksand:wght@300;400;500;700&display=swap');
    
    /* Configuración de Contenedor Global */
    .stApp {
        background: linear-gradient(135deg, #fdfaf6 0%, #e9edc9 100%);
        color: #1A1A1A;
    }

    /* News Ticker - Huincha Americana Pro */
    .ticker-container {
        width: 100%; overflow: hidden; background: #2D4030; 
        color: #E9EDC9; padding: 12px 0; position: fixed; 
        top: 0; left: 0; z-index: 9999; box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    .ticker-text {
        display: inline-block; white-space: nowrap; padding-left: 100%;
        animation: ticker-animation 40s linear infinite;
        font-family: 'Quicksand', sans-serif; font-weight: 700; font-size: 1.1rem;
    }
    @keyframes ticker-animation {
        0% { transform: translate3d(0, 0, 0); }
        100% { transform: translate3d(-100%, 0, 0); }
    }

    /* Glassmorphism Premium Cards - Contraste Asegurado */
    .glass-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(15px);
        border-radius: 40px;
        padding: 45px;
        border: 2px solid #A3B18A;
        box-shadow: 0 20px 45px rgba(0,0,0,0.1);
        margin-bottom: 30px;
        color: #1A1A1A !important;
    }

    /* Tipografía Dinámica */
    h1, h2, h3 { 
        color: #2D4030 !important; 
        font-family: 'Playfair Display', serif !important; 
        font-weight: 700 !important;
    }
    p, li, span, label { 
        color: #1A1A1A !important; 
        font-family: 'Quicksand', sans-serif !important; 
        font-weight: 600 !important;
    }

    /* Botones de Acción SaaS */
    .stButton>button {
        background: linear-gradient(45deg, #4A5D4E 0%, #6B8E23 100%);
        color: #FFFFFF !important;
        border-radius: 50px; border: none; padding: 20px 45px;
        font-weight: 700; width: 100%;
        box-shadow: 0 10px 20px rgba(107, 142, 35, 0.3);
    }
    </style>
    
    <div class="ticker-container">
        <div class="ticker-text">
            🌟 PRÓXIMO TALLER: BIODANZA Y COMUNICACIÓN NO VIOLENTA - SÁBADO 15 DE MARZO | 🧘‍♀️ NUEVOS CUPOS: YOGA INTEGRAL MATINAL | 📰 HEMEROTECA: "NEUROCIENCIA Y MOVIMIENTO" YA DISPONIBLE | 🤖 CONSULTA A FABI IA
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 3. CABECERA Y HERO SECTION
# ==========================================
st.markdown("<br><br>", unsafe_allow_html=True)
col_header_1, col_header_2, col_header_3 = st.columns([1, 3, 1])
with col_header_2:
    if lottie_zen: st_lottie(lottie_zen, height=220, key="lotus")
    st.markdown("<h1 style='text-align: center; font-size: 5rem; margin-bottom: 0;'>FAYOGA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 2rem; color: #4A5D4E;'><b>Fabiola Pastén</b></p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2rem; opacity: 0.9;'>Periodista, Comunicadora y Experta en Wellness, Yoga y Biodanza</p>", unsafe_allow_html=True)

st.divider()

# ==========================================
# 4. NAVEGACIÓN Y FUNCIONALIDADES
# ==========================================
tabs = st.tabs(["💎 Dashboard", "🧘‍♂️ Mi Práctica", "🤖 FABI IA", "📅 Agendar", "📰 Hemeroteca"])

with tabs[0]: # Dashboard de Experiencia
    st.markdown("### El Ecosistema de Bienestar")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class='glass-card'>
            <h3>Yoga Integral</h3>
            <p>Hatha y Vinyasa terapéutico para el equilibrio del sistema nervioso.</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class='glass-card'>
            <h3>Biodanza</h3>
            <p>Integración humana y renovación vital a través del movimiento grupal.</p>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class='glass-card'>
            <h3>Wellness Pro</h3>
            <p>Consultoría en bienestar corporativo y comunicación consciente.</p>
        </div>""", unsafe_allow_html=True)

    # Gráficos Pro con Plotly
    st.markdown("### Métricas de Integración Wellness")
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        categories = ['Fuerza', 'Calma', 'Flexibilidad', 'Energía', 'Conexión']
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(r=[85, 95, 80, 90, 95], theta=categories, fill='toself', line_color='#6B8E23'))
        fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False, title="Equilibrio Fayoga")
        st.plotly_chart(fig_radar, use_container_width=True)
    with col_g2:
        st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=1200", caption="La ciencia del equilibrio por Fabiola Pastén.")

with tabs[1]: # Mi Práctica (Interactividad)
    st.markdown("### Sesión de Pausa Activa")
    col_p1, col_p2 = st.columns([2, 1])
    with col_p1:
        st.info("Simulador de Respiración Guiada para Alumnos.")
        if st.button("🚀 Iniciar Ciclo de Respiración"):
            bar = st.progress(0)
            t = st.empty()
            for i in range(101):
                msg = "Inhala profundamente..." if i < 50 else "Exhala lentamente..."
                t.markdown(f"**{msg}**")
                bar.progress(i)
                time.sleep(0.05)
            st.success("Ciclo completado. Siente la paz.")
    with col_p2:
        if lottie_yoga_pro: st_lottie(lottie_yoga_pro, height=300)

with tabs[2]: # FABI IA
    st.markdown("### FABI: Tu Asesora IA Premium")
    col_ia1, col_ia2 = st.columns([1, 2])
    with col_ia1:
        if lottie_ia_brain: st_lottie(lottie_ia_brain, height=250)
    with col_ia2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        pregunta = st.text_input("¿Cómo puedo mejorar mi bienestar hoy?")
        if st.button("Consultar a FABI"):
            with st.spinner("Analizando con rigor periodístico..."):
                time.sleep(1)
                st.markdown(f"""
                **Respuesta de FABI:**
                Como comunicadora y experta, te sugiero que para mejorar '{pregunta}', 
                integres pausas de silencio de 3 minutos cada 2 horas. 
                La Biodanza nos enseña que el ritmo orgánico es la base de la salud.
                """)
        st.markdown("</div>", unsafe_allow_html=True)

with tabs[3]: # Agendamiento con Mapa
    st.markdown("### Reserva tu Transformación")
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        with st.form("agenda_pro"):
            st.text_input("Nombre Completo")
            st.selectbox("Servicio", ["Yoga Privado", "Biodanza Grupal", "Wellness Corporativo"])
            st.date_input("Fecha", min_value=date.today())
            st.form_submit_button("Confirmar Reserva Pro")
    with col_a2:
        st.markdown("#### Nuestra Ubicación en La Serena")
        # Mapa Interactivo con Folium
        m = folium.Map(location=[-29.9045, -71.2519], zoom_start=14)
        folium.Marker([-29.9045, -71.2519], popup="Fayoga Studio", tooltip="Fabiola Pastén").add_to(m)
        st_folium(m, height=300, width=600)

with tabs[4]: # Hemeroteca (Contenido Propio)
    st.markdown("### Hemeroteca Wellness Mundial")
    st.write("Curaduría periodística de lo mejor del mundo wellness.")
    n1, n2 = st.columns(2)
    with n1:
        st.markdown("<div class='glass-card'><b>Neurociencia del Yoga</b><p>Análisis profundo sobre el nervio vago y la práctica matinal.</p></div>", unsafe_allow_html=True)
    with n2:
        st.markdown("<div class='glass-card'><b>Biodanza en 2026</b><p>Cómo la integración grupal está salvando la salud mental corporativa.</p></div>", unsafe_allow_html=True)

# FOOTER PRO
st.markdown("<br><hr><p style='text-align: center; opacity: 0.6;'>FAYOGA 2026 | Wellness SaaS Premium por Fabiola Pastén</p>", unsafe_allow_html=True)
