class Bodega:
    def __init__(self, periodo_actualizacion, nombre, historia, descripcion, region):
        self.periodo_actualizacion = periodo_actualizacion
        self.nombre = nombre
        self.historia = historia
        self.descripcion = descripcion

        self.region = region

    def get_nombre(self):
        return self.nombre

    def obtener_region_y_pais(self):
        return self.region.get_nombre(), self.region.obtener_pais()
