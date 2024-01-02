import sys
sys.path.append('../app')

import unittest
from protocol import *

class DeserializeMessagesTest(unittest.TestCase):

    def test_can_deserialize_simple_string(self):
        encoded_message = b"+OK\r\n"

        decoded_message = deserialize_simple_string(encoded_message)

        asserted_decoded_message = "OK"

        self.assertIsNotNone(decoded_message)
        self.assertEqual(decoded_message, asserted_decoded_message)

    def test_can_deserialize_error_message(self):
        encoded_message = b"-Error message\r\n"

        decoded_message = deserialize_error_message(encoded_message)

        asserted_decoded_message = "Error message"

        self.assertIsNotNone(decoded_message)
        self.assertEqual(decoded_message, asserted_decoded_message)

    def test_can_deserialize_echo_message(self):
        encoded_message = b"*2\r\n$4\r\necho\r\n$5\r\nsalut\r\n"

        decoded_message = deserialize_echo_message(encoded_message)

        asserted_decoded_message = b"salut"

        self.assertIsNotNone(decoded_message)
        self.assertEqual(decoded_message, asserted_decoded_message)

    def test_can_deserialize_get_message(self):
        encoded_message = b"*2\r\n$3\r\nget\r\n$3\r\nkey\r\n"

        decoded_message = deserialize_get_message(encoded_message)

        asserted_decoded_message = b"key"

        self.assertIsNotNone(decoded_message)
        self.assertEqual(decoded_message, asserted_decoded_message)

    def test_can_deserialize_set_message(self):
        encoded_message = b"*2\r\n$3\r\nset\r\n$5\r\nvalue\r\n"

        decoded_message = deserialize_set_message(encoded_message)

        asserted_decoded_mesage = b"value"

        self.assertIsNotNone(decoded_message)
        self.assertEqual(decoded_message, asserted_decoded_mesage)

if __name__ == '__main__':

    unittest.main()

