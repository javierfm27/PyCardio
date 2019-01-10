
import unittest

from PyCardio.HRV.HRV import HRV

class TestPycardio(unittest.TestCase):

    #Test Básico para crear un objeto HRV()
    def test_create_HRV(self):
        x = HRV()
        self.assertIsInstance(x,HRV)

if __name__ == '__main__':
    unittest.main()
