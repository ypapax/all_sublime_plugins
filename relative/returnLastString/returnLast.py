
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/moveNearReplace')
import filer2
import color		
import re
def go(fileContent):
	m = re.search(r"return (\[.+?\]).*?$", fileContent)
	if m:

		result = m.group(1)
		return result
	else:
		return ""	


def replaceNullByErr(string):
	return string.replace("null","err")

def finalPrepare(string):
	if string:
		return "\n"+string + " = result\nth.err err"
	else:
		return ""	

def autocbOneEnding(targetFileContent):
	# it means there is one argument, get it:
	m = re.search(r"return ([^\]\[]+).*?$", targetFileContent) # all except [ ] square brackets
	if m:

		result = m.group(1)
		return result
	else:
		return ""


def doAllByFileName(fileName):
	fileContent = filer2.read (fileName)
	fileContent = fileContent.strip()
	return finalPrepare(replaceNullByErr(go(fileContent)))

def justArgsForSync(targetFileContent):
	fileContent = targetFileContent.strip()
	result = go(fileContent)
	if not result:
		# it means there is one argument, get it:
		m = re.search(r"return (.+).*?$", fileContent)
		if m:

			result = m.group(1)
			return result
		else:
			# no return word, try get last word in last row:
			m = re.search(r"\n(.+).*?$", fileContent)
			if m:

				result = m.group(1)
				words = result.strip().split(" ")
				print("words")
				print(words)
				if len(words) != 1:
					result = "actual"
				return result.strip()
			else:
				return "actual"	
	return result


def getReturnParamsForAutocbCommaSeparated(fileContent): # cb arg1, arg2
	fileContent = fileContent.strip()
	m = re.findall(r"cb (.+)", fileContent)

	if m:

		commaSeparatedArgs = m[-1]
		color.red("commaSeparatedArgs")
		print(commaSeparatedArgs)
		return replaceNullByErr(commaSeparatedArgs)
	else:
		return "()" # no params for func: (cb)->


def returnArgsByExpressionWithoutWordReturn(targetFileContent):
	fileContent = targetFileContent.strip()
	regex = re.compile(r"([\w\d_]+) =")
	m = regex.findall(fileContent)
	if m:
		lastGroup = m[-1]
		result = lastGroup
		return result
	else:
		return ""	

def returnParamsForSyncExpressionOrReturn(targetFileContent):
	returnParams = justArgsForSync(targetFileContent)	
	color.red ("returnParams")
	print (returnParams)
	if returnParams == 'actual':
		
		returnParamsExpression = returnArgsByExpressionWithoutWordReturn(targetFileContent)
		color.red("returnParamsExpression")
		print(returnParamsExpression)
		if not returnParamsExpression == "exports": # exception	
			returnParams = returnParamsExpression
	return returnParams





