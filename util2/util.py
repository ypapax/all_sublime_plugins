import color
import re
def startsWith(myVeryLongStr, prefix):
	
	result = myVeryLongStr[:len(prefix)].lower() == prefix.lower()
	return result
def uniqueList(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]	

def itemInList(item, listik):
    return any( x for x in listik if item == x)	
def clearEmptyLines(text):
	regex = '\n*\s*\n+'
	m = re.findall(regex, text)
	print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
	color.red('m')
	print(repr(m))
	print('*****************************************************************')
	result = re.sub(regex, '\n', text)

	
	return result	
def replaceSequence(string, substring):
	target = ''
	while True:
		target_backup = target
		target = target + substring

		if target not in string: 
			target = target_backup
			break	
	result = string

	if target:
		result = re.sub(target, substring, string)	
		
	result = clearEmptyLines(result)	
	return result
def replaceTabsAndNewLinesToOne(text):
	return replaceSequence(text, '\n\t\t\t')
def replaceLastAndFirstQuotes(string):
	return re.sub('^\'|\'$', '', string)


needToReprList = ['\n', '\t']
def goodRepr(i):
	if (i in needToReprList):
		return replaceLastAndFirstQuotes(repr(i))
	else:
		return i	