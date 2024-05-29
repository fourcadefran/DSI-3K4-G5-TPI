# class interfaz excel
class InterfazExcel:
    def __init__(self):
        pass

    def exportarExcel(self, objetos):
        reporte = []
        contador = 0
        for objeto in objetos:
            if contador == 9:
                break
            reporte.append({
                "nombre": objeto[0].nombre,
                "calificacion": objeto[1],
                "precio": objeto[0].precioARS,
                "bodega": objeto[0].bodega.nombre,
                "varietal": objeto[0].varietal.descripcion,
                "region": objeto[0].bodega.region.nombre,
                "pais": objeto[0].bodega.region.provincia.pais.nombre,
            })
            contador += 1
        return reporte
