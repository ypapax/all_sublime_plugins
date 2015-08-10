import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '../util'))
import util

import sys
import color

import re


def startsWithOk(line):
	okList = ["import ", "sys.path.insert(0, "]
	for ok in okList:
		if util.startsWith(line, ok):
			return True
	return False		


def indexes(mylist, item):
	return [i for i, x in enumerate(mylist) if x == item and mylist.count(x) > 1]


def remove(text):
	lines = text.split('\n')
	removeList = []
	for i in lines:
		if (startsWithOk(i)):
			indexesFound = indexes(lines, i)
			if(len(indexesFound)>1):
				exceptFirstIndexes = indexesFound[1:]
				if(len(exceptFirstIndexes)):
					removeList.extend(exceptFirstIndexes)
	removeList = util.uniqueList(removeList)
	for r in removeList:

		del(lines[r])
	return str.join('\n', lines)