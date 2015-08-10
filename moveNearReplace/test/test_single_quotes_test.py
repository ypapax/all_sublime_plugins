

import unittest
import getRel

import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color
class Test(unittest.TestCase):
	def test_single_quotes(self):
		
		text = """ target = require '../grab/2_allFilesAtOnes/findInFullRegion'
			assert = require 'assert'
			rf = require '../grab/redisFunc'


			find = (findWhat, expected, test, autocb)->
				rf = require '../grab/redisFunc' """
		result = getRel.getRel(text)
		color.red('result')
		print(result)
		expected = ["../grab/2_allFilesAtOnes/findInFullRegion", "../grab/redisFunc"]
		self.assertEqual (result, expected)
		

if __name__ == '__main__':
	unittest.main()		