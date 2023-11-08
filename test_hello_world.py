import unittest
from helloworld import hello_world,bad_word

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, World!")

class TestBadWord(unittest.TestCase):
    def test_bad_world(self):
        self.assertEqual(bad_word(), "pussy")

if __name__ == "__main__":
    unittest.main()
