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
# 2. DISEÑO AVANZADO (CORRECCIÓN MÓVIL Y UX IA)
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@900&family=Quicksand:wght@400;600;700&display=swap');
    
    /* FONDO GENERAL */
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
        text-align: center; color: #4A5D4E !important; font-weight: 700; letter-spacing: 12px; 
        margin-top: 15px; text-transform: uppercase;
    }

    /* CORRECCIÓN DE CONTRASTE MÓVIL: Títulos generales SIEMPRE verde oscuro */
    h1, h2, h3, h4, h5, h6 { color: #2D4030 !important; font-family: 'Playfair Display', serif !important; }
    p, label { color: #1A1A1A !important; font-family: 'Quicksand', sans-serif !important; }

    /* TARJETAS PREMIUM (Excepción: Aquí adentro todo es blanco) */
    .premium-card {
        background: #2D4030; border-radius: 35px; padding: 40px; border: 2px solid #A3B18A;
        box-shadow: 0 20px 40px rgba(0,0,0,0.15); margin-bottom: 30px; transition: transform 0.3s ease;
    }
    .premium-card:hover { transform: translateY(-5px); }
    .premium-card h2, .premium-card h3, .premium-card h4 { color: #FFFFFF !important; }
    .premium-card p, .premium-card li { color: #FDF9F3 !important; font-size: 1.15rem !important; line-height: 1.6; }

    /* BOTONERA CRISTALINA (TABS) */
    .stTabs [data-baseweb="tab-list"] { 
        gap: 20px; justify-content: center; flex-wrap: wrap; 
        background: rgba(255, 255, 255, 0.2); backdrop-filter: blur(15px);
        padding: 15px; border-radius: 25px; border: 1px solid rgba(255, 255, 255, 0.4);
    }
    .stTabs [data-baseweb="tab"] { 
        font-size: 1.3rem !important; font-weight: 700 !important; color: #2D4030 !important; 
        background: rgba(255, 255, 255, 0.6); padding: 12px 30px !important; border-radius: 20px !important; transition: all 0.3s ease;
    }
    .stTabs [aria-selected="true"] { 
        background: linear-gradient(45deg, #2D4030 0%, #4A5D4E 100%) !important; color: white !important;
        transform: scale(1.05); box-shadow: 0 10px 20px rgba(45, 64, 48, 0.4) !important; border-bottom: none !important;
    }

    /* MEJORAS INTERFAZ FABI IA (Textos y Cajas más grandes) */
    .stTextInput input {
        font-size: 1.25rem !important; 
        padding: 15px !important; 
        border-radius: 15px !important; 
        border: 2px solid #A3B18A !important;
        background: rgba(255,255,255,0.9) !important;
        color: #2D4030 !important;
    }
    .stAlert p {
        font-size: 1.25rem !important; 
        font-weight: 600 !important; 
        line-height: 1.5 !important;
    }

    /* IMÁGENES */
    img { border-radius: 25px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); margin-bottom: 20px; }

    /* BOTONES INTERNOS */
    .stButton>button {
        background: linear-gradient(45deg, #2D4030 0%, #6B8E23 100%); color: white !important; 
        border-radius: 50px !important; border: none !important; padding: 15px 35px !important; 
        font-weight: 700 !important; font-size: 1.2rem !important; width: 100% !important;
        box-shadow: 0 10px 20px rgba(45, 64, 48, 0.3) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. HEADER MAJESTUOSO
# ==========================================
c_logo_1, c_logo_2, c_logo_3 = st.columns([1, 2, 1])
with c_logo_2:
    if lottie_logo: st_lottie(lottie_logo, height=150, key="header_anim")
    st.markdown("<h1 class='brand-title'>FAYOGA</h1>", unsafe_allow_html=True)
    st.markdown("<p class='brand-subtitle'>Fabiola Pastén</p>", unsafe_allow_html=True)

st.divider()

# ==========================================
# RADIO FAYOGA (10 PISTAS)
# ==========================================
col_rad1, col_rad2, col_rad3 = st.columns([1, 2, 1])
with col_rad2:
    st.markdown("<h4 style='text-align: center;'>📻 Radio Fayoga: Sintoniza tu Frecuencia</h4>", unsafe_allow_html=True)
    pistas_radio = {
        "🌿 1. Despertar Zen (Silencio)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", 
        "💧 2. Flujo de Vinyasa (Activo)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
        "🌬️ 3. Respiración Profunda (Paz)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
        "🪷 4. Meditación Loto (Mantras)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",
        "🔥 5. Fuego Interior (Energía)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3",
        "🎋 6. Feng Shui Balance (Naturaleza)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3",
        "🌙 7. Relajación Nocturna (Ondas)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3",
        "💃 8. Biodanza Ritual (Percusión)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3",
        "✨ 9. Conexión Afectiva (Piano)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-9.mp3",
        "🧘‍♀️ 10. Namasté (Cierre Suave)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3"
    }
    tema_elegido = st.selectbox("Elige tu pista:", list(pistas_radio.keys()), label_visibility="collapsed")
    st.audio(pistas_radio[tema_elegido], format="audio/mp3", autoplay=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# 4. NAVEGACIÓN Y CONTENIDO TOTAL
# ==========================================
tabs = st.tabs(["💎 Inicio", "🧘‍♀️ Practiquemos", "✨ Lo que Hago", "🤖 FABI IA", "🔐 Zona VIP"])

with tabs[0]: 
    st.markdown("## Bienvenido al Universo Fayoga")
    st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=1600&q=80", use_container_width=True, caption="Un espacio diseñado desde las emociones para tu bienestar integral.")
    
    col_d1, col_d2, col_d3 = st.columns(3)
    with col_d1:
        st.markdown("<div class='premium-card'><h3>Practiquemos</h3><p>Vinyasa, Yoga en Silla y sesiones terapéuticas enfocadas en liberar dolencias y bloqueos emocionales.</p></div>", unsafe_allow_html=True)
    with col_d2:
        st.markdown("<div class='premium-card'><h3>Lo Que Hago</h3><p>Círculos de mujeres, retiros, festivales, yoga para niños y experiencias empresariales.</p></div>", unsafe_allow_html=True)
    with col_d3:
        st.markdown("<div class='premium-card'><h3>Biodanza</h3><p>Integración afectiva y renovación vital a través del movimiento orgánico y la música.</p></div>", unsafe_allow_html=True)

with tabs[1]: 
    st.markdown("## Practiquemos: Encuentra tu Equilibrio")
    
    c_clas1, c_clas2, c_clas3 = st.columns(3)
    with c_clas1:
        st.markdown("<div class='premium-card'><h4>🌊 Vinyasa Flow</h4><p>Flujo continuo que sincroniza respiración y movimiento. Ideal para liberar tensiones dinámicas.</p></div>", unsafe_allow_html=True)
    with c_clas2:
        st.markdown("<div class='premium-card'><h4>🪑 Yoga en Silla</h4><p>Práctica accesible y gentil, perfecta para pausas activas, adultos mayores o movilidad reducida.</p></div>", unsafe_allow_html=True)
    with c_clas3:
        st.markdown("<div class='premium-card'><h4>❤️ Yoga Terapéutico</h4><p>Clases enfocadas en aliviar el dolor físico trabajando directamente desde la raíz emocional.</p></div>", unsafe_allow_html=True)

    st.divider()
    
    st.markdown("### Simulador Práctico Interactivo (Niveles 1 al 10)")
    nivel = st.slider("Desliza para explorar los niveles del método Fayoga:", 1, 10, 1)
    
    ejercicios = {
        1: ("Respiración Diafragmática", "🧘‍♀️ Postura: Sentado. Inhala 4s expandiendo barriga, exhala 6s contrayendo."),
        2: ("Enraizamiento Tadasana", "🧍‍♂️ Postura: De pie. Siente las 4 esquinas de tus pies ancladas al suelo."),
        3: ("Despertar Vinyasa", "🌊 Postura: Movimiento continuo. Sincroniza brazos arriba al inhalar, plégate al exhalar."),
        4: ("Apertura de Corazón", "🐍 Postura: Tumbado boca abajo. Eleva el pecho suavemente (Cobra)."),
        5: ("Equilibrio del Árbol", "🌳 Postura: De pie sobre una pierna. Encuentra tu centro visual y físico."),
        6: ("Torsión Detox", "🪢 Postura: Sentado. Gira tu torso desde la base de la columna al exhalar."),
        7: ("Inversión Suave", "🧱 Postura: Piernas en la pared. Eleva las piernas para el retorno venoso."),
        8: ("Pranayama de Fuego", "🔥 Postura: Sentado. Respiración rápida bombeando el ombligo."),
        9: ("Meditación Caminando", "🚶‍♀️ Postura: Caminata lenta. Mindfulness en acción plena."),
        10: ("Integración Total (Savasana)", "🛌 Postura: Acostado boca arriba. El nivel maestro. Solo integra.")
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
            status = st.empty()
            for i in range(101):
                status.markdown(f"**{'Concéntrate en el ejercicio...' if i < 50 else 'Mantén y siente los beneficios...'}**")
                bar.progress(i)
                time.sleep(0.04)
            st.success(f"¡Nivel {nivel} Completado con éxito!")
    with col_y2:
        if lottie_yoga_flow: st_lottie(lottie_yoga_flow, height=300)

with tabs[2]: 
    st.markdown("## Lo Que Hago: Experiencias y Emociones")
    
    col_h1, col_h2, col_h3, col_h4 = st.columns(4)
    with col_h1:
        st.markdown("<div class='premium-card'><h4>🎒 Niños</h4><p>Manejo de emociones desde la infancia.</p></div>", unsafe_allow_html=True)
    with col_h2:
        st.markdown("<div class='premium-card'><h4>🥂 Despedidas</h4><p>Rituales de bienestar y conexión.</p></div>", unsafe_allow_html=True)
    with col_h3:
        st.markdown("<div class='premium-card'><h4>⛺ Retiros</h4><p>Inmersiones en la naturaleza.</p></div>", unsafe_allow_html=True)
    with col_h4:
        st.markdown("<div class='premium-card'><h4>🌕 Círculos</h4><p>Sanación femenina y contención.</p></div>", unsafe_allow_html=True)
        
    st.divider()
    
    st.markdown("### Biodanza Flow: Secuencias por Etapa Vital")
    categoria_biodanza = st.radio("Selecciona tu grupo para ver la secuencia adaptada:", 
                                  ["💃 Adultos (Dinámico)", "🪑 Adulto Mayor (Suave)", "🧸 Infantil (Lúdico)"], horizontal=True)
    
    c_b1, c_b2 = st.columns([1.5, 1])
    with c_b1:
        if "Adultos" in categoria_biodanza:
            secuencia = ["1. Marcha sinérgica.", "2. Coordinación rítmica en parejas.", "3. Fluidez y extensión.", "4. Encuentro y mirada.", "5. Ronda final."]
        elif "Mayor" in categoria_biodanza:
            secuencia = ["1. Despertar articular sentados.", "2. Balanceo suave.", "3. Caminata lenta.", "4. Danza de los brazos.", "5. Ronda de gratitud."]
        else:
            secuencia = ["1. El juego de los animales.", "2. Saltos y ritmos rápidos.", "3. Vuelo de pájaros.", "4. El nido (relajación).", "5. Abrazo grupal."]
        
        html_pasos = "".join([f"<li>{paso}</li>" for paso in secuencia])
        st.markdown(f"""<div class='premium-card'>
            <h3>Secuencia: {categoria_biodanza.split(' ')[1]}</h3>
            <p>Sigue estos pasos guiados por la música:</p>
            <ul>{html_pasos}</ul>
        </div>""", unsafe_allow_html=True)
    with c_b2:
        if lottie_dance: st_lottie(lottie_dance, height=250)

with tabs[3]: 
    st.markdown("## FABI IA Asesora: Inteligencia Emocional")
    st.write("Selecciona una 'pastilla' rápida enfocada en tus emociones o escribe tu consulta:")
    
    col_p1, col_p2, col_p3 = st.columns(3)
    if col_p1.button("😴 Insomnio / Ansiedad"):
        st.success("🧠 **FABI IA:** Para la ansiedad nocturna, te recomiendo el Nivel 10 (Savasana) y escuchar la pista 'Despertar Zen' en la radio.")
    if col_p2.button("🔋 Fatiga / Desmotivación"):
        st.success("🧠 **FABI IA:** El 'Vinyasa Flow' o el Nivel 8 (Pranayama de Fuego) despertarán tu energía vital al instante.")
    if col_p3.button("💥 Estrés / Bloqueo"):
        st.success("🧠 **FABI IA:** Haz una pausa ahora. Practica el Nivel 1 (Respiración) en tu silla para reducir el cortisol.")

    st.markdown("<br>", unsafe_allow_html=True)
    
    col_ia1, col_ia2 = st.columns([1, 2])
    with col_ia1:
        if lottie_ia: st_lottie(lottie_ia, height=250)
    with col_ia2:
        st.markdown("<div class='premium-card' style='padding: 30px;'>", unsafe_allow_html=True)
        pregunta = st.text_input("O describe cómo te sientes hoy:", placeholder="Ej: Siento tensión en la espalda baja por tristeza...")
        if st.button("Consultar a FABI Expert"):
            if pregunta:
                st.info(f"**FABI responde:** Evaluando tu inquietud sobre '{pregunta}'... Te sugiero explorar una clase de 'Yoga para Dolencias' enfocada en la liberación emocional y física de esa zona.")
            else:
                st.warning("Escribe cómo te sientes para que pueda ayudarte.")
        st.markdown("</div>", unsafe_allow_html=True)

with tabs[4]: 
    st.markdown("## Zona VIP")
    col_log1, col_log2, col_log3 = st.columns([1, 2, 1])
    with col_log2:
        if not st.session_state.logged_in:
            st.markdown("""<div class='premium-card'>
                <h3>Accede a tu cuenta Premium</h3>
                <p>Inicia sesión para guardar tu progreso, reservar Retiros y acceder a clases Live.</p>
            </div>""", unsafe_allow_html=True)
            usuario = st.text_input("Usuario o Email")
            if st.button("Ingresar a mi portal"):
                if usuario:
                    st.session_state.logged_in = True
                    st.session_state.username = usuario
                    st.rerun()
        else:
            st.markdown(f"""<div class='premium-card'>
                <h3>Bienvenido de vuelta, {st.session_state.username}</h3>
                <p>Tu pase Premium está activo. Tienes acceso a la Hemeroteca privada.</p>
            </div>""", unsafe_allow_html=True)
            if st.button("Cerrar Sesión"):
                st.session_state.logged_in = False
                st.rerun()

# FOOTER
st.markdown("<br><hr><p style='text-align: center; color: #2D4030; font-weight: 600;'>FAYOGA 2026 | Wellness SaaS Premium por Fabiola Pastén</p>", unsafe_allow_html=True)
