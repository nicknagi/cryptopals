import unittest

class TestSingleCharKeySearch(unittest.TestCase):

    def test_single_char_key_search_returns_expected_decrypted_text_when_encrypted_hex_passed(self):
        from utils import single_char_key_search
        encrypted_hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
        
        self.assertEqual((b'Cooking MC\'s like a pound of bacon', 2.14329), single_char_key_search(encrypted_hex))
    
    def test_single_char_key_search_with_random_length_encrypted_string_breaks_properly(self):
        from utils import single_char_key_search
        from encryption import repeating_key_xor
        import faker

        faker = faker.Faker()

        random_base_string = faker.text().replace('\n', '')
        encrypted_base_string = repeating_key_xor(faker.word()[0], random_base_string)

        self.assertEqual(random_base_string, single_char_key_search(encrypted_base_string)[0].decode())