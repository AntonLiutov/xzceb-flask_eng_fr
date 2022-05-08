import unittest
from translator import french_to_english, english_to_french

class testEnglishToFrenchTranslator(unittest.TestCase):
    def tests(self):
        self.assertEqual(english_to_french("Man"), "Homme")
        self.assertEqual(english_to_french("Language"), "Langue")
        self.assertEqual(english_to_french(""), "")
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class testFrenchToEnglishTranslator(unittest.TestCase):
    def tests(self):
        self.assertEqual(french_to_english("Homme"), "Man")
        self.assertEqual(french_to_english("Langue"), "Language")
        self.assertEqual(french_to_english(""), "")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()
