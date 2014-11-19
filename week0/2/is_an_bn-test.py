import unittest
from is_an_bn import is_an_bn


class IsAnBnTest(unittest.TestCase):

    def test_a_and_b_0(self):
        self.assertTrue(is_an_bn(""))

    def test_a_and_b_2(self):
        self.assertTrue(is_an_bn("aabb"))

    def test_a_and_b_false(self):
        self.assertFalse(is_an_bn("aabbb"))
if __name__ == '__main__':
    unittest.main()
