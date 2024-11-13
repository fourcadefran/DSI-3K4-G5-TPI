from clases.Entity.IteradorVinos import IteradorVinos
from clases.Entity.Vino import Vino
from clases.Interfaces.IAgregado import IAgregado
from typing import List

#Realizar la interfaz IAgregado
class GestorRankingVinos(IAgregado):

    #Reimplementacion del metodo create_iterable de la interfaz IAgregado - concreciones
    def create_iterable(self, coleccion: List[Vino]) -> IteradorVinos:
        return IteradorVinos(coleccion, 0)

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

    def buscarVinosConReseniasEnPeriodo(self, vinos_generales, fecha_desde, fecha_hasta):
        iterador_vino = self.create_iterable(vinos_generales)
        iterador_vino.primero()
        while iterador_vino.ha_terminado():
            vino = iterador_vino.actual()
            if iterador_vino.cumple_filtro([fecha_desde, fecha_hasta]):
                self.vinosQueCumplenFiltros.append(vino)
            iterador_vino.siguiente()


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
