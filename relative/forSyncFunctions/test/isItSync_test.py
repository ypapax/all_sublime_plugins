import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/relative/forSyncFunctions')
import color
import assertMy
import callForSyncFunc

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		fileContent = """require 'colors'
module.exports = (str1, str2)->
	outStr1 = ""
	outStr2 = """
		result = callForSyncFunc.isItSync(fileContent)
		expected = True
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()