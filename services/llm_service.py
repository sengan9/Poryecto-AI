import os
import google.generativeai as genai
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(dotenv_path)

# Configurar la clave API
api_key = os.getenv("GEMINI_API_KEY")  # Leer clave API desde variables de entorno
if not api_key:
    raise ValueError("La clave API no está configurada. Verifica tu archivo .env o las variables de entorno.")

genai.configure(api_key=api_key)

print("API configurada correctamente con la clave proporcionada.")

def recomendar_ruta(prompt):
    """
    Genera recomendaciones de rutas de senderismo basadas en la consulta proporcionada.
    """
    try:
        # Construir el prompt para el modelo
        prompt_ruta = f"Recomiéndame una ruta de senderismo: {prompt}"

        # Crear el modelo generativo
        model = genai.GenerativeModel("models/gemini-1.5-flash")

        # Generar contenido con el modelo
        response = model.generate_content(prompt_ruta)
        print("Respuesta completa:", response)  # Depuración: Imprimir respuesta completa

        # Validar y extraer el contenido generado
        if not response or not hasattr(response, "text"):
            raise ValueError("Respuesta vacía o no válida del modelo.")
        return response.text
    except Exception as e:
        return f"Error al generar respuesta: {str(e)}"