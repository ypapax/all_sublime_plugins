import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
sys.path.insert(0, os.path.join(currentFolder, '../../moveNearReplace'))
sys.path.insert(0, os.path.join(currentFolder, '../../makeTest'))
sys.path.insert(0, os.path.join(currentFolder, '../../pythonTestCreate'))
import assertMy
import forPy
import unittest
import color

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		filename = forPy.createFileName('/Users/maks/Library/Application Support/Sublime Text 3/Packages/makeTest/testPoligon/test', "world")		

		color.red('filename')
		print(repr(filename))

		# expected = "/Users/maks/Library/Application Support/Sublime Text 3/Packages/makeTest/testPoligon/test/world1_test.py"
		# assertMy.equals(filename, expected)


if __name__ == '__main__':
	unittest.main()		
