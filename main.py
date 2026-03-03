import streamlit as st
import requests
from streamlit_lottie import st_lottie
import time

# 1. Configuración de Marca y Layout de Pantalla Completa
st.set_page_config(page_title="Fayoga | Fabiola Pastén", page_icon="🧘‍♀️", layout="wide")

# Función para carga segura de animaciones
def load_lottie(url):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except: return None

# Recursos Visuales (Lotties Premium)
lottie_yoga = load_lottie("https://lottie.host/9f5064e4-399a-426c-829d-64d898517228/qG4K3nE0H5.json")
lottie_lotus = load_lottie("https://lottie.host/807f4340-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")

# 2. SISTEMA DE DISEÑO (CSS Personalizado)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;500;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Quicksand', sans-serif; background-color: #FDF9F3; color: #2D4030; }
    
    /* HUINCHA AMERICANA (News Ticker) */
    .ticker-wrapper {
        width: 100%; overflow: hidden; background: #6B8E23; color: white;
        padding: 10px 0; position: fixed; top: 0; left: 0; z-index: 999;
    }
    .ticker {
        display: inline-block; white-space: nowrap; padding-left: 100%;
        animation: ticker 30s linear infinite; font-weight: bold; font-size: 1.1rem;
    }
    @keyframes ticker {
        0% { transform: translate3d(0, 0, 0); }
        100% { transform: translate3d(-100%, 0, 0); }
    }

    /* CARDS RESPONSIVAS */
    .feature-card {
        background: white; padding: 2rem; border-radius: 30px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.03); border: 1px solid #E9EDC9;
        transition: transform 0.3s ease; height: 100%;
    }
    .feature-card:hover { transform: translateY(-10px); }
    
    .stTabs [data-baseweb="tab-list"] { justify-content: center; }
    </style>
    
    <div class="ticker-wrapper">
        <div class="ticker">
            ✨ PRÓXIMO TALLER DE BIODANZA EN LA SERENA - SÁBADO 15 MARZO ✨ | 🧘 NUEVOS CUPOS PARA YOGA MATINAL ONLINE | 📚 CURADURÍA DE BIENESTAR POR FABIOLA PASTÉN | ✨ SUSCRÍBETE AL NEWSLETTER WELLNESS ✨
        </div>
    </div>
    <br><br>
    """, unsafe_allow_html=True)

# 3. HEADER DINÁMICO
with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if lottie_lotus: st_lottie(lottie_lotus, height=180, key="lotus")
        st.markdown("<h1 style='text-align: center; color: #4A5D4E;'>Fayoga</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 1.2rem;'><b>Fabiola Pastén</b><br>Periodista & Wellness Expert</p>", unsafe_allow_html=True)

# 4. NAVEGACIÓN Y CONTENIDO
tabs = st.tabs(["💎 Dashboard", "🧘 Mi Práctica", "📰 Noticias Ágiles", "📩 Contacto"])

with tabs[0]: # Dashboard / Inicio
    st.markdown("### Experiencia Wellness de Clase Mundial")
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        st.markdown("""<div class='feature-card'>
            <h4>🧘 Yoga Integral</h4>
            <p>Clases de Hatha y Vinyasa Flow enfocadas en la alineación y la paz mental. 
            Sesiones grabadas y en vivo.</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class='feature-card'>
            <h4>💃 Biodanza</h4>
            <p>El sistema de integración humana a través del movimiento y la música. 
            Talleres grupales exclusivos.</p>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class='feature-card'>
            <h4>🗞️ Periodismo Wellness</h4>
            <p>Información curada con rigor periodístico sobre salud, neurociencia 
            y tendencias globales.</p>
        </div>""", unsafe_allow_html=True)

with tabs[1]: # Mi Práctica (Simulación/Interactividad)
    st.markdown("### Pausa Activa Consciente")
    col_p1, col_p2 = st.columns([2, 1])
    with col_p1:
        st.info("Utiliza este simulador para una respiración guiada de 1 minuto.")
        if st.button("🚀 Iniciar Respiración Guiada"):
            prog = st.progress(0)
            status = st.empty()
            for i in range(100):
                if i < 50: status.text("Inhala profundamente...")
                else: status.text("Exhala suavemente...")
                prog.progress(i + 1)
                time.sleep(0.06)
            st.success("Pausa completada. Namasté.")
    with col_p2:
        if lottie_yoga: st_lottie(lottie_yoga, height=250, key="yoga_sim")

with tabs[2]: # Noticias Ágiles (Hemeroteca)
    st.markdown("### ⚡ Lo Último en Bienestar")
    # Grid de noticias tipo "News Feed"
    n1, n2 = st.columns(2)
    with n1:
        st.markdown("""<div class='feature-card'>
            <small>MARZO 2026</small>
            <h5>Neurociencia y Meditación</h5>
            <p>Nuevos estudios confirman que 10 min de yoga diario rejuvenecen el cerebro...</p>
            <a href='#'>Leer más</a>
        </div>""", unsafe_allow_html=True)
    with n2:
        st.markdown("""<div class='feature-card'>
            <small>MARZO 2026</small>
            <h5>Biodanza en Empresas</h5>
            <p>Cómo el movimiento grupal está mejorando la productividad en el coworking...</p>
            <a href='#'>Leer más</a>
        </div>""", unsafe_allow_html=True)

with tabs[3]: # Contacto / Agenda
    st.markdown("### Conectemos")
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        with st.form("agenda"):
            st.text_input("Nombre")
            st.selectbox("Me interesa", ["Yoga", "Biodanza", "Coaching Wellness"])
            st.form_submit_button("Enviar Solicitud")
    with col_f2:
        st.write("**Fabiola Pastén**")
        st.write("📍 La Serena, Chile")
        st.write("📧 contacto@fayoga.cl")

# FOOTER
st.markdown("<br><hr><p style='text-align: center; opacity: 0.5;'>Fayoga 2026 | Wellness de Clase Mundial</p>", unsafe_allow_html=True)
