import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
sys.path.insert(0, os.path.join(currentFolder, '..'))
import assertMy
import duplicateLines
import unittest
import color

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		inputText = "import\n\ndef func"
		result = duplicateLines.remove(inputText)

		expected = inputText
		assertMy.equals(result, expected)
		

if __name__ == '__main__':
	unittest.main()		
		