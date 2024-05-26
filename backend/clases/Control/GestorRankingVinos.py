from Entity.Vino import Vino

class GestorRankingVinos:
    def __init__(self, fechaDesde, fechaHasta, tipoRankingSeleccionado, vinosOrdenados, vinosQueCumplenFiltros):
        self.fechaDesde = fechaDesde
        self.fechaHasta = fechaHasta
        self.tipoRankingSeleccionado = tipoRankingSeleccionado
        self.vinosOrdenados = vinosOrdenados
        self.vinosQueCumplenFiltros = vinosQueCumplenFiltros
    

    def opcionGenerarRankingVinos(self):
        pass


    def tomarSelFechaDesdeHasta(self):
        pass


    def tomarSelTipoResenia(self):
        pass


    def tomarSelTipoVisualizacion(self):
        pass


    def buscarVinosConReseniasEnPeriodo(self, lista):
        self.vinosOrdenados = []
        self.vinosQueCumplenFiltros = []
        
        #periodo
        fechaDesde = '1-06-2003'
        fechaHasta = '16-06-2003'

        for vino in lista:
            lista[vino].tenesReseniasDeVinosEnPeriodo(fechaDesde, fechaHasta, vino.resenia)


    def calcularPuntajeDeSommelierEnPeriodo(self, vino: Vino):
        vino.calcularPuntajeDeSommelierEnPeriodo()


    def ordenarVinos(self):
        # ordenados de mayor a menor puntaje
        pass


    def finCU(self):
        pass