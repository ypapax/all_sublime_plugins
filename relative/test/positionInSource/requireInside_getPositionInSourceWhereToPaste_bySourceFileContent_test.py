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
		sourceFileContent = """th = require 'throw'
th.Throw()	
assert = require 'assert'

module.exports = (input, test)->
	th.log "input"
	th.log input
	inputModel = require "./#{input}/input.js"
	th.log "inputModel"
	th.log inputModel

	

	th.log "actual"
	th.log actual
	th.log "actual.length"
	th.log actual.length

	expected = require "./#{input}/expected.js"
	
	actual = JSON.stringify actual
	expected = JSON.stringify expected
	assert.deepEqual actual, expected
	
	db.fin()
	test.done()
	"""
		result = relativeRequireIced_model.getPositionInSourceWhereToPaste_bySourceFileContent(sourceFileContent)
		expected = 58
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()