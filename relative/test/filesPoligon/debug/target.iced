th = require 'throw'
mdb_shir_cb = require '../mdb_shir_cb.iced'
cityCollection = require './cityCollection.iced'


module.exports = (db, cb)->
	await mdb_shir_cb defer err, db

	collection = cityCollection db
	query = longLat: {$exists: true}

	await collection.find(query).toArray defer err, cityListWithLongLat
	th.err err
	cb cityListWithLongLat
	