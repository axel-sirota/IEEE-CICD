import unittest
import funniest


class TestJoke(unittest.TestCase):

    def test_joke(self):
        joke = funniest.joke()
        self.assertEqual(isinstance(joke, str), True)
