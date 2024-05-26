from Entity.Pais import Pais

class Provincia:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

    def obtenerPais(self):
        return self.pais.getNombre()