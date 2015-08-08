import unittest
import sys
sys.path.insert(0, '../../util')
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
		expectedFile = "/Users/maks/Library/Application Support/Sublime Text 3/Packages/navigateTo/testPoligon/folder1/a.py"
		expectedPosition = 20
		assertMy.equals(resultFile, expectedFile)
		self.assertEqual(resultPosition, expectedPosition)

if __name__ == '__main__':
	unittest.main()