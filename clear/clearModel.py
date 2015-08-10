import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '../util'))
sys.path.insert(0, os.path.join(currentFolder, '../moveNearReplace'))
import filer2

import color
import re
import filer2 as filer
import util


def py(text):
	regex = "{0}print\(.+\)|{0}color\..+\)".format("\n\s+")
	replace1 = re.sub (regex, '', text)
	result = util.clearEmptyLines(replace1)
	# result = replace1
	return result


def pyFile(filename):
	fileText = filer.read(filename)
	fileText = py(fileText)
	filer.write(filename, fileText)