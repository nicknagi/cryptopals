import unittest

class TestRepeatingKeyXorEncryption(unittest.TestCase):

    def test_base_case_as_specified_in_problem_statement(self):
        from encryption import repeating_key_xor

        key='ICE'
        input_string='''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

        expected = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

        self.assertEqual(expected, repeating_key_xor(key=key, data=input_string))