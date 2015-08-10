import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import assertMy
import duplicateLines
import unittest
import color

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		inputText = "import sys\nimport sys"
		result = duplicateLines.remove(inputText)

		expected = "import sys"
		assertMy.equals(result, expected)
		

if __name__ == '__main__':
	unittest.main()		
		