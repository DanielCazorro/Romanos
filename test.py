from romanos import RomanNumber
import unittest

class RomanosTest(unittest.TestCase):

    def test_crear_numero_romano_desde_entero(self):
        # Prueba de creación de números romanos desde enteros
        numero_uno = RomanNumber(1)
        self.assertEqual(numero_uno.valor, 1)
        self.assertEqual(str(numero_uno), "I")

        numero_dos = RomanNumber(2)
        self.assertEqual(numero_dos.valor, 2)
        self.assertEqual(str(numero_dos), "II")

        numero = RomanNumber(1123)
        self.assertEqual(numero.valor, 1123)
        self.assertEqual(str(numero), "MCXXIII")

    def test_crear_numero_romano_desde_cadena(self):
        # Prueba de creación de números romanos desde cadenas
        numero_uno = RomanNumber("I")
        self.assertEqual(numero_uno.valor, 1)
        self.assertEqual(str(numero_uno), "I")

        numero = RomanNumber("MCXXIII")
        self.assertEqual(numero.valor, 1123)
        self.assertEqual(str(numero), "MCXXIII")

    def test_comprobar_igualdad(self):
        # Prueba de comprobar igualdad entre números romanos
        uno = RomanNumber(1)
        otro_uno = RomanNumber(1)
        dos = RomanNumber(2)

        self.assertEqual(uno, otro_uno)
        self.assertNotEqual(uno, dos)
        self.assertNotEqual(otro_uno, dos)

    def test_suma(self):
        # Prueba de la operación de suma
        uno = RomanNumber(1)
        dos = RomanNumber(2)

        self.assertEqual(uno + dos, 3)
        self.assertEqual(uno + 3, 4)
        self.assertEqual(uno + "IV", 5)

if __name__ == '__main__':
    unittest.main()
