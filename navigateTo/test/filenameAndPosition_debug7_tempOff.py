import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import color
import assertMy
import navigateToModel

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		filename=os.path.join(currentFolder, '../../find_usages_plugin.py')
		position= 626
		(resultFile, resultPosition) = navigateToModel.filenameAndPositionTransform(filename, position)
		expectedFile = os.path.join(currentFolder, '../../findUsages/reactOnCursorPosition.py')
		expectedPosition = 159
		assertMy.equals(resultFile, expectedFile)
		self.assertEqual(resultPosition, expectedPosition)

if __name__ == '__main__':
	unittest.main()