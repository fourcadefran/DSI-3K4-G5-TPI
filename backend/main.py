from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from clases.Interface.InterfazExcel import InterfazExcel
from config.models import RankingRequest
from clases.Control.GestorRankingVinos import GestorRankingVinos
from clases.Entity.Vino import vinos_generales

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/ranking")
async def root(request: RankingRequest):
    print(request)
    fecha_desde = request.fecha_desde.date()  # Convertir a objeto date
    fecha_hasta = request.fecha_hasta.date()  # Convertir a objeto date
    resenia = request.tipo_de_resenia
    visualizacion = request.tipo_de_visualizacion

    gestor = GestorRankingVinos(fecha_desde, fecha_hasta, resenia, vinos_generales)
    gestor.buscarVinosConReseniasEnPeriodo(vinos_generales)
    gestor.calcularPuntajeDeSommelierEnPeriodo()
    gestor.ordenarVinos()
    interfaz_excel = InterfazExcel()
    reporte = interfaz_excel.exportarExcel(objetos=gestor.vinosOrdenados)
    return {
        "message": "Ranking received",
        "reporte": reporte
    }


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
