from clases.Entity.Vino import Vino


class GestorRankingVinos:
    def __init__(self, fechaDesde, fechaHasta, tipoRankingSeleccionado, vinosOrdenados=[], vinosQueCumplenFiltros=[]):
        self.fechaDesde = fechaDesde
        self.fechaHasta = fechaHasta
        self.tipoRankingSeleccionado = tipoRankingSeleccionado
        self.vinosOrdenados = vinosOrdenados  # [(vino1, puntaje1), (vino2, puntaje2)]
        self.vinosQueCumplenFiltros = vinosQueCumplenFiltros

    def opcionGenerarRankingVinos(self):
        pass

    def tomarSelFechaDesdeHasta(self):
        pass

    def tomarSelTipoResenia(self):
        pass

    def tomarSelTipoVisualizacion(self):
        pass

    def buscarVinosConReseniasEnPeriodo(self, vinos_generales):
        for vino in vinos_generales:
            cumple_filtro = vino.tenesReseniasDeTipoEnPeriodo(self.fechaDesde, self.fechaHasta, vino.resenia)
            if cumple_filtro:
                self.vinosQueCumplenFiltros.append(vino)

    def calcularPuntajeDeSommelierEnPeriodo(self):
        self.vinosOrdenados = []
        for vino in self.vinosQueCumplenFiltros:
            acumulador_de_puntaje_sommelier = vino.calcularPuntajeDeSommelierEnPeriodo(self)
            puntaje_promedio = vino.calcularPuntajePromedio(acumulador_de_puntaje_sommelier, len(vino.resenia))
            self.vinosOrdenados.append((vino, puntaje_promedio))  # [ (vino1, puntaje1) , (vino2, puntaje2)]

    def ordenarVinos(self):
        self.vinosOrdenados.sort(key=lambda x: x[1], reverse=True)

    def finCU(self):
        pass
