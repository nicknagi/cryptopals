import unittest

class TestRepeatingKeyXorEncryption(unittest.TestCase):

    def test_base_case_as_specified_in_problem_statement(self):
        from encryption import repeating_key_xor

        key='ICE'
        input_string='''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

        expected = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

        self.assertEqual(expected, repeating_key_xor(key=key, data=input_string))

    def test_repeating_key_xor_when_base64_input_used(self):
        from encryption import repeating_key_xor_base64

        base64_text = 'SGVsbG8gV29ybGQhIQ==' # Hello World in base64

        encrypted_base64_text = repeating_key_xor_base64('yo', 'SGVsbG8gV29ybGQhIQ==')
        self.assertEqual(encrypted_base64_text, 'MQoVAxZPLgALAx1OWA==')
    
    def test_repeating_key_xor_is_commutative(self):
        from encryption import repeating_key_xor_base64

        base64_text = 'SGVsbG8gV29ybGQhIQ==' # Hello World in base64

        encrypted_base64_text = repeating_key_xor_base64('yo', 'SGVsbG8gV29ybGQhIQ==')
        self.assertEqual(encrypted_base64_text, 'MQoVAxZPLgALAx1OWA==')

        decrypted_base64_text = repeating_key_xor_base64('yo', encrypted_base64_text)
        self.assertEqual(decrypted_base64_text, base64_text)
