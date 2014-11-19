import unittest
from unique_words_count import unique_words_count

class UniqueWordsCountTest(unittest.TestCase):
	def test_0_words(self):
		self.assertEqual(unique_words_count([]),0)
	def test_3_unique_words(self):
		self.assertEqual(unique_words_count(["apple", "banana", "pie"]),3)
	def test_1_word(self):
		self.assertEqual(unique_words_count(["HELLO!"] * 10),1)

if __name__ == '__main__':
	unittest.main()		