import os
import re
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '../util'))
import color
import ast
import pickle
import filer2 as filer
import match

fileName = "/Users/maks/Library/Application Support/Sublime Text 3/Packages/clipToFile/data.data"
import next3 as next
def writeFile(data):
	filer.write(fileName, data)
	# fileP = open( fileName, "wt", encoding="utf-8" )
	# pickle.dump(data, fileP)
	# fileP.close()

def readFile():
	color.red ("reading file")
	
	data = filer.readToObj(fileName)
		
	return data	


def read(fileNameWithLine, move):
	data = readFile()
	result = next.get(data, fileNameWithLine, move)
	
	return result
def parseIced(clip):
	return parseIcedOrPython(clip, False)

def parseIcedOrPython(clip, python):
	color.red("input here baby")
	print(clip)
	# m = re.findall(r'File "/*.py", line \d+, in ', clip)
	if (python):
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		color.red('python')
		print(python)
		print('*****************************************************************')
		m = re.findall(r'File "(/.*.py)", line (\d+)', clip)	
	else:
		m = match.iced(clip)
	print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
	color.red('m')
	print(m)
	print('*****************************************************************')	
		
	color.blue("matches")
	pathes = [ i + ":" + j for (i,j) in m]
	print (m)

	# File "/Users/maks/Library/Application Support/Sublime Text 3/Packages/move_near_replace/replace_require_test.py", line 6, in <module>
	return  pathes


def parseIcedOrPythonOrGo(clip, pythonOrIcedOrGo):
	python = pythonOrIcedOrGo == 'python'
	iced = pythonOrIcedOrGo == 'iced'
	go = pythonOrIcedOrGo == 'go'

	color.red("input here baby")
	print(clip)
	# m = re.findall(r'File "/*.py", line \d+, in ', clip)
	if (python):
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		color.red('python')
		print(python)
		print('*****************************************************************')
		m = re.findall(r'File "(/.*.py)", line (\d+)', clip)	
	elif iced:
		m = match.iced(clip)
	elif go:
		m = match.iced(clip)
	print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
	color.red('m')
	print(m)
	print('*****************************************************************')	
		
	color.blue("matches")
	pathes = [ i + ":" + j for (i,j) in m]
	print (m)

	# File "/Users/maks/Library/Application Support/Sublime Text 3/Packages/move_near_replace/replace_require_test.py", line 6, in <module>
	return  pathes

def parseGo(clip):
	color.red("input here baby")
	print(clip)
	# m = re.findall(r'File "/*.py", line \d+, in ', clip)
	if (python):
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		color.red('python')
		print(python)
		print('*****************************************************************')
		m = re.findall(r'File "(/.*.py)", line (\d+)', clip)	
	else:
		m = match.iced(clip)
	print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
	color.red('m')
	print(m)
	print('*****************************************************************')	
		
	color.blue("matches")
	pathes = [ i + ":" + j for (i,j) in m]
	print (m)

	# File "/Users/maks/Library/Application Support/Sublime Text 3/Packages/move_near_replace/replace_require_test.py", line 6, in <module>
	return  pathes
def parse(clip):
	return parseIcedOrPython(clip, True)
