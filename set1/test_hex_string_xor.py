import unittest

class TestHexStringXor(unittest.TestCase):

    def test_base_case_specified_in_problem_statement(self):
        from utils import hex_string_xor

        self.assertEqual(hex_string_xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965'), '746865206b696420646f6e277420706c6179')

    def test_strings_of_unequal_lengths_returns_error(self):
        from utils import hex_string_xor

        with self.assertRaises(AssertionError) as err:
            hex_string_xor('12a344bd', '17237acd236273')
