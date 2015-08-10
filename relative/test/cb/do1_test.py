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
		targeFilename = '/Users/maks/Library/Application Support/Sublime Text 3/Packages/relative/test/cb/filePoligon/target.iced'
		sourceFilename = '/Users/maks/Library/Application Support/Sublime Text 3/Packages/relative/test/cb/filePoligon/source/source.iced'
		
		result = relativeRequireIced_model.do(targeFilename, sourceFilename)
		expected = ("target = require '../target.iced'", 'await target db, text, orgId, defer err, comments')
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()