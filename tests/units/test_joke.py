import unittest
import funniest_ieee


class TestJoke(unittest.TestCase):

    def test_joke(self):
        joke = funniest_ieee.joke()
        self.assertEqual(isinstance(joke, str), True)
