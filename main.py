from fastapi import FastAPI
from app.routers import reservas  # 1. Importamos tu nuevo archivo de reservas

app = FastAPI(
    title="Fayoga API",
    description="Backend oficial para la app de bienestar y yoga de Fabiola Pastén",
    version="1.0.0"
)

# 2. Le decimos a la app que use las rutas que creaste en la carpeta routers
app.include_router(reservas.router, prefix="/api/v1/reservas", tags=["Reservas y Clases"])

@app.get("/")
def inicio():
    return {
        "status": "Online", 
        "proyecto": "Fayoga", 
        "instructora": "Fabiola Pastén"
    }

@app.get("/api/v1/fabiola")
def perfil_instructora():
    """Información de perfil y contacto de Fabiola Pastén."""
    return {
        "nombre": "Fabiola Pastén",
        "rol": "Instructora Principal y Fundadora",
        "bio": "Añadir aquí la biografía o enfoque del yoga de Fabiola."
    }
