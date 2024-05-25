class Bodega:
    def __init__(self, periodoActualizacion, nombre, historia, descripcion, region):
        self.periodoActualizacion = periodoActualizacion
        self.nombre = nombre
        self.historia = historia
        self.descripcion = descripcion

        self.region = region

    def getNombre(self):
        return self.nombre

    def obtenerRegionYPais(self):
        return self.region.getNombre(), self.region.obtenerPais()