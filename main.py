import streamlit as st
import requests
from streamlit_lottie import st_lottie

# 1. Configuración de Marca y SEO
st.set_page_config(page_title="Fayoga | Fabiola Pastén", page_icon="🧘‍♀️", layout="wide")

# Función para cargar animaciones livianas (Lottie)
def load_lottieurl(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

# Iconos en movimiento (Wellness & Yoga)
lottie_yoga = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_96bovdur.json")
lottie_wellness = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_07as9pva.json")

# 2. Estilo CSS para que se vea "Hermoso y Liviano"
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;500&display=swap');
    html, body, [class*="css"] { font-family: 'Quicksand', sans-serif; background-color: #fdfaf6; }
    .expert-card {
        background: white; padding: 25px; border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-left: 10px solid #A3B18A;
    }
    .stButton>button { background-color: #6b8e23; color: white; border-radius: 25px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Header: El Perfil de Fabiola Pastén
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("🧘‍♀️ Fayoga")
        st.subheader("Fabiola Pastén")
        st.markdown("""
        **Periodista · Comunicadora · Experta en Wellness, Yoga y Biodanza**
        
        Una plataforma diseñada para la reconexión profunda. Aquí, la comunicación consciente 
        se une con el movimiento sanador para ofrecer una experiencia de bienestar de clase mundial.
        """)
    with col2:
        st_lottie(lottie_yoga, height=200, key="yoga_main")

st.divider()

# 4. Secciones con Lógica SEO y Wellness Top
tabs = st.tabs(["✨ Disciplinas", "💃 Biodanza", "📚 Hemeroteca Top", "📅 Agenda"])

with tabs[0]: # Yoga & Wellness
    st.markdown("### Yoga & Bienestar Integral")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class='expert-card'>
        <h4>Práctica Consciente</h4>
        <p>Sesiones de Hatha y Vinyasa Flow que equilibran el sistema nervioso. 
        Enfoque en la biomecánica y la paz mental.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st_lottie(lottie_wellness, height=200)

with tabs[1]: # Biodanza
    st.markdown("### Biodanza: El Arte de Vivir")
    st.write("Fabiola utiliza el sistema de **Biodanza** para promover la integración afectiva y el despliegue de las potencialidades humanas a través de la música y la danza grupal.")
    st.image("https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=800", caption="Conexión y Movimiento")

with tabs[2]: # Hemeroteca (Perfil Periodista)
    st.markdown("### 📚 Hemeroteca Wellness Mundial")
    st.info("Curaduría periodística de lo mejor del mundo del Yoga y el bienestar global.")
    
    col_h1, col_h2, col_h3 = st.columns(3)
    with col_h1:
        st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=400")
        st.caption("Tendencias: El Yoga en la Neurociencia")
    with col_h2:
        st.image("https://images.unsplash.com/photo-1599447421416-3414500d18a5?auto=format&fit=crop&w=400")
        st.caption("Mindfulness y Comunicación No Violenta")
    with col_h3:
        st.image("https://images.unsplash.com/photo-1512438248247-f0f2a5a8b7f0?auto=format&fit=crop&w=400")
        st.caption("Well-being Corporativo: El futuro del trabajo")

with tabs[3]: # Reservas
    st.markdown("### Reserva tu Sesión")
    with st.form("reserva"):
        nombre = st.text_input("Nombre")
        interes = st.multiselect("Interés", ["Yoga", "Biodanza", "Wellness Coaching"])
        if st.form_submit_button("Solicitar Información"):
            st.balloons()
            st.success(f"¡Gracias {nombre}! Fabiola te contactará pronto.")

# 5. Footer liviano
st.markdown("<hr><p style='text-align: center;'>Fayoga 2026 | Wellness de Clase Mundial por Fabiola Pastén</p>", unsafe_allow_html=True)
