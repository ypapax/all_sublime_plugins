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
		result = relativeRequireIced_model.removeRowsStartingFromSpace()
		expected = ""
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()