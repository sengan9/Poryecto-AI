from fastapi import FastAPI
from routes.senderismo import router as senderismo_router

app = FastAPI(title="Recomendador de Rutas de Senderismo")

# Agregar las rutas definidas en senderismo.py
app.include_router(senderismo_router)

@app.get("/")
async def home():
    return {"message": "Bienvenido a la API de Recomendación de Rutas de Senderismo"}

