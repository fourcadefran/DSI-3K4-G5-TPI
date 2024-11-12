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
    fecha_desde = request.fecha_desde.date()  # Convertir a objeto date
    fecha_hasta = request.fecha_hasta.date()  # Convertir a objeto date
    resenia = request.tipo_de_resenia

    gestor = GestorRankingVinos(fecha_desde, fecha_hasta, resenia, [], [])
    gestor.buscar_vinos_con_resenias_en_periodo(vinos_generales)
    gestor.calcular_puntaje_de_sommelier_en_periodo()
    gestor.ordenar_vinos()
    interfaz_excel = InterfazExcel()
    # TODO: METER MAS COMENTARIOS
    return {
        "message": "Ranking received",
        "reporte": interfaz_excel.exportar_excel(objetos=gestor.vinos_ordenados)
    }


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
