import unittest
from reduce_file_path import reduce_file_path

class ReduceFilePathTest(unittest.TestCase):
	def test_two_slashes (self):
		self.assertEqual("home/pesho",reduce_file_path("/home//pesho"))

	def test_two_dots (self):
		self.assertEqual("home/pesho1/",reduce_file_path("/home/pesho1/pesho2/../"))
	def test_one_dot (self):
		self.assertEqual("home/pesho1/",reduce_file_path("/home/pesho1/./pesho2/../"))
	def test_from_git(self):
		self.assertEqual(reduce_file_path("/srv/../"),"/")
	def test_from_git2(self):
		self.assertEqual(reduce_file_path("/srv/www/htdocs/wtf/"),"srv/www/htdocs/wtf")
if __name__ == '__main__':
	unittest.main()		