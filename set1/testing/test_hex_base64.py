import unittest
from utils import hex_to_base64

class TestHexToBase64(unittest.TestCase):

    def test_empty_hex_input_returns_nothing(self):
        input_string = ''
        self.assertEqual('',hex_to_base64(input_string))

    def test_singular_hex_character_returns_appropriate_base64_string(self):
        input_string = '3a'
        self.assertEqual('Og==', hex_to_base64(input_string))
    
    def test_random_hex_number_returns_correct_base64_string(self):
        import string, random
        import codecs

        input_string = ''.join(random.choice('0123456789abcdef') for n in range(int(random.randint(1,10000) * 2)))
        expected_output = codecs.encode(codecs.decode(input_string, 'hex'), 'base64').decode().replace('\n', '')
        actual_output = hex_to_base64(input_string)

        self.assertEqual(expected_output, actual_output)
    
    def test_case_specified_in_docs(self):
        input_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        expected_output = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

        self.assertEqual(expected_output, hex_to_base64(input_string))