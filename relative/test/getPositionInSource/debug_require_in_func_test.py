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
		fileContent="""
(require 'throw').Throw()
assert = require 'assert'
async = require 'async'
cheerio = require 'myAssert/cheerio'

module.exports = (test)=>
	cheerio = require 'myAssert/cheerio'"""
		result = relativeRequireIced_model.getPositionInSourceWhereToPaste_bySourceFileContent(fileContent)
		expected = 113
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()