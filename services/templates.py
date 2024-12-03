from langchain.prompts import PromptTemplate
import google.generativeai as genai

def recomendar_ruta(lugar: str, distancia: int, dificultad: str, belleza: str) -> str:
    """
    Genera recomendaciones de rutas de senderismo utilizando PromptTemplate de LangChain.
    """
    try:
        # Configurar el prompt usando PromptTemplate
        prompt_template = PromptTemplate(
            input_variables=["lugar", "distancia", "dificultad", "belleza"],
            template=(
                "Recomiéndame una ruta de senderismo en {lugar} de aproximadamente {distancia} km, "
                "con una dificultad {dificultad}, y que sea especialmente {belleza}. Proporciona detalles adicionales."
            )
        )

        # Construir el prompt dinámicamente
        prompt = prompt_template.format(
            lugar=lugar, distancia=distancia, dificultad=dificultad, belleza=belleza
        )

        # Crear el modelo generativo
        model = genai.GenerativeModel("models/gemini-1.5-flash")

        # Generar contenido con el modelo
        response = model.generate_content(prompt=prompt)
        print("Respuesta completa:", response)  # Depuración

        # Validar y extraer el contenido generado
        if not response or not hasattr(response, "text"):
            raise ValueError("Respuesta vacía o no válida del modelo.")
        return response.text
    except Exception as e:
        return f"Error al generar respuesta: {str(e)}"
