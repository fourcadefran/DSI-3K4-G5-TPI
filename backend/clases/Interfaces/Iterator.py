from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def primero(self) -> object:
        pass

    @abstractmethod
    def siguiente(self) -> object:
        pass

    @abstractmethod
    def ha_terminado(self) -> bool:
        pass

    @abstractmethod
    def elemento_actual(self) -> object:
        pass