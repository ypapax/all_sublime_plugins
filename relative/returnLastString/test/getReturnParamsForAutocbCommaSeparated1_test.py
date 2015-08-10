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
		fileContent = """th = require 'throw'
mdb_shir_cb = require '../mdb_shir_cb.iced'
cityCollection = require './cityCollection.iced'


module.exports = (db, cb)->
	await mdb_shir_cb defer err, db

	collection = cityCollection db
	query = longLat: {$exists: true}

	await collection.find(query).toArray defer err, cityListWithLongLat
	th.err err
	cb cityListWithLongLat
	"""
		result = returnLast.getReturnParamsForAutocbCommaSeparated(fileContent)
		expected = "cityListWithLongLat"
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()