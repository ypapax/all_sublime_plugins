import sys
import absRel3
import getRel
import color

import filer2 as filer
import replacePath
def Replace2(oldPath, newPath):
	fileContent = filer.read (newPath)
	newContent = Replace(oldPath, newPath, fileContent)
	color.blue ("newContent")
	
	filer.write(newPath, newContent)


def Replace(oldPath, newPath, fileContent):
	
	relList = getRel.getRel (fileContent)
	
	newRelatives = [absRel3.RelToRel(oldPath, newPath, relative) for relative in relList]

	fileContent = replacePath.go(relList, newRelatives, fileContent)
	return fileContent
