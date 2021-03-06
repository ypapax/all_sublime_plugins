import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import color
import assertMy
import relativeRequireIced_model

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		source = os.path.join(currentFolder, 'filesPoligon/source.iced')
		target = os.path.join(currentFolder, 'filesPoligon/targetEmptyParams.iced')
		result = relativeRequireIced_model.do(target, source)
		expected = ("targetEmptyParams = require './targetEmptyParams.iced'", 'await targetEmptyParams defer result')
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()