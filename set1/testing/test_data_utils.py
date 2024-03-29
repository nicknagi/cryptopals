import unittest

class TestDataUtils(unittest.TestCase):

    def test_when_hex_char_input_mapping_returns_expected_binary_value(self):
        from data_utils import generate_hex_to_binary_mapping

        map = generate_hex_to_binary_mapping()
        self.assertEqual('0011', map['3'])
        self.assertEqual('1010', map['a'])
        self.assertEqual('0000', map['0'])
    
    def test_when_base64_char_input_mapping_returns_expected_binary_value(self):
        from data_utils import generate_base64_to_binary_mapping

        map = generate_base64_to_binary_mapping()
        self.assertEqual('001100', map['M'])
        self.assertEqual('101011', map['r'])
        self.assertEqual('000010', map['C'])

    def test_when_binary_string_input_mapping_returns_expected_base64_value(self):
        from data_utils import generate_binary_to_base64_mapping

        map = generate_binary_to_base64_mapping()
        self.assertEqual(map['001100'], 'M')
        self.assertEqual(map['101011'], 'r')
        self.assertEqual(map['000010'], 'C')

    def test_when_binary_string_input_mapping_returns_expected_hex_value(self):
        from data_utils import generate_binary_to_hex_mapping

        map = generate_binary_to_hex_mapping()
        self.assertEqual(map['0011'], '3')
        self.assertEqual(map['1010'], 'a')
        self.assertEqual(map['0000'], '0')

    def test_character_frequency_mapping_returns_expected_frequencies_when_queried(self):
        from data_utils import generate_english_character_frequencies

        map = generate_english_character_frequencies()
        self.assertEqual(map['a'], .08167)
        self.assertEqual(map['z'], .00074)
        self.assertEqual(map['g'], .02015)