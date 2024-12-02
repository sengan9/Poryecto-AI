import pytest
from services.llm_service import recomendar_ruta

def test_recomendar_ruta():
    """
    Verifica que el servicio de recomendación de rutas devuelva una respuesta válida.
    """
    prompt = "Recomiéndame una ruta en Madrid de 10 km, dificultad media."
    respuesta = recomendar_ruta(prompt)
    assert isinstance(respuesta, str), "La respuesta debe ser un string."
    assert len(respuesta) > 0, "La respuesta no debe estar vacía."
