from sqlalchemy import Column, Integer, String, Boolean
from config.database import Base

# todo: aca deberian ir las clases - solo las que necesitan persistencia son las que heredan de Base, las otras son
#  copy-paste del diagrama de clases

# ¿los vinos los sacamos de la base de datos?
class Vinos(Base):
    __tablename__ = "vinos"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, index=True)
    nota_de_cata_bodega = Column(String, index=True)
    precio_ars = Column(Integer, index=True)
    imagen_etiqueta = Column(String, index=True)
    aniada = Column(String, index=True)

    def __init__(self, nombre, nota_de_cata_bodega, precio_ars, aniada, imagen_etiqueta):
        self.nombre = nombre
        self.nota_de_cata_bodega = nota_de_cata_bodega
        self.precio_ars = precio_ars
        self.aniada = aniada
        self.imagen_etiqueta = imagen_etiqueta


class Resenia:
    def __init__(self, comentario, es_premium, fecha_resenia, puntaje):
        self.comentario = comentario
        self.es_premium = es_premium
        self.fecha_resenia = fecha_resenia
        self.puntaje = puntaje

    def es_premium(self):
        return self.es_premium

    def sos_de_enofilo(self):
        # como sabemos a quien le corresponde?
        return ""

    def sos_de_sommelier(self):
        return ""