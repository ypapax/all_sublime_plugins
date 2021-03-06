import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import assertMy
import beatyModel
import unittest
import color

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		inputText = """beatyModel\n\nim"""
		expected = """beatyModel\nim"""
		result = beatyModel.removeEmptyLines(inputText)
		
		assertMy.stringDiffByLines(result, expected)

if __name__ == '__main__':
	unittest.main()		
