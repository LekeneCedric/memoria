import unittest
from protocol import *

class ProtocolTest(unittest.TestCase):

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

        asserted_decoded_message = "salut"

        self.assertIsNotNone(decoded_message)
        self.assertEqual(decoded_message, asserted_decoded_message)

    def test_can_deserialize_get_message(self):
        encoded_message = b"*2\r\n$3\r\nget\r\n$3\r\nkey\r\n"

        decoded_message = deserialize_get_message(encoded_message)

        asserted_decoded_message = "key"

        self.assertIsNotNone(decoded_message)
        self.assertEqual(decoded_message, asserted_decoded_message)

    def test_can_deserialize_set_message(self):
        encoded_message = b"*3\r\n$3\r\nset\r\n$3\r\nkey\r\n$5\r\nvalue\r\n"

        decoded_message = deserialize_set_message(encoded_message)
        decoded_message_key = decoded_message["key"]
        decode_message_value = decoded_message["value"]

        asserted_decoded_mesage_key = "key"
        asserted_decoded_message_value = "value"

        self.assertIsNotNone(decoded_message)
        self.assertEqual(decoded_message_key, asserted_decoded_mesage_key)
        self.assertEqual(decode_message_value, asserted_decoded_message_value)

    def test_can_serialize_simple_string(self):

        message = "OK"

        serialized_message = serialize_simple_string(message)

        asserted_serialized_message = b"+OK\r\n"

        self.assertIsNotNone(serialized_message)
        self.assertEqual(serialized_message, asserted_serialized_message)

    def test_can_serialize_error_message(self):

        message = "Error message"

        serialized_message = serialize_error_message(message)

        asserted_serialized_message = b"-Error message\r\n"

if __name__ == '__main__':

    unittest.main()

