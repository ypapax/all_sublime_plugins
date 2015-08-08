import sys
sys.path.insert(0, '..')

import color

import sys
import util
import unittest
class Test(unittest.TestCase):


	def test_testName(self):
		inputText = repr("'")
		result = util.replaceLastAndFirstQuotes(inputText)

		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		color.red('result')
		print(repr(result))
		print('*****************************************************************')


if __name__ == '__main__':
	unittest.main()