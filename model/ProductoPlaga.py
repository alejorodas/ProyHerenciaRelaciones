from ProyHerenciaRelaciones.model import ProductoControl as pc

class ProductoPlaga(pc.ProductoControl):
  def __init__(self, registro_ica, nombre_producto, frecuencia_aplicacion, periodo_carencia):
    super().__init__(registro_ica, nombre_producto, frecuencia_aplicacion)
    self.__periodo_carencia = periodo_carencia

  @property
  def periodo_carencia(self):
    return self.__periodo_carencia

  @periodo_carencia.setter
  def periodo_carencia(self, periodo_carencia):
    self.__periodo_carencia = periodo_carencia