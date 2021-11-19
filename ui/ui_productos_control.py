def menus_seleccion_productos_control():
  msj = """
  1. Productos Fertilizante
  2. Producto Plagas
  3. Antibioticos
  """
  return input(msj)

def menu_producto_fertilizante():
  registro_ica = input("Digite Registro ICA")
  nombre_producto = input("Digite Nombre Producto")
  frecuencia_aplicacion = input("Digite Frecuencia Aplicacion")
  fecha_aplicacion = input("Digite Fecha Aplicacion")
  
  return [registro_ica, nombre_producto, frecuencia_aplicacion, fecha_aplicacion]

def menu_producto_plaga():
  registro_ica = input("Digite Registro ICA")
  nombre_producto = input("Digite Nombre Producto")
  frecuencia_aplicacion = input("Digite Frecuencia Aplicacion")
  periodo_carencia = input("Digite Periodo Carencia")
  
  return [registro_ica, nombre_producto, frecuencia_aplicacion, periodo_carencia]