
import sys
sys.path.insert(0, '..')
import colorDiff
		

import unittest
import sys
import color

class Test(unittest.TestCase):
	def test_testName(self):
		print('newtest')
		colorDiff.do("123", "123")
	def test_testNameNotEqual(self):
		print('newtest')

		colorDiff.do("143", "123")	
	def test_testNameNotEqualLonger(self):
		print('newtest')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		

		colorDiff.do("1234", "123")		
	def test_testNameNotEqualLonger2(self):
		print('newtest')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		

		colorDiff.do("123", "1235")		

if __name__ == '__main__':
	unittest.main()		
		