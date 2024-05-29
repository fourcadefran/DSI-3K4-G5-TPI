from Entity.Resenia import Resenia
from Entity.Varietal import Varietal
from Entity.Bodega import Bodega
from Entity.Vino import Vino
from Entity.RegionVitivinicola import RegionVitivinicola
from Entity.Provincia import Provincia
from Entity.Pais import Pais

vino1 = Vino(
    2020, "img_etiqueta_1.jpg", "Cabernet Sauvignon", "Notas de cata ricas y complejas", 1500.00, 
    [
        Resenia("Un vino excepcional", True, '10-02-2021', 9, None),
        Resenia("Muy bueno", True, '12-05-2021', 8, None)
    ], 
    Varietal("Aromas a frutas rojas", 80), 
    Bodega('15-08-2019', "Bodega Norton", "Historia de Bodega Norton", "Descripción detallada de Bodega Norton", 
           RegionVitivinicola("Región vitivinícola de Mendoza", "Mendoza", Provincia("Mendoza", Pais("Argentina"))))
)

vino2 = Vino(
    2019, "img_etiqueta_2.jpg", "Merlot", "Aromas a frutas negras y especias", 1300.00, 
    [
        Resenia("Sabor suave y aterciopelado", False, '12-09-2020', 8, None),
        Resenia("No me gustó", False, '25-11-2020', 6, None)
    ], 
    Varietal("Toques de roble", 70), 
    Bodega('20-07-2018', "Bodega Catena Zapata", "Historia de Catena Zapata", "Descripción detallada de Catena Zapata", 
           RegionVitivinicola("Región vitivinícola de Salta", "Salta", Provincia("Salta", Pais("Argentina"))))
)

vino3 = Vino(
    2021, "img_etiqueta_3.jpg", "Syrah", "Cuerpo robusto y taninos presentes", 1600.00, 
    [
        Resenia("Ideal para carnes rojas", True, '05-11-2022', 9, None),
        Resenia("Muy sabroso", True, '10-01-2023', 8, None),
        Resenia("Buenísimo", True, '18-02-2023', 9, None)
    ], 
    Varietal("Aromas intensos a especias", 85), 
    Bodega('11-04-2020', "Bodega Luigi Bosca", "Historia de Luigi Bosca", "Descripción detallada de Luigi Bosca", 
           RegionVitivinicola("Región vitivinícola de La Rioja", "La Rioja", Provincia("La Rioja", Pais("Argentina"))))
)

vino4 = Vino(
    2018, "img_etiqueta_4.jpg", "Malbec", "Notas de ciruela y frambuesa", 1400.00, 
    [
        Resenia("Perfecto con asados", True, '18-06-2019', 10, None),
        Resenia("Impresionante", True, '25-07-2019', 9, None)
    ], 
    Varietal("Sabor afrutado", 90), 
    Bodega('25-03-2021', "Bodega Trapiche", "Historia de Trapiche", "Descripción detallada de Trapiche", 
           RegionVitivinicola("Región vitivinícola de San Juan", "San Juan", Provincia("San Juan", Pais("Argentina"))))
)

vino5 = Vino(
    2017, "img_etiqueta_5.jpg", "Chardonnay", "Aromas a manzana y cítricos", 1200.00, 
    [
        Resenia("Fresco y vibrante", False, '10-05-2018', 7, None),
        Resenia("Demasiado ácido", False, '20-07-2018', 6, None)
    ], 
    Varietal("Aromas florales", 65), 
    Bodega('30-01-2017', "Bodega Rutini", "Historia de Rutini", "Descripción detallada de Rutini", 
           RegionVitivinicola("Región vitivinícola de Patagonia", "Patagonia", Provincia("Río Negro", Pais("Argentina"))))
)

vino6 = Vino(
    2022, "img_etiqueta_6.jpg", "Pinot Noir", "Aromas a cerezas y frambuesas", 1800.00, 
    [
        Resenia("Elegante y complejo", True, '02-02-2023', 9, None),
    ], 
    Varietal("Aromas frutales", 75), 
    Bodega('15-07-2016', "Bodega López", "Historia de López", "Descripción detallada de López", 
           RegionVitivinicola("Región vitivinícola de Mendoza", "Mendoza", Provincia("Mendoza", Pais("Argentina"))))
)

vino7 = Vino(
    2020, "img_etiqueta_7.jpg", "Tempranillo", "Aromas a bayas oscuras", 1250.00, 
    [
        Resenia("Buena acidez y equilibrio", False, '17-04-2021', 8, None),
        Resenia("No está mal", False, '20-05-2021', 7, None)
    ], 
    Varietal("Aromas a especias", 70), 
    Bodega('23-09-2017', "Bodega El Esteco", "Historia de El Esteco", "Descripción detallada de El Esteco", 
           RegionVitivinicola("Región vitivinícola de Salta", "Salta", Provincia("Salta", Pais("Argentina"))))
)

vino8 = Vino(
    2018, "img_etiqueta_8.jpg", "Sauvignon Blanc", "Notas de hierbas frescas", 1350.00, 
    [
        Resenia("Fresco y mineral", True, '12-11-2019', 9, None)
    ], 
    Varietal("Aromas herbales", 80), 
    Bodega('05-05-2018', "Bodega Amalaya", "Historia de Amalaya", "Descripción detallada de Amalaya", 
           RegionVitivinicola("Región vitivinícola de La Rioja", "La Rioja", Provincia("La Rioja", Pais("Argentina"))))
)

vino9 = Vino(
    2019, "img_etiqueta_9.jpg", "Torrontés", "Aromas florales y cítricos", 1450.00, 
    [
        Resenia("Ligero y refrescante", False, '08-07-2020', 8, None)
    ], 
    Varietal("Aromas florales", 75), 
    Bodega('28-10-2019', "Bodega Colomé", "Historia de Colomé", "Descripción detallada de Colomé", 
           RegionVitivinicola("Región vitivinícola de Salta", "Salta", Provincia("Salta", Pais("Argentina"))))
)

vino10 = Vino(
    2021, "img_etiqueta_10.jpg", "Bonarda", "Aromas a frutas maduras", 1500.00, 
    [
        Resenia("Gran relación calidad-precio", True, '15-03-2022', 9, None)
    ], 
    Varietal("Aromas a frutas rojas", 85), 
    Bodega('12-12-2018', "Bodega La Rural", "Historia de La Rural", "Descripción detallada de La Rural", 
           RegionVitivinicola("Región vitivinícola de Mendoza", "Mendoza", Provincia("Mendoza", Pais("Argentina"))))
)


vinos_general = [vino1, vino2, vino3, vino4, vino5, vino6, vino7, vino8, vino9, vino10]
