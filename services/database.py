import os
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
from datetime import datetime
from sqlalchemy import Text

# Cargar variables desde el archivo .env
dotenv_path = os.path.abspath(os.path.join(os.getcwd(), ".env"))
load_dotenv(dotenv_path)

# URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está configurada. Verifica el archivo .env.")

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para definir las tablas
Base = declarative_base()

# Modelo de la tabla 'Interaction'
class Interaction(Base):
    __tablename__ = "interactions"
    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(String(255), nullable=False)  # Longitud máxima especificada
    response = Column(Text, nullable=False)  
    timestamp = Column(DateTime, default=datetime.utcnow)

def init_db():
    """
    Inicializa la base de datos y crea las tablas definidas.
    """
    Base.metadata.create_all(bind=engine)

