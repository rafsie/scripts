import unittest
from Zad04 import levqwerty


class LevenshteinTestCase(unittest.TestCase):

   def test_levqwerty(self):
       self.assertEqual(levqwerty('pies', 'pies'), 0)
       self.assertEqual(levqwerty('granat', 'granit'), 1)
       self.assertEqual(levqwerty('kot', 'kita'), 1.5)
       self.assertEqual(levqwerty('drab', 'dal'), 2)


if __name__ == '__main':
    unittest.main()
