import unittest
from simplify_fraction import simplify_fraction


class SimplifyFractionTest(unittest.TestCase):

    def test_a_grather_than_b(self):
        result = simplify_fraction((2, 6))
        test = (1, 3)
        self.assertEqual(result, test)

    def test_b_grather_than_a(self):
        result = simplify_fraction((6, 2))
        test = (3, 1)
        self.assertEqual(result, test)
    
    def test_a_equal_b(self):
        result = simplify_fraction((6, 6))
        test = (1, 1)
        self.assertEqual(result, test)


if __name__ == '__main__':
    unittest.main()
