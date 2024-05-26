from clases.Entity.Vino import Vino


class GestorRankingVinos:
    def __init__(self, fechaDesde, fechaHasta, tipoRankingSeleccionado, vinosOrdenados = [], vinosQueCumplenFiltros = []):
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

    def buscarVinosConReseniasEnPeriodo(self, vinos_generales):
        for vino in vinos_generales:
            print(vino)
            cumple_filtro = vino.tenesReseniasDeTipoEnPeriodo(self.fechaDesde, self.fechaHasta, vino.resenia)
            if cumple_filtro:
                self.vinosQueCumplenFiltros.append(vino)
                # print("el vino cumplio los filtros")
                # nombre = vino.getNombre()
                # precio = vino.getPrecio()
                # nombre_bodega, region_y_pais = vino.buscarInfoBodega()
                # nombre_region = region_y_pais[0]
                # nombre_pais = region_y_pais[1]
                # print("Datos del vino que cumple los filtros:")
                # print("nombre: ", nombre)
                # print("precio: ", precio)
                # print("nombre_bodega: ", nombre_bodega)
                # print("TUPLA: region_y_pais: ", region_y_pais)
                # print("nombre_region: ", nombre_region)
                # print("nombre_pais: ", nombre_pais)
        print(self.vinosQueCumplenFiltros)


    def calcularPuntajeDeSommelierEnPeriodo(self):
        puntajes_por_vino = []  # [(vino1, puntaje_del_vino1)]
        for vino in self.vinosQueCumplenFiltros:
            vino.calcularPuntajeDeSommelierEnPeriodo(self)

    def ordenarVinos(self):
        self.vinosOrdenados = sorted(self.vinosQueCumplenFiltros, key=lambda vino: vino.puntaje_promedio, reverse=True)


    def finCU(self):
        pass