import unittest

class TestBase64ToBinary(unittest.TestCase):

    def test_random_base64_string_gets_converted_to_right_binary(self):
        from utils import base64_to_binary
        from testing.mixin.testing_commons import generate_random_base64_string
        from base64 import decodebytes

        random_base64_string = generate_random_base64_string()
        expected_binary_string = "".join(["{:08b}".format(x) for x in decodebytes(random_base64_string)])

        self.assertEqual(expected_binary_string, base64_to_binary(random_base64_string.decode()))

