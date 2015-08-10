import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/navigateTo')
import navigateToModel
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/moveNearReplace')
import absRel3
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color
import sys
import os


import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/moveNearReplace')
import filer2



def createFromPosition(filename, position):
	### read from file ###
	text = filer2.read(filename)
	### get method name ###
	methodName = navigateToModel.method(text, position)
	color.red('methodName')
	print(repr(methodName))
	### generate test file and write it to disk ###
	return create(filename, methodName)


def createFileName(testFolder, methodName):
	i = 0
	while(True):
		if i == 0:
			iStr = ''
		else:
			iStr = str(i)
		testFileName = "{0}{1}_test.py".format(methodName.strip(), iStr)
		
		testFile = os.path.join(testFolder, testFileName)
		exists = os.path.isfile(testFile)
		color.red('testFile')
		print(repr(testFile))

		if not exists: break
		i = i + 1

	return testFile

### attention - this is old method - currently not used in plugin ###
def create(filename, methodName):
	### get filename's folder name ###
	dirName = absRel3.folder(filename)	
	### generate test folder abs path ###
	testFolder = os.path.join(dirName, "test")
	### if test folder do not exists create it: ###
	if not os.path.exists(testFolder): os.makedirs(testFolder)
	### generate test file name ###
	testFile = createFileName(testFolder, methodName)
	### from full filename get just filename ###
	justFileName = absRel3.filename(filename)
	### test file content ###
	testText = """import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '{0}')
import color
import assertMy
import {1}

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		result = {1}.{2}()
		expected = ""
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()"""
	testText = testText.format(dirName, justFileName, methodName)




	filer2.write(testFile, testText)
	return testFile