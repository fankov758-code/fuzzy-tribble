# -*- coding: utf-8 -*-
import unittest
from main import get_max_strength

class TestDragonStrength(unittest.TestCase):
    def test_basic_cases(self):
        # Проверка базовых значений
        self.assertEqual(get_max_strength(1), 1)
        self.assertEqual(get_max_strength(2), 2)
        self.assertEqual(get_max_strength(3), 3)
        self.assertEqual(get_max_strength(4), 4)   # 2 * 2 или 4
        self.assertEqual(get_max_strength(5), 6)   # 2 * 3
        self.assertEqual(get_max_strength(6), 9)   # 3 * 3
        self.assertEqual(get_max_strength(7), 12)  # 3 * 4
        self.assertEqual(get_max_strength(8), 18)  # 3 * 3 * 2
        
    def test_large_cases(self):
        # Проверка на более крупных значениях
        self.assertEqual(get_max_strength(10), 36)  # 3 * 3 * 4 = 36
        self.assertEqual(get_max_strength(15), 243) # 3^5 = 243

if __name__ == "__main__":
    unittest.main()
