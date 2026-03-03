from fastapi import FastAPI

app = FastAPI(
    title="Fayoga API",
    description="Backend oficial para la app de bienestar y yoga de Fabiola Pastén",
    version="1.0.0"
)

@app.get("/")
def inicio():
    return {
        "status": "Online", 
        "proyecto": "Fayoga", 
        "instructora": "Fabiola Pastén"
    }

@app.get("/api/v1/clases")
def obtener_clases():
    """Retorna el listado de clases impartidas por Fabiola."""
    return [
        {"id": 1, "estilo": "Hatha Yoga", "nivel": "Principiante", "cupos": 15},
        {"id": 2, "estilo": "Vinyasa Flow", "nivel": "Intermedio", "cupos": 10},
        {"id": 3, "estilo": "Yoga Restaurativo", "nivel": "Todos", "cupos": 20}
    ]

@app.get("/api/v1/fabiola")
def perfil_instructora():
    """Información de perfil y contacto de Fabiola Pastén."""
    return {
        "nombre": "Fabiola Pastén",
        "rol": "Instructora Principal y Fundadora",
        "bio": "Añadir aquí la biografía o enfoque del yoga de Fabiola."
    }
