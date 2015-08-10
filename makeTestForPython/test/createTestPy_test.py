
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
sys.path.insert(0, os.path.join(currentFolder, '../../moveNearReplace'))
sys.path.insert(0, os.path.join(currentFolder, '../../makeTest'))
sys.path.insert(0, os.path.join(currentFolder, '../../pythonTestCreate'))
import assertMy
		

import sys
import filer2 as filer
		
expected = """import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/testPoligon')
import color
import assertMy
import a

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		result = a.method()
		expected = ""
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()"""

import forPy
import unittest
import color

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		filename = '/Users/maks/testPoligon/a.py'

		testFile = forPy.create(filename, "method")
		result = filer.read(testFile)


		assertMy.equals(result, expected)


if __name__ == '__main__':
	unittest.main()		
			