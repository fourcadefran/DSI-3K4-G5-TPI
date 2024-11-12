from abc import ABC, abstractmethod
from typing import List

#Interfaz (en python es una clase abstracta) IIterador con los metodos abstractos
class IIterator(ABC):

    # abstracciones
    @abstractmethod
    def primero(self):
        pass

    @abstractmethod
    def siguiente(self):
        pass

    @abstractmethod
    def ha_terminado(self) -> bool:
        pass

    @abstractmethod
    def actual(self) -> object:
        pass

    @abstractmethod
    def cumple_filtro(self, filtro: List[object]) -> bool:
        pass