import unittest
from utils import hex_to_base64

class TestHexToBase64(unittest.TestCase):

    def test_empty_hex_input_returns_nothing(self):
        input_string = ''
        self.assertEqual('',hex_to_base64(input_string))

    def test_singular_hex_character_returns_appropriate_base64_string(self):
        input_string = '3A'
        self.assertEqual('Og==', hex_to_base64(input_string))
    
    def test_random_hex_number_returns_correct_base64_string(self):
        import string, random
        import codecs

        input_string = ''.join(random.choice('0123456789ABCDEF') for n in range(int(random.randint(1,10000) * 2)))
        self.assertEqual(codecs.encode(codecs.decode(input_string, 'hex'), 'base64').decode().strip('\n'), hex_to_base64(input_string))