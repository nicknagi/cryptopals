import unittest

class TestHammingDistance(unittest.TestCase):

    def test_hamming_distance_between_base_case_strings_as_specified_in_problem_spec(self):
        from utils import hamming_distance
        from data_utils import convert_string_to_binary_string

        self.assertEqual(37,hamming_distance(convert_string_to_binary_string('this is a test'),\
             convert_string_to_binary_string('wokka wokka!!!')))