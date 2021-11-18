class Cliente:
  def __init__(self, nombre, id):
    self.__nombre = nombre
    self.__id = id
    self.__factura = []
  
  @property
  def nombre(self):
    return self.__nombre
  
  @nombre.setter
  def nombre(self, nombre):
    self.__nombre = nombre
  
  @property
  def id(self):
    return self.__id
  
  @id.setter
  def id(self, id):
    self.__id = id

  @property
  def factura(self):
    return self.__factura
  
  @factura.setter
  def factura(self, factura):
    self.__factura.append(factura)

  def asociar_factura(self, factura):
    self.factura = factura