import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import color
import assertMy
import relativeRequireIced_model

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		fileContent="""window.$ = window.jQuery = require 'jquery'
myAutocomplete = require './myAutocomplete.coffee'

my_tips_browserify = require './my_tips_browserify.coffee'
auto_wide_browserify = require './auto_wide_browserify.coffee'
neworg_submitButtonEvent_browserify = require './neworg_submitButtonEvent_browserify.coffee'
selectize = require 'selectize'

autoWide = auto_wide_browserify $
  

require 'bootstrap'

  
my_tips_browserify $

"""
		result = relativeRequireIced_model.getPositionInSourceWhereToPaste_bySourceFileContent(fileContent)
		expected = 401
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()