mdb_vgo = require './mdb_vgo.iced'
th = require 'throw'

module.exports = (cb)->

	await mdb_vgo defer result
	[err, db] = result
	th.err err
    
    cb err, db