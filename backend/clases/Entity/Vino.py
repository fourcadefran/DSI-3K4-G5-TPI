from clases.Entity.Bodega import Bodega
from clases.Entity.Resenia import Resenia
from clases.Entity.Varietal import Varietal


class Vino:
    def __init__(self, aniada, imagenEtiqueta, nombre, notaDeCataBodega, precioARS, resenia: list[Resenia], varietal, bodega):
        self.aniada = aniada
        self.imagenEtiqueta = imagenEtiqueta
        self.nombre = nombre
        self.notaDeCataBodeba = notaDeCataBodega
        self.precioARS = precioARS
        
        self.resenia = resenia
        self.varietal = varietal
        self.bodega = bodega

    def tenesReseniasDeTipoEnPeriodo(self):
        # Revisar relacion con gestor
        fechaDesde = None
        fechaHasta = None
        
        return self.resenia.sosDelPeriodo(fechaDesde, fechaHasta)

    def calcularPuntajeDeSommelierEnPeriodo(self):
        acumulador = 0
        contador = 0

        for resenia in self.resenia:
            if resenia.sosDeSommelier() and resenia.sosDelPeriodo():
                acumulador += resenia.getPuntaje()
                contador += 1
        self.calcularPuntajePromedio(acumulador, contador)

    def calcularPuntajePromedio(self, acumulador, contador):
        if contador != 0:
            return acumulador / contador
        else:
            return 0

    def getNombre(self):
        return self.nombre

    def getPrecio(self):
        return self.precioARS

    def buscarInfoBodega(self):
        return self.bodega.getNombre()

    # Loop en DS -> aclara que solo tiene un Varietal en los CU
    def buscarVarietal(self):
        return self.varietal.getDescripcion()