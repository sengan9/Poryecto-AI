from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from services.llm_service import recomendar_ruta

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def render_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/procesar-texto", response_class=HTMLResponse)
async def procesar_texto(request: Request, mensaje: str = Form(...)):
    try:
        # Llamar a la función de recomendación
        respuesta = recomendar_ruta(mensaje)
        return templates.TemplateResponse(
            "index.html", {"request": request, "mensaje": mensaje, "respuesta": respuesta}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
