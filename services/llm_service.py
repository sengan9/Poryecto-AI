import os
import google.generativeai as genai
from dotenv import load_dotenv
from services.database import SessionLocal, Interaction
from datetime import datetime

# Cargar variables desde el archivo .env
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(dotenv_path)

# Configurar la clave API
api_key = os.getenv("GEMINI_API_KEY")  # Leer clave API desde variables de entorno
if not api_key:
    raise ValueError("La clave API no está configurada. Verifica tu archivo .env o las variables de entorno.")

genai.configure(api_key=api_key)

print("API configurada correctamente con la clave proporcionada.")


def guardar_interaccion(prompt: str, response: str):
    """
    Guarda una interacción en la base de datos.
    """
    db = SessionLocal()
    try:
        nueva_interaccion = Interaction(
            prompt=prompt,
            response=response,
            timestamp=datetime.now()
        )
        db.add(nueva_interaccion)
        db.commit()
    except Exception as e:
        print(f"Error al guardar en la base de datos: {e}")
    finally:
        db.close()

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
        
        response_text = response.text

        # Guardar en la base de datos
        guardar_interaccion(prompt, response_text)

        return response_text
    except Exception as e:
        return f"Error al generar respuesta: {str(e)}"


