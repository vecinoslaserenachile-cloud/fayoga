import streamlit as st
import requests
from streamlit_lottie import st_lottie
import datetime

# 1. CONFIGURACIÓN PREMIUM SAAS
st.set_page_config(
    page_title="Fayoga | Fabiola Pastén",
    page_icon="🧘‍♀️",
    layout="wide", # Clave para TV y Escritorio
    initial_sidebar_state="collapsed"
)

# Función segura para carga de animaciones vectoriales (Lottie)
def load_lottie(url):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except: return None

# Inicialización de recursos visuales de alta calidad y bajo peso
lottie_zen_lotus = load_lottie("https://lottie.host/807f4340-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")
lottie_yoga_flow = load_lottie("https://lottie.host/9f5064e4-399a-426c-829d-64d898517228/qG4K3nE0H5.json")
lottie_brain_wellness = load_lottie("https://lottie.host/07as9pva-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json") # Simulación

# 2. SISTEMA DE DISEÑO PRO (Corrección de visibilidad y Estética Glassmorphism)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Quicksand:wght@300;500;700&display=swap');
    
    /* Fondo Degradado Relajante */
    .stApp { background: linear-gradient(135deg, #fdfaf6 0%, #e9edc9 100%); }
    
    /* Ticker / Huincha Americana Live (Noticias y Promociones) */
    .ticker-wrapper {
        width: 100%; overflow: hidden; background: #2D4030; color: #E9EDC9;
        padding: 8px 0; position: fixed; top: 0; left: 0; z-index: 1000;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    .ticker {
        display: inline-block; white-space: nowrap; padding-left: 100%;
        animation: ticker 25s linear infinite; font-weight: 500; font-family: 'Quicksand', sans-serif;
    }
    @keyframes ticker { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-100%, 0, 0); } }

    /* Glassmorphism Cards - CORRECCIÓN DE COLOR DE TEXTO */
    .premium-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(15px);
        border-radius: 30px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 10px 32px 0 rgba(31, 38, 135, 0.07);
        margin-bottom: 25px;
        transition: transform 0.3s ease;
    }
    .premium-card:hover { transform: translateY(-5px); }
    
    /* Forzar colores oscuros para contraste profesional */
    .premium-card h1, .premium-card h2, .premium-card h3, .premium-card h4 {
        color: #2D4030 !important; font-family: 'Playfair Display', serif !important;
    }
    .premium-card p, .premium-card li, .premium-card span {
        color: #333333 !important; font-family: 'Quicksand', sans-serif !important;
        font-weight: 500; font-size: 1.05rem;
    }
    .premium-card small { color: #555555 !important; }

    /* Botones Premium Boutique */
    .stButton>button {
        background: linear-gradient(45deg, #4A5D4E 0%, #6B8E23 100%);
        color: white !important; font-family: 'Quicksand', sans-serif; font-weight: 700;
        border-radius: 50px; border: none; padding: 15px 35px;
        width: 100%; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(107, 142, 35, 0.2);
    }
    .stButton>button:hover {
        transform: scale(1.03); box-shadow: 0 6px 20px rgba(107, 142, 35, 0.3);
    }
    
    /* Mejoras en pestañas (Tabs) */
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 20px; }
    .stTabs [data-baseweb="tab"] { font-family: 'Quicksand', sans-serif; font-weight: 700; color: #4A5D4E; }
    .stTabs [aria-selected="true"] { color: #6B8E23 !important; border-bottom-color: #6B8E23 !important; }
    </style>
    
    <div class="ticker-wrapper"><div class="ticker">
        🌟 NOVEDAD: Taller Boutique de Biodanza y Comunicación Consciente - Cupos Limitados | 🧘‍♀️ Clases Matinales de Yoga Integral Online | 📚 Hemeroteca Wellness: Curaduría periodística mundial | ✨ Consulta a FABI IA, tu asesora de bienestar 24/7
    </div></div><br><br><br>
    """, unsafe_allow_html=True)

# 3. HEADER & HERO (Marca y Fabiola)
# Usamos un layout de 3 columnas para TVs/Escritorios que se apila solo en móviles
col_h1, col_h2, col_h3 = st.columns([1, 2, 1])
with col_h2:
    if lottie_zen_lotus: st_lottie(lottie_zen_lotus, height=180, key="lotus_header")
    st.markdown("<h1 style='text-align: center; color: #2D4030; font-family: Playfair Display, serif;'>FAYOGA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.4rem;'>Fabiola Pastén</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-weight: 300; font-style: italic;'>Periodista & Wellness Master <br>Experta en Yoga, Biodanza y Comunicación Consciente</p>", unsafe_allow_html=True)

st.divider()

# 4. NAVEGACIÓN BOUTIQUE (SEO y UX Optimizado)
tabs = st.tabs(["💎 Dashboard Experience", "📅 Agenda Tu Sesión", "🤖 FABI IA Asesora", "📰 Hemeroteca Ágil"])

with tabs[0]: # Dashboard Premium (Lógica de SEO Wellness Top)
    st.markdown("### El Universo Fayoga")
    st.write("Explora las disciplinas integrales diseñadas por Fabiola para tu transformación.")
    
    # Grid responsivo para TV y Móvil
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class='premium-card'>
            <h4>🧘 Yoga Integral</h4>
            <p>Sesiones personalizadas de Hatha y Vinyasa terapéutico. Alineación perfecta para mentes y cuerpos modernos.</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class='premium-card'>
            <h4>💃 Biodanza grupal</h4>
            <p>Integración humana y renovación vital a través del movimiento y la música orgánica. Talleres boutique exclusivos.</p>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class='premium-card'>
            <h4>🌱 Wellness Coaching</h4>
            <p>Asesorías basadas en comunicación consciente y bienestar corporativo de alto impacto.</p>
        </div>""", unsafe_allow_html=True)
    
    st.markdown("### Contenido Propio")
    st.write("Fabiola utiliza su expertise periodístico para ofrecerte contenido único de bienestar.")
    col_content, col_content_2 = st.columns(2)
    with col_content:
        st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=800", caption="Yoga: La alineación interna.")
    with col_content_2:
        st.write("### El camino a la integración grupal.")
        st.write("La Biodanza no es solo baile; es un sistema terapéutico que restaura la alegría de vivir. Fabiola explica cómo la música grupal resetea nuestro sistema nervioso...")
        st.button("Ver artículo completo")

with tabs[1]: # Agendamiento Pro Nivel Premium (SaaS UX)
    st.markdown("### Agenda Tu Sesión Boutique")
    col_ag1, col_ag2 = st.columns([2, 1])
    with col_ag1:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        nombre = st.text_input("Nombre Completo del Alumno", placeholder="Ej: Juan Pérez")
        email = st.text_input("Correo Electrónico Pro", placeholder="Ej: juan.perez@empresa.com")
        
        # Grid para inputs secundarios
        c_i1, c_i2 = st.columns(2)
        with c_i1:
            servicio = st.selectbox("Clase o Sesión", ["Yoga Matinal Online", "Taller Biodanza Serena", "Coaching Wellness 1:1", "Programa Empresas"])
        with c_i2:
            fecha = st.date_input("Fecha preferida", min_value=datetime.date.today())
            
        if st.button("Confirmar Cita Pro"):
            if nombre and email:
                st.balloons()
                st.success(f"Solicitud Premium enviada para {nombre} ({email}). Fabiola te contactará pronto para la confirmación.")
            else:
                st.warning("Por favor, completa los campos de Nombre y Email.")
        st.markdown("</div>", unsafe_allow_html=True)
    with col_ag2:
        if lottie_yoga_flow: st_lottie(lottie_yoga_flow, height=300, key="yoga_booking")
        st.markdown("<small style='text-align: center; display: block;'>Tu espacio de paz boutique te espera.</small>", unsafe_allow_html=True)

with tabs[2]: # ASESORA IA: FABI (Integración de Expertise)
    st.markdown("### FABI: Tu Asesora IA de Bienestar 24/7")
    st.info("FABI está entrenada exclusivamente con la metodología periodística y wellness de Fabiola Pastén. No es un chatbot genérico, es la esencia de Fayoga.")
    
    col_ia1, col_ia2 = st.columns([2, 1])
    with col_ia1:
        user_q = st.text_input("¿En qué área de tu bienestar quieres profundizar hoy con la guía de Fabiola?")
        if st.button("Consultar a FABI Expert"):
            if user_q:
                with st.spinner("Conectando con la sabiduría de Fabiola Pastén..."):
                    # Simulación Pro de respuesta IA nivel SaaS Premium
                    st.markdown(f"""
                    <div class='premium-card'>
                    <small>CONSULTA SOBRE: {user_q}</small>
                    <h3>Respuesta Asesora de FABI:</h3>
                    <p><i>"Como comunicadora y experta wellness, entiendo que tu búsqueda de '{user_q}' necesita un enfoque integrado. 
                    Mi recomendación para hoy es que inicies con 5 minutos de respiración consciente (Mindfulness) antes de tu práctica de yoga. 
                    Esto permitirá que tu sistema nervioso se alinee, facilitando la integración de la Biodanza si ese es tu camino grupal secundario. <br><br>
                    Namasté."</i></p>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("Por favor, ingresa tu consulta wellness.")
    with col_ia2:
        if lottie_brain_wellness: st_lottie(lottie_brain_wellness, height=250, key="brain_ia")

with tabs[3]: # Hemeroteca Ágil Nivel Pro (Noticias & SEO)
    st.markdown("### Hemeroteca Mundial Curada por Periodista Experta")
    st.write("Lo último en salud, neurociencia y tendencias globales wellness, curado con rigor periodístico por Fabiola Pastén.")
    
    # Grid responsivo para feed de noticias
    col_n1, col_n2, col_n3 = st.columns(3)
    with col_n1:
        st.markdown("""<div class='premium-card'>
            <small>MARZO 2026</small>
            <h4>Neurociencia y Meditación</h4>
            <p>Nuevos estudios confirman que 10 min de yoga diario rejuvenecen el cerebro. Fabiola analiza cómo la Biodanza grupal potencia este efecto.</p>
            <a href='#' style='color: #6B8E23; text-decoration: none; font-weight: 700;'>Leer análisis...</a>
        </div>""", unsafe_allow_html=True)
    with col_n2:
        st.markdown("""<div class='premium-card'>
            <small>MARZO 2026</small>
            <h4>Biodanza en el Freelance</h4>
            <p>Cómo el movimiento grupal está mejorando la productividad en los centros de coworking. Reportaje exclusivo de Fayoga.</p>
            <a href='#' style='color: #6B8E23; text-decoration: none; font-weight: 700;'>Ver reportaje...</a>
        </div>""", unsafe_allow_html=True)
    with col_n3:
        st.markdown("""<div class='premium-card'>
            <small>MARZO 2026</small>
            <h4>Wellness Corporativo 2026</h4>
            <p>Tendencias globales en well-being para empresas top. Fabiola Pastén ofrece las claves para la comunicación consciente empresarial.</p>
            <a href='#' style='color: #6B8E23; text-decoration: none; font-weight: 700;'>Suscribirse al feed...</a>
        </div>""", unsafe_allow_html=True)

# FOOTER PRO
st.markdown("<br><hr><p style='text-align: center; opacity: 0.6; font-size: 0.9rem;'>Fayoga 2026 | Wellness SaaS Premium de Clase Mundial por Fabiola Pastén</p>", unsafe_allow_html=True)
