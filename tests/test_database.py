import pytest
from sqlalchemy import inspect
from services.database import engine, SessionLocal, Interaction, init_db

def test_engine_connection():
    """
    Verifica que se puede conectar al motor de la base de datos.
    """
    try:
        with engine.connect() as connection:
            assert connection is not None, "La conexión al motor falló."
    except Exception as e:
        pytest.fail(f"Error al conectar al motor: {e}")

def test_create_interaction_table():
    """
    Verifica que la tabla 'interactions' puede ser creada.
    """
    try:
        # Inicializa la base de datos y las tablas
        init_db()
        
        # Usa el inspector para verificar la tabla
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        assert "interactions" in tables, "La tabla 'interactions' no fue creada."
    except Exception as e:
        pytest.fail(f"Error al crear la tabla 'interactions': {e}")

def test_interaction_insert_and_query():
    """
    Verifica que se pueden insertar y consultar datos en la tabla 'interactions'.
    """
    try:
        # Inserta un registro de prueba
        session = SessionLocal()
        test_data = Interaction(
            prompt="Test Prompt",
            response="Test Response"
        )
        session.add(test_data)
        session.commit()

        # Consulta el registro insertado
        query_result = session.query(Interaction).filter_by(prompt="Test Prompt").first()
        session.close()

        assert query_result is not None, "No se encontró el registro insertado."
        assert query_result.response == "Test Response", "Los datos no coinciden con lo esperado."
    except Exception as e:
        pytest.fail(f"Error al insertar o consultar datos en la tabla 'interactions': {e}")
