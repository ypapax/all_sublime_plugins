import replace_require


def test_first():
	print("oke")
	replace_require.Replace("/Users/maks/Dropbox/nodeApps/call/test/findInFullRegion_yamal_test.iced", 
		"/Users/maks/Dropbox/nodeApps/call/test/db/findInFullRegion/findInFullRegion_yamal_test.iced", 
		""" target = require '../grab/2_allFilesAtOnes/findInFullRegion'
		assert = require 'assert'
		rf = require '../grab/redisFunc'


		find = (findWhat, expected, test, autocb)->
			rf = require '../grab/redisFunc' """)

	