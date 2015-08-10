th = require 'throw'
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


	return cityList