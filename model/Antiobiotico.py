class Antibiotico:
  def __init__(self, nombre_producto, dosis, tipo_animal):
    self.__nombre_producto = nombre_producto
    self.__dosis = dosis
    self.__tipo_animal = tipo_animal
  
  @property
  def nombre_producto(self):
    return self.__nombre_producto
  
  @nombre_producto.setter
  def nombre_producto(self, nombre_producto):
    self.__nombre_producto = nombre_producto

  @property
  def dosis(self):
    return self.__dosis

  @dosis.setter
  def dosis(self, dosis):
    self.__dosis = dosis

  @property
  def tipo_animal(self):
    return self.__tipo_animal

  @dosis.setter
  def tipo_animal(self, tipo_animal):
    self.__tipo_animal = tipo_animal