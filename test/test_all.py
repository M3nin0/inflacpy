import unittest
from test.scrap_test import ScrapTest

suite = unittest.TestSuite()

# Adicionando os testes
suite.addTest(unittest.makeSuite(ScrapTest))
