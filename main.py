import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pandas as pd
import time
from datetime import date

# ==========================================
# 1. NÚCLEO Y PANTALLA TOTAL
# ==========================================
st.set_page_config(
    page_title="Fayoga | Academia Premium",
    page_icon="🧘‍♀️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Cargador de animaciones (Lottie) robusto
def load_lottie(url: str):
    try:
        r = requests.get(url, timeout=5)
        return r.json() if r.status_code == 200 else None
    except: return None

# Galería de Animaciones Lottie
lottie_yoga_header = load_lottie("https://lottie.host/9f5064e4-399a-426c-829d-64d898517228/qG4K3nE0H5.json") 
lottie_biodanza = load_lottie("https://lottie.host/807f4340-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")
lottie_ia_brain = load_lottie("https://lottie.host/07as9pva-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")

# ==========================================
# 2. SISTEMA DE DISEÑO (CSS CORREGIDO Y BLINDADO)
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@900&family=Quicksand:wght@400;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #fdfaf6 0%, #e9edc9 100%);
        background-attachment: fixed;
    }
    
    .main .block-container {
        padding-top: 4rem !important;
        max-width: 95% !important;
    }

    /* TÍTULO FAYOGA: SÓLIDO Y LEGIBLE */
    .brand-title {
        font-family: 'Playfair Display', serif;
        font-size: clamp(5rem, 15vw, 10rem) !important;
        color: #2D4030 !important; /* Verde oscuro sólido */
        text-align: center;
        line-height: 0.8;
        font-weight: 900;
        margin-bottom: 0px;
        margin-top: -10px;
        text-shadow: 2px 4px 10px rgba(0,0,0,0.15); /* Sombra elegante */
    }

    .brand-subtitle {
        font-family: 'Quicksand', sans-serif;
        font-size: clamp(1.2rem, 3vw, 2.2rem) !important;
        text-align: center;
        color: #4A5D4E !important;
        font-weight: 600;
        letter-spacing: 12px;
        text-transform: uppercase;
        margin-top: 15px;
        margin-bottom: 30px;
    }

    /* CORRECCIÓN MENÚ MÓVIL (TABS) - AHORA SE ADAPTAN HACIA ABAJO */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        justify-content: center;
        flex-wrap: wrap; /* Clave para que en móviles no se corte */
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 1.3rem !important;
        font-family: 'Quicksand', sans-serif !important;
        font-weight: 700 !important;
        color: #4A5D4E !important;
        padding: 10px 15px;
        background: rgba(255,255,255,0.4);
        border-radius: 10px 10px 0 0;
    }
    .stTabs [aria-selected="true"] {
        background: rgba(255,255,255,0.8);
        border-bottom: 4px solid #6B8E23 !important;
        color: #2D4030 !important;
    }

    /* TARJETAS PREMIUM - PADDING REDUCIDO PARA NO CORTAR TEXTO */
    .premium-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(20px);
        border-radius: 30px;
        padding: 35px; /* Reducido de 60px a 35px */
        border: 2px solid #A3B18A;
        box-shadow: 0 15px 35px rgba(0,0,0,0.08);
        margin-bottom: 25px;
    }
    
    /* SUBTÍTULOS Y TEXTOS - CONTRASTE OBLIGATORIO */
    h2, h3, h4 { color: #2D4030 !important; font-family: 'Playfair Display', serif !important; font-weight: 900 !important; }
    p, li, label, div.stMarkdown { 
        font-size: 1.15rem !important; 
        color: #1A1A1A !important; 
        font-family: 'Quicksand', sans-serif !important; 
        font-weight: 600 !important;
        line-height: 1.6 !important;
    }

    /* BOTONES */
    .stButton>button {
        background: linear-gradient(45deg, #4A5D4E 0%, #6B8E23 100%);
        color: white !important;
        border-radius: 50px !important;
        border: none !important;
        padding: 15px 35px !important;
        font-weight: 700 !important;
        font-size: 1.3rem !important;
        width: 100% !important;
        box-shadow: 0 10px 20px rgba(107, 142, 35, 0.2) !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover { transform: translateY(-3px) !important; box-shadow: 0 15px 25px rgba(107, 142, 35, 0.4) !important; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. HEADER (LOGO + ICONO)
# ==========================================
c_logo_1, c_logo_2, c_logo_3 = st.columns([1, 2, 1])
with c_logo_2:
    if lottie_yoga_header: 
        st_lottie(lottie_yoga_header, height=160, key="header_icon")
    st.markdown("<h1 class='brand-title'>FAYOGA</h1>", unsafe_allow_html=True)
    st.markdown("<p class='brand-subtitle'>Fabiola Pastén</p>", unsafe_allow_html=True)

# ==========================================
# 4. SISTEMA DE NAVEGACIÓN
# ==========================================
tabs = st.tabs(["💎 Dashboard", "🎓 YogaDoc Learning", "💃 Biodanza Flow", "👥 Alumnos", "🤖 FABI IA"])

with tabs[0]: # DASHBOARD
    st.markdown("## Bienvenida al Universo Fayoga")
    col_d1, col_d2 = st.columns([1.2, 1]) # Damos un poco más de espacio al texto
    with col_d1:
        st.markdown("""<div class='premium-card'>
            <h3>La Evolución del Bienestar</h3>
            <p>Fayoga trasciende la clase de yoga tradicional para convertirse en un sistema de aprendizaje integral. Navega por nuestros módulos interactivos, avanza a tu ritmo y descubre una nueva forma de conectar cuerpo, mente y comunicación.</p>
        </div>""", unsafe_allow_html=True)
    with col_d2:
        st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=1200", use_container_width=True, caption="Tu espacio de paz.")

with tabs[1]: # YOGADOC
    st.markdown("## YogaDoc: Progresión de Conciencia")
    
    nivel = st.select_slider("Selecciona tu Nivel", options=[i for i in range(1, 12)], 
                            format_func=lambda x: f"Nivel {x}" if x <= 10 else "💎 MODO PREMIUM")
    
    if nivel <= 10:
        ejercicios = {
            1: ("Respiración Primordial", "Iniciación al silencio mental. Aprende a controlar el diafragma.", "https://images.unsplash.com/photo-1506126613408-eca07ce68773"),
            2: ("Alineación Ósea", "Conexión con la estructura física para evitar lesiones.", "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b"),
            3: ("Fluidez Vinyasa", "El arte de transitar entre asanas con gracia.", "https://images.unsplash.com/photo-1599447421416-3414500d18a5"),
            4: ("Resonancia Vocal", "Uso del sonido para liberar tensiones acumuladas.", "https://images.unsplash.com/photo-1512438248247-f0f2a5a8b7f0"),
            5: ("Equilibrio Estático", "Encontrar el centro absoluto en la quietud.", "https://images.unsplash.com/photo-1510894347713-fc3ed6fdf539"),
            6: ("Biodanza Matinal", "Movimiento rítmico para despertar la energía vital.", "https://images.unsplash.com/photo-1518310383802-640c2de311b2"),
            7: ("Pranayama Avanzado", "Control profundo de los flujos de energía.", "https://images.unsplash.com/photo-1499209974431-9dac3adaf471"),
            8: ("Yoga de los Sentidos", "Exploración consciente de tu entorno.", "https://images.unsplash.com/photo-1524633212363-36dd03f0dd2e"),
            9: ("Meditación Periodística", "Análisis crítico y limpieza del ruido mental.", "https://images.unsplash.com/photo-1474418397713-7ded018049ce"),
            10: ("Integración Fayoga", "La maestría de todos los elementos unificados.", "https://images.unsplash.com/photo-1447452001602-7090c7ab2db3")
        }
        titulo, desc, img = ejercicios[nivel]
        
        col_ex1, col_ex2 = st.columns([1.3, 1])
        with col_ex1:
            st.markdown(f"""<div class='premium-card'>
                <h3>Nivel {nivel}: {titulo}</h3>
                <p>{desc}</p>
                <hr style="border-color: #A3B18A;">
                <p style="font-size: 0.9rem !important;"><i>Completa este ejercicio práctico para avanzar en tu ruta de bienestar.</i></p>
            </div>""", unsafe_allow_html=True)
            
            if st.button(f"🚀 Iniciar Práctica: {titulo}"):
                bar = st.progress(0)
                status = st.empty()
                for i in range(101):
                    msg = "Inhala profundamente..." if i < 50 else "Exhala y relaja..."
                    status.markdown(f"**{msg}**")
                    bar.progress(i)
                    time.sleep(0.04)
                st.success(f"¡Nivel {nivel} Superado! Tu mente está más clara.")
        with col_ex2:
            st.image(f"{img}?auto=format&fit=crop&w=800", use_container_width=True)

    else:
        st.markdown("""<div class='premium-card' style='text-align: center; border: 4px solid #6B8E23; background: rgba(255,255,255,0.95);'>
            <h2 style='color: #2D4030 !important;'>💎 MODO PREMIUM DESBLOQUEADO</h2>
            <p>Has completado la formación de 10 niveles. 
            El modo Premium te da acceso a clases Live con Fabiola, biblioteca infinita y consultoría IA.</p>
        </div>""", unsafe_allow_html=True)
        st.button("✨ OBTENER MEMBRESÍA PREMIUM ✨")

with tabs[2]: # BIODANZA FLOW
    st.markdown("## Biodanza: La Danza de la Vida")
    c_b1, c_b2 = st.columns([1.5, 1])
    with c_b1:
        st.markdown("""<div class='premium-card'>
            <h4>Afectividad y Movimiento Rítmico</h4>
            <p>El sistema de integración grupal de Fabiola Pastén. Recupera la alegría de vivir a través del ritmo, reconectando con tu esencia y con la comunidad mediante ejercicios guiados.</p>
        </div>""", unsafe_allow_html=True)
    with c_b2:
        if lottie_biodanza: st_lottie(lottie_biodanza, height=250)

with tabs[3]: # ALUMNOS
    st.markdown("## Comunidad Fayoga")
    st.write("Conoce el progreso de nuestros alumnos en la academia.")
    
    # Simulación lista grande
    nombres = ["Rodrigo Godoy", "Fabiola Pastén", "María José R.", "Carlos Rivera", "Ana Silva", 
               "Pedro Morales", "Lucía Soto", "Javier Díaz", "Camila Rojas", "Diego Vega", 
               "Valentina Cruz", "Mateo Ríos", "Sofía Lagos", "Benjamín Ortiz", "Martina Peña"]
    niveles = [8, 11, 3, 5, 2, 10, 7, 4, 1, 9, 6, 2, 8, 5, 11]
    membresias = ["Premium", "Staff", "Gratuito", "Live", "Gratuito", "Premium", "Live", "Gratuito", "Gratuito", "Live", "Premium", "Gratuito", "Live", "Gratuito", "Premium"]
    
    df_alumnos = pd.DataFrame({"Alumno": nombres, "Nivel Alcanzado": niveles, "Plan Actual": membresias})
    st.dataframe(df_alumnos, use_container_width=True, height=400)

with tabs[4]: # FABI IA
    st.markdown("## FABI IA Asesora")
    col_ia1, col_ia2 = st.columns([1, 2])
    with col_ia1:
        if lottie_ia_brain: st_lottie(lottie_ia_brain, height=300)
    with col_ia2:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        st.markdown("<h4>Consulta a tu mentora virtual</h4>", unsafe_allow_html=True)
        pregunta = st.text_input("¿En qué área de tu bienestar necesitas ayuda hoy?")
        if st.button("Consultar a FABI Expert"):
            st.success(f"**FABI responde:** Para tu consulta sobre '{pregunta}', te recomiendo respirar hondo y revisar el Nivel 3 de YogaDoc. La fluidez física te ayudará a destrabar la tensión mental.")
        st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 5. FOOTER: CONSEJOS PRÁCTICOS
# ==========================================
st.markdown("""
<div style='background: #2D4030; color: #E9EDC9; padding: 40px 20px; border-radius: 30px; text-align: center; margin-top: 60px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);'>
    <h3 style='color: #E9EDC9 !important; font-family: "Playfair Display", serif;'>🌿 El Consejo Práctico de Fayoga</h3>
    <p style='color: #E9EDC9 !important; font-size: 1.3rem !important; max-width: 800px; margin: auto;'>
        La respiración es el puente entre la mente y el cuerpo. Si te sientes abrumado hoy en <b>La Serena</b> o en cualquier lugar del mundo, detente un momento. 
        Inhala en 4 tiempos, retén en 4 tiempos, y exhala en 4 tiempos. El equilibrio siempre comienza desde adentro.
    </p>
    <hr style='border-color: #4A5D4E; margin: 30px 0;'>
    <p style='color: #A3B18A !important; font-size: 1rem !important; font-weight: 400 !important;'>
        © 2026 Fayoga Academy | Wellness SaaS Premium desarrollado para Fabiola Pastén | La Serena, Chile
    </p>
</div>
""", unsafe_allow_html=True)
