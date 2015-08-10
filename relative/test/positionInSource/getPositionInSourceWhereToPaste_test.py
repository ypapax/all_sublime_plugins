import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/relative')
import color
import assertMy
import relativeRequireIced_model

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		sourceFilename = '/Users/maks/Library/Application Support/Sublime Text 3/Packages/relative/test/positionInSource/poligon/source.iced'
		result = relativeRequireIced_model.getPositionInSourceWhereToPaste(sourceFilename)
		expected = 129
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()