class Provincia:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

    def obtener_pais(self):
        return self.pais.get_nombre()
