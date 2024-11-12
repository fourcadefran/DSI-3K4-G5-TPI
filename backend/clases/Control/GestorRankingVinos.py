class GestorRankingVinos:
    def __init__(self, fecha_desde, fecha_hasta, tipo_ranking_seleccionado, vinos_ordenados=[],
                 vinos_que_cumplen_filtros=[]):
        self.fecha_desde = fecha_desde
        self.fecha_hasta = fecha_hasta
        self.tipo_ranking_seleccionado = tipo_ranking_seleccionado
        self.vinos_ordenados = vinos_ordenados  # [(vino1, puntaje1), (vino2, puntaje2)]
        self.vinos_que_cumplen_filtros = vinos_que_cumplen_filtros

    def opcion_generar_ranking_vinos(self):
        pass

    def tomar_sel_fecha_desde_hasta(self):
        pass

    def tomar_sel_tipo_resenia(self):
        pass

    def tomar_sel_tipo_visualizacion(self):
        pass

    def buscar_vinos_con_resenias_en_periodo(self, vinos_generales):
        for vino in vinos_generales:
            cumple_filtro = vino.tenes_resenias_de_tipo_en_periodo(self.fecha_desde, self.fecha_hasta, vino.resenia)
            if cumple_filtro:
                self.vinos_que_cumplen_filtros.append(vino)

    def calcular_puntaje_de_sommelier_en_periodo(self):
        self.vinos_ordenados = []
        for vino in self.vinos_que_cumplen_filtros:
            acumulador_de_puntaje_sommelier = vino.calcular_puntaje_de_sommelier_en_periodo(self)
            puntaje_promedio = vino.calcular_puntaje_promedio(acumulador_de_puntaje_sommelier, len(vino.resenia))
            self.vinos_ordenados.append((vino, puntaje_promedio))  # [ (vino1, puntaje1) , (vino2, puntaje2)]

    def ordenar_vinos(self):
        self.vinos_ordenados.sort(key=lambda x: x[1], reverse=True)

    def fin_cu(self):
        pass
