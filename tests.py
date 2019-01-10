
import unittest

from PyCardio.HRV.HRV import HRV

class TestPycardio(unittest.TestCase):

    def test_create_HRV(self):
        x = HRV()
        aseertIsInstance(HRV,HRV)

if __name__ == '__main__':
    unittest.main()
