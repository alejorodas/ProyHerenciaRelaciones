import unittest
from ProyHerenciaRelaciones.model import  Factura as factura
from ProyHerenciaRelaciones.model import  ProductoPlaga as producto_plaga
from ProyHerenciaRelaciones.model import  ProductoFertilizante as producto_fertilizante
from ProyHerenciaRelaciones.model import Antiobiotico as antiobiotico

class TestFactura(unittest.TestCase):
  def setUp(self):
    self.pc_plaga = producto_plaga.ProductoPlaga("ABC23", "plagaX", "20","15")
    self.pc_fertilizante = producto_fertilizante.ProductoFertilizante("WER98", "fertec-X", "8","20")
    self.fact = factura.Factura()


  def test_vende_varios_producto_control(self):
    self.fact.asociar_producto_control(self.pc_plaga)
    self.fact.asociar_producto_control(self.pc_fertilizante)
    
    self.assertEqual(2,len(self.fact.producto_control), "No se ha asociado producto control")
    
  def test_vende_varios_antibiotico(self):
    anti_1 = antiobiotico.Antibiotico("anti_1", "10ml", "bovino")
    anti_2 = antiobiotico.Antibiotico("anti_2", "8ml", "caprino")
    self.fact.asociar_antibiotico(anti_1)
    self.fact.asociar_antibiotico(anti_2)

    self.assertEqual(2,len(self.fact.antibiotico), "No se ha asociado antibiotico")
    
  def test_vende_varios_producto_control_antibiotico(self):
    anti_1 = antiobiotico.Antibiotico("anti_1", "10ml", "bovino")
    anti_2 = antiobiotico.Antibiotico("anti_2", "8ml", "caprino")
    pc_plaga = producto_plaga.ProductoPlaga("ABC23", "plagaX", "20","15")
    pc_fertilizante = producto_fertilizante.ProductoFertilizante("WER98", "fertec-X", "8","20")
    
    self.fact.asociar_producto_control(pc_plaga)
    self.fact.asociar_producto_control(pc_fertilizante)
    self.fact.asociar_antibiotico(anti_1)
    self.fact.asociar_antibiotico(anti_2)
    
    self.assertEqual(2, len(self.fact.antibiotico), "No se han asociado antibioticos")
    self.assertEqual(2, len(self.fact.producto_control), "No se han asociado productos control")

if __name__ == '__main__':
  unittest.main()
