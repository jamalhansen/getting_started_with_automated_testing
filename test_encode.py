import unittest

import encode

class TestEncode(unittest.TestCase):
    def test_that_a_encodes_to_n(self):
        result = encode.character_encode('a')
        self.assertEqual('n', result)

    def test_that_a_does_not_equal_c(self):
        result = encode.character_encode('a')
        self.assertNotEqual('c', result)

    def test_that_s_encodes_to_f(self):
        result = encode.character_encode('s')
        self.assertEqual('f', result)

    def test_that_string_encodes_to_correct_value(self):
        result = encode.encode_string('test')
        self.assertEqual('grfg', result)

    def test_that_we_convert_character_to_number(self):
        result = encode.char_to_num('a')
        self.assertTrue(type(result) is int)

    def test_that_char_to_num_returns_ascii_value(self):
        result = encode.char_to_num('a')
        self.assertEqual(ord('a'), result)

    def test_that_we_rotate_thirteen(self):
        result = encode.char_to_encoded('a')
        self.assertEqual(110, result)

    def test_that_we_can_convert_num_to_char(self):
        result = encode.num_to_char(110)
        self.assertEqual('n', result)

    def test_that_char_to_encoded_does_not_return_a_value_greater_than_end_of_alphabet(self):
        result = encode.char_to_encoded('z')
        self.assertTrue(122 > result)

    def test_full_alphabet(self):
        test_string = "thequickbrownfoxjumpsoverthelazydog"
        encoded = encode.encode_string(test_string)
        decoded = encode.encode_string(encoded)
        self.assertEqual(test_string, decoded)
