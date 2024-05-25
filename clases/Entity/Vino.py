from Bodega import *

class Vino:
    def __init__(self, aniada, imagenEtiqueta, nombre, notaDeCataBodega, precioARS, resenia, varietal, bodega: list[Bodega]):
        self.aniada = aniada
        self.imagenEtiqueta = imagenEtiqueta
        self.nombre = nombre
        self.notaDeCataBodeba = notaDeCataBodega
        self.precioARS = precioARS
        
        # Revisar relaciones
        self.resenia = resenia
        self.varietal = varietal
        self.bodega = bodega

    def tenesReseniasDeTipoEnPeriodo(self):
        pass

    def calcularPuntajeDeSommelierEnPeriodo(self):
        pass

    def calcularPuntajePromedio(self):
        pass

    def getNombre(self):
        return self.nombre

    def getPrecio(self):
        return self.precioARS

    def buscarInfoBodega(self):
        return self.bodega[2]

    def buscarVarietal(self):
        pass