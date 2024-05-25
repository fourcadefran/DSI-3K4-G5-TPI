from Entity.Resenia import Resenia
from Entity.Varietal import Varietal
from Entity.Bodega import Bodega
from Entity.Vino import Vino

resenia1 = Resenia('asda', True, '1213', 10)
varietal1 = Varietal('varietal1', 'adasd')
bodega1 = Bodega(123, 'qsy', 'asd', 'asdasd')

vino1 = Vino(12, 'a', 'toro', 'rico', 1200, resenia1, varietal1, bodega1)

print(vino1.buscarInfoBodega())


