#from django.test import TestCase
#from catalogo.forms import ProductoForm


#class TestForms(TestCase):

 #   def test_producto_form_valid_data(self):
  ##      form = ProductoForm(data={
    #        'nombre': 'asus',
     #       'categoria': 'notebook',
      #      'marca': 'asus'
       # })

        #self.assertTrue(form.is_valid())
    
#    def test_producto_nombre_valid(self):
 ##       form = ProductoForm(data={'nombre': 'asus'})
   #     self.assertTrue(form.is_valid())
    
   # def test_producto_marca_no_valid(self):
    ##    form = ProductoForm(data={'marca': '123$$`+'})
      #  self.assertFalse(form.is_valid())

    #def test_producto_categoria_no_valid(self):
     #   form = ProductoForm(data={'categoria': 'telefono'})
      #  self.assertFalse(form.is_valid())

    #def test_producto_no_data(self):
       # form = ProductoForm(data={})
     #   self.assertFalse(form.is_valid())
      #  self.assertEquals(len(form.errors), 8)