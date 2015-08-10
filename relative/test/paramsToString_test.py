import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
sys.path.insert(0, os.path.join(currentFolder, '..'))
import color
import assertMy
import getParams

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		inputModel = ['1', '2', '3']
		result = getParams.paramsToString(inputModel)
		expected = "1, 2, 3"
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()