
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/moveNearReplace')
import filer2
		
import re
def getParams(fileContent):
	# module.exports = (countryId, autocb)->
	m = re.search(r"module.exports = \((.*?) autocb\)->", fileContent)
	if m:

		result = m.group(1)
		result = result.split(',')
		result = list(filter(None, result))
		result = [x.strip() for x in result] # trim every element
		print("result")
		print(result)
		return result
	else:
		return [] 

def getParamsByRegex(fileContent, regex): 
# from fileContent 
# 	module.exports = (a, b, autocb)->
# or 
#   module.exports = (a, b, cb)->
# should return 
# 	" a, b"
# depending on regex
	m = re.search(regex, fileContent)
	if m:

		result = m.group(1)

		# for filtering elements from excess commas we split to array and then join to comma separated list:
		result = result.split(',')
		result = list(filter(None, result))
		result = [x.strip() for x in result] # trim every element
		print("result")
		print(result)

		print("result")
		print(result)

		params = paramsToString(result)

		if params:
			params = " "+ params + ","

		return params

	else:
		return ""

def getParamsCb(fileContent):
	return getParamsByRegex(fileContent, r"module.exports = \((.*?) cb\)->")
def getParamsAutocb(fileContent):
	return getParamsByRegex(fileContent, r"module.exports = \((.*?) autocb\)->")
			

def paramsToString(paramList):
	return ', '.join(paramList)			


def fileNameToParamString(fileName):
	content = filer2.read ( fileName)
	params = getParams (content)
	string = paramsToString(params)
	return string