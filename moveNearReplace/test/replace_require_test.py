import pprint
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color

import replace_require
import difflib
import unittest
import filer2 as filer


def copmare_2_texts(actual, expected, self):
	color.green ("actual")
	print(actual)
	

	color.green ("expected")
	print(expected)		

	actualLines = actual.split('\n')
	expectedLines = expected.split('\n')

	color.green("actualLines")
	print(actualLines)
	color.green("expectedLines")
	print(expectedLines)
	zipped  = zip(actualLines, expectedLines)

	color.green ("zipped")
	print(zipped)
	color.green ("compare zipped")
	color.blue("comparing")

	for i,j in zipped:
		color.green (i)
		color.red (j)
	
		self.assertEqual(i.strip(),j.strip())

class Test(unittest.TestCase):
# 	def test_Replace2(self):
# 		oldFileName = '/Users/maks/Library/Application Support/Sublime Text 3/Packages/move_near_replace/testPath/read/read.iced'
# 		newFileName = '/Users/maks/Library/Application Support/Sublime Text 3/Packages/move_near_replace/testPath/write/write.iced'
# 		expectedFileContent = """target = require '../read/testLib/lib1.iced'
# assert = require 'assert'"""
# 		oldContent = filer.read (oldFileName)

# 		filer.write(newFileName, oldContent)
# 		fileContent_mustBeEmpty = filer.read(newFileName)
# 		self.assertEqual (fileContent_mustBeEmpty, oldContent)


# 		replace_require.Replace2(oldFileName, newFileName)
# 		fileContent_mustBeConverted = filer.read(newFileName)
# 		copmare_2_texts (fileContent_mustBeConverted, expectedFileContent, self)

	def test_Replace(self):
		inputContent = """target = require '../grab/2_allFilesAtOnes/findInFullRegion'
			assert = require 'assert'
			rf = require '../grab/redisFunc'


			find = (findWhat, expected, test, autocb)->
				rf = require '../grab/redisFunc' """
		expectedContent = """target = require '../../../grab/2_allFilesAtOnes/findInFullRegion'
			assert = require 'assert'
			rf = require '../../../grab/redisFunc'


			find = (findWhat, expected, test, autocb)->
				rf = require '../../../grab/redisFunc'"""	
		
		actual = replace_require.Replace("/Users/maks/Dropbox/nodeApps/call/test/findInFullRegion_yamal_test.iced", 
			"/Users/maks/Dropbox/nodeApps/call/test/db/findInFullRegion/findInFullRegion_yamal_test.iced", 
			inputContent)

		copmare_2_texts(actual, expectedContent, self)


if __name__ == '__main__':
	unittest.main()			