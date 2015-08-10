commentCollection = require '../commentCollection.iced'
th = require 'throw'

module.exports = (db, text, orgId, cb)->

	collection = commentCollection db
	await collection.ensureIndex {Info: text}, defer()
	await collection.find({Info: text, OrgId: orgId}).sort({DateCreate: -1}).toArray defer err, comments

	cb null, comments

	