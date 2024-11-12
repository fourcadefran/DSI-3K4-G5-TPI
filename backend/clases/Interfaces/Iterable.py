from abc import abstractmethod, ABC
from clases.Interfaces import Iterator

class Iterable(ABC):
    @abstractmethod
    def create_iterable(self) -> Iterator:
        pass
