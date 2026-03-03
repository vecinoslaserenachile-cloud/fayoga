import streamlit as st
import requests
from streamlit_lottie import st_lottie

# 1. Configuración de Marca y Pantalla
st.set_page_config(page_title="Fayoga | Fabiola Pastén", page_icon="🧘‍♀️", layout="wide")

# Función para animaciones livianas (Lottie)
def load_lottieurl(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

# Carga de iconos en movimiento (Wellness & Yoga)
lottie_zen = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_96bovdur.json")
lottie_dance = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_S7j7Z9.json")

# 2. Estilo CSS para "Clase Mundial"
st.markdown("""
    <style>
    .main { background-color: #fdfaf6; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px; white-space: pre-wrap; background-color: #f0f2f6;
        border-radius: 10px 10px 0px 0px; gap: 1px; padding: 10px;
    }
    .stTabs [aria-selected="true"] { background-color: #e9edc9; font-weight: bold; }
    .expert-card {
        background: white; padding: 25px; border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05); border-left: 8px solid #A3B18A;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header: Perfil de Fabiola Pastén
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("🧘‍♀️ Fayoga")
        st.subheader("Fabiola Pastén")
        st.markdown("""
        **Periodista · Comunicadora · Experta en Wellness, Yoga y Biodanza**
        
        Una visión integral que une la comunicación consciente con el movimiento sanador. 
        Transformamos el bienestar en un estilo de vida de clase mundial.
        """)
    with col2:
        st_lottie(lottie_zen, height=200, key="zen_icon")

st.divider()

# 4. Navegación Estratégica (SEO & UX)
tabs = st.tabs(["✨ Disciplinas", "💃 Biodanza", "📚 Hemeroteca Top", "📅 Reservas"])

with tabs[0]: # Seccion Yoga y Wellness
    st.markdown("### El Arte del Bienestar")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class='expert-card'>
        <h4>Yoga Integral</h4>
        <p>Hatha y Vinyasa Flow diseñados para la reconexión profunda. 
        Sesiones de nivel mundial que equilibran el sistema nervioso y fortalecen el cuerpo.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=800", use_container_width=True)

with tabs[1]: # Sección Biodanza
    st.markdown("### Biodanza: El Movimiento de la Vida")
    col_d1, col_d2 = st.columns([1, 2])
    with col_d1:
        st_lottie(lottie_dance, height=250)
    with col_d2:
        st.write("""
        Como experta en **Biodanza**, Fabiola guía procesos de integración afectiva a través de la música y el movimiento. 
        Un sistema de crecimiento que estimula la alegría de vivir y la conexión con el otro.
        """)
        st.video("https://www.youtube.com/watch?v=Ev6LhJ6_X_M") # Clip ilustrativo liviano

with tabs[2]: # Hemeroteca (Perfil Periodista)
    st.markdown("### Hemeroteca Wellness Mundial")
    st.info("Curaduría periodística de lo mejor del Yoga y la Salud Global.")
    
    # Grid de noticias/artículos
    h1, h2, h3 = st.columns(3)
    with h1:
        st.image("https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=400")
        st.caption("Tendencias: Yoga en la era digital")
    with h2:
        st.image("https://images.unsplash.com/photo-1599447421416-3414500d18a5?auto=format&fit=crop&w=400")
        st.caption("Biodanza y Neurociencia: El estudio del movimiento")
    with h3:
        st.image("https://images.unsplash.com/photo-1512438248247-f0f2a5a8b7f0?auto=format&fit=crop&w=400")
        st.caption("Well-being empresarial en 2026")

with tabs[3]: # Reservas
    st.markdown("### Agenda tu Sesión")
    with st.form("reserva_form"):
        nombre = st.text_input("Nombre Completo")
        email = st.text_input("Correo Electrónico")
        servicio = st.selectbox("Interés", ["Clase Yoga Matinal", "Taller de Biodanza", "Asesoría Wellness Personalizada"])
        submitted = st.form_submit_button("Solicitar Información")
        if submitted:
            st.balloons()
            st.success(f"¡Gracias {nombre}! Fabiola se comunicará contigo pronto.")

# Footer
st.markdown("<br><hr><p style='text-align: center;'>Fayoga 2026 | Wellness de Clase Mundial por Fabiola Pastén</p>", unsafe_allow_html=True)
