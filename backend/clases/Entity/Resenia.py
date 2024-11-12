from datetime import datetime


class Resenia:
    def __init__(self, comentario, es_premium, fecha_resenia, puntaje, vino):
        self.comentario = comentario
        self.es_premium = es_premium
        self.fecha_resenia = fecha_resenia
        self.puntaje = puntaje
        self.vino = vino

    def sos_del_periodo(self, fecha_desde, fecha_hasta):
        date_fecha_resenia = datetime.strptime(self.fecha_resenia, "%Y-%m-%d").date()
        if fecha_desde <= date_fecha_resenia <= fecha_hasta:
            return True
        else:
            return False

    def sos_de_sommelier(self):
        if self.es_premium:
            return True
        else:
            return False

    def get_puntaje(self):
        return self.puntaje
