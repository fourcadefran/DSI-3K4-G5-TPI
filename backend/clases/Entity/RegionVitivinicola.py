from clases.Entity.Provincia import Provincia


class RegionVitivinicola:
    def __init__(self, descripcion, nombre, provincia):
        self.descripcion = descripcion
        self.nombre = nombre

        self.provincia = provincia


    def getNombre(self):
        return self.nombre


    def obtenerPais(self):
        return self.provincia.obtenerPais()