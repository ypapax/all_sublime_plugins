import re
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, 'returnLastString'))
sys.path.insert(0, os.path.join(currentFolder, 'forSyncFunctions'))
import callForSyncFunc
sys.path.insert(0, os.path.join(currentFolder, '../moveNearReplace'))
import filer2
import returnLast
import getParams
import absRel3 as absRel
import color

def do(targeFilename, sourceFilename):
		target = targeFilename
		source = sourceFilename
		print('target:', target, '-----------------------------------------------------')
		print('source:', source, '-----------------------------------------------------')
		rel = absRel.RelAndCutIfNodeModules(source, target)
		
		# 1) get fileName by filePath
		filename = absRel.filename (target)
		# 2) create string: #{fileName} = require '#{relativePath}'
		require = "{0} = require '{1}'".format(filename, rel)
		# 3) set to cliboard objectName - filename
			# 3.1) get param names:

		# get fileContent_target to load it once:
		fileContent_target = filer2.read (target)
		# check if function sync:
		sync = callForSyncFunc.isItSync (fileContent_target)
		color.red("sync in relativeRequireIced_model.py")
		print(sync)




		isCbWithouAutocb = callForSyncFunc.isItCb (fileContent_target)

		color.red("isCbWithouAutocb in relativeRequireIced_model.py")
		print(isCbWithouAutocb)
		
		if isCbWithouAutocb: # (...,cb)->
			params = getParams.getParamsCb(fileContent_target)
			ending = returnLast.getReturnParamsForAutocbCommaSeparated(fileContent_target)
			toClip = "await {0}{1} defer {2}".format(filename, params, ending)	
		else:
			if sync:
				# load params sync
				params = callForSyncFunc.byFileContent(fileContent_target)
				returnParams = returnLast.returnParamsForSyncExpressionOrReturn(fileContent_target)
				toClip = "{2} = {0}{1}".format(filename, params, returnParams)
			else: # async: (..., autocb)->	
				params = getParams.getParamsAutocb(fileContent_target)	

				autocbOneEnding = returnLast.autocbOneEnding(fileContent_target)
				if autocbOneEnding:
					toClip = "await {0}{1} defer {2}".format(filename, params, autocbOneEnding)		
				else:
					ending = returnLast.doAllByFileName(target)	
					toClip = "await {0}{1} defer result{2}".format(filename, params, ending)	
			
		
		result = (require, toClip)
		return result
	
def getPositionInSourceWhereToPaste(sourceFilename):
	fileContent_source = filer2.read (sourceFilename)
	return getPositionInSourceWhereToPaste_bySourceFileContent(fileContent_source)


def getPositionInSourceWhereToPaste_bySourceFileContent(sourceFileContent):
	# sourceFileContent = removeRowsStartingFromSpace(sourceFileContent)
	sourceFileContent = removeAfterModuleExports(sourceFileContent)
	fileContent_source = sourceFileContent

	color.red("fileContent_source")
	print(fileContent_source)

	newRequirePosition = 0

	for m in re.finditer(r"(require.*)", fileContent_source):
		newRequirePosition = m.start() + len(m.group())

	return newRequirePosition

def removeAfterModuleExports(fileContent):
	color.red("fileContent in relativeRequireIced_model.py")
	print(fileContent)
	sub =  "module.exports"
	if sub in fileContent:
		index = fileContent.index(sub)
		fileContent = fileContent[:index]
	return fileContent



def removeRowsStartingFromSpace(fileContent):
	# should remove the second and third strings from the following content:
	# module.exports = (input, test)->
	# 	th.log "input"
	# 	th.log input
	fileContentWithouIntendedRows = re.sub(r'\n\s+.*', '', fileContent)
	color.red("fileContentWithouIntendedRows in py")
	print(fileContentWithouIntendedRows)
	return fileContentWithouIntendedRows

def ifSourceHaveRequireString(sourceFileContent, requireString):
	return requireString in sourceFileContent




def doEveryThingByView(view, edit, insertRequireUsage):
	import sublime, sublime_plugin, os.path

	target = sublime.get_clipboard()
	source = view.file_name()
	
	sourceContent = view.substr(sublime.Region(0, view.size()))

	print ("sourceContent in relativeRequireIced.py")
	print (sourceContent)
	
	(require, toClip) = do (target, source)
	sourceAllreadyHasRequireString = ifSourceHaveRequireString(sourceContent, require)
	require = '\n'+require

	cursorPosition = view.sel()[0].begin()
	if insertRequireUsage:
		view.insert(edit, cursorPosition, toClip) # do not change clipboard just inserts near cursor

	if not sourceAllreadyHasRequireString:
		requireInsertPosition = getPositionInSourceWhereToPaste_bySourceFileContent(sourceContent)
		if cursorPosition < requireInsertPosition:
			requireInsertPosition = cursorPosition
		view.insert(edit, requireInsertPosition, require+"\n")


													
