from clases.Interfaces.IIterator import IIterator
from typing import List
from clases.Entity.Vino import Vino


# Clase de fabricacion pura IteradorVinos realizando la interfaz IIterador
class IteradorVinos(IIterator):

    # concreciones
    def __init__(self, vinos: List[Vino], posicion_actual: int):
        self.vinos = vinos
        self.posicion_actual = posicion_actual

    #Reimplementacion de los metodos abstractos
    def primero(self):
        self.posicion_actual = 0

    def siguiente(self):
        self.posicion_actual += 1
        pass

    def ha_terminado(self) -> bool:
        return self.posicion_actual < len(self.vinos)

    def actual(self) -> Vino:
        return self.vinos[self.posicion_actual]

    def cumple_filtro(self, filtros) -> bool:
        #acceder al vino actual y ejecutar el metodo pasando los filtros como parametro
        return self.vinos[self.posicion_actual].tenesReseniasDeTipoEnPeriodo(filtros[0], filtros[1], self.vinos[self.posicion_actual].resenia)
