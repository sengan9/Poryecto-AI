import pytest
from sqlalchemy import inspect
from services.database import engine, SessionLocal, Interaction

def test_database_connection():
    """
    Verifica que se puede conectar al motor de la base de datos.
    """
    try:
        with engine.connect() as connection:
            assert connection is not None, "La conexión a la base de datos falló."
    except Exception as e:
        pytest.fail(f"Error al conectar a la base de datos: {e}")

def test_table_exists():
    """
    Verifica que la tabla 'interactions' existe en la base de datos.
    """
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    assert "interactions" in tables, "La tabla 'interactions' no existe en la base de datos."

def test_insert_and_query_record():
    """
    Verifica que se pueden insertar y recuperar registros en la tabla 'interactions'.
    """
    # Crear una sesión de prueba
    session = SessionLocal()

    # Crear un registro de prueba
    new_interaction = Interaction(
        prompt="¿Cuál es la capital de Francia?",
        response="La capital de Francia es París.",
    )
    try:
        session.add(new_interaction)
        session.commit()

        # Consultar el registro de prueba
        result = session.query(Interaction).filter_by(prompt="¿Cuál es la capital de Francia?").first()
        assert result is not None, "No se pudo recuperar el registro insertado."
        assert result.response == "La capital de Francia es París.", "La respuesta recuperada no coincide."
    except Exception as e:
        pytest.fail(f"Error al insertar o recuperar registros: {e}")
    finally:
        # Limpieza: Eliminar el registro de prueba
        session.query(Interaction).filter_by(prompt="¿Cuál es la capital de Francia?").delete()
        session.commit()
        session.close()
