import sys

import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import beatyModel
		

import unittest
import sys
import color

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		inputText = "adfasd\n\nadsfasd"
		expected = "adfasd\nadsfasd"
		result = beatyModel.removeEmptyLines(inputText)
		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()		
