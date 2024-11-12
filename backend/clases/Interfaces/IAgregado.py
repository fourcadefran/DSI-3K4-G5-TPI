from abc import abstractmethod, ABC
from clases.Interfaces import IIterator
from typing import List

#Interfaz (en python es una clase abstracta) IAgregado con los metodos abstractos
class IAgregado(ABC):

    # abstracciones
    @abstractmethod
    def create_iterable(self, vinos: List[object]) -> IIterator:
        pass
