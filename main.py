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
# 1. CONFIGURACIÓN DE NÚCLEO Y PANTALLA TOTAL
# ==========================================
st.set_page_config(
    page_title="Fayoga Premium | Fabiola Pastén",
    page_icon="🧘‍♀️",
    layout="wide", # Clave para ocupar todo el espacio en TVs y monitores 4K
    initial_sidebar_state="collapsed"
)

# Cargador seguro de activos visuales vectoriales
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except: return None

# Galería de Animaciones Lottie (Premium Livianas)
lottie_lotus = load_lottieurl("https://lottie.host/807f4340-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")
lottie_yoga_zen = load_lottieurl("https://lottie.host/9f5064e4-399a-426c-829d-64d898517228/qG4K3nE0H5.json")
lottie_pulso_resp = load_lottieurl("https://lottie.host/0a9f5d34-d9ae-44d5-83e8-8a033b0067b5/7L6A0G0U0V.json") # Simulación Zen Pulse

# ==========================================
# 2. SISTEMA DE DISEÑO PRO "EXPANSIVO" (CSS Avanzado)
# ==========================================
# Forzamos contraste profundo y ocupación total de espacio
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Quicksand:wght@300;400;500;700&display=swap');
    
    /* Configuración de Contenedor Global Expandido */
    .stApp {
        background: linear-gradient(135deg, #fdfaf6 0%, #e9edc9 100%);
        color: #1A1A1A;
    }
    
    /* Eliminar márgenes Streamlit para TV */
    .block-container {
        padding-top: 5rem !important;
        padding-bottom: 3rem !important;
        max-width: 90% !important; /* Estirar contenido */
        margin: auto;
    }

    /* News Ticker - Huincha Americana Pro Estilizada */
    .ticker-container {
        width: 100%; overflow: hidden; background: #2D4030; 
        color: #E9EDC9; padding: 15px 0; position: fixed; 
        top: 0; left: 0; z-index: 1001; box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .ticker-text {
        display: inline-block; white-space: nowrap; padding-left: 100%;
        animation: ticker-animation 40s linear infinite;
        font-family: 'Quicksand', sans-serif; font-weight: 700; font-size: 1.2rem;
    }
    @keyframes ticker-animation {
        0% { transform: translate3d(0, 0, 0); }
        100% { transform: translate3d(-100%, 0, 0); }
    }

    /* Glassmorphism Premium Cards - Contraste Blindado */
    .glass-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(18px);
        border-radius: 40px;
        padding: 60px; /* Más aire interno */
        border: 2px solid #A3B18A;
        box-shadow: 0 25px 50px rgba(0,0,0,0.12);
        margin-bottom: 35px;
        color: #1A1A1A !important;
        transition: transform 0.4s ease, box-shadow 0.4s ease;
    }
    .glass-card:hover { transform: translateY(-10px); box-shadow: 0 35px 70px rgba(0,0,0,0.15); }

    /* Tipografía Dinámica Escalada para Escritorio/TV */
    h1 { font-size: 4.8rem !important; }
    h2 { font-size: 3rem !important; }
    h3 { font-size: 2.2rem !important; }
    
    h1, h2, h3 { 
        color: #2D4030 !important; 
        font-family: 'Playfair Display', serif !important; 
        font-weight: 700 !important;
        margin-top: 1rem; margin-bottom: 1.5rem;
    }
    p, li, span, label, input, select { 
        color: #1A1A1A !important; 
        font-family: 'Quicksand', sans-serif !important; 
        font-weight: 600 !important;
        font-size: 1.25rem !important; /* Texto base más grande */
        line-height: 1.7;
    }

    /* Botones de Acción SaaS Boutqiue */
    .stButton>button {
        background: linear-gradient(45deg, #4A5D4E 0%, #6B8E23 100%);
        color: #FFFFFF !important;
        border-radius: 60px; border: none; padding: 22px 50px;
        font-weight: 700; width: 100%; font-size: 1.4rem;
        box-shadow: 0 12px 25px rgba(107, 142, 35, 0.4);
        transition: 0.3s;
    }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 18px 35px rgba(107, 142, 35, 0.6); }

    /* Ajuste Tabs */
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 30px; }
    .stTabs [data-baseweb="tab"] { font-size: 1.5rem !important; font-weight: 700; color: #4A5D4E; }
    </style>
    
    <div class="ticker-container">
        <div class="ticker-text">
            🌟 PRÓXIMO TALLER DE BIODANZA Y COMUNICACIÓN NO VIOLENTA - SÁBADO 15 DE MARZO ✨ | 🧘‍♀️ NUEVOS CUPOS ONLINE PARA YOGA MATINAL | 📚 HEMEROTECA WELLNESS: CURADURÍA PERIODÍSTICA MUNDIAL | 🤖 CONSULTA A FABI IA
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 3. CABECERA & HERO (PANTALLA COMPLETA)
# ==========================================
st.markdown("<br><br>", unsafe_allow_html=True)
col_header_1, col_header_2, col_header_3 = st.columns([1, 4, 1])
with col_header_2:
    if lottie_lotus: st_lottie(lottie_lotus, height=250, key="lotus_header")
    st.markdown("<h1 style='text-align: center; color: #2D4030;'>FAYOGA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 2.5rem !important; color: #4A5D4E;'><b>Fabiola Pastén</b></p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-style: italic; opacity: 0.8;'>Periodista, Comunicadora y Experta en Wellness, Yoga y Biodanza</p>", unsafe_allow_html=True)

st.divider()

# ==========================================
# 4. NAVEGACIÓN Y FUNCIONALIDADES
# ==========================================
tabs = st.tabs(["💎Dashboard Experience", "🧘‍♀️ Mi Práctica Zen", "🤖 FABI IA Asesora", "📅 Agendar Pro", "📰 Hemeroteca Ágil"])

with tabs[0]: # Dashboard Full Visual
    st.markdown("### El Universo Wellness Boutique")
    st.write("Explora las disciplinas integrales diseñadas por Fabiola para tu transformación profunda, con el rigor de una comunicadora experta.")
    
    # Grid de Funciones Líquido (TV responsivo)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class='glass-card'>
            <h4>Yoga Integral</h4>
            <p>Hatha y Vinyasa terapéutico. Alineación perfecta para cuerpos y mentes modernas.</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class='glass-card'>
            <h4>Biodanza Grupal</h4>
            <p>Integración humana y renovación vital a través del movimiento orgánico y la música.</p>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class='glass-card'>
            <h4>Wellness Corporativo</h4>
            <p>Consultoría en comunicación consciente y bienestar de alto impacto empresarial.</p>
        </div>""", unsafe_allow_html=True)

    # Gráficos y Datos Wellness (Plotly Interactivo)
    st.markdown("### Métricas de Evolución Wellness")
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        categories = ['Fuerza Consciente', 'Calma Mental', 'Flexibilidad Orgánica', 'Energía Vital', 'Conexión']
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(r=[85, 95, 80, 90, 95], theta=categories, fill='toself', name='Usuario Pro', line_color='#6B8E23'))
        fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False, title="Tu Perfil Fayoga")
        st.plotly_chart(fig_radar, use_container_width=True)
    with col_g2:
        st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=1200", caption="La ciencia del equilibrio por Fabiola Pastén.")

with tabs[1]: # Mi Práctica (INMERSIVA CON ANIMACIÓN)
    st.markdown("### Pausa Activa Consciente")
    col_p1, col_p2 = st.columns([1, 1])
    with col_p1:
        st.write("Utiliza este simulador inmersivo para un ejercicio rápido de respiración guiada. **FABI te guiará visualmente.**")
        st.markdown("""
        **Lógica:**
        1.  Inhala profundamente por la nariz (4 segundos).
        2.  Exhala suavemente por la boca (6 segundos).
        """)
        
        if st.button("🚀 Iniciar Guía de Respiración 🚀"):
            prog = st.progress(0)
            status = st.empty()
            # Ciclo de 10 segundos: Inhala 4, Exhala 6
            for sec in range(101):
                prog.progress(sec)
                msg = "**Inhala profundamente...** 😤" if sec < 41 else "**Exhala suavemente...** 😮‍💨"
                status.markdown(msg)
                time.sleep(0.1)
            st.success("Ciclo completado. Namasté.")
            st.balloons()
            
    with col_p2:
        st.markdown("<div class='glass-card' style='text-align: center;'>", unsafe_allow_html=True)
        # La animación Lottie actúa como el "pulso zen" contextual
        if lottie_pulso_resp: st_lottie(lottie_pulso_resp, height=350, key="zen_pulse")
        st.markdown("</div>", unsafe_allow_html=True)

with tabs[2]: # ASESORA IA: FABI Pro
    st.markdown("### FABI IA: Tu Asesora Premium")
    col_ia1, col_ia2 = st.columns([1, 2])
    with col_ia1:
        st.info("FABI está entrenada con la metodología periodística y wellness de Fabiola Pastén. No es genérica, es pura Fayoga.")
        if lottie_yoga_zen: st_lottie(lottie_yoga_zen, height=350, key="yoga_zen_ia")
    with col_ia2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        pregunta = st.text_input("¿Cómo puedo equilibrar mi energía hoy con Fabiola?", placeholder="Ej: Ejercicio respiración ansiedad")
        if st.button("Consultar a FABI Expert"):
            if pregunta:
                with st.spinner("Conectando con la sabiduría wellness periodística..."):
                    time.sleep(1)
                    # Simulación Pro nivel SaaS Premium
                    st.markdown(f"""
                    **Respuesta Asesora de FABI:**
                    Como comunicadora y experta, entiendo que '{pregunta}' busca un equilibrio profundo. Basada en el enfoque Fayoga:
                    - Inicia con 5 minutos de 'coherencia cardíaca' (respiración matinal).
                    - Integra movimiento rítmico (Biodanza) si sientes bloqueo emocional.
                    - Namasté.
                    """)
            else: st.warning("Por favor, ingresa tu consulta wellness.")
        st.markdown("</div>", unsafe_allow_html=True)

with tabs[3]: # Agendamiento con Mapa Pro
    st.markdown("### Reserva tu Transformación Pro")
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        with st.form("agenda_premium"):
            st.text_input("Nombre Completo del Alumno")
            st.text_input("Email", placeholder="juan.perez@pro.com")
            st.selectbox("Servicio", ["Yoga Privado 1:1", "Taller Biodanza Serena", "Wellness Corporativo empresas"])
            st.date_input("Fecha preferida", min_value=date.today())
            if st.form_submit_button("Confirmar Cita Boutique"):
                st.balloons()
                st.success("Solicitud Premium enviada. Fabiola te contactará pronto.")
        st.markdown("</div>", unsafe_allow_html=True)
    with col_a2:
        st.markdown("#### Ubicación Fayoga Studio (La Serena)")
        # Mapa Interactivo Folium de alta gama
        m = folium.Map(location=[-29.9045, -71.2519], zoom_start=15)
        folium.Marker([-29.9045, -71.2519], popup="Fayoga Studio", tooltip="Fabiola Pastén").add_to(m)
        st_folium(m, height=400, width=700)

with tabs[4]: # Hemeroteca Ágil (Noticias Curadas)
    st.markdown("### Hemeroteca Wellness Curada Mundial")
    st.write("Lo último en salud global, neurociencia y tendencias wellness, con el rigor periodístico de Fabiola Pastén.")
    
    col_n1, col_n2, col_n3 = st.columns(3)
    with col_n1:
        st.markdown("""<div class='glass-card'>
            <small>MARZO 2026</small>
            <h4>Neurociencia y Meditación</h4>
            <p>Nuevos estudios confirman que 10 min de yoga diario rejuvenecen el cerebro. Fabiola analiza cómo la Biodanza grupal potencia este efecto.</p>
            <a href='#' style='color: #6B8E23; text-decoration: none; font-weight: 700;'>Leer análisis...</a>
        </div>""", unsafe_allow_html=True)
    with col_n2:
        st.markdown("""<div class='glass-card'>
            <small>MARZO 2026</small>
            <h4>Biodanza en el Freelance</h4>
            <p>Cómo el movimiento grupal está mejorando la productividad en los centros de coworking. Reportaje exclusivo.</p>
            <a href='#' style='color: #6B8E23; text-decoration: none; font-weight: 700;'>Ver reportaje...</a>
        </div>""", unsafe_allow_html=True)
    with col_n3:
        st.markdown("""<div class='glass-card'>
            <small>MARZO 2026</small>
            <h4>Wellness Corporativo Pro</h4>
            <p>Tendencias globales en well-being para empresas top. Claves para la comunicación consciente empresarial.</p>
            <a href='#' style='color: #6B8E23; text-decoration: none; font-weight: 700;'>Suscribirse al feed...</a>
        </div>""", unsafe_allow_html=True)

# FOOTER PRO
st.markdown("<br><hr><p style='text-align: center; opacity: 0.6; font-size: 0.95rem !important;'>Fayoga 2026 | SaaS Premium de Clase Mundial por Fabiola Pastén</p>", unsafe_allow_html=True)
