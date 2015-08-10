import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../moveNearReplace'))
import duplicateLines
import filer2 as filer
import re
import color


def py(text):
	regex = '[\t\s]*\n+(\t*def )'
	m = re.findall(regex, text)
	replace1 = re.sub(regex, r"\n\n\n\1", text).rstrip()
	replace2 = re.sub("^\n+", '', replace1)
	return replace2


def removeEmptyLines(text):
	regex = '\t*\n+'
	m = re.findall(regex, text)
	return re.sub(regex, r"\n", text)


def pyFull(text):
	return py(removeEmptyLines(duplicateLines.remove(text)))


def pyFile(filename):
	text = filer.read(filename)
	result = py(text)
	if (result != text):
		filer.write(filename, result)


def pyFileFull(filename):
	text = filer.read(filename)
	result = pyFull(text)
	if (result != text):
		filer.write(filename, result)
	