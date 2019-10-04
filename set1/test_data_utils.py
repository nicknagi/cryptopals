import unittest

class TestDataUtils(unittest.TestCase):

    def test_when_hex_char_input_mapping_returns_expected_binary_value(self):
        from data_utils import generate_hex_to_binary_mapping

        map = generate_hex_to_binary_mapping()
        self.assertEqual('0011', map['3'])
        self.assertEqual('1010', map['A'])
        self.assertEqual('0000', map['0'])