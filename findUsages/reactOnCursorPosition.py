import sys
from findUsagesModel import FindUsagesModel
		
def starter(filename, position, obj, command):
	if obj == 'usages':
		findUsagesModel = FindUsagesModel()
		return findUsagesModel.command(command, filename, position)


