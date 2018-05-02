import unittest

from inflacpy.scrap.scrap import Scrap


class ScrapTest(unittest.TestCase):
    scrap = None

    def setUp(self):
        self.scrap = Scrap()

    def tearDown(self):
        self.scrap = None

    def testA(self):
        """ Método de teste do get_data. Espera-se uma lista
        com os valores de inflação
        :rtype: None
        """
        self.assertTrue(self.scrap.get_data(2016, 2016, 'brasil'))

    def testB(self):
        """ Teste do método get_data. Espera-se deste exceção, já que
        a data inserida não é válida
        :rtype: None
        """
        with self.assertRaises(Exception) as context:
            self.scrap.get_data(2027, 2027, 'brasil')

        self.assertTrue('list index out of range' in str(context.exception))

    def testC(self):
        """ Teste do método get_data. Espera-se deste exceção, já que
        o país inserido é inválido
        :rtype: None
        """
        with self.assertRaises(Exception) as context:
            self.scrap.get_data(2016, 2016, 'UM_PAIS')

        self.assertTrue('list index out of range' in str(context.exception))
