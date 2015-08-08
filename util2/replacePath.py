def go(oldRelPathList, newRelPathList, fileContent):
	for newRel in newRelPathList:
		index = newRelPathList.index(newRel)
		oldRel = oldRelPathList[index]
		fileContent = fileContent.replace(oldRel, newRel)
	return fileContent	