import streamlit as st
import requests
from streamlit_lottie import st_lottie
import datetime

# 1. CONFIGURACIÓN PREMIUM
st.set_page_config(page_title="Fayoga | Fabiola Pastén", page_icon="🧘‍♀️", layout="wide")

def load_lottie(url):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except: return None

# Recursos Visuales
lottie_zen = load_lottie("https://lottie.host/807f4340-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")

# 2. SISTEMA DE DISEÑO (Corrección de visibilidad y Estética Pro)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Quicksand:wght@300;500&display=swap');
    
    /* Fondo General */
    .stApp { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }
    
    /* Ticker / Huincha Americana */
    .ticker-wrapper {
        width: 100%; overflow: hidden; background: #2D4030; color: #E9EDC9;
        padding: 8px 0; position: fixed; top: 0; left: 0; z-index: 1000;
    }
    .ticker {
        display: inline-block; white-space: nowrap; padding-left: 100%;
        animation: ticker 25s linear infinite; font-weight: 500;
    }
    @keyframes ticker { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-100%, 0, 0); } }

    /* Glassmorphism Cards - CORRECCIÓN DE COLOR */
    .premium-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(12px);
        border-radius: 25px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        margin-bottom: 20px;
        color: #1a1a1a !important; /* Texto oscuro asegurado */
    }
    h1, h2, h3, h4 { color: #2D4030 !important; font-family: 'Playfair Display', serif; }
    p, li { color: #333333 !important; font-family: 'Quicksand', sans-serif; }

    /* Botones Premium */
    .stButton>button {
        background: #4A5D4E; color: white !important;
        border-radius: 50px; border: none; padding: 12px 30px;
        font-weight: bold; width: 100%; transition: 0.3s;
    }
    .stButton>button:hover { background: #6B8E23; transform: scale(1.02); }
    </style>
    
    <div class="ticker-wrapper"><div class="ticker">
        🔥 NOVEDAD: Taller de Biodanza y Comunicación Consciente - Cupos Limitados | 🧘‍♀️ Clases Online en Directo con Fabiola Pastén | 🗞️ Nueva entrada en Hemeroteca: Neurociencia del Bienestar
    </div></div><br><br>
    """, unsafe_allow_html=True)

# 3. HEADER & HERO
col_h1, col_h2, col_h3 = st.columns([1, 2, 1])
with col_h2:
    if lottie_zen: st_lottie(lottie_zen, height=150)
    st.markdown("<h1 style='text-align: center;'>FAYOGA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.3rem;'><b>Fabiola Pastén</b><br>Periodista & Wellness Master</p>", unsafe_allow_html=True)

# 4. NAVEGACIÓN BOUTIQUE
tabs = st.tabs(["💎 Experience", "🧘‍♀️ Reservas", "🤖 FABI IA", "📰 Hemeroteca"])

with tabs[0]: # Dashboard Premium
    st.markdown("### El Universo Fayoga")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='premium-card'><h4>Yoga Integral</h4><p>Hatha y Vinyasa con enfoque terapéutico. Alineación perfecta para cuerpos modernos.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='premium-card'><h4>Biodanza</h4><p>Integración humana y renovación vital a través del movimiento y la música orgánica.</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='premium-card'><h4>Wellness Pro</h4><p>Asesorías basadas en comunicación consciente y bienestar corporativo de alto impacto.</p></div>", unsafe_allow_html=True)

with tabs[1]: # Agendamiento Pro
    st.markdown("### Agenda tu Transformación")
    col_ag1, col_ag2 = st.columns(2)
    with col_ag1:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        nombre = st.text_input("Nombre del Alumno")
        servicio = st.selectbox("Clase o Sesión", ["Yoga Matinal", "Biodanza Grupal", "Coaching 1:1", "Wellness para Empresas"])
        fecha = st.date_input("Fecha preferida", min_value=datetime.date.today())
        if st.button("Confirmar Cita"):
            st.balloons()
            st.success(f"Solicitud enviada para {nombre}. Fabiola te contactará pronto.")
        st.markdown("</div>", unsafe_allow_html=True)
    with col_ag2:
        st.image("https://images.unsplash.com/photo-1545209114-159518055c6f?auto=format&fit=crop&w=800", caption="Tu espacio de paz te espera.")

with tabs[2]: # ASESORA IA: FABI
    st.markdown("### FABI: Tu Asesora IA de Bienestar")
    st.info("FABI está entrenada con la metodología y el enfoque periodístico de Fabiola Pastén.")
    user_q = st.text_input("¿En qué área de tu bienestar quieres profundizar hoy?")
    if st.button("Consultar a FABI"):
        with st.spinner("Conectando con la esencia de Fayoga..."):
            # Simulación de respuesta IA nivel Pro
            st.markdown(f"""
            <div class='premium-card'>
            <b>Respuesta de FABI:</b><br>
            <i>"Como comunicadora y experta wellness, entiendo que tu interés por '{user_q}' busca un equilibrio entre acción y calma. 
            Te recomiendo iniciar con 5 minutos de respiración consciente antes de tu práctica de yoga para alinear tu centro."</i>
            </div>
            """, unsafe_allow_html=True)

with tabs[3]: # Hemeroteca Ágil
    st.markdown("### Hemeroteca Mundial Curada")
    col_n1, col_n2 = st.columns(2)
    with col_n1:
        st.markdown("<div class='premium-card'><b>Noticia Flash</b><br>El impacto del yoga en la productividad remota: estudio 2026.</div>", unsafe_allow_html=True)
    with col_n2:
        st.markdown("<div class='premium-card'><b>Bienestar Global</b><br>Biodanza se expande en centros de coworking europeos.</div>", unsafe_allow_html=True)

# FOOTER
st.markdown("<br><hr><p style='text-align: center; opacity: 0.6;'>Fayoga 2026 | Wellness de Clase Mundial</p>", unsafe_allow_html=True)
