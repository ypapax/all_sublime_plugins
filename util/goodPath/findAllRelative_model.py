import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color
	


sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/moveNearReplace')

import getRel


import replacePath

import filer2 as filer
import absRel3 as absRel
import getFutherFolder_model
import recursiveSearch_model
def go(filePath):
	"""Returns file content with repaired relative paths"""
	fileContent = filer.read(filePath)
	relPathList = getRel.getRel (fileContent)

	fileNames = [relPath.split("/")[-1] for relPath in relPathList]
	color.blue("fileNames")
	print(fileNames)

	futherFolder = getFutherFolder_model.get(filePath)
	absFileNames = [recursiveSearch_model.find_files(futherFolder, fileName) for fileName in fileNames]

	color.blue("absFileNames")
	print(absFileNames)

	newRelPathList = [absRel.Rel(filePath, absPath) for absPath in absFileNames]
	
	# first found would be inserted

	fileContent = replacePath.go(relPathList, newRelPathList, fileContent)
	return fileContent

def goAndWrite(filePath):
	newContent = go(filePath)
	filer.write(filePath, newContent)
def repaireRecursive(filePath):
	allFiles = recursiveSearch_model.getAllFiles(filePath)
	for fileName in allFiles:
		goAndWrite(fileName)
	
	