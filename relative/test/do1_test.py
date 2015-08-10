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
		targeFilename = os.path.join(currentFolder, 'filesPoligon/debug/target.iced')
		sourceFilename = os.path.join(currentFolder, 'filesPoligon/debug/source.iced')
		result = relativeRequireIced_model.do(targeFilename, sourceFilename)
		expected = ("target = require './target.iced'", 'await target db, defer cityListWithLongLat')
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()