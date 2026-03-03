from fastapi import FastAPI

app = FastAPI(title="Fayoga API")

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la plataforma de Fayoga"}

@app.get("/clases")
def get_clases():
    # Aquí iría la lógica para conectar con la base de datos
    return [{"id": 1, "nombre": "Hatha Yoga", "instructor": "Rodrigo"}]
