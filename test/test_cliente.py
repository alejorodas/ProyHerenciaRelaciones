import unittest
from ProyHerenciaRelaciones.model import Cliente as cliente
from ProyHerenciaRelaciones.model import Factura as factura
from ProyHerenciaRelaciones.model import  ProductoPlaga as producto_plaga
from ProyHerenciaRelaciones.model import  ProductoFertilizante as producto_fertilizante
from ProyHerenciaRelaciones.model import Antiobiotico as antiobiotico

class TestCliente(unittest.TestCase):
  def setUp(self):
    self.factura_1 = factura.Factura()
    self.factura_2 = factura.Factura()
    
    self.c = cliente.Cliente("william wallace", "666")
    self.pc_plaga = producto_plaga.ProductoPlaga("ABC23", "plagaX", "20","15")
    self.pc_fertilizante = producto_fertilizante.ProductoFertilizante("WER98", "fertec-X", "8","20")
    self.anti_1 = antiobiotico.Antibiotico("anti_1", "10ml", "bovino")
    self.anti_2 = antiobiotico.Antibiotico("anti_2", "8ml", "caprino")
  
  def test_cliente_tiene_varias_facturas_asociadas(self):
    self.factura_1.asociar_antibiotico(self.anti_1)
    self.factura_1.asociar_antibiotico(self.anti_2)
    self.factura_1.asociar_producto_control(self.pc_plaga)
    self.factura_1.asociar_producto_control(self.pc_fertilizante)
    
    self.factura_2.asociar_antibiotico(self.anti_1)
    self.factura_2.asociar_antibiotico(self.anti_2)
    self.factura_2.asociar_producto_control(self.pc_plaga)
    self.factura_2.asociar_producto_control(self.pc_fertilizante)
    
    self.c.asociar_factura(self.factura_1)
    self.c.asociar_factura(self.factura_2)
    
    self.assertEqual(2, len(self.c.factura), "Cliente no tiene facturas asociadas")


if __name__ == '__main__':
  unittest.main()