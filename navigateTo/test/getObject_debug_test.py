
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
import pyFind
import navigateToModel

import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color

inputText = """import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/navigateTo')
import color
import assertMy
import navigateToModel

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		filename="/Users/maks/Library/Application Support/Sublime Text 3/Packages/navigateTo/testPoligon/debug.py"
		position=374
		(resultFile, resultPosition) = navigateToModel.filenameAndPositionTransform(filename, position)
		expectedFile = "/Users/maks/Library/Application Support/Sublime Text 3/Packages/util/assertMy.py"
		expectedPosition = 410
		assertMy.equals(resultFile, expectedFile)
		self.assertEqual(resultPosition, expectedPosition)

if __name__ == '__main__':
	unittest.main()"""



class Test(unittest.TestCase):
    
    def test_bigFile(self):
        color.blue("test here baby")
        

        expected = ['assertMy', 'equals']
        
        position = 717

        result = navigateToModel.getObject(inputText, position)

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()     
