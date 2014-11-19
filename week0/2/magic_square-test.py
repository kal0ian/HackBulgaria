import unittest
from magic_square import magic_square


class MagicSquareTest(unittest.TestCase):

    def test_magic_square_0(self):
        self.assertFalse(magic_square([[],[],[]]))
    def test_magic_square_True(self):
    	self.assertTrue([[23, 28, 21], [22, 24, 26], [27, 20, 25]])
    def test_magic_square_False(self):
    	self.assertFalse(magic_square([[1,2,3], [4,5,6], [7,8,9]]))
    def test_magic_square_more_rows(self):
    	self.assertTrue(magic_square([[7,12,1,14], [2,13,8,11], [16,3,10,5], [9,6,15,4]]))
if __name__ == '__main__':
    unittest.main()
