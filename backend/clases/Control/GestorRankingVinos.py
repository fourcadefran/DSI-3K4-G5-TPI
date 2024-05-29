from clases.Entity.Vino import Vino


class GestorRankingVinos:
    def __init__(self, fechaDesde, fechaHasta, tipoRankingSeleccionado, vinosOrdenados = [], vinosQueCumplenFiltros = []):
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
                # nombre = vino.getNombre()
                # precio = vino.getPrecio()
                # nombre_bodega, region_y_pais = vino.buscarInfoBodega()
                # nombre_region = region_y_pais[0]
                # nombre_pais = region_y_pais[1]

    def calcularPuntajeDeSommelierEnPeriodo(self):
        puntaje_promedio = 0
        acumulador_de_puntaje_sommelier = 0

        for vino in self.vinosQueCumplenFiltros:
            acumulador_de_puntaje_sommelier = vino.calcularPuntajeDeSommelierEnPeriodo(self)
            puntaje_promedio = vino.calcularPuntajePromedio(acumulador_de_puntaje_sommelier, len(vino.resenia))
            print(puntaje_promedio)
            print((vino, puntaje_promedio))
            self.vinosOrdenados.append((vino, puntaje_promedio))  # [ (vino1, puntaje1) , (vino2, puntaje2)]


    def ordenarVinos(self):
        print(self.vinosOrdenados)

        # x = [(vino, puntaje)]

        self.vinosOrdenados.sort(key=lambda x: x[1], reverse=True)

    def finCU(self):
        pass