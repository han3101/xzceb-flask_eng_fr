import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test_not_null(self):
        self.assertIsNotNone(english_to_french("hello"), "Bonjour")
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour") #test for Hello to Bonjour
        self.assertNotEqual(english_to_french("Bonjour"), "Hello")

class TestF2E(unittest.TestCase):
    def test_not_null(self):
        self.assertIsNotNone(english_to_french("Bonjour"), "Hello")
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello") #test for Bonjour to Hello
        self.assertNotEqual(french_to_english("Hello"), "Bonjour")


unittest.main()