import unittest
from prepare_meal import prepare_meal


class PrepareMealTest(unittest.TestCase):

    #def test_0(self):
    #	self.assertEqual('',prepare_meal(0))
    def test_27(self):
    	self.assertEqual(prepare_meal(27),'spam spam spam ')
    def test_15(self):
    	self.assertEqual(prepare_meal(15),'spam and eggs')
if __name__ == '__main__':
    unittest.main()
