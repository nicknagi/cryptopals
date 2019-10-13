import unittest

class TestConversion(unittest.TestCase):

    def test_base64_to_text_conversion(self):
        from conversion import base64_to_text
        input_base64 = 'eW91ciB0ZXh0'
        expected_output = 'your text'

        self.assertEqual(expected_output, base64_to_text(input_base64))

