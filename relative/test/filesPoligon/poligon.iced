cityListInCountryId = require '../../city/filter/byCountryForCitiesWithoutRegion/cityListInCountryId.iced'
module.exports = (countryId, regionId, autocb)->

	# first try get cities by countryId: