# Test Zad. 9 (3.3)

import unittest
from Zad09 import Leapyear


class TestLeapyear(unittest.TestCase):
      def setUp(self):
          self.leapyear1 = Leapyear(1976)
          self.leapyear2 = Leapyear(1983)
          self.leapyear3 = Leapyear(1995)
          self.leapyear4 = Leapyear(2021)


class TestInit(TestLeapyear):
      def test_februaries(self):
          self.assertEqual(self.leapyear1.februaries(), 11)
          self.assertEqual(self.leapyear2.februaries(), 9)
          self.assertEqual(self.leapyear3.februaries(), 6)
          self.assertEqual(self.leapyear4.februaries(), 0)
