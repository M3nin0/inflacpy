import unittest
from scrap_test import ScrapTest

suite = unittest.TestSuite()

# Adicionando os testes
suite.addTest(unittest.makeSuite(ScrapTest))
