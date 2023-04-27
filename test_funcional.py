import unittest
from romanos_funcional import convertir_en_numero


class RomanosTest(unittest.TestCase):
    def test_unidades(self):
        self.assertEqual(convertir_en_numero('I'), 1)
        self.assertEqual(convertir_en_numero('V'), 5)
        self.assertEqual(convertir_en_numero('X'), 10)
        self.assertEqual(convertir_en_numero('L'), 50)
        self.assertEqual(convertir_en_numero('C'), 100,
                         "El valor de la letra C debe ser 100")
        self.assertEqual(convertir_en_numero('D'), 500)
        self.assertEqual(convertir_en_numero('M'), 1000)

    def test_numeros_basicos(self):
        self.assertEqual(convertir_en_numero("IV"), 4)
        self.assertEqual(convertir_en_numero("IX"), 9)
        self.assertEqual(convertir_en_numero("XL"), 40)
        self.assertEqual(convertir_en_numero("CCV"), 205)
        self.assertEqual(convertir_en_numero("MCXXIII"), 1123)
        self.assertEqual(convertir_en_numero('MDXC'), 1590)

    def test_no_resta_mas_de_un_orden_de_magnitud(self):
        # self.assertRaises(ValueError, convertir_en_numero, 'IC')
        # self.assertRaises(ValueError, convertir_en_numero, 'VC')
        with self.assertRaises(ValueError):
            convertir_en_numero('IC')
        with self.assertRaises(ValueError):
            convertir_en_numero('ID')
        with self.assertRaises(ValueError):
            convertir_en_numero('VC')
        with self.assertRaises(ValueError):
            convertir_en_numero('LM')

    def test_no_restas_consecutivas(self):
        self.assertRaises(ValueError, convertir_en_numero, 'CCM')
        self.assertRaises(ValueError, convertir_en_numero, 'XXC')
        self.assertRaises(ValueError, convertir_en_numero, 'MMCCMM')
        self.assertRaises(ValueError, convertir_en_numero, 'IIV')
        self.assertRaises(ValueError, convertir_en_numero, 'IIX')
        self.assertRaises(ValueError, convertir_en_numero, 'IIIX')
        self.assertRaises(ValueError, convertir_en_numero, 'IIIIX')
        self.assertRaises(ValueError, convertir_en_numero, 'IXC')

    def test_no_mas_de_tres_simbolos_iguales_consecutivos(self):
        self.assertRaises(ValueError, convertir_en_numero, 'MMMM')
        self.assertRaises(ValueError, convertir_en_numero, 'IIII')
        self.assertRaises(ValueError, convertir_en_numero, 'XXXX')

    def test_resta_imposible(self):
        self.assertRaises(ValueError, convertir_en_numero, 'XIXXIII')
        self.assertRaises(ValueError, convertir_en_numero, 'XIXX')
        self.assertRaises(ValueError, convertir_en_numero, 'IVI')
        self.assertRaises(ValueError, convertir_en_numero, 'XIXI')

    def test_no_restas_multiplos_cinco(self):
        self.assertRaises(ValueError, convertir_en_numero, 'VX')
        self.assertRaises(ValueError, convertir_en_numero, 'VXX')
        self.assertRaises(ValueError, convertir_en_numero, 'LC')
        self.assertRaises(ValueError, convertir_en_numero, 'DM')

    def test_no_simbolos_vld_repetidos(self):
        self.assertRaises(ValueError, convertir_en_numero, 'VV')
        self.assertRaises(ValueError, convertir_en_numero, 'LL')
        self.assertRaises(ValueError, convertir_en_numero, 'DD')
        self.assertRaises(ValueError, convertir_en_numero, 'DDI')


unittest.main()
