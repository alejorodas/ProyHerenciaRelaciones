from ProyHerenciaRelaciones.model import Cliente
from ProyHerenciaRelaciones.model import ProductoFertilizante as producto_fertilizante
from ProyHerenciaRelaciones.model import ProductoPlaga as producto_plaga
from ProyHerenciaRelaciones.model import Antiobiotico as antiobiotico
from ProyHerenciaRelaciones.model import Factura as factura
from ProyHerenciaRelaciones.ui import ui_cliente as ui_cliente
from ProyHerenciaRelaciones.ui import ui_productos_control as ui_productos_control
from ProyHerenciaRelaciones.ui import ui_antibioticos as ui_antibioticos

registroClientes = []

def main():
  while input("Desea terminar: [S/N]") == "N":
    nombre, id = ui_cliente.datos_cliente()
    cliente = Cliente.Cliente(nombre, id)

    opcion = ui_productos_control.menus_seleccion_productos_control()
    if opcion == 1:
      registro_ica, nombre_producto, frecuencia_aplicacion, fecha_aplicacion = \
        ui_productos_control.menu_producto_fertilizante()
      producto = producto_fertilizante.ProductoFertilizante(registro_ica, nombre_producto, frecuencia_aplicacion,
                                                 fecha_aplicacion)
    elif opcion == 2:
      registro_ica, nombre_producto, frecuencia_aplicacion, periodo_carencia = \
        ui_productos_control.menu_producto_plaga()
      producto = producto_plaga.ProductoPlaga(registro_ica, nombre_producto, frecuencia_aplicacion,
                                   periodo_carencia)
    else:
      nombre_producto, dosis, tipo_animal = ui_antibioticos.menu_producto_antibioticos()
      producto_antibiotico = antiobiotico.Antibiotico(nombre_producto, dosis, tipo_animal)
      

    factura.Factura().realizar_venta(producto = producto, antibiotico = producto_antibiotico)
    cliente.asociar_factura(factura)
    registroClientes.append(cliente)
  else:
    print("Saliste del sistema")



if __name__ == '__main__':
  main()