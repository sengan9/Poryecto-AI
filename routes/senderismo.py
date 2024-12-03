from fastapi import APIRouter, HTTPException, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from services.llm_service import recomendar_ruta

# Crear el enrutador
router = APIRouter()

# Configuración de las plantillas HTML
templates = Jinja2Templates(directory="templates")

# Ruta para el formulario
@router.get("/", response_class=HTMLResponse)
async def formulario(request: Request):
    """
    Renderiza el formulario HTML para ingresar una consulta de senderismo.
    """
    return templates.TemplateResponse("index.html", {"request": request})

# Ruta para procesar el texto enviado por el formulario
@router.post("/procesar-texto", response_class=HTMLResponse)
async def procesar_texto(request: Request, mensaje: str = Form(...)):
    """
    Procesa el texto enviado por el usuario, genera una recomendación y la muestra en una página HTML.
    """
    try:
        # Llamar al servicio de recomendación
        respuesta = recomendar_ruta(mensaje)
        return templates.TemplateResponse("index.html", {"request": request, "mensaje": mensaje, "respuesta": respuesta})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la consulta: {str(e)}")
