from fastapi import APIRouter

# Creamos el enrutador para este módulo
router = APIRouter()

@router.get("/")
def ver_horarios():
    """Devuelve los horarios de las próximas clases."""
    return [
        {"id": 1, "clase": "Hatha Yoga", "fecha": "2026-03-05T10:00:00", "cupos_disponibles": 5, "nivel": "Principiante"},
        {"id": 2, "clase": "Vinyasa Flow", "fecha": "2026-03-06T18:00:00", "cupos_disponibles": 2, "nivel": "Intermedio"}
    ]

@router.post("/{clase_id}/reservar")
def reservar_cupo(clase_id: int, alumno_id: int):
    """Reserva un cupo en una clase específica."""
    # Aquí luego conectaremos la base de datos para guardar la reserva real
    return {
        "mensaje": "Reserva confirmada con éxito.",
        "clase_id": clase_id,
        "alumno_id": alumno_id,
        "estado": "Confirmado"
    }
