from pydantic import BaseModel
from datetime import datetime


class RankingRequest(BaseModel):
    fecha_desde: datetime
    fecha_hasta: datetime
