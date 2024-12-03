import os
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
from datetime import datetime

# Cargar las variables de entorno
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(dotenv_path)

# Configuración de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("La URL de la base de datos no está configurada.")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Interaction(Base):
    __tablename__ = "interactions"
    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(String(500), nullable=False)
    response = Column(String(2000), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

def init_db():
    """
    Inicializa la base de datos y crea las tablas.
    """
    Base.metadata.create_all(bind=engine)
