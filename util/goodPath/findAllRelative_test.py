
import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')

sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/moveNearReplace')

sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath')

import color
import filer2 as filer
import findAllRelative_model
import recursiveSearch_model
class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		result = findAllRelative_model.go('/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest/a/b/c/test.iced')
		expected = """routes = require '../e.iced'
rrnt = require './k/f.iced'
db = require 'db'
module.exports = (url, param, test)->
	rrnt routes, url, param, test"""		
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

		print(result)
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		self.assertEqual (result, expected)
	def test_goAndWrite(self):
		color.blue("test here baby")
		inputFileContent = """routes = require '../../routes/e'
rrnt = require '../f.iced'
db = require 'db'
module.exports = (url, param, test)->
	rrnt routes, url, param, test
	"""	
		path = "/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest/a/b/c/testForWrite.iced"
		filer.write(path, inputFileContent)
		findAllRelative_model.goAndWrite(path)
		expected = """routes = require '../e.iced'
rrnt = require './k/f.iced'
db = require 'db'
module.exports = (url, param, test)->
	rrnt routes, url, param, test
	"""		
		result = filer.read(path)
		self.assertEqual (result, expected)	

	def test_recursiveWrite(self):
		color.blue("test here baby")
		inputFileContent = """routes = require '../../routes/e'
rrnt = require '../f.iced'
db = require 'db'
module.exports = (url, param, test)->
	rrnt routes, url, param, test
	"""	
	# 	expected = """routes = require '../e.iced'
	# rrnt = require './k/f.iced'
	# db = require 'db'
	# module.exports = (url, param, test)->
	# 	rrnt routes, url, param, test
	# 	"""		
		path = "/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forRecursiveTest"

		files = recursiveSearch_model.getAllFiles(path)
		for fileName in files:
			filer.write(fileName, inputFileContent)

		findAllRelative_model.repaireRecursive(path)
		
		for fileName in files:
			result = filer.read(fileName)
			self.assertNotEqual (result, inputFileContent)	
		
		
		
		
		


# allFiles = recursiveSearch_model.getAllFiles(filePath)

if __name__ == '__main__':
	unittest.main()		
