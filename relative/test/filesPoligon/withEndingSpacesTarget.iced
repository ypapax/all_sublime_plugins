th = require 'throw'
# th.Throw()	
rubricKeys = require '../../copyFromSql/2.rubric/rubricKeys.iced'
rf = require '../../rf.iced'
module.exports = (autocb)->
	[z] = rubricKeys ""
	await rf.client.zrevrange z, 0, -1, defer err, allRubricIdList
	th.err err

	return [null, allRubricIdList]


	