from clases.Entity.Provincia import Provincia


class RegionVitivinicola:
    def __init__(self, descripcion, nombre, provincia):
        self.descripcion = descripcion
        self.nombre = nombre

        self.provincia = provincia

    def get_nombre(self):
        return self.nombre

    def obtener_pais(self):
        return self.provincia.obtener_pais()
