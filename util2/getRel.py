import sys
import util
import re
import cutQuotes

def getRel(str):
	"""Returns relative path list from str"""
	m = re.findall(r"['\"]([\.]{1,2}/.*)['\"]", str)
	unique = util.uniqueList(m)
	print('unique list: ', unique)

	return unique

	
