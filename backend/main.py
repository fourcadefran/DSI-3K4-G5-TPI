from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from config.models import RankingRequest

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
    print(fecha_desde, fecha_hasta)
    return {"message": "Ranking received"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
