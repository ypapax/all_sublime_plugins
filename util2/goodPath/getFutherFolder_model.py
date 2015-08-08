import os
from os import listdir
from os.path import isfile, join

import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color
	


def get(startFromPath):
	path = startFromPath
	# sublime.status_message(path)
	path = os.path.dirname(path)
	while True:
		
		onlyfiles = [ f for f in listdir(path) if isfile(join(path,f)) and f == 'package.json' ]	
		
		print('++++++++++++++')
		print(onlyfiles)
		exit_condition = path == '/' or len(onlyfiles)
		color.red('exit_condition')
		print(exit_condition)
		if exit_condition:
			break
		path = os.path.abspath(os.path.join(path, '..'))	
	return path			



