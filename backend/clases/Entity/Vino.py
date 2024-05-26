from Entity.Bodega import Bodega
from Entity.Resenia import Resenia
from Entity.Varietal import Varietal
#from Control.GestorRankingVinos import GestorRankingVinos


class Vino:
    def __init__(self, aniada, imagenEtiqueta, nombre, notaDeCataBodega, precioARS, resenia: list[Resenia], varietal, bodega):
        self.aniada = aniada
        self.imagenEtiqueta = imagenEtiqueta
        self.nombre = nombre
        self.notaDeCataBodeba = notaDeCataBodega
        self.precioARS = precioARS
        
        self.resenia = resenia # []
        self.varietal = varietal
        self.bodega = bodega


    def tenesReseniasDeTipoEnPeriodo(self, fechaDesde, fechaHasta, resenias):
        
        for resenia in resenias:
            esPeriodo = resenias[resenia].sosDelPeriodo(fechaDesde, fechaHasta)
            sosSommelier = resenias[resenia].sosDeSommelier()
            if (esPeriodo and sosSommelier):
                nombre = self.getNombre()
                precio = self.getPrecio()


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