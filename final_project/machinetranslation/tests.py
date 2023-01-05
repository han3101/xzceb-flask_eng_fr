import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french(""), "Bonjour") #test for null input
        self.assertEqual(english_to_french("Hello"), "Bonjour") #test for Hello to Bonjour

class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english(""), "Hello") #test for null input
        self.assertEqual(french_to_english("Bonjour"), "Hello") #test for Bonjour to Hello