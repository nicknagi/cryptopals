import unittest

class TestDataUtils(unittest.TestCase):

    def test_when_hex_char_input_mapping_returns_expected_binary_value(self):
        from data_utils import generate_hex_to_binary_mapping

        map = generate_hex_to_binary_mapping()
        self.assertEqual('0011', map['3'])
        self.assertEqual('1010', map['a'])
        self.assertEqual('0000', map['0'])
    
    def test_when_binary_string_input_mapping_returns_expected_base64_value(self):
        from data_utils import generate_binary_to_base64_mapping

        map = generate_binary_to_base64_mapping()
        self.assertEqual(map['001100'], 'M')
        self.assertEqual(map['101011'], 'r')
        self.assertEqual(map['000010'], 'C')