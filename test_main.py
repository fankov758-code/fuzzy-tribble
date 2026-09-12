# -*- coding: utf-8 -*-
import unittest
from main import get_max_strength


class TestDragonStrength(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(get_max_strength(1), 1)
        self.assertEqual(get_max_strength(2), 2)
        self.assertEqual(get_max_strength(3), 3)
        self.assertEqual(get_max_strength(4), 4)
        self.assertEqual(get_max_strength(5), 6)
        self.assertEqual(get_max_strength(6), 9)
        self.assertEqual(get_max_strength(7), 12)
        self.assertEqual(get_max_strength(8), 18)

    def test_large_cases(self):
        self.assertEqual(get_max_strength(10), 36)
        self.assertEqual(get_max_strength(15), 243)

    def test_edge_cases(self):
        self.assertEqual(get_max_strength(0), 0)
        self.assertEqual(get_max_strength(-5), 0)


if __name__ == "__main__":
    unittest.main()
