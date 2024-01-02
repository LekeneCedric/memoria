import unittest
from test_protocol import ProtocolTest

if __name__ == '__main__':

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(ProtocolTest))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)
