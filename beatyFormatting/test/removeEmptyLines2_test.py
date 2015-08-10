import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import assertMy
import beatyModel
import unittest
import sys
import color

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		inputText = """import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/beatyFormatting')
import beatyModel\n\n\nimport unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color"""
		expected = """import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/beatyFormatting')
import beatyModel
import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color"""
		result = beatyModel.removeEmptyLines(inputText)
		
		assertMy.stringDiffByLines(result, expected)

if __name__ == '__main__':
	unittest.main()		
