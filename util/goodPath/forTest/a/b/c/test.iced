routes = require '../../routes/e'
rrnt = require '../f.iced'
db = require 'db'
module.exports = (url, param, test)=>
	rrnt routes, url, param, test