import unittest
from groupby import groupby

class GroupByTest(unittest.TestCase):
	def test_lambda(self):
		self.assertEqual(groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]),{'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]})
	def test_lambda2(self):
		self.assertEqual(groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]),{0: [0, 3, 6], 1: [1, 4, 7], 2: [2, 5]})
if __name__ == '__main__':
	unittest.main()		