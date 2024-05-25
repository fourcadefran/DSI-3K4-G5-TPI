from Entity.Bodega import Bodega
from Entity.Resenia import Resenia
from Entity.Varietal import Varietal


class Vino:
    def __init__(self, aniada, imagenEtiqueta, nombre, notaDeCataBodega, precioARS, resenia: list[Resenia], varietal: list[Varietal], bodega):
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
        pass

    def calcularPuntajePromedio(self):
        pass

    def getNombre(self):
        return self.nombre

    def getPrecio(self):
        return self.precioARS

    def buscarInfoBodega(self):
        return self.bodega.getNombre()

    # Agregar loop
    def buscarVarietal(self):
        return self.varietal.getDescripcion()