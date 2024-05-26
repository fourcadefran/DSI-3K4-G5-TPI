class Resenia:
    def __init__(self, comentario, esPremium, fechaResenia, puntaje, vino):
        self.comentario = comentario
        self.esPremium = esPremium
        self.fechaResenia = fechaResenia
        self.puntaje = puntaje
        self.vino = vino


    def sosDelPeriodo(self, fechaDesde, fechaHasta):
        if (fechaDesde <= self.fechaResenia <= fechaHasta):
            return True
        else: 
            return False


    def sosDeSommelier(self):
        if self.esPremium:
            return True
        else:
            return False


    def getPuntaje(self):
        return self.puntaje
