import re
def byFileContent(fileContent):
	
	m = re.search(r"module.exports = \((.*?)\)", fileContent)
	if m:

		result = m.group(1)
		if not result:
			result = "()"
		else:
			result = " "+result	
		return result

	else:
		return ""


def isItSync(fileContent):
		
	m = re.search(r"module.exports = \(.*?autocb\)->", fileContent)
	if m:
		return False
	else:
		return True


def isItCb(fileContent):

	# isAutocb = isItSync(fileContent)
	# if isAutocb:
	# 	return False
	# else:
		m = re.search(r"[\( ]cb\)->", fileContent)
		if m:
			return True
		else:
			return False	