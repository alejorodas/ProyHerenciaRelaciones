from ProyHerenciaRelaciones.model import ProductoControl as pc

class ProductoFertilizante(pc.ProductoControl):
  def __init__(self, registro_ica, nombre_producto, frecuencia_aplicacion, fecha_aplicacion):
    super().__init__(registro_ica, nombre_producto, frecuencia_aplicacion)
    self.__fecha_aplicacion = fecha_aplicacion

  @property
  def fecha_aplicacion(self):
    return self.__fecha_aplicacion

  @fecha_aplicacion.setter
  def fecha_aplicacion(self, fecha_aplicacion):
    self.__fecha_aplicacion =   fecha_aplicacion