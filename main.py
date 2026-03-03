import streamlit as st
import requests
from streamlit_lottie import st_lottie

# 1. Configuración de Marca y Layout
st.set_page_config(page_title="Fayoga | Fabiola Pastén", page_icon="🧘‍♀️", layout="wide")

# Función segura para animaciones
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except:
        return None

# Carga de recursos visuales livianos
lottie_yoga = load_lottieurl("https://lottie.host/9f5064e4-399a-426c-829d-64d898517228/qG4K3nE0H5.json")
lottie_zen = load_lottieurl("https://lottie.host/807f4340-9a4c-4a37-975a-5942488390b4/vJ2Wd8vL8Y.json")

# 2. Estilo CSS "Relajante y Premium"
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Quicksand', sans-serif;
        background-color: #fdfaf6;
        color: #2d4030;
    }
    .stApp { background-color: #fdfaf6; }
    
    /* Tarjetas de Experto */
    .expert-card {
        background: white;
        padding: 2rem;
        border-radius: 25px;
        box-shadow: 0 10px 30px rgba(107, 142, 35, 0.05);
        border: 1px solid #e9edc9;
        margin-bottom: 1rem;
    }
    
    /* Botones Suaves */
    .stButton>button {
        background-color: #a3b18a;
        color: white;
        border-radius: 30px;
        border: none;
        padding: 0.6rem 2rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #588157;
        transform: translateY(-2px);
    }
    
    /* Header Personalizado */
    .header-text { text-align: center; padding: 2rem 0; }
    </style>
    """, unsafe_allow_html=True)

# 3. Identidad: Fabiola Pastén
with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if lottie_zen: st_lottie(lottie_zen, height=180, key="zen")
        st.markdown("<div class='header-text'><h1>Fayoga</h1><p style='font-size: 1.2rem; font-style: italic;'>By Fabiola Pastén</p></div>", unsafe_allow_html=True)
        st.markdown("""
        <div style='text-align: center;'>
        <b>Periodista · Comunicadora · Expert en Wellness, Yoga & Biodanza</b><br>
        Un espacio diseñado para la integración del cuerpo, la mente y el alma a través de la comunicación consciente.
        </div>
        """, unsafe_allow_html=True)

st.divider()

# 4. Navegación Intuitiva (Estructura de Empresa Top)
tabs = st.tabs(["🧘 Yoga & Bienestar", "💃 Biodanza", "📚 Hemeroteca Mundial", "📅 Agenda Tu Sesión"])

with tabs[0]: # Yoga
    st.markdown("### Disciplinas y Práctica")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class='expert-card'>
        <h4>Yoga Consciente</h4>
        <p>Sesiones personalizadas de Hatha y Vinyasa Flow que priorizan la biomecánica 
        saludable y la calma mental.</p>
        </div>
        """, unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=800")
    with c2:
        if lottie_yoga: st_lottie(lottie_yoga, height=350, key="yoga_main")

with tabs[1]: # Biodanza
    st.markdown("### El Movimiento de la Vida")
    st.write("Como experta en **Biodanza**, Fabiola facilita talleres de integración afectiva, renovando la alegría de vivir a través de la música y la danza.")
    st.video("https://www.youtube.com/watch?v=Ev6LhJ6_X_M") # Clip ilustrativo liviano

with tabs[2]: # Hemeroteca (Perfil Periodístico)
    st.markdown("### Hemeroteca Wellness Mundial")
    st.info("Curaduría periodística de Fabiola Pastén sobre las últimas tendencias globales en salud.")
    
    h1, h2, h3 = st.columns(3)
    with h1:
        st.image("https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=400")
        st.caption("Neurociencia y Meditación en 2026")
    with h2:
        st.image("https://images.unsplash.com/photo-1599447421416-3414500d18a5?auto=format&fit=crop&w=400")
        st.caption("La Biodanza como terapia social")
    with h3:
        st.image("https://images.unsplash.com/photo-1512438248247-f0f2a5a8b7f0?auto=format&fit=crop&w=400")
        st.caption("Wellness Corporativo de Clase Mundial")

with tabs[3]: # Agenda
    st.markdown("### Conectemos")
    with st.container():
        st.markdown("<div class='expert-card'>", unsafe_allow_html=True)
        nombre = st.text_input("Tu Nombre")
        area = st.multiselect("Me interesa:", ["Clases de Yoga", "Talleres de Biodanza", "Comunicación Wellness"])
        if st.button("Enviar Solicitud"):
            st.balloons()
            st.success(f"Gracias, {nombre}. Fabiola se pondrá en contacto contigo pronto.")
        st.markdown("</div>", unsafe_allow_html=True)

# Footer liviano
st.markdown("<br><hr><p style='text-align: center; opacity: 0.6;'>Fayoga 2026 | Innovación en Bienestar</p>", unsafe_allow_html=True)
