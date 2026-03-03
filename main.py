import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pandas as pd
import time
from datetime import date

# ==========================================
# 1. NÚCLEO Y MEMORIA DE SESIÓN (LOGIN Y NIVELES)
# ==========================================
st.set_page_config(page_title="Fayoga Academy", page_icon="🧘‍♀️", layout="wide", initial_sidebar_state="collapsed")

# Inicializar variables de sesión (Memoria de la App)
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'nivel_actual' not in st.session_state:
    st.session_state.nivel_actual = 1
if 'plan' not in st.session_state:
    st.session_state.plan = "Gratuito"

def load_lottie(url: str):
    try:
        r = requests.get(url, timeout=5)
        return r.json() if r.status_code == 200 else None
    except: return None

# Animaciones
lottie_yoga_header = load_lottie("https://lottie.host/9f5064e4-399a-426c-829d-64d898517228/qG4K3nE0H5.json") 
lottie_dance_1 = load_lottie("https://lottie.host/807f4340-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json") # Animación rítmica
lottie_dance_2 = load_lottie("https://lottie.host/0a9f5d34-d9ae-44d5-83e8-8a033b0067b5/7L6A0G0U0V.json") # Animación flujo
lottie_diploma = load_lottie("https://lottie.host/07as9pva-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json") # Simulación trofeo/diploma

# ==========================================
# 2. SISTEMA DE DISEÑO (TEXTO BLANCO SOBRE VERDE)
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@900&family=Quicksand:wght@400;600;700&display=swap');
    
    .stApp { background: linear-gradient(135deg, #fdfaf6 0%, #e9edc9 100%); background-attachment: fixed; }
    .main .block-container { padding-top: 3rem !important; max-width: 95% !important; }

    /* FAYOGA MAJESTUOSO */
    .brand-title {
        font-family: 'Playfair Display', serif; font-size: clamp(4rem, 12vw, 8rem) !important;
        color: #2D4030 !important; text-align: center; line-height: 0.8; font-weight: 900; margin-bottom: 0px;
    }
    .brand-subtitle {
        font-family: 'Quicksand', sans-serif; font-size: clamp(1.2rem, 3vw, 2rem) !important;
        text-align: center; color: #4A5D4E !important; font-weight: 700; letter-spacing: 10px; margin-top: 15px;
    }

    /* TARJETAS PREMIUM: VERDE OSCURO CON TEXTO BLANCO INMACULADO */
    .premium-card {
        background: #2D4030; /* Verde oscuro elegante */
        border-radius: 30px;
        padding: 40px;
        border: 2px solid #A3B18A;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        margin-bottom: 25px;
    }
    
    /* FORZAR TEXTO BLANCO EN LAS TARJETAS */
    .premium-card h2, .premium-card h3, .premium-card h4 { color: #FFFFFF !important; font-family: 'Playfair Display', serif !important; }
    .premium-card p, .premium-card li, .premium-card span, .premium-card div { 
        color: #FDF9F3 !important; /* Blanco hueso para no cansar la vista */
        font-family: 'Quicksand', sans-serif !important; 
        font-size: 1.2rem !important;
    }

    /* BOTONES */
    .stButton>button {
        background: linear-gradient(45deg, #6B8E23 0%, #A3B18A 100%);
        color: white !important; border-radius: 50px !important; border: none !important;
        padding: 15px 35px !important; font-weight: 700 !important; font-size: 1.2rem !important; width: 100% !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover { transform: translateY(-3px) !important; box-shadow: 0 15px 25px rgba(107, 142, 35, 0.4) !important; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. HEADER
# ==========================================
c_logo_1, c_logo_2, c_logo_3 = st.columns([1, 2, 1])
with c_logo_2:
    if lottie_yoga_header: st_lottie(lottie_yoga_header, height=120, key="header_icon")
    st.markdown("<h1 class='brand-title'>FAYOGA</h1>", unsafe_allow_html=True)
    st.markdown("<p class='brand-subtitle'>Fabiola Pastén</p>", unsafe_allow_html=True)

st.divider()

# ==========================================
# 4. SISTEMA DE LOGIN SIMULADO
# ==========================================
if not st.session_state.logged_in:
    col_login1, col_login2, col_login3 = st.columns([1, 2, 1])
    with col_login2:
        st.markdown("<div class='premium-card' style='text-align: center;'>", unsafe_allow_html=True)
        st.markdown("<h3>Bienvenido a Fayoga Academy</h3>", unsafe_allow_html=True)
        st.markdown("<p>Ingresa tus datos para acceder a tu plataforma de bienestar.</p>", unsafe_allow_html=True)
        
        usuario_input = st.text_input("Usuario / Email", placeholder="Escribe cualquier cosa...")
        pass_input = st.text_input("Contraseña", type="password", placeholder="Escribe cualquier clave...")
        plan_input = st.selectbox("Simular Membresía", ["Gratuito", "Live", "Premium"])
        
        if st.button("Ingresar a la Academia"):
            if usuario_input:
                st.session_state.logged_in = True
                st.session_state.username = usuario_input
                st.session_state.plan = plan_input
                st.rerun() # Recarga la página para mostrar el dashboard
            else:
                st.warning("Por favor, ingresa un usuario válido.")
        st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 5. PLATAFORMA (SOLO VISIBLE SI ESTÁ LOGUEADO)
# ==========================================
else:
    # Radio Fayoga Integrada
    with st.expander("📻 Radio Fayoga: Sintoniza tu Frecuencia"):
        pistas_radio = {
            "🌿 1. Despertar Zen": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
            "💧 2. Flujo de Vinyasa": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
        }
        tema_elegido = st.selectbox("🎵 Selecciona la vibra:", list(pistas_radio.keys()))
        st.audio(pistas_radio[tema_elegido], format="audio/mp3")

    tabs = st.tabs(["💎 Mi Dashboard", "🎓 YogaDoc Learning", "💃 Biodanza Flow", "👥 Alumnos", "⚙️ Salir"])

    with tabs[0]: # DASHBOARD PERSONALIZADO
        st.markdown(f"## Hola, {st.session_state.username}")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"""<div class='premium-card'>
                <h3>Tu Estado Actual</h3>
                <p><b>Membresía:</b> Nivel {st.session_state.plan}</p>
                <p><b>Nivel YogaDoc:</b> {st.session_state.nivel_actual} / 10</p>
            </div>""", unsafe_allow_html=True)
        with c2:
            st.markdown("""<div class='premium-card'>
                <h3>Próxima Clase Live</h3>
                <p>Viernes 19:00 hrs<br>Enfoque: Alineación de Chakras</p>
            </div>""", unsafe_allow_html=True)
        with c3:
            st.markdown("""<div class='premium-card'>
                <h3>Estadísticas</h3>
                <p>Horas de práctica: 12 hrs<br>Meditaciones completadas: 5</p>
            </div>""", unsafe_allow_html=True)

    with tabs[1]: # YOGADOC: AVANCE POR BOTONES HASTA EL DIPLOMA
        st.markdown("## YogaDoc: Tu Ruta de Aprendizaje")
        
        nivel = st.session_state.nivel_actual
        
        ejercicios = {
            1: "Respiración Primordial: Control del diafragma.",
            2: "Alineación Ósea: Postura base y enraizamiento.",
            3: "Fluidez Vinyasa: Movimiento continuo.",
            4: "Resonancia Vocal: Uso del sonido OM.",
            5: "Equilibrio Estático: El árbol y la quietud.",
            6: "Biodanza Matinal: Despertar el cuerpo.",
            7: "Pranayama Avanzado: Retención de aire.",
            8: "Yoga Sensorial: Ojos cerrados.",
            9: "Meditación Periodística: Observar sin juzgar.",
            10: "Integración Fayoga: Flujo Maestro."
        }
        
        col_y1, col_y2 = st.columns([1.5, 1])
        with col_y1:
            if nivel <= 10:
                st.markdown(f"""<div class='premium-card'>
                    <h3>Módulo {nivel}: {ejercicios[nivel].split(':')[0]}</h3>
                    <p>{ejercicios[nivel].split(':')[1]}</p>
                    <hr style="border-color: #A3B18A;">
                    <p>Completa el ejercicio práctico para desbloquear el siguiente nivel.</p>
                </div>""", unsafe_allow_html=True)
                
                if st.button(f"✨ Completar Módulo {nivel} y Avanzar"):
                    st.session_state.nivel_actual += 1
                    st.rerun()
            else:
                # DIPLOMA AL LLEGAR AL FINAL
                st.markdown("""<div class='premium-card' style='text-align: center; background: #DAA520; border: none;'>
                    <h2 style='color: white !important;'>🎓 DIPLOMA FAYOGA OBTENIDO</h2>
                    <p style='color: white !important;'>¡Felicidades! Has completado los 10 niveles fundamentales de la Academia. Ahora tienes acceso vitalicio al Modo Premium.</p>
                </div>""", unsafe_allow_html=True)
                if lottie_diploma: st_lottie(lottie_diploma, height=200)
                if st.button("Reiniciar mi camino (Volver al Nivel 1)"):
                    st.session_state.nivel_actual = 1
                    st.rerun()
                    
        with col_y2:
            st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=800", use_container_width=True)

    with tabs[2]: # BIODANZA FLOW CON ANIMACIONES
        st.markdown("## Biodanza Flow")
        c_b1, c_b2 = st.columns([1.2, 1])
        with c_b1:
            st.markdown("""<div class='premium-card'>
                <h3>El Ritmo de la Vida</h3>
                <p>La Biodanza es la poética del encuentro humano. A través de estos ejercicios rítmicos, estimulamos la vitalidad y la conexión afectiva. Sigue los movimientos de las animaciones para entrar en sintonía con tu grupo.</p>
            </div>""", unsafe_allow_html=True)
        with c_b2:
            # Varias animaciones simulando movimiento/baile al costado derecho
            if lottie_dance_1: st_lottie(lottie_dance_1, height=150, key="dance1")
            if lottie_dance_2: st_lottie(lottie_dance_2, height=150, key="dance2")

    with tabs[3]: # ALUMNOS (ACCESO PROTEGIDO)
        st.markdown("## Comunidad de Alumnos Fayoga")
        st.write("Directorio exclusivo para miembros de la academia.")
        df_alumnos = pd.DataFrame({
            "Alumno": ["Rodrigo Godoy", "Fabiola Pastén", st.session_state.username, "Carlos R.", "Ana Silva"],
            "Nivel Alcanzado": [8, 11, st.session_state.nivel_actual, 5, 2],
            "Plan Actual": ["Premium", "Master", st.session_state.plan, "Live", "Gratuito"]
        })
        st.dataframe(df_alumnos, use_container_width=True)

    with tabs[4]: # LOGOUT
        st.markdown("## Configuración de Sesión")
        if st.button("Cerrar Sesión"):
            st.session_state.logged_in = False
            st.rerun()

# FOOTER PRO
st.markdown("<br><hr><p style='text-align: center; opacity: 0.6;'>FAYOGA 2026 | Wellness SaaS Premium por Fabiola Pastén</p>", unsafe_allow_html=True)
