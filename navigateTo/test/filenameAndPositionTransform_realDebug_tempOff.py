import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/navigateTo')
import color
import assertMy
import navigateToModel

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		filename=os.path.dirname(os.path.realpath(__file__)) + "/poligon/debug2.py"
		position=717
		(resultFile, resultPosition) = navigateToModel.filenameAndPositionTransform(filename, position)
		expectedFile = "/Users/maks/Library/Application Support/Sublime Text 3/Packages/util/assertMy.py"
		expectedPosition = 1861
		assertMy.equals(resultFile, expectedFile)
		self.assertEqual(resultPosition, expectedPosition)

if __name__ == '__main__':
	unittest.main()