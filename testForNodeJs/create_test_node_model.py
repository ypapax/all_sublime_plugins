# todo
	# write test: dont write if file already exist
	# write test: if 1_Love folder exist create 2_Love folder
import os
import sys
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '../moveNearReplace'))
sys.path.insert(0, os.path.join(currentFolder, '../util'))
sys.path.insert(0, os.path.join(currentFolder, '../goodPath'))
import filer2
import color
import getFutherFolder_model
oneLoveFolderName = "1_Love"
def get(filename):
	(testingFileName, test_test, expected, inputJs) = getAllLoveFileNames(filename)
	testingContent = """th = require 'throw'
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
	"""
	test_testContent = """testing = require '../testing'	
module.exports = 
	test: (test)->
		testing '{0}', test	
	""".format(oneLoveFolderName)

	inputContent = """module.exports = {}"""
	
	fileNameContentDict = ((testingFileName, testingContent), (test_test, test_testContent), (expected, inputContent), (inputJs, inputContent))
	if not os.path.exists(testingFileName):
		for fileName, content in fileNameContentDict:
			if not os.path.exists(fileName):
				filer2.writeEvenIfNoDir(fileName, content)
	print('fileNameContentDict')
	print(repr(fileNameContentDict))
	return testingFileName		

def getTestingFolder (fatherFolder, localPath):
	return "{0}/test/{1}/".format(fatherFolder, localPath)


def getOneLoveFolder (testingFolder):
	# result = ""
	# i = 1
	# while True:
	# 	result = "{0}{1}_Love/".format(testingFolder, i)
	# 	exists = os.path.exists(result)
	# 	new = not exists
	# 	i = i + 1
	# 	if new:
	# 		break 


	return "{0}{1}/".format(testingFolder, oneLoveFolderName)	

def getTestingFileName(testingFolder):
	testingFileName = os.path.join(testingFolder, "testing.iced")
	return testingFileName

def getOneLoveTestTestFileName(oneLoveFolder):
	return os.path.join(oneLoveFolder, "test_test.iced")

def getExpectedJsFileName(oneLoveFolder):
	return "{0}expected.js".format(oneLoveFolder)

def getInputJsFileName(oneLoveFolder):
	return "{0}input.js".format(oneLoveFolder)


def getAllLoveFileNames(filename):
	fatherFolder = getFutherFolder_model.get(filename)
	color.red('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
	print('fatherFolder')
	print(repr(fatherFolder))
	color.red('*****************************************************************')
	localPath = localFileName(filename, fatherFolder) 
	testingFolder = getTestingFolder (fatherFolder, localPath)	
	oneLoveFolder = getOneLoveFolder(testingFolder)


	testingFileName = getTestingFileName (testingFolder)
	test_test = getOneLoveTestTestFileName (oneLoveFolder)
	inputJs = getInputJsFileName (oneLoveFolder)
	expectedJs = getExpectedJsFileName (oneLoveFolder)
	return (testingFileName, test_test, expectedJs, inputJs)



def localFileName(fullPath, fatherPath):
	result = fullPath.replace(fatherPath, '')
	if result[0] == '/':
		result = result[1:]
	return result
get2 = get