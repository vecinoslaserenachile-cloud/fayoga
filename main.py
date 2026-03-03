import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pandas as pd
import time

# ==========================================
# 1. NÚCLEO Y SESIÓN
# ==========================================
st.set_page_config(page_title="Fayoga Academy", page_icon="🧘‍♀️", layout="wide", initial_sidebar_state="collapsed")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = "Invitado"

# Cargador de Animaciones (Lottie)
def load_lottie(url: str):
    try:
        r = requests.get(url, timeout=5)
        return r.json() if r.status_code == 200 else None
    except: return None

lottie_logo = load_lottie("https://lottie.host/807f4340-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json") 
lottie_yoga_flow = load_lottie("https://lottie.host/9f5064e4-399a-426c-829d-64d898517228/qG4K3nE0H5.json") 
lottie_dance = load_lottie("https://lottie.host/0a9f5d34-d9ae-44d5-83e8-8a033b0067b5/7L6A0G0U0V.json") 
lottie_ia = load_lottie("https://lottie.host/07as9pva-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")

# ==========================================
# 2. DISEÑO AVANZADO (GLASSMORPHISM Y CONTRASTE)
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@900&family=Quicksand:wght@400;600;700&display=swap');
    
    .stApp { background: linear-gradient(135deg, #fdfaf6 0%, #e9edc9 100%); background-attachment: fixed; }
    .main .block-container { padding-top: 3rem !important; max-width: 95% !important; }

    /* FAYOGA: EL LOGO GIGANTE */
    .brand-title {
        font-family: 'Playfair Display', serif; font-size: clamp(5rem, 15vw, 10rem) !important;
        color: #2D4030 !important; text-align: center; line-height: 0.8; font-weight: 900; margin-bottom: 0px;
        text-shadow: 2px 5px 15px rgba(0,0,0,0.1);
    }
    .brand-subtitle {
        font-family: 'Quicksand', sans-serif; font-size: clamp(1.2rem, 3vw, 2.2rem) !important;
        text-align: center; color: #6B8E23 !important; font-weight: 700; letter-spacing: 12px; 
        margin-top: 15px; text-transform: uppercase;
    }

    /* TARJETAS PREMIUM (VERDE OSCURO + TEXTO BLANCO) */
    .premium-card {
        background: #2D4030; border-radius: 35px; padding: 40px; border: 2px solid #A3B18A;
        box-shadow: 0 20px 40px rgba(0,0,0,0.15); margin-bottom: 30px;
    }
    .premium-card h2, .premium-card h3, .premium-card h4 { color: #FFFFFF !important; font-family: 'Playfair Display', serif !important; }
    .premium-card p, .premium-card li { color: #FDF9F3 !important; font-family: 'Quicksand', sans-serif !important; font-size: 1.25rem !important; line-height: 1.6; }

    /* BOTONERA CRISTALINA Y ANCHA (TABS) */
    .stTabs [data-baseweb="tab-list"] { 
        gap: 20px; justify-content: center; flex-wrap: wrap; 
        background: rgba(255, 255, 255, 0.2); backdrop-filter: blur(15px);
        padding: 15px; border-radius: 25px; border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    }
    .stTabs [data-baseweb="tab"] { 
        font-size: 1.4rem !important; font-family: 'Quicksand', sans-serif !important; font-weight: 700 !important; 
        color: #2D4030 !important; background: rgba(255, 255, 255, 0.6);
        padding: 15px 35px !important; border-radius: 20px !important; transition: all 0.3s ease;
    }
    .stTabs [aria-selected="true"] { 
        background: linear-gradient(45deg, #6B8E23 0%, #A3B18A 100%) !important; color: white !important;
        transform: scale(1.05); box-shadow: 0 10px 20px rgba(107, 142, 35, 0.3) !important; border-bottom: none !important;
    }

    /* IMÁGENES CON ESTILO */
    img { border-radius: 25px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); margin-bottom: 20px; }

    /* BOTONES INTERNOS */
    .stButton>button {
        background: linear-gradient(45deg, #6B8E23 0%, #A3B18A 100%); color: white !important; 
        border-radius: 50px !important; border: none !important; padding: 18px 40px !important; 
        font-weight: 700 !important; font-size: 1.3rem !important; width: 100% !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. HEADER MAJESTUOSO Y RADIO
# ==========================================
c_logo_1, c_logo_2, c_logo_3 = st.columns([1, 2, 1])
with c_logo_2:
    if lottie_logo: st_lottie(lottie_logo, height=150, key="header_anim")
    st.markdown("<h1 class='brand-title'>FAYOGA</h1>", unsafe_allow_html=True)
    st.markdown("<p class='brand-subtitle'>Fabiola Pastén</p>", unsafe_allow_html=True)

st.divider()

with st.expander("📻 Radio Fayoga: Sintoniza tu Frecuencia antes de iniciar"):
    pistas_radio = {"🌿 Despertar Zen": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "💧 Flujo de Vinyasa": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"}
    st.audio(pistas_radio[st.selectbox("🎵 Selecciona la vibra:", list(pistas_radio.keys()))], format="audio/mp3")

# ==========================================
# 4. NAVEGACIÓN Y CONTENIDO TOTAL
# ==========================================
tabs = st.tabs(["💎 Inicio", "🎓 YogaDoc Learning", "💃 Biodanza Flow", "🤖 FABI IA", "🔐 Mi Cuenta (VIP)"])

with tabs[0]: # DASHBOARD CON FOTOS REALES (Reemplazando placeholders)
    st.markdown("## Bienvenido al Universo Fayoga")
    st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=1600&q=80", use_container_width=True, caption="La integración perfecta entre cuerpo, mente y entorno.")
    
    col_d1, col_d2, col_d3 = st.columns(3)
    with col_d1:
        st.markdown("""<div class='premium-card'><h3>Yoga Integral</h3><p>Alineación y paz mental con el rigor comunicacional de Fabiola. Sesiones 1:1 y grupales.</p></div>""", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1599447421416-3414500d18a5?auto=format&fit=crop&w=600&q=80", use_container_width=True)

    with col_d2:
        st.markdown("""<div class='premium-card'><h3>Biodanza</h3><p>Integración afectiva y renovación vital a través del movimiento orgánico y la música.</p></div>""", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1518310383802-640c2de311b2?auto=format&fit=crop&w=600&q=80", use_container_width=True)
        
    with col_d3:
        st.markdown("""<div class='premium-card'><h3>Wellness Pro</h3><p>Consultoría en bienestar corporativo y comunicación consciente para instituciones.</p></div>""", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1512438248247-f0f2a5a8b7f0?auto=format&fit=crop&w=600&q=80", use_container_width=True)

with tabs[1]: # YOGADOC: 10 NIVELES
    st.markdown("## YogaDoc: Tu Ruta de Aprendizaje (1 al 10)")
    nivel = st.slider("Desliza para explorar tu nivel:", 1, 10, 1)
    
    ejercicios = {
        1: ("Respiración Diafragmática", "🧘‍♀️ Sentado. Inhala 4s expandiendo barriga, exhala 6s contrayendo."),
        2: ("Enraizamiento Tadasana", "🧍‍♂️ De pie. Siente las 4 esquinas de tus pies ancladas al suelo."),
        3: ("Despertar Vinyasa", "🌊 Movimiento continuo. Sincroniza brazos arriba al inhalar, plégate al exhalar."),
        4: ("Apertura de Corazón", "🐍 Tumbado boca abajo. Eleva el pecho suavemente (Cobra)."),
        5: ("Equilibrio del Árbol", "🌳 De pie sobre una pierna. Encuentra tu centro visual y físico."),
        6: ("Torsión Detox", "🪢 Sentado. Gira tu torso desde la base de la columna al exhalar."),
        7: ("Inversión Suave", "🧱 Piernas en la pared. Acuéstate y eleva las piernas para el retorno venoso."),
        8: ("Pranayama de Fuego", "🔥 Sentado. Respiración rápida bombeando el ombligo (No de noche)."),
        9: ("Meditación Caminando", "🚶‍♀️ De pie. Caminata muy lenta y plenamente consciente."),
        10: ("Integración Total", "🛌 Acostado boca arriba (Savasana). No hagas nada. Solo integra.")
    }
    titulo, instruccion = ejercicios[nivel]
    
    col_y1, col_y2 = st.columns([1.5, 1])
    with col_y1:
        st.markdown(f"""<div class='premium-card'>
            <h3>Nivel {nivel}: {titulo}</h3>
            <p>{instruccion}</p>
        </div>""", unsafe_allow_html=True)
        if st.button(f"▶️ Iniciar Práctica Nivel {nivel}"):
            bar = st.progress(0)
            for i in range(101):
                bar.progress(i)
                time.sleep(0.03)
            st.success(f"¡Nivel {nivel} completado con éxito!")
    with col_y2:
        if lottie_yoga_flow: st_lottie(lottie_yoga_flow, height=350)

with tabs[2]: # BIODANZA FLOW CLASIFICADO
    st.markdown("## Biodanza Flow: Secuencias por Etapa")
    categoria = st.radio("Selecciona tu grupo:", ["💃 Adultos", "🪑 Adulto Mayor", "🧸 Infantil"], horizontal=True)
    
    c_b1, c_b2 = st.columns([1.5, 1])
    with c_b1:
        secuencia = "Marcha, Coordinación, Fluidez, Encuentro, Ronda final." if "Adultos" in categoria else "Despertar articular, Balanceo, Caminata, Expresión de brazos, Gratitud." if "Mayor" in categoria else "Juego animal, Saltos, Vuelo libre, Descanso en nido, Abrazo."
        st.markdown(f"""<div class='premium-card'>
            <h3>Secuencia {categoria}</h3>
            <p>Sigue el ritmo: {secuencia}</p>
        </div>""", unsafe_allow_html=True)
    with c_b2:
        if lottie_dance: st_lottie(lottie_dance, height=250)

with tabs[3]: # FABI IA Y PASTILLAS
    st.markdown("## FABI IA Asesora")
    st.write("Selecciona una consulta rápida:")
    p1, p2, p3 = st.columns(3)
    if p1.button("😴 Insomnio"): st.success("FABI: Te recomiendo el Nivel 10 (Savasana) y la pista 'Despertar Zen' suave.")
    if p2.button("🔋 Fatiga"): st.success("FABI: El Nivel 3 (Vinyasa) despertará tu sistema nervioso al instante.")
    if p3.button("💥 Estrés"): st.success("FABI: Haz el Nivel 1 (Respiración) por 3 minutos ahora mismo.")

    col_ia1, col_ia2 = st.columns([1, 2])
    with col_ia1:
        if lottie_ia: st_lottie(lottie_ia, height=250)
    with col_ia2:
        st.markdown("<div class='premium-card'><h3>O describe cómo te sientes:</h3></div>", unsafe_allow_html=True)
        if st.button("Consultar a FABI Expert"):
            st.info("**FABI:** Evaluando tu energía... Explora la meditación caminando (Nivel 9).")

with tabs[4]: # LOGIN VIP
    st.markdown("## Zona de Alumnos (VIP)")
    col_log1, col_log2, col_log3 = st.columns([1, 2, 1])
    with col_log2:
        if not st.session_state.logged_in:
            st.markdown("""<div class='premium-card'>
                <h3>Accede a tu cuenta</h3>
                <p>Inicia sesión para desbloquear seguimiento y clases Live.</p>
            </div>""", unsafe_allow_html=True)
            usuario = st.text_input("Usuario")
            if st.button("Ingresar a mi portal"):
                if usuario:
                    st.session_state.logged_in = True
                    st.session_state.username = usuario
                    st.rerun()
        else:
            st.markdown(f"""<div class='premium-card'>
                <h3>Bienvenido de vuelta, {st.session_state.username}</h3>
                <p>Tu pase Premium está activo.</p>
            </div>""", unsafe_allow_html=True)
            if st.button("Cerrar Sesión"):
                st.session_state.logged_in = False
                st.rerun()

# FOOTER
st.markdown("<br><hr><p style='text-align: center; opacity: 0.6;'>FAYOGA 2026 | Wellness SaaS Premium por Fabiola Pastén</p>", unsafe_allow_html=True)
