from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.senderismo import router as senderismo_router

app = FastAPI(title="Recomendador de Rutas de Senderismo")

# Configurar directorios para plantillas y archivos estáticos
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Agregar rutas
app.include_router(senderismo_router)

@app.get("/")
async def home():
    return {"message": "Bienvenido a la API de Recomendación de Rutas de Senderismo"}
