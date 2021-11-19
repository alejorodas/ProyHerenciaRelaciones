from ProyHerenciaRelaciones.model.ProductoControl import ProductoControl as pc

class Factura:
  def __init__(self):
    self.__antibiotico = []
    self.__producto_control = []
    
  @property
  def antibiotico(self):
    return self.__antibiotico
  
  @antibiotico.setter
  def antibiotico(self,antibiotico):
    self.__antibiotico.append(antibiotico)

  @property
  def producto_control(self):
    return self.__producto_control
  
  @producto_control.setter
  def producto_control(self, producto_control):
    self.__producto_control.append(producto_control)


  def asociar_producto_control(self,producto_control):
    self.producto_control = producto_control

  def asociar_antibiotico(self, antibiotico):
    self.antibiotico = antibiotico
    
  def realizar_venta(self, producto_control = None, antibiotico = None):
    if producto_control != None:
      self.asociar_producto_control(producto_control)
    if antibiotico != None:
      self.asociar_antibiotico(antibiotico)