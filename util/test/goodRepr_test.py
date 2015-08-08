

import sys
sys.path.insert(0, '..')
import util



import unittest
import sys
import color

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		result = util.goodRepr('\n')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		color.red('result')
		print(result)
		print('*****************************************************************')

if __name__ == '__main__':
	unittest.main()		
