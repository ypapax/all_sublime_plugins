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
		fileContent = """sqlCopyOrgs = require '../1.org/sqlCopyOrgs.iced'

module.exports = (autocb)-> """
		result = callForSyncFunc.isItSync(fileContent)
		expected = False
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()