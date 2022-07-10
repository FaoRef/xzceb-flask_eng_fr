import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_english_to_french_1(self):
        self.assertIsNone(english_to_french(""), None)    

    def test_french_to_english_1(self):
        self.assertEqual(french_to_english(""), None)

    def test_english_to_french_2(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_french_to_english_2(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test_english_to_french_3(self):
        self.assertNotEqual(english_to_french("Hello"), "BBB")

    def test_french_to_english_3(self):
        self.assertNotEqual(french_to_english("Bonjour"), "HHH")

if __name__ == "__main__":
    unittest.main()

