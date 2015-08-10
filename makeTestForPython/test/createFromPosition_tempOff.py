

import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
sys.path.insert(0, os.path.join(currentFolder, '../../moveNearReplace'))
sys.path.insert(0, os.path.join(currentFolder, '../../makeTest'))
sys.path.insert(0, os.path.join(currentFolder, '../../pythonTestCreate'))
import filer2 as filer
import assertMy
import forPy
import unittest
import color

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		filename = os.path.abspath(os.path.join(currentFolder, '../../makeTestForGo/test/createFileName1_test/deep/deep/deep/a.py'))
		position = 10

		testFile = forPy.createFromPosition(filename, position)

		 
		result = filer.read(testFile)
		expected = """import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/makeTest/test/createFileName1_test/deep/deep/deep')
import color
import assertMy
import a

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		result = a.()
		expected = ""
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()"""
		assertMy.equals(result, expected)


if __name__ == '__main__':
	unittest.main()		
