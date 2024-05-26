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
                "nombre": objeto.nombre,
                "calificacion": objeto.puntaje_promedio,
                "precio": objeto.precioARS,
                "bodega": objeto.bodega.nombre,
                "varietal": objeto.varietal.descripcion,
                "region": objeto.bodega.region.nombre,
                "pais": objeto.bodega.region.provincia.pais.nombre,
            })
            contador += 1
        return reporte
