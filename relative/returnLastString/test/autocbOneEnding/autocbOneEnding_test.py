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
getCitiesByCountry = require './getCitiesByCountry.iced'
regionsByCountryId = require '../../region/regionsByCountryId.iced'
citiesByRegionId_slow = require './citiesByRegionId_slow.iced'
_ = require 'underscore'		


module.exports = (db, countryId, autocb)->
	await getCitiesByCountry db, countryId, defer result
	[err, cityList] = result
	th.err err
	
	unless cityList
		await regionsByCountryId db, countryId, defer result
		[err, regions] = result
		th.err err

		cityList = []

		for region in regions
			await citiesByRegionId_slow db, regionId, defer result
			[err, cities] = result
			th.err err

			cityList = _.union cityList, cities


	return cityList"""
		result = returnLast.autocbOneEnding(targetFileContent)
		expected = "cityList"
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()