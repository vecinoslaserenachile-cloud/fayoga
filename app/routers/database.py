from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Definimos el nombre del archivo de nuestra base de datos (se creará solo)
SQLALCHEMY_DATABASE_URL = "sqlite:///./fayoga.db"

# 2. Creamos el "motor" que se conecta a la base de datos
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Creamos la "fábrica" de sesiones (las conexiones individuales de cada usuario)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Esta es la clase base que usaremos luego para crear nuestras tablas (Alumnos, Clases, etc.)
Base = declarative_base()

# 5. Función auxiliar que usaremos en nuestros endpoints para abrir y cerrar la conexión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
