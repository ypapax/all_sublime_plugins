
import unittest
import sys
sys.path.insert(0, '..')

import color


import sys
import util


class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		result = util.itemInList('1', ['1', '2'])
		expected = True
		self.assertEqual(result, expected)
	def test_testNameFalse(self):
		color.blue("test here baby")
		result = util.itemInList('3', ['1', '2'])
		expected = False
		self.assertEqual(result, expected)	
		

if __name__ == '__main__':
	unittest.main()		
