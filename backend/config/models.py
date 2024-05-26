from pydantic import BaseModel
from datetime import datetime


class RankingRequest(BaseModel):
    fecha_desde: datetime
    fecha_hasta: datetime
    tipo_de_resenia: str
    tipo_de_visualizacion: str
