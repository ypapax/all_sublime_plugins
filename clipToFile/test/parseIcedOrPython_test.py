import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
sys.path.insert(0, os.path.join(currentFolder, '..'))
import color
import assertMy
import pyOutPutParse5

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		isPython = True
		clipboard = """  File "/Users/maks/Library/Application Support/Sublime Text 3/Packages/clipToFile/test/parseIcedOrPython_test.py", line 12, in test_testName
"""
		result = pyOutPutParse5.parseIcedOrPython(clipboard, isPython)
		expected = ['/Users/maks/Library/Application Support/Sublime Text 3/Packages/clipToFile/test/parseIcedOrPython_test.py:12']
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()