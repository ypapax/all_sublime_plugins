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
		fileContent = """commentCollection = require '../commentCollection.iced'
th = require 'throw'

module.exports = (db, text, orgId, cb)->

	collection = commentCollection db
	await collection.ensureIndex {Info: text}, defer()
	await collection.find({Info: text, OrgId: orgId}).sort({DateCreate: -1}).toArray defer err, comments

	cb null, comments"""
		result = callForSyncFunc.isItCb(fileContent)
		expected = True
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()