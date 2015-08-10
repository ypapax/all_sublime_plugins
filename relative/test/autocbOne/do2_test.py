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
		target = "/Users/maks/Library/Application Support/Sublime Text 3/Packages/relative/test/filesPoligon/autocbOnePoligin/target.iced"
		source = "/Users/maks/Library/Application Support/Sublime Text 3/Packages/relative/test/filesPoligon/autocbOnePoligin/source.iced"
		result = relativeRequireIced_model.do(target, source)
		expected = ("target = require './target.iced'", 'await target db, countryId, defer cityList')
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()