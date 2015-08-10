th = require 'throw'
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
	