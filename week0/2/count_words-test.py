import unittest
from count_words import count_words

class CountWordsTest(unittest.TestCase):
	def test_empty_arr(self):
		result= {}
		self.assertEqual(result,count_words([]))
	def test_arr(self):
		result={"python":2}
		self.assertEqual(count_words(["python", "python"]),result)
		
if __name__ == '__main__':
	unittest.main()