import sys
sys.path.append('../app')

import unittest
from protocol import *

class SerializeMessageTests(unittest.TestCase):

    def test_can_serialize_simple_string(self):

        message = "OK"

        serialized_message = serialize_simple_string(message)

        asserted_serialized_message = b"+OK\r\n"

        self.assertIsNotNone(serialized_message)
        self.assertEqual(serialized_message, asserted_serialized_message)

    def test_can_serialize_error_message(self):

        message = "Error message"

        serialized_message = serialized_error_message(message)

        asserted_serialized_message = b"-Error message\r\n"

if __name__ == '__main__':
    unittest.main()
