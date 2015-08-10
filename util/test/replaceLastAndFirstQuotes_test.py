
import sys
sys.path.insert(0, '..')

import util
import unittest
import sys
import color

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		inputText = repr('\n')
		result = util.replaceLastAndFirstQuotes(inputText)		

		color.red('inputText')
		print(inputText)

		color.red('result')
		print(result)

	def test_testNameWithColors(self):
		color.blue("test here baby")
		
		inputText = color.color(repr('\n'), 'green')
		
		result = util.replaceLastAndFirstQuotes(inputText)		

		color.red('inputText')
		print(inputText)

		color.red('result')
		print(result)


if __name__ == '__main__':
	unittest.main()		
