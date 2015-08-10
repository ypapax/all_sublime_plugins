import shutil

import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
sys.path.insert(0, os.path.join(currentFolder, '..'))
import color
import assertMy
import create_test_node_model
import os

def makeGetTest(clearBeforeTest):
	color.blue("test here baby")
	inputFileName = '/Users/maks/Library/Application Support/Sublime Text 3/Packages/testForNodeJs/test/testPoligon/a/b.iced'
	testFolder = '/Users/maks/Library/Application Support/Sublime Text 3/Packages/testForNodeJs/test/testPoligon/test/'
	
	targetTestingFileName = testFolder+'a/b.iced/testing.iced'
	if clearBeforeTest and os.path.exists (testFolder):
		shutil.rmtree(testFolder)
		beforeTestNoFileActual = os.path.isfile(targetTestingFileName)
		beforeTestNoFileExpected = False
		assertMy.equals(beforeTestNoFileActual, beforeTestNoFileExpected)

	create_test_node_model.get(inputFileName)
	result = os.path.isfile(targetTestingFileName)
	expected = True
	assertMy.equals(result, expected)