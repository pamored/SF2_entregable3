import unittest
from game import Juego

class testJuego(unittest.TestCase):
    def __init__(self):
        pass
    def testnombreVentana(self):
        juego=Juego()
        nombre_ventana=juego.set_nombre_ventana
        self.assertEqual(nombre_ventana,"Prueba de jugabilidad")
    

if __name__ == '__main__':
    unittest.main()