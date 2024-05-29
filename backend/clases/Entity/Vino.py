from clases.Entity.Bodega import Bodega
from clases.Entity.Resenia import Resenia
from clases.Entity.Varietal import Varietal
from clases.Entity.RegionVitivinicola import RegionVitivinicola
from clases.Entity.Provincia import Provincia
from clases.Entity.Pais import Pais


class Vino:
    def __init__(self, aniada, imagenEtiqueta, nombre, notaDeCataBodega, precioARS, resenia: list[Resenia], varietal, bodega):
        self.aniada = aniada
        self.imagenEtiqueta = imagenEtiqueta
        self.nombre = nombre
        self.notaDeCataBodeba = notaDeCataBodega
        self.precioARS = precioARS
        
        self.resenia = resenia  # []
        self.varietal = varietal
        self.bodega = bodega


    def tenesReseniasDeTipoEnPeriodo(self, fechaDesde, fechaHasta, resenias):
        for resenia in resenias:
            es_periodo = resenia.sosDelPeriodo(fechaDesde, fechaHasta)
            sos_sommelier = resenia.sosDeSommelier()
            if es_periodo and sos_sommelier:
                return True

    def calcularPuntajeDeSommelierEnPeriodo(self, gestor):
        acumulador_de_puntaje_sommelier = 0  # la suma de puntajes de las resenias de sommelier

        fecha_desde = gestor.fechaDesde
        fecha_hasta = gestor.fechaHasta

        for resenia in self.resenia:
            if resenia.sosDeSommelier() and resenia.sosDelPeriodo(fecha_desde, fecha_hasta):
                acumulador_de_puntaje_sommelier += resenia.getPuntaje()
        return acumulador_de_puntaje_sommelier



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

vino11 = Vino(
    2022, "img_etiqueta_11.jpg", "Viognier", "Aromas a durazno y albaricoque", 1700.00, 
    [
        Resenia("Excelente para mariscos", True, '10-05-2023', 9, None),
        Resenia("Muy floral", True, '12-06-2023', 8, None)
    ], 
    Varietal("Aromas frutales y florales", 85), 
    Bodega('10-10-2019', "Bodega Familia Schroeder", "Historia de Familia Schroeder", "Descripción detallada de Familia Schroeder", 
           RegionVitivinicola("Región vitivinícola de Patagonia", "Patagonia", Provincia("Neuquén", Pais("Argentina"))))
)

vino12 = Vino(
    2021, "img_etiqueta_12.jpg", "Petit Verdot", "Notas de frutos negros y violetas", 1600.00, 
    [
        Resenia("Muy buen cuerpo", True, '18-07-2022', 9, None),
        Resenia("Un vino con carácter", True, '22-08-2022', 8, None)
    ], 
    Varietal("Aromas a frutos oscuros", 80), 
    Bodega('05-04-2020', "Bodega Pulenta Estate", "Historia de Pulenta Estate", "Descripción detallada de Pulenta Estate", 
           RegionVitivinicola("Región vitivinícola de Mendoza", "Mendoza", Provincia("Mendoza", Pais("Argentina"))))
)

vino13 = Vino(
    2019, "img_etiqueta_13.jpg", "Cabernet Franc", "Aromas a pimiento y especias", 1500.00, 
    [
        Resenia("Perfecto para platos especiados", False, '12-10-2020', 8, None),
        Resenia("Sabor fuerte", False, '15-11-2020', 7, None)
    ], 
    Varietal("Aromas especiados", 70), 
    Bodega('20-06-2018', "Bodega Doña Paula", "Historia de Doña Paula", "Descripción detallada de Doña Paula", 
           RegionVitivinicola("Región vitivinícola de San Juan", "San Juan", Provincia("San Juan", Pais("Argentina"))))
)

vino14 = Vino(
    2020, "img_etiqueta_14.jpg", "Grenache", "Aromas a frambuesas y fresas", 1450.00, 
    [
        Resenia("Muy afrutado", True, '05-02-2021', 9, None),
        Resenia("Ideal para días calurosos", True, '10-03-2021', 8, None)
    ], 
    Varietal("Aromas frutales intensos", 80), 
    Bodega('25-11-2017', "Bodega El Porvenir", "Historia de El Porvenir", "Descripción detallada de El Porvenir", 
           RegionVitivinicola("Región vitivinícola de Salta", "Salta", Provincia("Salta", Pais("Argentina"))))
)

vino15 = Vino(
    2018, "img_etiqueta_15.jpg", "Zinfandel", "Notas de moras y vainilla", 1500.00, 
    [
        Resenia("Muy suave y equilibrado", True, '22-08-2019', 9, None),
        Resenia("Un poco dulce", True, '30-09-2019', 8, None),
        Resenia("Perfecto para una cena especial", True, '05-12-2019', 9, None),
        Resenia("Excelente relación calidad-precio", True, '10-01-2020', 9, None)
    ], 
    Varietal("Aromas a frutas maduras", 75), 
    Bodega('05-03-2016', "Bodega Humberto Canale", "Historia de Humberto Canale", "Descripción detallada de Humberto Canale", 
           RegionVitivinicola("Región vitivinícola de Patagonia", "Patagonia", Provincia("Río Negro", Pais("Argentina"))))
)

vino16 = Vino(
    2021, "img_etiqueta_16.jpg", "Sangiovese", "Aromas a cerezas y tabaco", 1600.00, 
    [
        Resenia("Perfecto con pasta", True, '10-05-2022', 9, None),
        Resenia("Gran estructura", True, '15-06-2022', 8, None),
        Resenia("Muy buen vino para su precio", True, '10-09-2022', 9, None),
        Resenia("Aromas intensos y complejos", True, '20-10-2022', 8, None)
    ], 
    Varietal("Aromas frutales y especiados", 85), 
    Bodega('10-07-2019', "Bodega Navarro Correas", "Historia de Navarro Correas", "Descripción detallada de Navarro Correas", 
           RegionVitivinicola("Región vitivinícola de Mendoza", "Mendoza", Provincia("Mendoza", Pais("Argentina"))))
)

vino17 = Vino(
    2020, "img_etiqueta_17.jpg", "Riesling", "Aromas a manzana verde y miel", 1400.00, 
    [
        Resenia("Muy fresco y vibrante", True, '12-04-2021', 9, None),
        Resenia("Un poco dulce para mi gusto", True, '18-05-2021', 8, None),
        Resenia("Ideal para acompañar postres", True, '05-08-2021', 8, None),
        Resenia("Excelente para una tarde de verano", True, '20-09-2021', 9, None)
    ], 
    Varietal("Aromas florales y frutales", 80), 
    Bodega('15-01-2018', "Bodega Luigi Bosca", "Historia de Luigi Bosca", "Descripción detallada de Luigi Bosca", 
           RegionVitivinicola("Región vitivinícola de La Rioja", "La Rioja", Provincia("La Rioja", Pais("Argentina"))))
)

vino18 = Vino(
    2022, "img_etiqueta_18.jpg", "Moscato", "Aromas a flores blancas y cítricos", 1200.00, 
    [
        Resenia("Muy dulce y aromático", True, '22-03-2023', 8, None),
        Resenia("Perfecto para postres", True, '10-04-2023', 9, None),
        Resenia("Ideal para una tarde de verano", True, '05-06-2023', 8, None),
        Resenia("Excelente para una fiesta", True, '12-07-2023', 9, None)
    ], 
    Varietal("Aromas frutales y florales", 75), 
    Bodega('18-08-2020', "Bodega Santa Julia", "Historia de Santa Julia", "Descripción detallada de Santa Julia", 
           RegionVitivinicola("Región vitivinícola de Mendoza", "Mendoza", Provincia("Mendoza", Pais("Argentina"))))
)

vino19 = Vino(
    2020, "img_etiqueta_19.jpg", "Rosado", "Aromas a fresas y melón", 1100.00, 
    [
        Resenia("Muy fresco y afrutado", False, '05-11-2021', 8, None),
        Resenia("Ideal para verano", False, '12-12-2021', 7, None)
    ], 
    Varietal("Aromas a frutas rojas", 65), 
    Bodega('15-10-2019', "Bodega Séptima", "Historia de Séptima", "Descripción detallada de Séptima", 
           RegionVitivinicola("Región vitivinícola de Mendoza", "Mendoza", Provincia("Mendoza", Pais("Argentina"))))
)

vino20 = Vino(
    2021, "img_etiqueta_20.jpg", "Garnacha", "Notas de frambuesas y hierbas", 1350.00, 
    [
        Resenia("Muy afrutado y fresco", True, '10-06-2022', 9, None),
        Resenia("Sabor complejo", True, '15-07-2022', 8, None)
    ], 
    Varietal("Aromas frutales y herbales", 80), 
    Bodega('25-02-2020', "Bodega Finca Las Moras", "Historia de Finca Las Moras", "Descripción detallada de Finca Las Moras", 
           RegionVitivinicola("Región vitivinícola de San Juan", "San Juan", Provincia("San Juan", Pais("Argentina"))))
)

vino21 = Vino(
    2018, "img_etiqueta_21.jpg", "Carmenere", "Aromas a frutas negras y especias", 1500.00, 
    [
        Resenia("Muy especiado y complejo", True, '05-09-2019', 9, None),
        Resenia("Buen cuerpo", True, '12-10-2019', 8, None)
    ], 
    Varietal("Aromas a frutas maduras", 80), 
    Bodega('10-11-2017', "Bodega Alta Vista", "Historia de Alta Vista", "Descripción detallada de Alta Vista", 
           RegionVitivinicola("Región vitivinícola de Mendoza", "Mendoza", Provincia("Mendoza", Pais("Argentina"))))
)


vinos_generales = [vino1, vino2, vino3, vino4, vino5, vino6, vino7, vino8, vino9, vino10, vino11, vino12, vino13, 
                   vino14, vino15, vino16, vino17, vino18, vino19, vino20, vino21]

