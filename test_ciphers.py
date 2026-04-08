import unittest
from vigenere import vigenere
from morsecode import process_morse
from caeesar import caesar 

class TestCipherSuite(unittest.TestCase):

    # VIGENÈRE CIPHER TESTS

    def test_vigenere_standard(self):
        """Tests standard execution of Vigenere (all lowercase)"""
        result_lemon = vigenere("lemon", "cat", "encode")
        self.assertEqual(result_lemon, "nefqn")
        
        result_new_york = vigenere("new york", "winter", "encode")
        self.assertEqual(result_new_york, "jmj rsig")
        
        result_peppers = vigenere("peppers", "spicy", "encode")
        self.assertEqual(result_peppers, "htxrcjh")

    def test_vigenere_capitalization_handling(self):
        """Tests that capitalized keys are handled cleanly"""
        result = vigenere("lemon", "CAT", "encode")
        self.assertEqual(result, "nefqn")

    def test_vigenere_whitespace_key(self):
        """Tests that whitespace in the key is successfully ignored"""
        result = vigenere("lemon", "c at", "encode")
        self.assertEqual(result, "nefqn")

    def test_vigenere_special_characters_error(self):
        """Tests that invalid keys return the exact error string, not a server crash"""
        expected_error = "Error: Vigenère key must only contain letters. Please remove any numbers or special characters."
        
        # Test 1: Symbol in key
        result_symbol = vigenere("lemon", "c@t", "encode")
        self.assertEqual(result_symbol, expected_error)
        
        # Test 2: Number in key
        result_number = vigenere("lemon", "cat1", "encode")
        self.assertEqual(result_number, expected_error)


    # MORSE CODE TESTS

    def test_morse_encode_standard(self):
        """Tests basic lowercase word encoding"""
        result_sos = process_morse("sos", "encode")
        self.assertEqual(result_sos, "... --- ...")
        
        result_hello = process_morse("hello", "encode")
        self.assertEqual(result_hello, ".... . .-.. .-.. ---")

    def test_morse_encode_sentences(self):
        """Tests lowercase sentence encoding with the '/' word separator"""
        result_hello_world = process_morse("hello world", "encode")
        self.assertEqual(result_hello_world, ".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
        
        result_new_york = process_morse("new york", "encode")
        self.assertEqual(result_new_york, "-. . .-- / -.-- --- .-. -.--")

    def test_morse_decode_error(self):
        """Tests that improperly formatted morse code returns the safe error string"""
        expected_error = "Error: Invalid Morse code detected. Please use dots/dashes, spaces between letters, and '/' between words."
        
        # Testing a string with missing spaces between the letters
        result = process_morse("...---...", "decode")
        self.assertEqual(result, expected_error)


    # CAESAR CIPHER TESTS

    def test_caesar_standard(self):
        """Tests standard positive shift with lowercase"""
        result = caesar("hello", 3, "encode")
        self.assertEqual(result, "khoor")
        
        result_world = caesar("hello world", 7, "encode")
        self.assertEqual(result_world, "olssv dvysk")

    def test_caesar_negative_shift(self):
        """Tests that a negative shift correctly reverses the alphabet"""
        result = caesar("new york", -1, "encode")
        self.assertEqual(result, "mdv xnqj")


if __name__ == '__main__':
    unittest.main(verbosity=2)