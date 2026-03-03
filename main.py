import streamlit as st

# Configuración de página
st.set_page_config(page_title="Fayoga | Fabiola Pastén", page_icon="🧘‍♀️", layout="centered")

# --- ESTILO PERSONALIZADO (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #fdfaf6; }
    h1 { color: #4a5d4e; font-family: 'Helvetica Neue', sans-serif; }
    .stButton>button {
        background-color: #6b8e23;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 25px;
    }
    .stButton>button:hover { background-color: #556b2f; color: white; }
    .sidebar .sidebar-content { background-color: #e9edc9; }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA CON ILUSTRACIÓN ---
st.title("🧘‍♀️ Fayoga")
st.markdown("#### *Tu espacio de paz en La Serena*")

# --- MENÚ LATERAL ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3048/3048374.png", width=100) # Icono decorativo
menu = st.sidebar.radio("Menú", ["Inicio", "Reservar Clase", "Contenido Exclusivo"])

if menu == "Inicio":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("### Bienvenida")
        st.write("Fayoga es el resultado de años de práctica y dedicación de **Fabiola Pastén**. Aquí no solo entrenas el cuerpo, sino que cultivas la mente.")
    with col2:
        # Simulación de clip/ilustración liviana
        st.image("https://img.freepik.com/free-vector/yoga-meditation-concept-illustration_114360-1453.jpg")

elif menu == "Reservar Clase":
    st.write("### Encuentra tu equilibrio")
    # Tarjetas visuales para clases
    c1, c2 = st.columns(2)
    with c1:
        st.info("**Hatha Yoga**\n\nEnfoque en posturas físicas y respiración.")
    with c2:
        st.success("**Vinyasa Flow**\n\nMovimiento fluido y dinámico.")
    
    with st.expander("📅 Ver calendario y reservar"):
        nombre = st.text_input("Nombre completo")
        clase = st.selectbox("Elige tu clase", ["Mañana (10:00)", "Tarde (19:00)"])
        if st.button("Reservar Ahora"):
            st.balloons() # Efecto visual de celebración
            st.success(f"¡Reserva lista para {nombre}!")

elif menu == "Contenido Exclusivo":
    st.write("### Biblioteca de Bienestar")
    # Simulación de clips livianos
    st.video("https://www.youtube.com/watch?v=Ev6LhJ6_X_M") # Ejemplo de yoga suave
