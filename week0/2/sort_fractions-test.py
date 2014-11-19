import unittest
from sort_fractions import sort_fractions

class SortFractionsTest(unittest.TestCase):
	def test_sort_fractions(self):
		self.assertEqual(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]),[(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)])
	def test_sort_fractions2(self):
		self.assertEqual(sort_fractions([]),[])


if __name__ == '__main__':
	unittest.main()		