from clases.Entity.Bodega import Bodega
from clases.Entity.Resenia import Resenia
from clases.Entity.Varietal import Varietal
from clases.Entity.RegionVitivinicola import RegionVitivinicola
from clases.Entity.Provincia import Provincia
from clases.Entity.Pais import Pais


class Vino:
    def __init__(self, aniada, imagenEtiqueta, nombre, notaDeCataBodega, precioARS, resenia: list[Resenia], varietal, bodega, puntaje_promedio=0):
        self.aniada = aniada
        self.imagenEtiqueta = imagenEtiqueta
        self.nombre = nombre
        self.notaDeCataBodeba = notaDeCataBodega
        self.precioARS = precioARS
        
        self.resenia = resenia  # []
        self.varietal = varietal
        self.bodega = bodega
        # TODO: PREGUNTAR SI PUEDO GUARDAR ACA EL PUNTAJE PROMEDIO
        self.puntaje_promedio = puntaje_promedio

    def tenesReseniasDeTipoEnPeriodo(self, fechaDesde, fechaHasta, resenias):
        for resenia in resenias:
            es_periodo = resenia.sosDelPeriodo(fechaDesde, fechaHasta)
            sos_sommelier = resenia.sosDeSommelier()
            if es_periodo and sos_sommelier:
                return True

    def calcularPuntajeDeSommelierEnPeriodo(self, gestor):
        acumulador = 0  # la suma de puntajes
        contador = 0  # cantidad de resenias
        fecha_desde = gestor.fechaDesde
        fecha_hasta = gestor.fechaHasta

        for resenia in self.resenia:
            if resenia.sosDeSommelier() and resenia.sosDelPeriodo(fecha_desde, fecha_hasta):
                acumulador += resenia.getPuntaje()
                contador += 1
                self.puntaje_promedio = self.calcularPuntajePromedio(acumulador, contador)


    def calcularPuntajePromedio(self, acumulador, contador):
        if contador != 0:
            return acumulador / contador
        else:
            return 0


    def getNombre(self):
        return self.nombre


    def getPrecio(self):
        return self.precioARS


    def buscarInfoBodega(self):
        nombre = self.bodega.getNombre()
        region_y_pais = self.bodega.obtenerRegionYPais()
        return nombre, region_y_pais


    # Loop en DS -> aclara que solo tiene un Varietal en los CU
    def buscarVarietal(self):
        return self.varietal.getDescripcion()



vino1 = Vino(
    2020, "img_etiqueta_1.jpg", "Cabernet Sauvignon", "Notas de cata ricas y complejas", 1500.00,
    [
        Resenia("Un vino excepcional", True, '2021-02-10', 9, None),
        Resenia("Muy bueno", True, '2021-05-12', 8, None)
    ],
    Varietal("Aromas a frutas rojas", 80),
    Bodega('2019-08-15', "Bodega Norton", "Historia de Bodega Norton", "Descripción detallada de Bodega Norton",
           RegionVitivinicola("Región vitivinícola de Mendoza", "Mendoza", Provincia("Mendoza", Pais("Argentina"))))
)

vino2 = Vino(
    2019, "img_etiqueta_2.jpg", "Merlot", "Aromas a frutas negras y especias", 1300.00,
    [
        Resenia("Sabor suave y aterciopelado", False, '2020-09-12', 8, None),
        Resenia("No me gustó", False, '2020-11-25', 6, None)
    ],
    Varietal("Toques de roble", 70),
    Bodega('2018-07-20', "Bodega Catena Zapata", "Historia de Catena Zapata", "Descripción detallada de Catena Zapata",
           RegionVitivinicola("Región vitivinícola de Salta", "Salta", Provincia("Salta", Pais("Argentina"))))
)

vino3 = Vino(
    2021, "img_etiqueta_3.jpg", "Syrah", "Cuerpo robusto y taninos presentes", 1600.00,
    [
        Resenia("Ideal para carnes rojas", True, '2024-05-10', 9, None),
        Resenia("Muy sabroso", True, '2024-05-15', 8, None),
        Resenia("Buenísimo", True, '2024-05-18', 9, None)
    ],
    Varietal("Aromas intensos a especias", 85),
    Bodega('2020-04-11', "Bodega Luigi Bosca", "Historia de Luigi Bosca", "Descripción detallada de Luigi Bosca",
           RegionVitivinicola("Región vitivinícola de La Rioja", "La Rioja", Provincia("La Rioja", Pais("Argentina"))))
)

vino4 = Vino(
    2018, "img_etiqueta_4.jpg", "Malbec", "Notas de ciruela y frambuesa", 1400.00,
    [
        Resenia("Perfecto con asados", True, '2019-06-18', 10, None),
        Resenia("Impresionante", True, '2019-07-25', 9, None)
    ],
    Varietal("Sabor afrutado", 90),
    Bodega('2021-03-25', "Bodega Trapiche", "Historia de Trapiche", "Descripción detallada de Trapiche",
           RegionVitivinicola("Región vitivinícola de San Juan", "San Juan", Provincia("San Juan", Pais("Argentina"))))
)

vino5 = Vino(
    2017, "img_etiqueta_5.jpg", "Chardonnay", "Aromas a manzana y cítricos", 1200.00,
    [
        Resenia("Fresco y vibrante", False, '2018-05-10', 7, None),
        Resenia("Demasiado ácido", False, '2018-07-20', 6, None)
    ],
    Varietal("Aromas florales", 65),
    Bodega('2017-01-30', "Bodega Rutini", "Historia de Rutini", "Descripción detallada de Rutini",
           RegionVitivinicola("Región vitivinícola de Patagonia", "Patagonia", Provincia("Río Negro", Pais("Argentina"))))
)

vino6 = Vino(
    2022, "img_etiqueta_6.jpg", "Pinot Noir", "Aromas a cerezas y frambuesas", 1800.00,
    [
        Resenia("Elegante y complejo", True, '2023-02-02', 9, None),
    ],
    Varietal("Aromas frutales", 75),
    Bodega('2016-07-15', "Bodega López", "Historia de López", "Descripción detallada de López",
           RegionVitivinicola("Región vitivinícola de Mendoza", "Mendoza", Provincia("Mendoza", Pais("Argentina"))))
)

vino7 = Vino(
    2020, "img_etiqueta_7.jpg", "Tempranillo", "Aromas a bayas oscuras", 1250.00,
    [
        Resenia("Buena acidez y equilibrio", False, '2021-04-17', 8, None),
        Resenia("No está mal", False, '2021-05-20', 7, None)
    ],
    Varietal("Aromas a especias", 70),
    Bodega('2017-09-23', "Bodega El Esteco", "Historia de El Esteco", "Descripción detallada de El Esteco",
           RegionVitivinicola("Región vitivinícola de Salta", "Salta", Provincia("Salta", Pais("Argentina"))))
)

vino8 = Vino(
    2018, "img_etiqueta_8.jpg", "Sauvignon Blanc", "Notas de hierbas frescas", 1350.00,
    [
        Resenia("Fresco y mineral", True, '2019-11-12', 9, None)
    ],
    Varietal("Aromas herbales", 80),
    Bodega('2018-05-05', "Bodega Amalaya", "Historia de Amalaya", "Descripción detallada de Amalaya",
           RegionVitivinicola("Región vitivinícola de La Rioja", "La Rioja", Provincia("La Rioja", Pais("Argentina"))))
)

vino9 = Vino(
    2019, "img_etiqueta_9.jpg", "Torrontés", "Aromas florales y cítricos", 1450.00,
    [
        Resenia("Ligero y refrescante", False, '2020-07-08', 8, None)
    ],
    Varietal("Aromas florales", 75),
    Bodega('2019-10-28', "Bodega Colomé", "Historia de Colomé", "Descripción detallada de Colomé",
           RegionVitivinicola("Región vitivinícola de Salta", "Salta", Provincia("Salta", Pais("Argentina"))))
)

vino10 = Vino(
    2021, "img_etiqueta_10.jpg", "Bonarda", "Aromas a frutas maduras", 1500.00,
    [
        Resenia("Gran relación calidad-precio", True, '2024-05-18', 9, None)
    ],
    Varietal("Aromas a frutas rojas", 85),
    Bodega('2018-12-12', "Bodega La Rural", "Historia de La Rural", "Descripción detallada de La Rural",
           RegionVitivinicola("Región vitivinícola de Mendoza", "Mendoza", Provincia("Mendoza", Pais("Argentina"))))
)


vinos_generales = [vino1, vino2, vino3, vino4, vino5, vino6, vino7, vino8, vino9, vino10]


# prueba mostrar el PRIMER comentario de las reseñas de los vinos
for vino in vinos_generales:
    print(vino.resenia[0].comentario)