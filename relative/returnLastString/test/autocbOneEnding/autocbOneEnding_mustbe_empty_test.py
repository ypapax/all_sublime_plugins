import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/relative/returnLastString')
import color
import assertMy
import returnLast

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		targetFileContent = """th = require 'throw'
# th.Throw()	
rubricKeys = require '../../copyFromSql/2.rubric/rubricKeys.iced'
rf = require '../../rf.iced'
module.exports = (autocb)->
	[z] = rubricKeys ""
	await rf.client.zrevrange z, 0, -1, defer err, allRubricIdList
	th.err err

	return [null, allRubricIdList]"""

		result = returnLast.autocbOneEnding(targetFileContent)
		expected = ""
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()