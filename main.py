import streamlit as st

# Configuración de la pestaña del navegador
st.set_page_config(page_title="Fayoga", page_icon="🧘‍♀️", layout="centered")

# Título principal
st.title("🧘‍♀️ Fayoga - Bienestar y Comunidad")
st.subheader("Instructora: Fabiola Pastén")

# Menú lateral
menu = st.sidebar.selectbox("Navegación", ["Inicio", "Horarios y Reservas", "Catálogo On-Demand"])

if menu == "Inicio":
    st.write("Bienvenido a la plataforma oficial de clases de yoga.")
    st.divider()
    st.write("### Perfil de la Instructora")
    st.write("**Fabiola Pastén** - Instructora Principal y Fundadora")
    st.info("Únete a nuestras clases para encontrar equilibrio, mejorar tu flexibilidad y potenciar tu bienestar físico y mental.")

elif menu == "Horarios y Reservas":
    st.write("### Próximas Clases")
    
    # Creamos una tabla visual con los horarios
    clases = [
        {"Clase": "Hatha Yoga", "Fecha": "Jueves 10:00 AM", "Nivel": "Principiante", "Cupos libres": 5},
        {"Clase": "Vinyasa Flow", "Fecha": "Viernes 18:00 PM", "Nivel": "Intermedio", "Cupos libres": 2},
        {"Clase": "Yoga Restaurativo", "Fecha": "Sábado 09:00 AM", "Nivel": "Todos", "Cupos libres": 10}
    ]
    st.table(clases)
    
    st.write("### Reservar tu cupo")
    opcion = st.selectbox("Selecciona la clase que deseas tomar:", ["Hatha Yoga", "Vinyasa Flow", "Yoga Restaurativo"])
    nombre_alumno = st.text_input("Tu nombre completo:")
    
    if st.button("Confirmar Reserva"):
        if nombre_alumno:
            st.success(f"¡Listo, {nombre_alumno}! Tu cupo para {opcion} ha sido reservado. Te enviaremos un mensaje de confirmación.")
        else:
            st.warning("Por favor, ingresa tu nombre para reservar.")

elif menu == "Catálogo On-Demand":
    st.write("### Videos y Rutinas")
    st.write("Aquí estarán disponibles las clases grabadas de Fabiola.")
    # Un espacio reservado (placeholder) para un futuro video
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Video de prueba
