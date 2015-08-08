import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import color
import assertMy
import pyFind

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		filename = os.path.join(currentFolder, '../testPoligon/local.py')
		result = pyFind.filename2(filename, 'y')
		expected = filename
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()