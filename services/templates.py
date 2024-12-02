from langchain.prompts import PromptTemplate

# Definir un template para rutas de senderismo
ruta_prompt_template = PromptTemplate(
    input_variables=["lugar", "distancia", "dificultad"],
    template=(
        "Recomiéndame una ruta de senderismo en {lugar} de aproximadamente {distancia} km, "
        "con dificultad {dificultad}."
    )
)
